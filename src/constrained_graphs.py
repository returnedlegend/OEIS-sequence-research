"""Optional degree-preserving tensor mutations constrained to triangle-free graphs.

This module is separate from the baseline operator so comparative runs can
explicitly select their mutation policy. It makes no chromatic-number claims.
"""
from __future__ import annotations

from collections import defaultdict
import random

from .graphs import Adjacency, _validate


def is_triangle_free(adjacency: Adjacency) -> bool:
    """Validate simplicity and return whether no edge has a common neighbor."""
    _validate(adjacency)
    n = len(adjacency)
    return not any(
        adjacency[u][v] and any(adjacency[u][w] and adjacency[v][w] for w in range(n))
        for u in range(n) for v in range(u + 1, n)
    )


def mutate_triangle_free_batch(
    parents: list[Adjacency],
    batch_size: int,
    rng: random.Random,
    device: str = "cpu",
    swap_attempts: int = 8,
) -> list[Adjacency]:
    """Sample parents and apply only simple, triangle-free double-edge swaps.

    For each proposal remove (a,b), (c,d), then add (a,d), (c,b). Four distinct
    endpoints and absent replacement edges ensure simplicity and preserve
    every degree. Any newly introduced triangle must contain a new edge.
    Testing whether either new edge has a common neighbor in the proposed
    graph is therefore an exact rejection test. Each attempt is checked
    separately, retaining prior successful swaps instead of rejecting the
    entire sequence. All proposal and triangle tests use batched PyTorch
    tensors on the requested device.

    Parent triangle-freeness is checked exactly before generation. Failed
    proposals leave that child unchanged; connectivity and chromatic number
    are not guaranteed. CUDA unavailability raises explicitly. Fixed RNG
    seeds reproduce results on the same device, not necessarily across devices.
    """
    if batch_size < 0 or swap_attempts < 0:
        raise ValueError("batch_size and swap_attempts must be nonnegative")
    if batch_size == 0:
        return []
    if not parents:
        raise ValueError("at least one parent is required")
    if any(not is_triangle_free(parent) for parent in parents):
        raise ValueError("all parents must be triangle-free")

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
            # An edgeless row needs a nonzero sampling weight; its dummy loop
            # fails the distinct-endpoint check and cannot become an edge.
            weights[weights.sum(dim=1) == 0, 0] = 1
            edges = torch.multinomial(weights, 2, replacement=True, generator=generator)
            a, b = edges[:, 0] // n, edges[:, 0] % n
            c, d = edges[:, 1] // n, edges[:, 1] % n
            valid = (a != b) & (a != c) & (a != d) & (b != c) & (b != d) & (c != d)
            valid &= ~tensor[batch_indices, a, d] & ~tensor[batch_indices, c, b]
            chosen = batch_indices[valid]
            aa, bb, cc, dd = a[valid], b[valid], c[valid], d[valid]
            proposal = tensor.clone()
            proposal[chosen, aa, bb] = False
            proposal[chosen, bb, aa] = False
            proposal[chosen, cc, dd] = False
            proposal[chosen, dd, cc] = False
            proposal[chosen, aa, dd] = True
            proposal[chosen, dd, aa] = True
            proposal[chosen, cc, bb] = True
            proposal[chosen, bb, cc] = True
            # Only two row intersections per graph are needed, O(batch*n),
            # rather than a full adjacency-square multiplication.
            triangle_ad = (proposal[batch_indices, a, :] & proposal[batch_indices, d, :]).any(dim=1)
            triangle_cb = (proposal[batch_indices, c, :] & proposal[batch_indices, b, :]).any(dim=1)
            accepted = valid & ~triangle_ad & ~triangle_cb
            tensor = torch.where(accepted[:, None, None], proposal, tensor)
        matrices = tensor.to(dtype=torch.int8).cpu().tolist()
        for (output_index, _), matrix in zip(members, matrices):
            outputs[output_index] = matrix
    assert all(matrix is not None for matrix in outputs)
    return outputs  # type: ignore[return-value]
