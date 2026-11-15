import random

import networkx as nx
import pytest

from src.graphs import mutate_batch, screen_graph, seed_graphs


def matrix(graph):
    return [[int(graph.has_edge(u, v)) for v in graph] for u in graph]


def assert_simple(adjacency):
    n = len(adjacency)
    assert all(len(row) == n for row in adjacency)
    assert all(adjacency[u][u] == 0 for u in range(n))
    assert all(adjacency[u][v] in (0, 1) and adjacency[u][v] == adjacency[v][u]
               for u in range(n) for v in range(n))


def test_seeds_are_bounded_simple_and_structured():
    seeds = dict(seed_graphs(25))
    assert {"odd_cycle_5", "mycielski_C5_1", "mycielski_C5_2", "petersen", "chvatal"} <= seeds.keys()
    assert "hoffman_singleton" not in seeds
    for adjacency in seeds.values():
        assert len(adjacency) <= 25
        assert_simple(adjacency)
    grotzsch = seeds["mycielski_C5_1"]
    assert len(grotzsch) == 11
    assert sum(map(sum, grotzsch)) // 2 == 20
    assert all(not (grotzsch[a][b] and grotzsch[a][c] and grotzsch[b][c])
               for a in range(11) for b in range(a) for c in range(b))


def test_swaps_preserve_individual_degrees_and_create_new_graphs():
    parent = matrix(nx.petersen_graph())
    children = mutate_batch([parent], 48, random.Random(1234), swap_attempts=12)
    assert len(children) == 48
    assert any(child != parent for child in children)
    for child in children:
        assert_simple(child)
        assert list(map(sum, child)) == list(map(sum, parent))
    assert parent == matrix(nx.petersen_graph())  # input is not mutated


def test_mixed_size_and_edge_case_parents():
    parents = [[], [[0]], matrix(nx.empty_graph(6)), matrix(nx.complete_graph(5)), matrix(nx.path_graph(7))]
    children = mutate_batch(parents, 80, random.Random(16))
    expected = {len(p): list(map(sum, p)) for p in parents}
    for child in children:
        assert_simple(child)
        assert list(map(sum, child)) == expected[len(child)]


def test_seeded_mutation_is_repeatable():
    parents = [matrix(nx.cycle_graph(9)), matrix(nx.petersen_graph())]
    assert mutate_batch(parents, 12, random.Random(1)) == mutate_batch(parents, 12, random.Random(1))


def test_screen_bounds_known_graphs():
    for graph, chromatic, clique in [
        (nx.empty_graph(0), 0, 0),
        (nx.empty_graph(5), 1, 1),
        (nx.complete_graph(5), 5, 5),
        (nx.cycle_graph(5), 3, 2),
        (nx.petersen_graph(), 3, 2),
        (nx.mycielskian(nx.cycle_graph(5)), 4, 2),
    ]:
        screen = screen_graph(matrix(graph))
        assert screen["clique_lower_bound"] <= clique
        assert screen["coloring_upper_bound"] >= chromatic
        actual_gap = chromatic - (screen["max_degree"] + clique + 2) // 2
        assert screen["optimistic_gap"] >= actual_gap


@pytest.mark.parametrize("bad", [[[1]], [[0, 1], [0, 0]], [[0, 2], [2, 0]], [[0, 1]]])
def test_invalid_graphs_are_rejected(bad):
    with pytest.raises(ValueError):
        screen_graph(bad)
    with pytest.raises(ValueError):
        mutate_batch([bad], 1, random.Random(1))


def test_empty_batch_and_missing_parents():
    assert mutate_batch([], 0, random.Random(1)) == []
    with pytest.raises(ValueError):
        mutate_batch([], 1, random.Random(1))
