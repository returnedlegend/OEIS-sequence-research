import random

import networkx as nx
import pytest
import torch

from src.constrained_graphs import is_triangle_free, mutate_triangle_free_batch


def matrix(graph):
    return [[int(graph.has_edge(u, v)) for v in graph] for u in graph]


def independent_triangle_check(adjacency):
    graph = nx.Graph()
    graph.add_nodes_from(range(len(adjacency)))
    graph.add_edges_from((u, v) for u, row in enumerate(adjacency)
                         for v, present in enumerate(row) if present)
    return not any(nx.triangles(graph).values())


def assert_simple(adjacency):
    n = len(adjacency)
    assert all(len(row) == n for row in adjacency)
    assert all(adjacency[u][u] == 0 for u in range(n))
    assert all(adjacency[u][v] in (0, 1) and adjacency[u][v] == adjacency[v][u]
               for u in range(n) for v in range(n))


@pytest.mark.parametrize("graph", [
    nx.chvatal_graph(), nx.mycielskian(nx.cycle_graph(5)),
    nx.petersen_graph(), nx.cycle_graph(9), nx.complete_bipartite_graph(3, 3),
])
def test_constrained_swaps_preserve_degrees_and_triangle_freeness(graph):
    parent = matrix(graph)
    children = mutate_triangle_free_batch([parent], 64, random.Random(1234), swap_attempts=32)
    for child in children:
        assert_simple(child)
        assert list(map(sum, child)) == list(map(sum, parent))
        assert independent_triangle_check(child)
    assert parent == matrix(graph)
    # Some saturated parents may admit no valid degree-preserving switch.
    if len(parent) in (9, 10, 11, 12):
        assert any(child != parent for child in children)


def test_all_small_triangle_free_graphs():
    # Test every unlabeled triangle-free graph on at most six vertices;
    # NetworkX's triangle counter is independent of the tensor rejection test.
    parents = [matrix(g) for g in nx.graph_atlas_g()
               if len(g) <= 6 and not any(nx.triangles(g).values())]
    assert len(parents) > 20
    for parent in parents:
        children = mutate_triangle_free_batch([parent], 5, random.Random(29))
        for child in children:
            assert_simple(child)
            assert list(map(sum, child)) == list(map(sum, parent))
            assert independent_triangle_check(child)


def test_mixed_sizes_edgeless_and_repeatability():
    parents = [[], [[0]], matrix(nx.empty_graph(6)), matrix(nx.path_graph(7)), matrix(nx.cycle_graph(9))]
    first = mutate_triangle_free_batch(parents, 60, random.Random(19))
    second = mutate_triangle_free_batch(parents, 60, random.Random(19))
    assert first == second
    degrees = {len(parent): list(map(sum, parent)) for parent in parents}
    for child in first:
        assert_simple(child)
        assert independent_triangle_check(child)
        assert list(map(sum, child)) == degrees[len(child)]


def test_rejects_triangles_and_malformed_inputs():
    triangle = matrix(nx.complete_graph(3))
    assert not is_triangle_free(triangle)
    with pytest.raises(ValueError, match="triangle-free"):
        mutate_triangle_free_batch([triangle], 1, random.Random(1))
    with pytest.raises(ValueError, match="square"):
        mutate_triangle_free_batch([[[0, 1]]], 1, random.Random(1))
    with pytest.raises(ValueError, match="symmetric"):
        mutate_triangle_free_batch([[[0, 1], [0, 0]]], 1, random.Random(1))


def test_empty_batch_and_invalid_arguments():
    assert mutate_triangle_free_batch([], 0, random.Random(1)) == []
    with pytest.raises(ValueError, match="parent"):
        mutate_triangle_free_batch([], 1, random.Random(1))
    with pytest.raises(ValueError, match="nonnegative"):
        mutate_triangle_free_batch([[]], -1, random.Random(1))
    with pytest.raises(ValueError, match="nonnegative"):
        mutate_triangle_free_batch([[]], 1, random.Random(1), swap_attempts=-1)


@pytest.mark.skipif(not torch.cuda.is_available(), reason="CUDA device unavailable")
def test_cuda_constrained_swaps():
    parent = matrix(nx.chvatal_graph())
    children = mutate_triangle_free_batch([parent], 32, random.Random(123), device="cuda")
    for child in children:
        assert_simple(child)
        assert list(map(sum, child)) == list(map(sum, parent))
        assert independent_triangle_check(child)
