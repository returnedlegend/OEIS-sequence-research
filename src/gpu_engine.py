"""Resident tensor search with checked proper-coloring certificates.

A proper coloring with U colors proves chi <= U. An edge proves omega >= 2,
so U - ceil((Delta + 3)/2) upper-bounds Reed's true gap. Every positive upper
bound is returned for exact verification. Nonpositive upper bounds certify
only nonviolation; they never establish exact chi or an exact gap.
"""
from __future__ import annotations

from collections import defaultdict

import torch

from .constrained_graphs import is_triangle_free


def _check_shape(adjacency):
    if adjacency.ndim != 3 or adjacency.shape[1] != adjacency.shape[2]:
        raise ValueError('adjacency must have shape (batch, n, n)')
    if adjacency.dtype != torch.bool:
        raise ValueError('adjacency must be a boolean tensor')


@torch.inference_mode()
def mutate_tensor(adjacency, generator, swap_attempts=8):
    """Triangle-free degree-preserving switches, without variable-size indexing.

Inputs must already be simple and triangle-free. Invalid proposals are masked
out in their entirety. The input is never modified.
"""
    _check_shape(adjacency)
    if swap_attempts < 0:
        raise ValueError('swap_attempts must be nonnegative')
    batch, n, _ = adjacency.shape
    result = adjacency.clone()
    if n < 4 or batch == 0:
        return result
    rows = torch.arange(batch, device=result.device)
    for _ in range(swap_attempts):
        weights = result.reshape(batch, n * n).float()
        # Dummy loop samples keep edgeless rows legal for multinomial; distinct
        # endpoints reject these samples before any mutation is accepted.
        weights[:, 0] = (weights.sum(1) == 0).to(weights.dtype)
        edges = torch.multinomial(weights, 2, replacement=True, generator=generator)
        a, b = edges[:, 0] // n, edges[:, 0] % n
        c, d = edges[:, 1] // n, edges[:, 1] % n
        valid = (a != b) & (a != c) & (a != d) & (b != c) & (b != d) & (c != d)
        valid &= ~result[rows, a, d] & ~result[rows, c, b]
        proposal = result.clone()
        proposal[rows, a, b] = False
        proposal[rows, b, a] = False
        proposal[rows, c, d] = False
        proposal[rows, d, c] = False
        proposal[rows, a, d] = True
        proposal[rows, d, a] = True
        proposal[rows, c, b] = True
        proposal[rows, b, c] = True
        triangle_ad = (proposal[rows, a] & proposal[rows, d]).any(1)
        triangle_cb = (proposal[rows, c] & proposal[rows, b]).any(1)
        accepted = valid & ~triangle_ad & ~triangle_cb
        result = torch.where(accepted[:, None, None], proposal, result)
    return result


@torch.inference_mode()
def greedy_color_batch(adjacency, trials=4, generator=None):
    """Parallel DSATUR greedy colorings, returning the best trial per graph.

Each step chooses the uncolored vertex seeing the most distinct neighboring
colors, then degree, then a randomized tie break. Saturation updates stay on
the GPU. All graphs/trials run together; vertex steps are serial. The output
must pass certified_screen before it is used for pruning.
"""
    _check_shape(adjacency)
    if trials < 1:
        raise ValueError('coloring trials must be positive')
    batch, n, _ = adjacency.shape
    if n == 0 or batch == 0:
        return (torch.empty((batch, n), device=adjacency.device, dtype=torch.long),
                torch.zeros(batch, device=adjacency.device, dtype=torch.long))
    work = adjacency.repeat(trials, 1, 1)
    count = work.shape[0]
    rows = torch.arange(count, device=work.device)
    tie_breaks = work.sum(2).float()
    tie_breaks += torch.rand((count, n), device=work.device, generator=generator)
    colors = torch.full((count, n), -1, device=work.device, dtype=torch.long)
    forbidden = torch.zeros((count, n, n), dtype=torch.bool, device=work.device)
    saturation = torch.zeros((count, n), dtype=torch.int32, device=work.device)
    for _ in range(n):
        priorities = saturation * (n + 1) + tie_breaks
        priorities.masked_fill_(colors >= 0, -1)
        vertices = priorities.argmax(1)
        chosen = (~forbidden[rows, vertices]).to(torch.int32).argmax(1)
        colors[rows, vertices] = chosen
        neighbors = work[rows, vertices]
        previous = forbidden[rows, :, chosen]
        saturation += (neighbors & ~previous).to(torch.int32)
        forbidden[rows, :, chosen] = previous | neighbors
    colors = colors.reshape(trials, batch, n)
    upper = colors.amax(2) + 1
    best = upper.argmin(0)
    rows = torch.arange(batch, device=adjacency.device)
    return colors[best, rows], upper[best, rows]


@torch.inference_mode()
def certified_screen(adjacency, colors):
    """Check the coloring on-device and return conservative gap bounds.

This check uses the final colors and original edges independently of the
greedy colorer's bookkeeping. A malformed graph or certificate fails closed.
The clique bound uses only an edge, so soundness does not assume triangle-free.
"""
    _check_shape(adjacency)
    batch, n, _ = adjacency.shape
    if (colors.shape != (batch, n) or colors.device != adjacency.device
            or colors.dtype not in (torch.int32, torch.int64)):
        raise RuntimeError('invalid coloring certificate shape, device, or dtype')
    malformed = adjacency.diagonal(dim1=1, dim2=2).any() | (adjacency != adjacency.transpose(1, 2)).any()
    invalid_color = ((colors < 0) | (colors >= n)).any()
    monochromatic = (adjacency & (colors[:, :, None] == colors[:, None, :])).any()
    if (malformed | invalid_color | monochromatic).item():
        raise RuntimeError('invalid graph or coloring certificate; refusing to prune')
    if n == 0:
        maximum = upper = clique_lower = torch.zeros(batch, dtype=torch.long, device=adjacency.device)
    else:
        degrees = adjacency.sum(2)
        maximum = degrees.amax(1)
        upper = colors.amax(1) + 1
        clique_lower = torch.where(maximum > 0, 2, 1)
    reed_lower = (maximum + clique_lower + 2) // 2
    return {'max_degree': maximum, 'clique_lower_bound': clique_lower,
            'coloring_upper_bound': upper, 'optimistic_gap': upper - reed_lower}


@torch.inference_mode()
def select_candidates(adjacency, screen, audit_size=8, generator=None):
    """Transfer every unresolved graph and a bounded sample of safe near misses."""
    if audit_size < 0:
        raise ValueError('audit_size must be nonnegative')
    gap = screen['optimistic_gap']
    potential_mask = gap > 0
    audit_mask = (gap >= -1) & ~potential_mask
    potential_ids = potential_mask.nonzero(as_tuple=True)[0]
    audit_ids = audit_mask.nonzero(as_tuple=True)[0]
    eligible = audit_ids.numel()
    if eligible > audit_size:
        permutation = torch.randperm(eligible, device=adjacency.device, generator=generator)
        audit_ids = audit_ids[permutation[:audit_size]]
    selected = torch.cat((potential_ids, audit_ids))
    potentials = potential_ids.numel()
    # Only selected matrices leave the GPU. Aggregate counts include repeated
    # labeled graphs; deduplication of exact-check candidates belongs to caller.
    matrices = adjacency[selected].to(torch.uint8).cpu().tolist()
    values = {key: value[selected].cpu().tolist() for key, value in screen.items()}
    candidates = [
        {'adjacency': matrix,
         'screen': {key: value[i] for key, value in values.items()},
         'kind': 'potential' if i < potentials else 'audit'}
        for i, matrix in enumerate(matrices)
    ]
    return {'generated': adjacency.shape[0],
            'certified_nonviolations': adjacency.shape[0] - potentials,
            'potential_count': potentials, 'audit_eligible': eligible,
            'candidates': candidates}


class TriangleFreeGPUGenerator:
    """Cycle homogeneous-order batches whose graph populations stay on-device.

Each graph is a persistent degree-preserving random walk from a validated seed.
Every order is visited in sorted cyclic order. This broadens generated coverage
without suggesting that generated counts are distinct or exhaustive.
"""

    def __init__(self, parents, batch_size=4096, seed=20261115, device='cuda',
                 swap_attempts=8, coloring_trials=4):
        if batch_size < 1 or coloring_trials < 1:
            raise ValueError('batch size and coloring trials must be positive')
        if swap_attempts < 0:
            raise ValueError('swap_attempts must be nonnegative')
        if not parents:
            raise ValueError('at least one parent is required')
        if any(not is_triangle_free(parent) for parent in parents):
            raise ValueError('all parents must be simple and triangle-free')
        self.device = torch.device(device)
        if self.device.type == 'cuda' and not torch.cuda.is_available():
            raise RuntimeError('CUDA requested but no CUDA device is available')
        self.generator = torch.Generator(device=self.device).manual_seed(seed)
        self.batch_size = batch_size
        self.swap_attempts = swap_attempts
        self.coloring_trials = coloring_trials
        grouped = defaultdict(list)
        for parent in parents:
            grouped[len(parent)].append(parent)
        self.orders = sorted(grouped)
        self.seed_pools = {}
        self.populations = {}
        self.cursor = 0
        for n, group in grouped.items():
            self.seed_pools[n] = torch.tensor(group, dtype=torch.bool, device=self.device).reshape(len(group), n, n)

    @torch.inference_mode()
    def next_batch(self, audit_size=8):
        n = self.orders[self.cursor % len(self.orders)]
        self.cursor += 1
        if n not in self.populations:
            pool = self.seed_pools[n]
            selected = torch.randint(len(pool), (self.batch_size,), device=self.device, generator=self.generator)
            self.populations[n] = pool[selected].clone()
        population = mutate_tensor(self.populations[n], self.generator, self.swap_attempts)
        self.populations[n] = population
        colors, _ = greedy_color_batch(population, self.coloring_trials, self.generator)
        result = select_candidates(population, certified_screen(population, colors),
                                   audit_size, self.generator)
        result['vertices'] = n
        return result
