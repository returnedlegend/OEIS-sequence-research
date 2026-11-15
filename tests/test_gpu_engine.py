"""Independent invariants for GPU generation and coloring certificates."""
import itertools

import networkx as nx
import pytest
import torch

from src.gpu_engine import (
    TriangleFreeGPUGenerator, certified_screen, greedy_color_batch,
    mutate_tensor, select_candidates,
)


def matrix(graph):
    return [[int(graph.has_edge(u, v)) for v in graph] for u in graph]


def tensor(graphs, device="cpu"):
    return torch.tensor([matrix(g) for g in graphs], dtype=torch.bool, device=device)


def assert_proper(graph, colors):
    assert len(colors) == len(graph)
    assert all(colors[u] != colors[v] for u, v in graph.edges())
    assert all(0 <= color < len(graph) for color in colors)


def brute_chi(graph):
    for k in range(len(graph) + 1):
        for colors in itertools.product(range(k), repeat=len(graph)):
            if all(colors[u] != colors[v] for u, v in graph.edges()):
                return k
    raise AssertionError("every graph is n-colorable")


def test_coloring_certificate_upper_bounds_every_small_graph():
    generator = torch.Generator().manual_seed(7)
    for n in range(1, 7):
        graphs = [g for g in nx.graph_atlas_g() if len(g) == n]
        batch = tensor(graphs)
        colors, upper = greedy_color_batch(batch, trials=3, generator=generator)
        screen = certified_screen(batch, colors)
        assert torch.equal(screen["coloring_upper_bound"], upper)
        for g, coloring, bound, optimistic in zip(
                graphs, colors.tolist(), upper.tolist(), screen["optimistic_gap"].tolist()):
            assert_proper(g, coloring)
            assert bound == max(coloring) + 1
            if n <= 4:
                chi = brute_chi(g)
                omega = max(map(len, nx.find_cliques(g)), default=0)
                gap = chi - (max(dict(g.degree()).values(), default=0) + omega + 2) // 2
                assert optimistic >= gap


def test_empty_graph_batch_has_valid_conventions():
    adjacency = torch.empty((3, 0, 0), dtype=torch.bool)
    colors, upper = greedy_color_batch(adjacency)
    assert colors.shape == (3, 0)
    assert upper.tolist() == [0, 0, 0]
    assert certified_screen(adjacency, colors)["optimistic_gap"].tolist() == [-1, -1, -1]


def test_connected_bipartite_cube_gets_two_color_certificate():
    # Degree-only randomized ordering wastes a color on this fixture. Choosing
    # maximum saturation first follows the connected bipartite frontier.
    adjacency = tensor([nx.cubical_graph()])
    colors, upper = greedy_color_batch(adjacency, trials=1,
                                      generator=torch.Generator().manual_seed(2))
    assert upper.tolist() == [2]
    assert_proper(nx.cubical_graph(), colors[0].tolist())


def test_invalid_coloring_certificate_fails_closed():
    adjacency = tensor([nx.cycle_graph(5)])
    with pytest.raises(RuntimeError, match="coloring"):
        certified_screen(adjacency, torch.zeros((1, 5), dtype=torch.long))
    with pytest.raises(RuntimeError, match="coloring"):
        certified_screen(adjacency, torch.full((1, 5), -1, dtype=torch.long))


@pytest.mark.parametrize("graph", [nx.chvatal_graph(), nx.petersen_graph(),
                                   nx.mycielskian(nx.cycle_graph(5)),
                                   nx.complete_bipartite_graph(3, 3), nx.empty_graph(6)])
def test_resident_mutations_preserve_degrees_and_triangle_freeness(graph):
    original = tensor([graph] * 64)
    mutated = mutate_tensor(original, torch.Generator().manual_seed(123), swap_attempts=32)
    assert torch.equal(mutated.sum(1), original.sum(1))
    assert torch.equal(original, tensor([graph] * 64))
    for adjacency in mutated.tolist():
        child = nx.from_numpy_array(torch.tensor(adjacency).numpy())
        assert not any(nx.triangles(child).values())
        assert all(not adjacency[i][i] for i in range(len(graph)))
        assert all(adjacency[i][j] == adjacency[j][i] for i in range(len(graph)) for j in range(len(graph)))
    if len(graph) in (10, 11, 12):
        assert not torch.equal(original, mutated)


def test_selection_never_drops_potential_candidates_and_samples_safe_audits():
    graphs = [nx.cycle_graph(5)] * 9
    adjacency = tensor(graphs)
    # Distinct valid colors prove only the weak upper bound chi <= 5.
    colors = torch.arange(5).repeat(9, 1)
    screen = certified_screen(adjacency, colors)
    result = select_candidates(adjacency, screen, audit_size=0, generator=torch.Generator().manual_seed(7))
    assert result["potential_count"] == 9
    assert len(result["candidates"]) == 9
    assert all(c["kind"] == "potential" for c in result["candidates"])
    colors, _ = greedy_color_batch(adjacency)
    result = select_candidates(adjacency, certified_screen(adjacency, colors),
                               audit_size=2, generator=torch.Generator().manual_seed(7))
    assert result["certified_nonviolations"] == 9
    assert result["audit_eligible"] == 9
    assert len(result["candidates"]) == 2
    assert all(c["kind"] == "audit" for c in result["candidates"])


def test_generator_is_repeatable_and_cycles_resident_graph_orders():
    parents = [matrix(nx.chvatal_graph()), matrix(nx.petersen_graph())]
    first = TriangleFreeGPUGenerator(parents, batch_size=32, seed=7, device="cpu")
    second = TriangleFreeGPUGenerator(parents, batch_size=32, seed=7, device="cpu")
    orders = set()
    for _ in range(4):
        result = first.next_batch(audit_size=4)
        assert result == second.next_batch(audit_size=4)
        assert result["generated"] == 32
        assert result["certified_nonviolations"] + result["potential_count"] == 32
        orders.add(result["vertices"])
    assert orders == {10, 12}


def test_generator_rejects_invalid_or_triangular_parents():
    with pytest.raises(ValueError, match="triangle-free"):
        TriangleFreeGPUGenerator([matrix(nx.complete_graph(3))], device="cpu")
    with pytest.raises(ValueError, match="parent"):
        TriangleFreeGPUGenerator([], device="cpu")
    with pytest.raises(ValueError, match="positive"):
        TriangleFreeGPUGenerator([matrix(nx.cycle_graph(5))], batch_size=0, device="cpu")


@pytest.mark.skipif(not torch.cuda.is_available(), reason="CUDA device unavailable")
def test_cuda_mutation_and_coloring_certificates():
    graph = nx.chvatal_graph()
    adjacency = tensor([graph] * 256, "cuda")
    rng = torch.Generator(device="cuda").manual_seed(47)
    mutated = mutate_tensor(adjacency, rng, swap_attempts=12)
    colors, upper = greedy_color_batch(mutated, trials=3, generator=rng)
    screen = certified_screen(mutated, colors)
    assert torch.equal(adjacency.sum(1), mutated.sum(1))
    assert screen["max_degree"].device.type == "cuda"
    for mat, coloring, bound in zip(mutated.cpu().tolist(), colors.cpu().tolist(), upper.cpu().tolist()):
        child = nx.from_numpy_array(torch.tensor(mat).numpy())
        assert_proper(child, coloring)
        assert not any(nx.triangles(child).values())
        assert bound >= brute_chi(nx.cycle_graph(5))
