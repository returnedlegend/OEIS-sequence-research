"""GPU generation/screening overlapped with a bounded pool of exact verifiers.

GPU screen counts are draws, not distinct graphs or exact invariant proofs.
Every unresolved possible violation is queued or preserved for later checking.
"""
from __future__ import annotations

from concurrent.futures import FIRST_COMPLETED, ProcessPoolExecutor, ThreadPoolExecutor, wait
from datetime import datetime, timezone
import hashlib
import json
import multiprocessing
from pathlib import Path
import shutil
import signal
import subprocess
import time

from .constrained_graphs import is_triangle_free
from .graphs import screen_graph, seed_graphs
from .independent_verify import verify_independently
from .verify import verify_graph


def initial_counters():
    return dict(generated=0, gpu_batches=0, gpu_screened_draws=0,
                gpu_certified_nonviolations=0, gpu_potential_draws=0,
                audit_samples=0, audit_not_selected=0, unique_screened=0,
                duplicates=0, screened_out=0, exact_calls=0, exact=0, unknown=0,
                pending=0, saved_tight=0, saved_near=0,
                independent_agreements=0, independent_unknown=0)


def record_batch(counters, batch):
    """Check routing conservation before trusting draw counts from the engine."""
    candidates = batch['candidates']
    potential = sum(candidate['kind'] == 'potential' for candidate in candidates)
    audits = sum(candidate['kind'] == 'audit' for candidate in candidates)
    if potential != batch['potential_count']:
        raise RuntimeError('GPU batch lost a potential counterexample candidate.')
    if potential + audits != len(candidates) or any(
            candidate['kind'] == 'audit' and candidate['screen']['optimistic_gap'] > 0
            for candidate in candidates):
        raise RuntimeError('GPU batch contains an invalid candidate routing label.')
    if (batch['generated'] != batch['certified_nonviolations'] + potential
            or audits > batch['audit_eligible']
            or min(batch['generated'], batch['certified_nonviolations'],
                   batch['potential_count'], batch['audit_eligible']) < 0):
        raise RuntimeError('GPU batch has inconsistent screening counts.')
    counters['generated'] += batch['generated']
    counters['gpu_batches'] += 1
    counters['gpu_screened_draws'] += batch['generated']
    counters['gpu_certified_nonviolations'] += batch['certified_nonviolations']
    counters['gpu_potential_draws'] += potential
    counters['audit_samples'] += audits
    counters['audit_not_selected'] += batch['audit_eligible'] - audits


class ResultRecorder:
    """Exact-result handling shared by completed asynchronous jobs and tests."""
    def __init__(self, output, run_dir, run_id, remaining):
        from .search import EventLog

        self.output = Path(output)
        self.run_dir = Path(run_dir)
        self.run_id = run_id
        self.remaining = remaining
        self.counters = initial_counters()
        self.best = None
        self.best_gap = None
        self.violation = False
        self.verifier_seconds = 0.0
        self.independent_seconds = 0.0
        self.events = EventLog(self.run_dir)
        self.signatures = set()
        for directory in ('best_candidates', 'near_misses'):
            for path in (self.output / directory).glob('*.json'):
                result = json.loads(path.read_text())['verification']
                self.signatures.add(tuple(result[key] for key in
                    ('n', 'edges', 'max_degree', 'omega', 'chi')))

    def defer(self, candidate, reason, result=None):
        from .search import graph_id

        self.counters['pending'] += 1
        payload = dict(candidate, graph_id=graph_id(candidate['adjacency']),
                       run_id=self.run_id, reason=reason,
                       verification=result or {'status': 'unknown', 'gap': None})
        with (self.run_dir / 'pending.jsonl').open('a', encoding='utf-8') as stream:
            stream.write(json.dumps(payload, separators=(',', ':')) + '\n')

    def accept(self, candidate, result):
        from .search import ROOT, graph_id, write_json

        adjacency = candidate['adjacency']
        digest = graph_id(adjacency)
        self.verifier_seconds += result.get('elapsed_seconds') or 0.0
        self.counters['exact' if result['status'] == 'exact' else 'unknown'] += 1
        self.events.write(json.dumps({
            'graph_id': digest, 'source': candidate['source'],
            'selection': candidate['kind'], 'screen': candidate['screen'],
            'verification': result}, separators=(',', ':')) + '\n')
        if result['status'] != 'exact':
            if candidate['kind'] == 'potential':
                self.defer(candidate, 'exact solver did not resolve potential violation', result)
            return
        gap = result['gap']
        rank = (gap, -result['omega'], result['chi'], result['n'])
        best_rank = ((self.best_gap, -self.best['omega'], self.best['chi'], self.best['n'])
                     if self.best is not None else None)
        if best_rank is None or rank > best_rank:
            self.best_gap = gap
            self.best = {'graph_id': digest, 'source': candidate['source'], **result}
        signature = tuple(result[key] for key in ('n', 'edges', 'max_degree', 'omega', 'chi'))
        if gap < -1 or (gap <= 0 and signature in self.signatures):
            return
        payload = {'graph_id': digest, 'source': candidate['source'], 'run_id': self.run_id,
                   'adjacency': adjacency, 'verification': result,
                   'description': 'Representative parameter tuple; no novelty claim.'}
        remaining = self.remaining()
        started = time.monotonic()
        independent = (verify_independently(adjacency, time_limit=min(60 if gap > 0 else 5, remaining))
                       if remaining > 0 else {'status': 'unknown', 'reason': 'run deadline exhausted'})
        self.independent_seconds += time.monotonic() - started
        payload['independent_verification'] = independent
        if independent['status'] == 'exact':
            keys = ('n', 'edges', 'max_degree', 'omega', 'chi', 'reed_bound', 'gap')
            if any(result[key] != independent[key] for key in keys):
                write_json(self.run_dir / f'disagreement-{digest}.json', payload)
                raise RuntimeError('Independent solvers disagree; search halted for diagnosis.')
            self.counters['independent_agreements'] += 1
        else:
            self.counters['independent_unknown'] += 1
        if gap > 0:
            if independent['status'] != 'exact':
                write_json(self.run_dir / f'unconfirmed-{digest}.json', payload)
                return
            directory = self.output / 'COUNTEREXAMPLE'
            write_json(directory / f'{digest}.json', payload)
            shutil.copyfile(ROOT / 'src' / 'independent_verify.py', directory / 'verify.py')
            readme = self.output / 'README.md'
            previous = readme.read_text() if readme.exists() else ''
            readme.write_text('# Verified Reed conjecture counterexample candidate\n\n'
                              f'Two exact implementations agree on positive gap {gap}. '
                              'Independent mathematical review is still warranted.\n\n' + previous)
            self.violation = True
        else:
            directory = 'best_candidates' if gap == 0 else 'near_misses'
            write_json(self.output / directory / f'{digest}.json', payload)
            self.counters['saved_tight' if gap == 0 else 'saved_near'] += 1
            self.signatures.add(signature)

    def close(self):
        self.events.close()


def _verify_job(adjacency, seconds):
    # Spawned workers import CPU solver modules only; CUDA belongs to the producer.
    return verify_graph(adjacency, time_limit=seconds, workers=1)


class BoundedVerifier:
    def __init__(self, executor, recorder, max_pending):
        self.executor = executor
        self.recorder = recorder
        self.max_pending = max_pending
        self.pending = {}

    def submit(self, candidate, seconds):
        if len(self.pending) >= self.max_pending:
            return False
        future = self.executor.submit(_verify_job, candidate['adjacency'], seconds)
        self.pending[future] = candidate
        self.recorder.counters['exact_calls'] += 1
        return True

    def collect(self, block_seconds=0.0):
        if block_seconds and self.pending:
            wait(self.pending, timeout=block_seconds, return_when=FIRST_COMPLETED)
        count = 0
        for future in list(self.pending):
            if not future.done():
                continue
            candidate = self.pending.pop(future)
            try:
                result = future.result()
            except BaseException:
                self.recorder.defer(candidate, 'worker failed before returning an exact result')
                raise
            self.recorder.accept(candidate, result)
            count += 1
            if self.recorder.violation:
                break
        return count

    def preserve_pending(self, reason):
        for future, candidate in list(self.pending.items()):
            future.cancel()
            self.recorder.defer(candidate, reason)
            del self.pending[future]


def route_candidates(candidates, route, preserve):
    """Retain the complete transferred batch if backpressure/routing fails.

The current candidate has entered the dedup set but has not been submitted;
the remainder has not entered it yet. The preserve callback distinguishes them.
"""
    candidates = iter(candidates)
    for candidate in candidates:
        try:
            route(candidate)
        except BaseException:
            preserve(candidate, current=True)
            for remaining in candidates:
                preserve(remaining, current=False)
            raise


def _push_checkpoint(root):
    """The network worker may only push an already committed repository HEAD."""
    try:
        result = subprocess.run(['git', 'push', 'origin', 'HEAD:main'], cwd=root,
                                text=True, capture_output=True, timeout=90)
        print('Git background push:', 'pushed' if result.returncode == 0 else result.stderr, flush=True)
        return result.returncode == 0
    except (OSError, subprocess.TimeoutExpired) as error:
        print(f'Git background push deferred: {error}', flush=True)
        return False


class AsyncCheckpointSync:
    """Commit on the controller; overlap one network push with GPU computation.

    A busy network push is never joined during normal checkpointing. New commits
    accumulate and the next push sends the latest HEAD. Rebase/retry is confined
    to a controller checkpoint after its completed records have been committed.
    """
    def __init__(self, root, sync, executor=None):
        self.root = root
        self.sync = sync
        self.executor = executor if executor is not None else ThreadPoolExecutor(max_workers=1)
        self.future = None
        self.pending_push = False
        self.pushes_started = 0

    @staticmethod
    def _result(future):
        try:
            return future.result()
        except Exception as error:
            print(f'Git background push failed: {error}', flush=True)
            return False

    def checkpoint(self, message):
        # This is called only from the controller, while event logging is paused.
        if not self.sync(message, prepare_only=True):
            return False
        self.pending_push = True
        if self.future is not None:
            if not self.future.done():
                return True
            succeeded = self._result(self.future)
            self.future = None
            if not succeeded:
                # No push is active now; existing sync handles a clean-tree
                # rebase and retry without racing the generator's file writes.
                succeeded = self.sync(message)
                self.pending_push = not succeeded
                return succeeded
        self.future = self.executor.submit(_push_checkpoint, self.root)
        self.pushes_started += 1
        self.pending_push = False
        return True

    def finish(self, message):
        """Join the active network call, then synchronously push the final HEAD."""
        try:
            if self.future is not None:
                self._result(self.future)
                self.future = None
            succeeded = self.sync(message)
            self.pending_push = not succeeded
            return succeeded
        finally:
            self.executor.shutdown(wait=True)


def run(args):
    """Run bounded CUDA search, with exact verification in separate CPU processes."""
    import torch
    from .gpu_engine import TriangleFreeGPUGenerator
    from .search import ROOT, graph_id, sync_git, utc, write_json

    if not args.triangle_free:
        raise ValueError('The GPU pipeline currently requires --triangle-free.')
    device = ('cuda' if torch.cuda.is_available() else 'cpu') if args.device == 'auto' else args.device
    if device == 'cuda' and not torch.cuda.is_available():
        raise SystemExit('CUDA requested but no usable CUDA device/runtime is exposed.')
    torch.set_num_threads(1)
    torch.manual_seed(args.seed)
    started = time.monotonic()
    deadline = started + args.seconds
    output = Path(args.output_dir).resolve()
    run_id = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S') + f'-gpu-seed{args.seed}'
    run_dir = output / 'runs' / run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    recorder = ResultRecorder(output, run_dir, run_id, lambda: deadline - time.monotonic())
    counters = recorder.counters
    stop = False
    stop_file = Path(args.stop_file) if getattr(args, 'stop_file', None) else None

    def request_stop(signum, frame):
        nonlocal stop
        stop = True

    old_signals = {sig: signal.signal(sig, request_stop) for sig in (signal.SIGINT, signal.SIGTERM)}

    def should_stop():
        return stop or recorder.violation or time.monotonic() >= deadline or (stop_file is not None and stop_file.exists())

    seeds = [(name, adjacency) for name, adjacency in seed_graphs(args.max_vertices)
             if is_triangle_free(adjacency)]
    parents = [adjacency for _, adjacency in seeds if max(map(sum, adjacency), default=0) >= 3]
    parents = parents or [adjacency for _, adjacency in seeds]
    config = {key: str(value) if isinstance(value, Path) else value for key, value in vars(args).items()}
    config.update(device_used=device, torch_version=torch.__version__,
                  cuda_available=torch.cuda.is_available(), started_utc=utc(), seed_count=len(seeds),
                  pipeline='gpu_batched_coloring_parallel_exact',
                  counts_note='GPU generated/screened/certified counts are draws, possibly repeated; unique_screened counts transferred candidates and seeds only.',
                  source_sha256={str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
                                 for path in sorted((ROOT / 'src').glob('*.py'))},
                  git_dirty_at_start=bool(subprocess.check_output(['git', 'status', '--porcelain'], cwd=ROOT, text=True).strip()),
                  git_head=subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip())
    write_json(run_dir / 'config.json', config)
    timings = dict(gpu_generation_screen_seconds=0.0, backpressure_seconds=0.0, git_sync_seconds=0.0)
    last_report = last_sync = started
    last_sync_count = 0
    seen = set()
    executor = ProcessPoolExecutor(max_workers=args.verifier_workers,
                                   mp_context=multiprocessing.get_context('spawn'))
    queue = BoundedVerifier(executor, recorder, max_pending=max(4, args.verifier_workers * 4))
    git_sync = AsyncCheckpointSync(ROOT, sync_git) if args.sync else None

    def checkpoint(reason, push=False, final=False):
        nonlocal last_sync, last_sync_count
        elapsed = time.monotonic() - started
        data = dict(run_id=run_id, timestamp_utc=utc(), reason=reason, device=device,
                    pipeline=config['pipeline'], elapsed_seconds=elapsed, **counters,
                    gpu_screened_draws_per_second=counters['gpu_screened_draws'] / max(elapsed, 1e-9),
                    unique_graphs_per_second=counters['unique_screened'] / max(elapsed, 1e-9),
                    verifier_worker_seconds=recorder.verifier_seconds,
                    independent_seconds=recorder.independent_seconds, **timings,
                    git_background_pushes=git_sync.pushes_started if git_sync is not None else 0,
                    in_flight=len(queue.pending), best_gap=recorder.best_gap, best=recorder.best,
                    counterexample_verified=recorder.violation)
        write_json(run_dir / 'summary.json', data)
        print(json.dumps(data), flush=True)
        with (output / 'RESEARCH_LOG.md').open('a', encoding='utf-8') as log:
            log.write(f"\n- {utc()} | {run_id} | {reason} | device={device}, GPU pipeline | "
                      f"generated draws={counters['generated']}, GPU certified nonviolations={counters['gpu_certified_nonviolations']}, "
                      f"unique transferred candidates={counters['unique_screened']}, exact={counters['exact']}, "
                      f"unknown={counters['unknown']}, pending={counters['pending']} | "
                      f"{data['gpu_screened_draws_per_second']:.2f} GPU screened draws/s | best exact gap={recorder.best_gap}.\n")
        if push and args.sync:
            sync_started = time.monotonic()
            message = f"GPU research {run_id}: {counters['generated']} draws, {counters['exact']} exact | best gap {recorder.best_gap} | {reason}"
            if final:
                git_sync.finish(message)
            else:
                git_sync.checkpoint(message)
            timings['git_sync_seconds'] += time.monotonic() - sync_started
        if push:
            last_sync, last_sync_count = time.monotonic(), counters['generated']

    def maintenance():
        nonlocal last_report
        now = time.monotonic()
        if now - last_report >= args.progress_seconds:
            checkpoint('progress')
            last_report = now
        if now - last_sync >= 900 or counters['generated'] - last_sync_count >= 50_000:
            checkpoint('scheduled sync', push=True)

    def route(candidate):
        digest = graph_id(candidate['adjacency'])
        if digest in seen:
            counters['duplicates'] += 1
            return
        seen.add(digest)
        counters['unique_screened'] += 1
        while not should_stop():
            queue.collect()
            if recorder.violation:
                break
            remaining = deadline - time.monotonic()
            if remaining > 0 and queue.submit(candidate, min(args.solver_seconds, remaining)):
                return
            wait_started = time.monotonic()
            queue.collect(block_seconds=min(0.05, max(0.0, remaining)))
            timings['backpressure_seconds'] += time.monotonic() - wait_started
            maintenance()
        recorder.defer(candidate, 'runtime/stop reached before verification submission')

    def preserve_unsubmitted(candidate, current=False):
        digest = graph_id(candidate['adjacency'])
        if not current:
            if digest in seen:
                counters['duplicates'] += 1
                return
            seen.add(digest)
            counters['unique_screened'] += 1
        recorder.defer(candidate, 'routing error before verification submission')

    final_reason = 'error'
    try:
        for name, adjacency in seeds:
            if should_stop():
                break
            counters['generated'] += 1
            screen = screen_graph(adjacency)
            if screen['optimistic_gap'] < -1:
                counters['screened_out'] += 1
                continue
            route_candidates([dict(adjacency=adjacency, screen=screen,
                       kind='potential' if screen['optimistic_gap'] > 0 else 'audit', source=name)],
                       route, preserve_unsubmitted)
        while queue.pending and not should_stop():
            queue.collect(block_seconds=0.05)
        checkpoint('seed evaluation', push=True)
        if not should_stop():
            generator = TriangleFreeGPUGenerator(parents, batch_size=args.batch_size, seed=args.seed,
                device=device, swap_attempts=args.swap_attempts, coloring_trials=args.coloring_trials)
        while not should_stop():
            queue.collect()
            if should_stop():
                break
            batch_started = time.monotonic()
            batch = generator.next_batch(audit_size=args.audit_per_batch)
            timings['gpu_generation_screen_seconds'] += time.monotonic() - batch_started
            record_batch(counters, batch)
            candidates = (dict(candidate, source='GPU triangle-free degree-preserving swaps')
                          for candidate in batch['candidates'])
            route_candidates(candidates, route, preserve_unsubmitted)
            maintenance()
        # Consume already finished results; bounded running work is retained below.
        queue.collect()
        final_reason = ('counterexample' if recorder.violation else 'stopped'
                        if stop or (stop_file is not None and stop_file.exists()) else 'runtime limit')
    finally:
        queue.preserve_pending(f'{final_reason}: verification unfinished')
        executor.shutdown(wait=True, cancel_futures=True)
        checkpoint(final_reason, push=True, final=True)
        recorder.close()
        for sig, old_handler in old_signals.items():
            signal.signal(sig, old_handler)
    return 0
