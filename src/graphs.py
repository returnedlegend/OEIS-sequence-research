"""Structured graph seeds, tensor mutations, and non-certifying screening.

Graphs are symmetric square binary adjacency matrices with a zero diagonal.
Screening produces a *possible* Reed gap using a coloring upper bound and a
clique lower bound; it never establishes the chromatic or clique number.
"""
from __future__ import annotations

from collections import defaultdict
import random
from typing import Iterator

import networkx as nx

Adjacency = list[list[int]]


def _validate(adjacency: Adjacency) -> None:
    n = len(adjacency)
    if any(len(row) != n for row in adjacency):
        raise ValueError("adjacency must be square")
    for u, row in enumerate(adjacency):
        if row[u] != 0:
            raise ValueError("self-loops are not allowed")
        for v, value in enumerate(row):
            if value not in (0, 1) or value != adjacency[v][u]:
                raise ValueError("adjacency must be symmetric and binary")


def _matrix(graph: nx.Graph) -> Adjacency:
    vertices = list(graph.nodes)
    return [[int(graph.has_edge(u, v)) for v in vertices] for u in vertices]


def seed_graphs(max_vertices: int = 40) -> Iterator[tuple[str, Adjacency]]:
    """Yield a bounded, deterministic mix of structured simple graphs.

    Mycielski constructions preserve clique number while increasing chromatic
    number; their degree growth is explicitly left for the exact verifier to
    assess. Circulants and ladders supply regular parents for edge switches.
    Labels and graph bytes are deduplicated; isomorphism is not tested here.
    """
    if max_vertices < 0:
        raise ValueError("max_vertices must be nonnegative")
    seen: set[tuple[tuple[int, ...], ...]] = set()

    def add(name: str, graph: nx.Graph):
        if len(graph) > max_vertices:
            return
        adjacency = _matrix(graph)
        key = tuple(map(tuple, adjacency))
        if key not in seen:
            seen.add(key)
            yield name, adjacency

    for n in range(3, min(max_vertices, 31) + 1, 2):
        yield from add(f"odd_cycle_{n}", nx.cycle_graph(n))
    for n in range(2, min(max_vertices, 6) + 1):
        yield from add(f"complete_{n}", nx.complete_graph(n))
    for base_name, base in (("C5", nx.cycle_graph(5)), ("K3", nx.complete_graph(3))):
        graph = base
        for iteration in range(1, 4):
            if 2 * len(graph) + 1 > max_vertices:
                break
            graph = nx.mycielskian(graph)
            yield from add(f"mycielski_{base_name}_{iteration}", graph)
    yield from add("petersen", nx.petersen_graph())
    yield from add("chvatal", nx.chvatal_graph())
    yield from add("hoffman_singleton", nx.hoffman_singleton_graph())
    for n in (6, 8, 10, 12, 14, 16, 20, 24, 28, 32, 40):
        if n <= max_vertices:
            yield from add(f"mobius_ladder_{n}", nx.circulant_graph(n, [1, n // 2]))
    for n in (7, 9, 11, 13, 15, 17, 19, 23, 27, 31, 35, 39):
        if n > max_vertices:
            continue
        for step in (2, 3, 4):
            if step <= n // 2:
                yield from add(f"circulant_{n}_1_{step}", nx.circulant_graph(n, [1, step]))
    # Andrasfai graphs: triangle-free, regular, and 3-chromatic for k >= 2.
    for k in range(2, min(10, (max_vertices + 1) // 3) + 1):
        yield from add(f"andrasfai_{k}", nx.circulant_graph(3 * k - 1, range(1, 3 * k - 1, 3)))
    for side in (2, 3, 4, 5, 8):
        if 2 * side <= max_vertices:
            yield from add(f"complete_bipartite_{side}_{side}", nx.complete_bipartite_graph(side, side))


def mutate_batch(
    parents: list[Adjacency],
    batch_size: int,
    rng: random.Random,
    device: str = "cpu",
    swap_attempts: int = 8,
) -> list[Adjacency]:
    """Sample parents and perform batched degree-preserving double-edge swaps.

    Existing directed edges (a,b), (c,d) are sampled with PyTorch. A swap to
    (a,d), (c,b) is accepted only when all endpoints differ and neither new
    edge exists. This preserves each vertex's degree, symmetry and simplicity.
    Connectivity, triangle-freeness and clique number are *not* preserved.
    Failed proposals leave that graph unchanged. Output order follows sampled
    parent order. An unavailable requested CUDA device raises an error rather
    than silently pretending to use a GPU.
    """
    if batch_size < 0 or swap_attempts < 0:
        raise ValueError("batch_size and swap_attempts must be nonnegative")
    if batch_size == 0:
        return []
    if not parents:
        raise ValueError("at least one parent is required")
    for parent in parents:
        _validate(parent)

    import torch

    requested_device = torch.device(device)
    if requested_device.type == "cuda" and not torch.cuda.is_available():
        raise RuntimeError("CUDA was requested but no CUDA device is available")
    generator = torch.Generator(device=requested_device)
    generator.manual_seed(rng.getrandbits(63))
    groups: dict[int, list[tuple[int, Adjacency]]] = defaultdict(list)
    for output_index in range(batch_size):
        parent = rng.choice(parents)
        groups[len(parent)].append((output_index, parent))
    outputs: list[Adjacency | None] = [None] * batch_size

    for n, members in groups.items():
        if n < 4:
            for output_index, parent in members:
                outputs[output_index] = [row[:] for row in parent]
            continue
        tensor = torch.tensor([p for _, p in members], dtype=torch.bool, device=requested_device)
        batch_indices = torch.arange(len(members), device=requested_device)
        for _ in range(swap_attempts):
            weights = tensor.reshape(len(members), n * n).float()
            # torch.multinomial requires nonzero row weights. An edgeless
            # graph receives a dummy loop sample which always fails validity.
            weights[weights.sum(dim=1) == 0, 0] = 1
            edges = torch.multinomial(weights, 2, replacement=True, generator=generator)
            a, b = edges[:, 0] // n, edges[:, 0] % n
            c, d = edges[:, 1] // n, edges[:, 1] % n
            valid = (a != b) & (a != c) & (a != d) & (b != c) & (b != d) & (c != d)
            valid &= ~tensor[batch_indices, a, d] & ~tensor[batch_indices, c, b]
            chosen = batch_indices[valid]
            aa, bb, cc, dd = a[valid], b[valid], c[valid], d[valid]
            tensor[chosen, aa, bb] = False
            tensor[chosen, bb, aa] = False
            tensor[chosen, cc, dd] = False
            tensor[chosen, dd, cc] = False
            tensor[chosen, aa, dd] = True
            tensor[chosen, dd, aa] = True
            tensor[chosen, cc, bb] = True
            tensor[chosen, bb, cc] = True
        for (output_index, _), matrix in zip(members, tensor.to(dtype=torch.int8).cpu().tolist()):
            outputs[output_index] = matrix
    assert all(matrix is not None for matrix in outputs)
    return outputs  # type: ignore[return-value]


def screen_graph(adjacency: Adjacency) -> dict[str, int]:
    """Return certified one-sided bounds, not exact graph invariants.

    The optimistic gap upper-bounds the actual Reed gap. A negative screen
    therefore cannot conceal a positive actual gap; a nonnegative screen is
    only a reason to call the exact verifier.
    """
    _validate(adjacency)
    n = len(adjacency)
    graph = nx.Graph()
    graph.add_nodes_from(range(n))
    graph.add_edges_from((u, v) for u in range(n) for v in range(u + 1, n) if adjacency[u][v])
    maximum_degree = max((degree for _, degree in graph.degree()), default=0)
    coloring_upper_bound = n
    for strategy in ("saturation_largest_first", "largest_first"):
        coloring = nx.coloring.greedy_color(graph, strategy=strategy)
        coloring_upper_bound = min(coloring_upper_bound, max(coloring.values(), default=-1) + 1)
    order = sorted(graph, key=lambda v: (-graph.degree(v), v))
    clique_lower_bound = 0
    for first in order[:8]:
        clique = [first]
        for vertex in order:
            if vertex != first and all(adjacency[vertex][other] for other in clique):
                clique.append(vertex)
        clique_lower_bound = max(clique_lower_bound, len(clique))
    optimistic_bound = (maximum_degree + clique_lower_bound + 2) // 2
    return {
        "max_degree": maximum_degree,
        "clique_lower_bound": clique_lower_bound,
        "coloring_upper_bound": coloring_upper_bound,
        "optimistic_gap": coloring_upper_bound - optimistic_bound,
    }
