"""Bounded, checkpointed research search. Run with python -m src.search."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import math
from pathlib import Path
import random
import shutil
import signal
import subprocess
import time

from .graphs import mutate_batch, screen_graph, seed_graphs
from .verify import verify_graph
from .independent_verify import verify_independently

ROOT = Path(__file__).resolve().parents[1]


def utc():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def graph_id(adjacency):
    return hashlib.sha256(bytes(x for row in adjacency for x in row) + str(len(adjacency)).encode()).hexdigest()[:20]


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(data, indent=2) + '\n')
    temp.replace(path)


def sync_git(message):
    """Push completed tracked research artifacts; errors never terminate search."""
    def git(*args):
        return subprocess.run(['git', *args], cwd=ROOT, text=True, capture_output=True, timeout=90)
    try:
        # Restrict staging to this project's research outputs, never git add -A.
        paths = [p for p in ('src', 'tests', 'scripts', 'best_candidates', 'near_misses',
                            'COUNTEREXAMPLE', 'runs', 'README.md', 'RESEARCH_LOG.md',
                            '.gitignore', 'requirements.txt', 'requirements.lock') if (ROOT / p).exists()]
        staged = git('diff', '--cached', '--quiet')
        if staged.returncode != 0:
            print('Git sync deferred: pre-existing staged changes.', flush=True)
            return False
        result = git('add', '--', *paths)
        if result.returncode:
            print('Git staging failed:', result.stderr, flush=True)
            return False
        if git('diff', '--cached', '--quiet').returncode == 1:
            result = git('commit', '-m', message)
            if result.returncode:
                print('Git commit failed:', result.stderr, flush=True)
                git('reset', '--', *paths)  # Only unstage what this call staged.
                return False
        result = git('push', 'origin', 'HEAD:main')
        if result.returncode:
            print('Git push failed:', result.stderr, flush=True)
            if git('status', '--porcelain').stdout.strip():
                print('Rebase deferred: working tree contains unsaved changes.', flush=True)
                return False
            rebased = git('pull', '--rebase', 'origin', 'main')
            if rebased.returncode:
                git('rebase', '--abort')
                print('Git rebase failed:', rebased.stderr, flush=True)
                return False
            result = git('push', 'origin', 'HEAD:main')
        print('Git sync:', 'pushed' if result.returncode == 0 else result.stderr, flush=True)
        return result.returncode == 0
    except (OSError, subprocess.TimeoutExpired) as error:
        print(f'Git sync deferred: {error}', flush=True)
        return False


def run(args):
    import torch
    torch.set_num_threads(1)
    torch.manual_seed(args.seed)
    if args.device == 'cuda' and not torch.cuda.is_available():
        raise SystemExit('CUDA requested but no usable CUDA device/runtime is exposed.')
    device = ('cuda' if torch.cuda.is_available() else 'cpu') if args.device == 'auto' else args.device
    rng = random.Random(args.seed)
    run_id = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S') + f'-seed{args.seed}'
    output = Path(args.output_dir).resolve()
    run_dir = output / 'runs' / run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    deadline = started + args.seconds
    stop = False
    def request_stop(signum, frame):
        nonlocal stop
        stop = True
    signal.signal(signal.SIGTERM, request_stop)
    signal.signal(signal.SIGINT, request_stop)
    counters = dict(generated=0, unique_screened=0, duplicates=0, screened_out=0,
                    exact_calls=0, exact=0, unknown=0, saved_tight=0, saved_near=0,
                    independent_agreements=0, independent_unknown=0)
    best_gap = None
    best = None
    seen = set()
    signatures = set()
    for directory in ('best_candidates', 'near_misses'):
        for path in (output / directory).glob('*.json'):
            data = json.loads(path.read_text())['verification']
            signatures.add(tuple(data[k] for k in ('n', 'edges', 'max_degree', 'omega', 'chi')))
    seeds = list(seed_graphs(args.max_vertices))
    parents = [adj for _, adj in seeds]
    base_parents = parents[:]
    last_report = last_sync = started
    last_sync_count = 0
    violation = False
    event_file = (run_dir / 'events.jsonl').open('a', buffering=1)
    config = vars(args) | {'device_used': device, 'torch_version': torch.__version__,
                           'cuda_available': torch.cuda.is_available(), 'started_utc': utc(),
                           'seed_count': len(seeds), 'git_head': subprocess.check_output(
                               ['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()}
    write_json(run_dir / 'config.json', config)

    def summary(reason):
        elapsed = time.monotonic() - started
        return {'run_id': run_id, 'timestamp_utc': utc(), 'reason': reason,
                'device': device, 'elapsed_seconds': elapsed, **counters,
                'unique_graphs_per_second': counters['unique_screened'] / max(elapsed, 1e-9),
                'best_gap': best_gap, 'best': best, 'counterexample_verified': violation}

    def checkpoint(reason, push=False):
        nonlocal last_sync, last_sync_count
        data = summary(reason)
        write_json(run_dir / 'summary.json', data)
        print(json.dumps(data), flush=True)
        with (output / 'RESEARCH_LOG.md').open('a') as log:
            log.write(f"\n- {utc()} | {run_id} | {reason} | device={device} | "
                      f"generated={counters['generated']}, unique screened={counters['unique_screened']}, "
                      f"exact={counters['exact']}, unknown={counters['unknown']} | "
                      f"{data['unique_graphs_per_second']:.2f} unique graphs/s | best exact gap={best_gap}.\n")
        if push and args.sync:
            sync_git(f"Research {run_id}: {counters['unique_screened']} graphs | best exact gap {best_gap} | {reason}")
        if push:
            last_sync = time.monotonic()
            last_sync_count = counters['unique_screened']

    def evaluate(name, adjacency):
        nonlocal best_gap, best, violation, parents
        counters['generated'] += 1
        digest = graph_id(adjacency)
        if digest in seen:
            counters['duplicates'] += 1
            return
        seen.add(digest)
        counters['unique_screened'] += 1
        screen = screen_graph(adjacency)
        if screen['optimistic_gap'] < -1:
            counters['screened_out'] += 1
            return
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            return
        counters['exact_calls'] += 1
        result = verify_graph(adjacency, time_limit=min(args.solver_seconds, remaining), workers=1)
        counters['exact' if result['status'] == 'exact' else 'unknown'] += 1
        event_file.write(json.dumps({'graph_id': digest, 'source': name, 'screen': screen,
                                     'verification': result}, separators=(',', ':')) + '\n')
        if result['status'] != 'exact':
            return
        gap = result['gap']
        rank = (gap, -result['omega'], result['chi'], result['n'])
        best_rank = ((best_gap, -best['omega'], best['chi'], best['n']) if best else None)
        if best_rank is None or rank > best_rank:
            best_gap, best = gap, {'graph_id': digest, 'source': name, **result}
        if gap >= -1 and screen['clique_lower_bound'] <= 3:
            # Retain all seed families and a moving pool of verified near candidates.
            parents.append(adjacency)
            parents = base_parents + parents[len(base_parents):][-128:]
        signature = tuple(result[k] for k in ('n', 'edges', 'max_degree', 'omega', 'chi'))
        if gap < -1 or (signature in signatures and gap <= 0):
            return
        payload = {'graph_id': digest, 'source': name, 'run_id': run_id,
                   'adjacency': adjacency, 'verification': result,
                   'description': 'Representative parameter tuple; no novelty claim.'}
        remaining = deadline - time.monotonic()
        independent = (verify_independently(adjacency, time_limit=min(60 if gap > 0 else 5, remaining))
                       if remaining > 0 else {'status': 'unknown', 'reason': 'run deadline exhausted'})
        payload['independent_verification'] = independent
        if independent['status'] == 'exact':
            keys = ('n', 'edges', 'max_degree', 'omega', 'chi', 'reed_bound', 'gap')
            if any(result[k] != independent[k] for k in keys):
                write_json(run_dir / f'disagreement-{digest}.json', payload)
                raise RuntimeError('Independent solvers disagree; search halted for diagnosis.')
            counters['independent_agreements'] += 1
        else:
            counters['independent_unknown'] += 1
        if gap > 0:
            if independent['status'] != 'exact':
                write_json(run_dir / f'unconfirmed-{digest}.json', payload)
                return
            folder = output / 'COUNTEREXAMPLE'
            write_json(folder / f'{digest}.json', payload)
            shutil.copyfile(ROOT / 'src' / 'independent_verify.py', folder / 'verify.py')
            readme = output / 'README.md'
            old = readme.read_text() if readme.exists() else ''
            readme.write_text('# Verified Reed conjecture counterexample candidate\n\n'
                              f'Two exact implementations agree on positive gap {gap}. '
                              'Independent mathematical review is still warranted.\n\n' + old)
            violation = True
        else:
            folder = 'best_candidates' if gap == 0 else 'near_misses'
            write_json(output / folder / f'{digest}.json', payload)
            counters['saved_tight' if gap == 0 else 'saved_near'] += 1
            signatures.add(signature)

    try:
        for name, adjacency in seeds:
            if stop or time.monotonic() >= deadline or violation:
                break
            evaluate(name, adjacency)
        checkpoint('seed evaluation', push=True)
        while not stop and not violation and time.monotonic() < deadline:
            for adjacency in mutate_batch(parents, args.batch_size, rng, device=device):
                if stop or violation or time.monotonic() >= deadline:
                    break
                evaluate('degree-preserving edge swaps', adjacency)
                now = time.monotonic()
                if now-last_report >= args.progress_seconds:
                    checkpoint('progress')
                    last_report = now
                if now-last_sync >= 900 or counters['unique_screened']-last_sync_count >= 50_000:
                    checkpoint('scheduled sync', push=True)
        checkpoint('counterexample' if violation else 'stopped' if stop else 'runtime limit', push=True)
    finally:
        event_file.close()
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seconds', type=float, default=3600, help='Finite wall-time search budget (default 1 hour).')
    parser.add_argument('--seed', type=int, default=20261115)
    parser.add_argument('--batch-size', type=int, default=64)
    parser.add_argument('--max-vertices', type=int, default=40)
    parser.add_argument('--solver-seconds', type=float, default=3)
    parser.add_argument('--progress-seconds', type=float, default=600)
    parser.add_argument('--device', choices=('auto', 'cpu', 'cuda'), default='auto')
    parser.add_argument('--output-dir', default=str(ROOT))
    parser.add_argument('--sync', action='store_true', help='Commit/push checkpoints to origin main (explicit opt-in).')
    args = parser.parse_args()
    if any(not math.isfinite(value) or value <= 0 for value in
           (args.seconds, args.solver_seconds, args.progress_seconds)) or args.batch_size < 1 or args.max_vertices < 5:
        parser.error('Time budgets/batch size must be positive; max-vertices must be at least 5.')
    if args.sync and Path(args.output_dir).resolve() != ROOT:
        parser.error('--sync requires repository-root output-dir.')
    with (ROOT / '.search.lock').open('w') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            parser.error('Another search is already running in this checkout.')
        return run(args)


if __name__ == '__main__':
    raise SystemExit(main())
