"""GPU-controller safety checks independent of CUDA scheduling."""
from concurrent.futures import Future
import json
from pathlib import Path
import subprocess
import sys

import pytest

from src import gpu_search


CYCLE5 = [[int((u - v) % 5 in (1, 4)) for v in range(5)] for u in range(5)]
EXACT = dict(status='exact', n=5, edges=5, max_degree=2, omega=2,
             chi=3, reed_bound=3, gap=0, coloring=[0, 1, 0, 1, 2], clique=[0, 1],
             elapsed_seconds=0.001)


@pytest.fixture
def recorder(tmp_path):
    run_dir = tmp_path / 'runs' / 'test-run'
    run_dir.mkdir(parents=True)
    return gpu_search.ResultRecorder(tmp_path, run_dir, 'test-run', lambda: 10.0)


def item(kind='potential'):
    return {'adjacency': CYCLE5, 'screen': {'optimistic_gap': 1 if kind == 'potential' else 0},
            'kind': kind, 'source': 'test'}


def test_unknown_never_becomes_verified_and_potential_is_retained(recorder):
    recorder.accept(item(), {'status': 'unknown', 'gap': None, 'elapsed_seconds': 1})
    assert recorder.counters['exact'] == 0
    assert recorder.counters['unknown'] == 1
    assert not (recorder.output / 'COUNTEREXAMPLE').exists()
    pending = [json.loads(line) for line in (recorder.run_dir / 'pending.jsonl').read_text().splitlines()]
    assert pending[0]['adjacency'] == CYCLE5
    assert pending[0]['verification']['status'] == 'unknown'
    recorder.close()


def test_positive_needs_independent_agreement(recorder, monkeypatch):
    positive = EXACT | {'chi': 4, 'gap': 1}
    monkeypatch.setattr(gpu_search, 'verify_independently', lambda *a, **k: {'status': 'unknown'})
    recorder.accept(item(), positive)
    assert not recorder.violation
    assert not (recorder.output / 'COUNTEREXAMPLE').exists()
    assert list(recorder.run_dir.glob('unconfirmed-*.json'))
    recorder.close()


def test_confirmed_positive_has_standalone_verifier_and_alert(recorder, monkeypatch):
    positive = EXACT | {'chi': 4, 'gap': 1}
    monkeypatch.setattr(gpu_search, 'verify_independently', lambda *a, **k: positive.copy())
    recorder.accept(item(), positive)
    assert recorder.violation
    assert (recorder.output / 'COUNTEREXAMPLE' / 'verify.py').is_file()
    assert 'counterexample' in (recorder.output / 'README.md').read_text()
    assert list((recorder.output / 'COUNTEREXAMPLE').glob('*.json'))
    recorder.close()


def test_solver_disagreement_fails_closed(recorder, monkeypatch):
    monkeypatch.setattr(gpu_search, 'verify_independently', lambda *a, **k: EXACT | {'chi': 4})
    with pytest.raises(RuntimeError, match='disagree'):
        recorder.accept(item(), EXACT.copy())
    assert not recorder.violation
    assert list(recorder.run_dir.glob('disagreement-*.json'))
    assert not (recorder.output / 'COUNTEREXAMPLE').exists()
    recorder.close()


def test_unsubmitted_candidate_is_saved_without_exact_claim(recorder):
    recorder.defer(item(), 'deadline')
    assert recorder.counters['pending'] == 1
    assert recorder.counters['exact'] == 0
    data = json.loads((recorder.run_dir / 'pending.jsonl').read_text())
    assert data['verification']['status'] == 'unknown'
    assert data['adjacency'] == CYCLE5
    recorder.close()


def test_heuristic_counts_are_not_exact_or_unique_claims():
    counters = gpu_search.initial_counters()
    gpu_search.record_batch(counters, {'generated': 4096, 'certified_nonviolations': 4090,
        'potential_count': 6, 'audit_eligible': 100,
        'candidates': [item() for _ in range(6)] + [item('audit') for _ in range(2)]})
    assert counters['generated'] == 4096
    assert counters['gpu_certified_nonviolations'] == 4090
    assert counters['exact'] == counters['unique_screened'] == 0
    assert counters['audit_not_selected'] == 98


def test_lost_potential_candidate_is_rejected():
    with pytest.raises(RuntimeError, match='potential'):
        gpu_search.record_batch(gpu_search.initial_counters(), {
            'generated': 10, 'certified_nonviolations': 8, 'potential_count': 2,
            'audit_eligible': 0, 'candidates': [item()]})


class FakeExecutor:
    def __init__(self):
        self.futures = []

    def submit(self, *args):
        future = Future()
        self.futures.append(future)
        return future


def test_bounded_verifier_keeps_backpressure_and_preserves_pending(recorder):
    executor = FakeExecutor()
    queue = gpu_search.BoundedVerifier(executor, recorder, max_pending=1)
    assert queue.submit(item(), 1)
    assert not queue.submit(item(), 1)
    assert len(executor.futures) == 1
    queue.preserve_pending('deadline')
    assert recorder.counters['pending'] == 1
    assert executor.futures[0].cancelled()
    assert recorder.counters['exact'] == 0
    recorder.close()


def test_finished_future_is_consumed_without_waiting(recorder, monkeypatch):
    monkeypatch.setattr(gpu_search, 'verify_independently', lambda *a, **k: EXACT.copy())
    executor = FakeExecutor()
    queue = gpu_search.BoundedVerifier(executor, recorder, max_pending=2)
    queue.submit(item(), 1)
    executor.futures[0].set_result(EXACT.copy())
    assert queue.collect() == 1
    assert not queue.pending
    assert recorder.counters['exact'] == 1
    assert recorder.counters['pending'] == 0
    recorder.close()


def test_worker_failure_retains_the_candidate_before_raising(recorder):
    executor = FakeExecutor()
    queue = gpu_search.BoundedVerifier(executor, recorder, max_pending=1)
    queue.submit(item(), 1)
    executor.futures[0].set_exception(RuntimeError('worker crashed'))
    with pytest.raises(RuntimeError, match='worker crashed'):
        queue.collect()
    assert recorder.counters['pending'] == 1
    assert json.loads((recorder.run_dir / 'pending.jsonl').read_text())['adjacency'] == CYCLE5
    recorder.close()


def test_routing_failure_preserves_current_and_all_unsubmitted_candidates(recorder):
    first = item()
    current = item()
    current['source'] = 'failed current'
    remaining = item()
    remaining['source'] = 'unsubmitted remainder'
    routed = []
    preserved = []

    def route(candidate):
        routed.append(candidate['source'])
        if candidate is current:
            raise RuntimeError('injected worker failure while applying backpressure')

    def preserve(candidate, current=False):
        preserved.append((candidate['source'], current))
        recorder.defer(candidate, 'exception before submission')

    with pytest.raises(RuntimeError, match='injected worker failure'):
        gpu_search.route_candidates([first, current, remaining], route, preserve)
    assert routed == ['test', 'failed current']
    assert preserved == [('failed current', True), ('unsubmitted remainder', False)]
    pending = [json.loads(line) for line in (recorder.run_dir / 'pending.jsonl').read_text().splitlines()]
    assert [entry['source'] for entry in pending] == ['failed current', 'unsubmitted remainder']
    assert all(entry['verification']['status'] == 'unknown' for entry in pending)
    recorder.close()


def pipeline_cli(output, *extra):
    return subprocess.run(
        [sys.executable, '-m', 'src.search', '--gpu-pipeline', '--triangle-free',
         '--device', 'cpu', '--seconds', '3', '--max-vertices', '5', '--batch-size', '16',
         '--audit-per-batch', '2', '--verifier-workers', '1', '--coloring-trials', '1',
         '--output-dir', str(output), *extra],
        cwd=Path(__file__).resolve().parents[1], text=True, capture_output=True, timeout=40,
    )


def test_real_pipeline_spawns_worker_and_writes_consistent_counts(tmp_path):
    process = pipeline_cli(tmp_path)
    assert process.returncode == 0, process.stderr
    run_dir, = (tmp_path / 'runs').iterdir()
    summary = json.loads((run_dir / 'summary.json').read_text())
    config = json.loads((run_dir / 'config.json').read_text())
    assert config['pipeline'] == 'gpu_batched_coloring_parallel_exact'
    assert summary['gpu_screened_draws'] > 0
    assert summary['gpu_screened_draws'] == summary['gpu_certified_nonviolations'] + summary['gpu_potential_draws']
    assert summary['exact'] >= 1
    assert summary['in_flight'] == 0
    assert summary['counterexample_verified'] is False
    events = [json.loads(line) for path in run_dir.glob('events-*.jsonl')
              for line in path.read_text().splitlines()]
    assert sum(event['verification']['status'] == 'exact' for event in events) == summary['exact']
    assert len(events) == summary['exact'] + summary['unknown']
    pending_path = run_dir / 'pending.jsonl'
    pending = pending_path.read_text().splitlines() if pending_path.exists() else []
    assert len(pending) == summary['pending']


def test_existing_stop_file_checkpoints_without_generation(tmp_path):
    stop_file = tmp_path / 'stop'
    stop_file.touch()
    process = pipeline_cli(tmp_path, '--stop-file', str(stop_file))
    assert process.returncode == 0, process.stderr
    run_dir, = (tmp_path / 'runs').iterdir()
    summary = json.loads((run_dir / 'summary.json').read_text())
    assert summary['reason'] == 'stopped'
    assert summary['generated'] == summary['gpu_batches'] == summary['exact_calls'] == 0
    assert summary['pending'] == summary['in_flight'] == 0


class FakePushExecutor:
    def __init__(self):
        self.futures = []
        self.submitted = []
        self.closed = False

    def submit(self, function, *args):
        future = Future()
        self.futures.append(future)
        self.submitted.append((function, args))
        return future

    def shutdown(self, wait=True):
        assert wait
        self.closed = True


def make_syncer(tmp_path):
    calls = []
    executor = FakePushExecutor()

    def sync(message, prepare_only=False):
        calls.append((message, prepare_only))
        return True

    syncer = gpu_search.AsyncCheckpointSync(tmp_path, sync, executor=executor)
    return syncer, executor, calls


def test_async_git_busy_push_coalesces_new_commits(tmp_path):
    syncer, executor, calls = make_syncer(tmp_path)
    assert syncer.checkpoint('50k')
    assert syncer.checkpoint('100k')
    assert calls == [('50k', True), ('100k', True)]
    assert len(executor.futures) == 1  # No second network operation while busy.
    executor.futures[0].set_result(True)
    assert syncer.checkpoint('150k')
    assert calls[-1] == ('150k', True)
    assert len(executor.futures) == 2
    # The worker receives only the network-push function, never commit/rebase.
    assert all(function is gpu_search._push_checkpoint for function, _ in executor.submitted)
    executor.futures[-1].set_result(True)
    assert syncer.finish('final')
    assert calls[-1] == ('final', False)
    assert executor.closed


def test_async_git_failed_push_recovers_on_controller_after_preparing(tmp_path):
    syncer, executor, calls = make_syncer(tmp_path)
    syncer.checkpoint('50k')
    executor.futures[0].set_result(False)
    assert syncer.checkpoint('100k')
    assert calls == [('50k', True), ('100k', True), ('100k', False)]
    assert len(executor.futures) == 1
    syncer.finish('final')


def test_async_git_shutdown_pushes_latest_commit_after_busy_push(tmp_path):
    syncer, executor, calls = make_syncer(tmp_path)
    syncer.checkpoint('50k')
    syncer.checkpoint('100k')
    executor.futures[0].set_result(True)
    assert syncer.finish('latest at shutdown')
    assert calls == [('50k', True), ('100k', True), ('latest at shutdown', False)]
    assert executor.closed


def test_git_prepare_only_does_not_start_network_or_rebase(tmp_path, monkeypatch):
    from src import search
    monkeypatch.setattr(search, 'ROOT', tmp_path)
    (tmp_path / 'runs').mkdir()
    calls = []
    differences = iter([0, 1])

    def git(command, **kwargs):
        calls.append(command[1:])
        code = next(differences) if command[1] == 'diff' else 0
        return subprocess.CompletedProcess(command, code, stdout='', stderr='')

    monkeypatch.setattr(search.subprocess, 'run', git)
    assert search.sync_git('checkpoint', prepare_only=True)
    assert ['commit', '-m', 'checkpoint'] in calls
    assert not any(command[0] in ('push', 'pull', 'rebase') for command in calls)
