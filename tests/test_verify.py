"""Cross-check exact optimization against elementary and brute-force cases."""
import itertools
import json
import subprocess
import sys

import networkx as nx
import pytest

from src.verify import verify_graph


def adjacency(graph):
    return nx.to_numpy_array(graph, dtype=int).tolist()


@pytest.mark.parametrize('graph,omega,chi,delta,gap', [
    (nx.empty_graph(0), 0, 0, 0, -1),
    (nx.empty_graph(5), 1, 1, 0, 0),
    (nx.complete_graph(6), 6, 6, 5, 0),
    (nx.cycle_graph(5), 2, 3, 2, 0),
    (nx.cycle_graph(6), 2, 2, 2, -1),
    (nx.petersen_graph(), 2, 3, 3, 0),
    (nx.mycielskian(nx.cycle_graph(5)), 2, 4, 5, 0),
    (nx.complete_bipartite_graph(4, 5), 2, 2, 5, -2),
])
def test_known_graphs(graph, omega, chi, delta, gap):
    result = verify_graph(adjacency(graph), time_limit=10)
    assert result['status'] == 'exact'
    assert (result['omega'], result['chi'], result['max_degree'], result['gap']) == (omega, chi, delta, gap)
    assert all(graph.has_edge(u, v) for u, v in itertools.combinations(result['clique'], 2))
    assert all(result['coloring'][u] != result['coloring'][v] for u, v in graph.edges())


def brute_invariants(matrix):
    n = len(matrix)
    omega = max((len(vertices) for size in range(n + 1)
                 for vertices in itertools.combinations(range(n), size)
                 if all(matrix[u][v] for u, v in itertools.combinations(vertices, 2))), default=0)
    if n == 0:
        return omega, 0
    for k in range(1, n + 1):
        for colors in itertools.product(range(k), repeat=n):
            if all(not matrix[u][v] or colors[u] != colors[v]
                   for u in range(n) for v in range(u)):
                return omega, k
    raise AssertionError('every finite graph is n-colorable')


def test_every_labeled_graph_through_four_vertices():
    checked = 0
    for n in range(5):
        pairs = list(itertools.combinations(range(n), 2))
        for mask in range(1 << len(pairs)):
            matrix = [[0] * n for _ in range(n)]
            for bit, (u, v) in enumerate(pairs):
                matrix[u][v] = matrix[v][u] = int(bool(mask & (1 << bit)))
            expected = brute_invariants(matrix)
            result = verify_graph(matrix)
            assert result['status'] == 'exact'
            assert (result['omega'], result['chi']) == expected
            checked += 1
    assert checked == 76


@pytest.mark.parametrize('matrix', [
    [[1]], [[0, 1], [0, 0]], [[0, 1]], [[0, 2], [2, 0]],
    [[0.0]], 'not a matrix', [None],
])
def test_rejects_invalid_graphs(matrix):
    with pytest.raises(ValueError):
        verify_graph(matrix)


def test_expired_budget_does_not_claim_a_gap():
    result = verify_graph(adjacency(nx.cycle_graph(5)), time_limit=0)
    assert result['status'] == 'unknown'
    assert result['omega'] is None
    assert result['chi'] is None
    assert result['gap'] is None


@pytest.mark.parametrize('limit', [-1, float('inf'), float('nan')])
def test_invalid_time_limits(limit):
    with pytest.raises(ValueError):
        verify_graph([], time_limit=limit)


def test_cli_recomputes_and_rejects_fabricated_claim(tmp_path):
    path = tmp_path / 'candidate.json'
    data = {'adjacency': adjacency(nx.cycle_graph(5)), 'verification': {'chi': 4, 'gap': 1}}
    path.write_text(json.dumps(data))
    process = subprocess.run([sys.executable, '-m', 'src.verify', str(path)],
                             text=True, capture_output=True)
    assert process.returncode == 1, process.stderr
    result = json.loads(process.stdout)
    assert result['chi'] == 3
    assert result['gap'] == 0
    assert set(result['claim_mismatches']) == {'chi', 'gap'}


def test_feasible_clique_solution_is_not_exact(monkeypatch):
    from types import SimpleNamespace
    from src import verify

    class IncompleteSolver:
        def __init__(self):
            self.parameters = SimpleNamespace()

        def Solve(self, model):
            return verify.cp_model.FEASIBLE

        def Value(self, variable):
            raise AssertionError('an unproven optimum must not be used')

    monkeypatch.setattr(verify.cp_model, 'CpSolver', IncompleteSolver)
    result = verify_graph(adjacency(nx.cycle_graph(5)))
    assert result['status'] == 'unknown'
    assert result['omega'] is None and result['chi'] is None and result['gap'] is None


def test_color_timeout_retains_only_proven_clique(monkeypatch):
    from types import SimpleNamespace
    from src import verify
    original_solver = verify.cp_model.CpSolver
    calls = 0

    class IncompleteSolver:
        def __init__(self):
            self.parameters = SimpleNamespace()

        def Solve(self, model):
            return verify.cp_model.UNKNOWN

    def solver_factory():
        nonlocal calls
        calls += 1
        return original_solver() if calls == 1 else IncompleteSolver()

    monkeypatch.setattr(verify.cp_model, 'CpSolver', solver_factory)
    result = verify_graph(adjacency(nx.cycle_graph(5)))
    assert calls == 2
    assert result['status'] == 'unknown'
    assert result['omega'] == 2 and result['reed_bound'] == 3
    assert result['chi'] is None and result['gap'] is None
