"""Standalone, standard-library-only exact checker for Reed search candidates.

The algorithms are independent of the CP-SAT verifier: a bit-set maximum-clique
search and DSATUR-ordered exhaustive k-colorability search. A deadline produces
``status: unknown``, never a claim of non-colorability. This file can be copied
unchanged alongside a candidate and run with Python 3.10 or newer.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
import time
from pathlib import Path


class _DeadlineExceeded(Exception):
    pass


def _validate(adjacency):
    if not isinstance(adjacency, (list, tuple)):
        raise ValueError("adjacency must be a square matrix")
    n = len(adjacency)
    for row in adjacency:
        if not isinstance(row, (list, tuple)) or len(row) != n:
            raise ValueError("adjacency must be a square matrix")
        if any(type(value) not in (int, bool) or value not in (0, 1) for value in row):
            raise ValueError("adjacency entries must be binary integers")
    for u in range(n):
        if adjacency[u][u]:
            raise ValueError("self-loops are not allowed")
        for v in range(u):
            if adjacency[u][v] != adjacency[v][u]:
                raise ValueError("adjacency must be symmetric")
    return [sum(1 << v for v, edge in enumerate(row) if edge) for row in adjacency]


def verify_independently(adjacency, time_limit=60.0):
    """Compute exact graph invariants, or return unknown if time runs out.

    ``omega`` is populated only after maximum-clique search finishes; ``chi``
    and ``gap`` only after the coloring proof finishes. A returned coloring is
    a feasible upper-bound witness until ``status`` is ``exact``. Time covers
    input validation and both searches; it is checked throughout their loops.
    """
    if not isinstance(time_limit, (int, float)) or not math.isfinite(time_limit) or time_limit <= 0:
        raise ValueError("time_limit must be finite and positive")
    started = time.monotonic()
    deadline = started + time_limit
    neighbors = _validate(adjacency)
    n = len(neighbors)
    degrees = [mask.bit_count() for mask in neighbors]
    result = {
        "status": "unknown", "n": n, "edges": sum(degrees) // 2,
        "max_degree": max(degrees, default=0), "omega": None, "chi": None,
        "reed_bound": None, "gap": None, "coloring": None, "clique": None,
        "elapsed_seconds": 0.0,
    }

    def check_deadline():
        if time.monotonic() >= deadline:
            raise _DeadlineExceeded

    def vertices(mask):
        while mask:
            bit = mask & -mask
            yield bit.bit_length() - 1
            mask ^= bit

    best_clique = []

    def clique_color_order(candidates):
        # Greedy proper coloring of the induced graph bounds its clique size.
        order, bounds = [], []
        remaining, color = candidates, 0
        while remaining:
            check_deadline()
            color += 1
            available = remaining
            while available:
                check_deadline()
                bit = available & -available
                vertex = bit.bit_length() - 1
                order.append(vertex)
                bounds.append(color)
                remaining ^= bit
                available &= ~bit & ~neighbors[vertex]
        return order, bounds

    def expand_clique(chosen, candidates):
        nonlocal best_clique
        check_deadline()
        if len(chosen) > len(best_clique):
            best_clique = chosen[:]
        order, bounds = clique_color_order(candidates)
        for index in range(len(order) - 1, -1, -1):
            check_deadline()
            if len(chosen) + bounds[index] <= len(best_clique):
                return
            vertex = order[index]
            expand_clique(chosen + [vertex], candidates & neighbors[vertex])
            candidates &= ~(1 << vertex)

    def select_vertex(uncolored, colors):
        selected, forbidden = -1, 0
        best_key = (-1, -1, -1)
        for vertex in vertices(uncolored):
            check_deadline()
            mask = 0
            for other in vertices(neighbors[vertex] & ~uncolored):
                mask |= 1 << colors[other]
            key = (mask.bit_count(), degrees[vertex], vertex)
            if key > best_key:
                selected, forbidden, best_key = vertex, mask, key
        return selected, forbidden

    def greedy_coloring():
        colors = [-1] * n
        uncolored = (1 << n) - 1
        while uncolored:
            vertex, forbidden = select_vertex(uncolored, colors)
            color = 0
            while forbidden & (1 << color):
                color += 1
            colors[vertex] = color
            uncolored &= ~(1 << vertex)
        return colors

    def k_coloring(k):
        colors = [-1] * n
        uncolored = (1 << n) - 1
        # Every coloring assigns distinct colors to the clique, so this only
        # fixes color-name symmetry and does not eliminate any solution.
        for color, vertex in enumerate(best_clique):
            colors[vertex] = color
            uncolored &= ~(1 << vertex)

        def search(remaining, used):
            check_deadline()
            if not remaining:
                return colors[:]
            vertex, forbidden = select_vertex(remaining, colors)
            # All unused color names are interchangeable; try only one new one.
            for color in range(min(k, used + 1)):
                if forbidden & (1 << color):
                    continue
                colors[vertex] = color
                solution = search(remaining & ~(1 << vertex), max(used, color + 1))
                if solution is not None:
                    return solution
                colors[vertex] = -1
            return None

        return search(uncolored, len(best_clique))

    try:
        check_deadline()
        expand_clique([], (1 << n) - 1)
        result["omega"] = len(best_clique)
        result["clique"] = best_clique[:]
        result["reed_bound"] = (result["max_degree"] + len(best_clique) + 2) // 2
        upper_coloring = greedy_coloring()
        result["coloring"] = upper_coloring
        lower = len(best_clique)
        upper = max(upper_coloring, default=-1) + 1
        while lower < upper:
            check_deadline()
            k = (lower + upper) // 2
            coloring = k_coloring(k)
            if coloring is None:
                lower = k + 1
            else:
                upper = max(coloring, default=-1) + 1
                result["coloring"] = coloring
        result["chi"] = lower
        result["gap"] = lower - result["reed_bound"]
        result["status"] = "exact"
    except _DeadlineExceeded:
        result["reason"] = "time limit exceeded; unproven invariants remain null"
    result["elapsed_seconds"] = time.monotonic() - started
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--time-limit", type=float, default=60.0)
    args = parser.parse_args(argv)
    try:
        payload = json.loads(args.candidate.read_text())
        if not isinstance(payload, dict) or "adjacency" not in payload:
            raise ValueError("candidate JSON must contain an adjacency matrix")
        result = verify_independently(payload["adjacency"], args.time_limit)
        claims = payload.get("verification", {})
        if not isinstance(claims, dict):
            raise ValueError("verification must be an object")
        mismatches = {}
        for key in ("omega", "chi", "max_degree", "reed_bound", "gap"):
            if claims.get(key) is not None and result.get(key) is not None and claims[key] != result[key]:
                mismatches[key] = {"claimed": claims[key], "computed": result[key]}
        if mismatches:
            result["claim_mismatches"] = mismatches
        print(json.dumps(result, indent=2))
        if mismatches:
            return 3
        return 0 if result["status"] == "exact" else 2
    except (OSError, ValueError, TypeError, RecursionError) as exc:
        print(json.dumps({"status": "error", "error": str(exc)}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
