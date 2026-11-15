"""Persistent checks for the separately implemented, stdlib-only verifier."""
from itertools import combinations, product
import json
from pathlib import Path
import subprocess
import sys

import networkx as nx
import pytest

from src.independent_verify import verify_independently


def matrix(graph):
    vertices = list(graph)
    return [[int(graph.has_edge(u, v)) for v in vertices] for u in vertices]


@pytest.mark.parametrize("graph,omega,chi", [
    (nx.empty_graph(0), 0, 0), (nx.empty_graph(4), 1, 1),
    (nx.complete_graph(6), 6, 6), (nx.cycle_graph(5), 2, 3),
    (nx.cycle_graph(6), 2, 2), (nx.petersen_graph(), 2, 3),
    (nx.mycielskian(nx.cycle_graph(5)), 2, 4),
])
def test_known_exact_invariants_and_witnesses(graph, omega, chi):
    adjacency = matrix(graph)
    result = verify_independently(adjacency)
    assert result["status"] == "exact"
    assert (result["omega"], result["chi"]) == (omega, chi)
    assert all(adjacency[u][v] for u, v in combinations(result["clique"], 2))
    assert all(not adjacency[u][v] or result["coloring"][u] != result["coloring"][v]
               for u, v in combinations(range(len(adjacency)), 2))
    assert result["reed_bound"] == (result["max_degree"] + omega + 2) // 2
    assert result["gap"] == chi - result["reed_bound"]


def test_exhaustive_small_graphs_against_literal_enumeration():
    for n in range(5):
        pairs = list(combinations(range(n), 2))
        for edge_bits in range(1 << len(pairs)):
            adjacency = [[0] * n for _ in range(n)]
            for bit, (u, v) in enumerate(pairs):
                adjacency[u][v] = adjacency[v][u] = (edge_bits >> bit) & 1
            omega = max(len(c) for size in range(n + 1)
                        for c in combinations(range(n), size)
                        if all(adjacency[u][v] for u, v in combinations(c, 2)))
            chi = next(k for k in range(n + 1)
                       if any(all(not adjacency[u][v] or colors[u] != colors[v]
                                  for u, v in pairs)
                              for colors in product(range(k), repeat=n)))
            result = verify_independently(adjacency)
            assert (result["omega"], result["chi"]) == (omega, chi)


def test_timeout_never_becomes_a_coloring_impossibility_claim():
    result = verify_independently(matrix(nx.mycielskian(nx.cycle_graph(5))), 1e-20)
    assert result["status"] == "unknown"
    assert result["chi"] is None
    assert result["gap"] is None


@pytest.mark.parametrize("adjacency", [[[1]], [[0, 1], [0, 0]], [[0, 2], [2, 0]], [[0], []]])
def test_malformed_graphs_rejected(adjacency):
    with pytest.raises(ValueError):
        verify_independently(adjacency)


def test_copied_standalone_script_rejects_false_claim(tmp_path):
    source = Path(__file__).resolve().parents[1] / "src" / "independent_verify.py"
    script = tmp_path / "verify.py"
    script.write_text(source.read_text())
    candidate = tmp_path / "candidate.json"
    candidate.write_text(json.dumps({"adjacency": matrix(nx.cycle_graph(5)),
                                     "verification": {"chi": 4, "gap": 1}}))
    completed = subprocess.run([sys.executable, "-I", str(script), str(candidate)],
                               cwd=tmp_path, text=True, capture_output=True, timeout=10)
    assert completed.returncode == 3
    result = json.loads(completed.stdout)
    assert result["chi"] == 3
    assert set(result["claim_mismatches"]) == {"chi", "gap"}
