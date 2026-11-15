"""Search orchestration checks, including fail-closed discovery handling."""
import json
from pathlib import Path
import signal
import shutil
import subprocess
import sys
import time
from types import SimpleNamespace

import pytest

from src import search


ROOT = Path(__file__).resolve().parents[1]
CYCLE5 = [[int((u - v) % 5 in (1, 4)) for v in range(5)] for u in range(5)]
EXACT_CYCLE = dict(status="exact", n=5, edges=5, max_degree=2, omega=2,
                   chi=3, reed_bound=3, gap=0, coloring=[0, 1, 0, 1, 2], clique=[0, 1],
                   elapsed_seconds=0.001)


@pytest.fixture
def harness(tmp_path, monkeypatch):
    saved = {sig: signal.getsignal(sig) for sig in (signal.SIGINT, signal.SIGTERM)}
    monkeypatch.setattr(search, "seed_graphs", lambda maximum: [("cycle5", CYCLE5)])

    def no_more_mutations(*args, **kwargs):
        time.sleep(0.04)
        return []

    monkeypatch.setattr(search, "mutate_batch", no_more_mutations)
    args = SimpleNamespace(seed=123, seconds=0.03, device="cpu", output_dir=str(tmp_path),
                           max_vertices=5, batch_size=4, solver_seconds=1.0,
                           progress_seconds=600.0, sync=False)
    yield args, tmp_path
    for sig, handler in saved.items():
        signal.signal(sig, handler)


def read_summary(output):
    paths = list((output / "runs").glob("*/summary.json"))
    assert len(paths) == 1
    return json.loads(paths[0].read_text())


def test_screen_skip_does_not_call_exact_solver(harness, monkeypatch):
    args, output = harness
    monkeypatch.setattr(search, "screen_graph", lambda a: {"optimistic_gap": -2})
    monkeypatch.setattr(search, "verify_graph", lambda *a, **k: pytest.fail("screened-out graph solved"))
    assert search.run(args) == 0
    summary = read_summary(output)
    assert summary["screened_out"] == 1
    assert summary["exact_calls"] == 0
    assert summary["best_gap"] is None


def test_unknown_solver_result_is_not_saved_as_verified(harness, monkeypatch):
    args, output = harness
    monkeypatch.setattr(search, "verify_graph", lambda *a, **k: dict(status="unknown", gap=None))
    monkeypatch.setattr(search, "verify_independently", lambda *a, **k: pytest.fail("unknown independently checked"))
    assert search.run(args) == 0
    summary = read_summary(output)
    assert summary["unknown"] == 1
    assert summary["exact"] == 0
    assert not (output / "best_candidates").exists()
    assert not (output / "COUNTEREXAMPLE").exists()


def test_exact_tight_candidate_is_saved_with_both_results(harness, monkeypatch):
    args, output = harness
    monkeypatch.setattr(search, "verify_graph", lambda *a, **k: EXACT_CYCLE.copy())
    monkeypatch.setattr(search, "verify_independently", lambda *a, **k: EXACT_CYCLE.copy())
    assert search.run(args) == 0
    paths = list((output / "best_candidates").glob("*.json"))
    assert len(paths) == 1
    payload = json.loads(paths[0].read_text())
    assert payload["adjacency"] == CYCLE5
    assert payload["verification"]["gap"] == 0
    assert payload["independent_verification"]["gap"] == 0
    assert read_summary(output)["independent_agreements"] == 1


def test_mocked_positive_gap_requires_independent_agreement_and_halts(harness, monkeypatch):
    # Synthetic solver results exercise routing only, not a mathematical claim.
    args, output = harness
    synthetic = EXACT_CYCLE | {"chi": 4, "gap": 1}
    monkeypatch.setattr(search, "verify_graph", lambda *a, **k: synthetic.copy())
    monkeypatch.setattr(search, "verify_independently", lambda *a, **k: synthetic.copy())
    monkeypatch.setattr(search, "mutate_batch", lambda *a, **k: pytest.fail("continued after discovery"))
    assert search.run(args) == 0
    summary = read_summary(output)
    assert summary["counterexample_verified"] is True
    assert summary["reason"] == "counterexample"
    assert len(list((output / "COUNTEREXAMPLE").glob("*.json"))) == 1
    assert (output / "COUNTEREXAMPLE" / "verify.py").is_file()
    assert "counterexample" in (output / "README.md").read_text()


def test_positive_gap_with_unknown_independent_check_is_unconfirmed(harness, monkeypatch):
    args, output = harness
    synthetic = EXACT_CYCLE | {"chi": 4, "gap": 1}
    monkeypatch.setattr(search, "verify_graph", lambda *a, **k: synthetic.copy())
    monkeypatch.setattr(search, "verify_independently", lambda *a, **k: {"status": "unknown"})
    assert search.run(args) == 0
    assert not (output / "COUNTEREXAMPLE").exists()
    assert len(list((output / "runs").glob("*/unconfirmed-*.json"))) == 1
    assert read_summary(output)["counterexample_verified"] is False


def test_solver_disagreement_halts_without_counterexample(harness, monkeypatch):
    args, output = harness
    monkeypatch.setattr(search, "verify_graph", lambda *a, **k: EXACT_CYCLE.copy())
    monkeypatch.setattr(search, "verify_independently", lambda *a, **k: EXACT_CYCLE | {"chi": 4})
    with pytest.raises(RuntimeError, match="disagree"):
        search.run(args)
    assert not (output / "COUNTEREXAMPLE").exists()
    assert len(list((output / "runs").glob("*/disagreement-*.json"))) == 1


def test_exact_result_at_runtime_deadline_still_checkpoints(harness, monkeypatch):
    args, output = harness

    def complete_after_deadline(*a, **k):
        time.sleep(0.04)
        return EXACT_CYCLE.copy()

    monkeypatch.setattr(search, "verify_graph", complete_after_deadline)
    assert search.run(args) == 0
    assert read_summary(output)["reason"] == "runtime limit"
    assert not (output / "COUNTEREXAMPLE").exists()


def test_git_transient_push_rebases_and_retries(tmp_path, monkeypatch):
    monkeypatch.setattr(search, "ROOT", tmp_path)
    (tmp_path / "src").mkdir()
    calls = []
    push_count = 0
    diff_count = 0

    def git(command, **kwargs):
        nonlocal push_count, diff_count
        calls.append(command[1:])
        code = 0
        if command[1] == "diff":
            diff_count += 1
            code = int(diff_count == 2)
        if command[1] == "push":
            push_count += 1
            code = int(push_count == 1)
        return subprocess.CompletedProcess(command, code, stdout="", stderr="temporary failure" if code else "")

    monkeypatch.setattr(search.subprocess, "run", git)
    assert search.sync_git("test checkpoint") is True
    assert ["pull", "--rebase", "origin", "main"] in calls
    assert push_count == 2


def test_git_timeout_does_not_crash_search(tmp_path, monkeypatch):
    monkeypatch.setattr(search, "ROOT", tmp_path)

    def timeout(*args, **kwargs):
        raise subprocess.TimeoutExpired("git", 90)

    monkeypatch.setattr(search.subprocess, "run", timeout)
    assert search.sync_git("test checkpoint") is False


def test_failed_commit_unstages_its_own_files_for_later_retry(tmp_path, monkeypatch):
    monkeypatch.setattr(search, "ROOT", tmp_path)
    (tmp_path / "src").mkdir()
    calls = []
    staged = False

    def git(command, **kwargs):
        nonlocal staged
        calls.append(command[1:])
        code = 0
        if command[1] == "diff":
            code = int(staged)
        elif command[1] == "add":
            staged = True
        elif command[1] == "commit":
            code = 1
        elif command[1] == "reset":
            staged = False
        return subprocess.CompletedProcess(command, code, stdout="", stderr="")

    monkeypatch.setattr(search.subprocess, "run", git)
    assert search.sync_git("test checkpoint") is False
    assert staged is False
    assert ["reset", "--", "src"] in calls
    assert not any(command[0] == "push" for command in calls)


def test_preexisting_staged_changes_are_not_committed(tmp_path, monkeypatch):
    monkeypatch.setattr(search, "ROOT", tmp_path)
    calls = []

    def staged(command, **kwargs):
        calls.append(command)
        return subprocess.CompletedProcess(command, 1, stdout="", stderr="")

    monkeypatch.setattr(search.subprocess, "run", staged)
    assert search.sync_git("test checkpoint") is False
    assert calls == [["git", "diff", "--cached", "--quiet"]]


def test_real_cpu_cli_run_writes_verified_checkpoint(tmp_path):
    # Copy the executable source into a disposable checkout so this test also
    # works while a real search holds the original checkout's process lock.
    project = tmp_path / "project"
    project.mkdir()
    shutil.copytree(ROOT / "src", project / "src", ignore=shutil.ignore_patterns("__pycache__"))
    for command in (["git", "init"], ["git", "add", "src"],
                    ["git", "-c", "user.name=Test", "-c", "user.email=test@example.invalid",
                     "commit", "-m", "test fixture"]):
        subprocess.run(command, cwd=project, check=True, capture_output=True, timeout=10)
    output = tmp_path / "output"
    completed = subprocess.run(
        [sys.executable, "-m", "src.search", "--device", "cpu", "--seconds", "0.3",
         "--max-vertices", "5", "--batch-size", "4", "--output-dir", str(output)],
        cwd=project, text=True, capture_output=True, timeout=30,
    )
    assert completed.returncode == 0, completed.stderr
    summary = read_summary(output)
    assert summary["device"] == "cpu"
    assert summary["exact"] >= 1
    assert summary["best_gap"] == 0
    assert summary["counterexample_verified"] is False
    for path in (output / "best_candidates").glob("*.json"):
        payload = json.loads(path.read_text())
        assert payload["verification"]["status"] == "exact"
        assert payload["verification"]["gap"] == 0


@pytest.mark.parametrize("option,value", [("--seconds", "nan"), ("--seconds", "inf"),
                                         ("--solver-seconds", "nan"), ("--progress-seconds", "inf")])
def test_cli_rejects_nonfinite_budgets(tmp_path, option, value):
    completed = subprocess.run(
        [sys.executable, "-m", "src.search", "--seconds", "0.01", option, value,
         "--output-dir", str(tmp_path)],
        cwd=ROOT, text=True, capture_output=True, timeout=15,
    )
    assert completed.returncode == 2, completed.stderr
    assert not (tmp_path / "runs").exists()
