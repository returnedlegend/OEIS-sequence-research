"""Exact, time-bounded verification of Reed's inequality.

``verify_graph(adjacency, time_limit=5.0, workers=1)`` accepts a binary,
symmetric, zero-diagonal matrix.  A numeric ``gap`` is returned only when
both clique and chromatic numbers have been proved.  CP-SAT FEASIBLE and
UNKNOWN statuses never establish optimality.  Witnesses are checked before
an exact result is returned; they complement, but do not replace, the
solver's optimality proofs.
"""
from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path
from typing import Any

from ortools.sat.python import cp_model


def validate_adjacency(adjacency: Any) -> list[list[int]]:
    """Return a normalized matrix, rejecting loops and nonsimple inputs."""
    if not isinstance(adjacency, (list, tuple)):
        raise ValueError("adjacency must be a square list or tuple of rows")
    n = len(adjacency)
    matrix = []
    for row in adjacency:
        if not isinstance(row, (list, tuple)) or len(row) != n:
            raise ValueError("adjacency must be square")
        if any(not isinstance(x, (bool, int)) or x not in (0, 1) for x in row):
            raise ValueError("adjacency entries must be binary integers")
        matrix.append([int(x) for x in row])
    for i in range(n):
        if matrix[i][i]:
            raise ValueError("self-loops are not allowed")
        if any(matrix[i][j] != matrix[j][i] for j in range(i)):
            raise ValueError("adjacency must be symmetric")
    return matrix


def _greedy_coloring(matrix: list[list[int]]) -> list[int]:
    """DSATUR proper coloring; only an upper bound, never an exact claim."""
    n = len(matrix)
    colors = [-1] * n
    degrees = [sum(row) for row in matrix]
    remaining = set(range(n))
    while remaining:
        v = max(remaining, key=lambda u: (
            len({colors[w] for w in range(n) if matrix[u][w] and colors[w] >= 0}),
            degrees[u], -u,
        ))
        forbidden = {colors[w] for w in range(n) if matrix[v][w] and colors[w] >= 0}
        color = 0
        while color in forbidden:
            color += 1
        colors[v] = color
        remaining.remove(v)
    return colors


def _checked_witnesses(matrix: list[list[int]], result: dict[str, Any]) -> None:
    """Fail closed if either solver/model witness is inconsistent."""
    clique, coloring = result["clique"], result["coloring"]
    if len(clique) != result["omega"] or len(set(clique)) != len(clique):
        raise RuntimeError("invalid maximum-clique witness")
    if any(not matrix[u][v] for i, u in enumerate(clique) for v in clique[:i]):
        raise RuntimeError("clique witness contains a nonedge")
    if len(coloring) != len(matrix) or len(set(coloring)) != result["chi"]:
        raise RuntimeError("invalid coloring witness")
    if any(matrix[u][v] and coloring[u] == coloring[v]
           for u in range(len(matrix)) for v in range(u)):
        raise RuntimeError("coloring witness contains a monochromatic edge")


def verify_graph(adjacency: Any, time_limit: float = 5.0, workers: int = 1) -> dict[str, Any]:
    """Compute exact invariants or explicitly return ``status='unknown'``.

    ``time_limit`` is a total wall-clock budget shared by the two solves.
    A deadline cannot preempt Python model construction, so a small amount
    of overhead can exceed that budget.  ``omega``/``chi`` are populated
    only once proved; ``gap`` requires both.  Empty-graph conventions are
    Delta=omega=chi=0, giving Reed bound 1 and gap -1.
    """
    if not isinstance(time_limit, (int, float)) or not math.isfinite(time_limit) or time_limit < 0:
        raise ValueError("time_limit must be a finite nonnegative number")
    if not isinstance(workers, int) or isinstance(workers, bool) or workers < 1:
        raise ValueError("workers must be a positive integer")
    started = time.monotonic()
    deadline = started + time_limit
    matrix = validate_adjacency(adjacency)
    n = len(matrix)
    degrees = [sum(row) for row in matrix]
    result: dict[str, Any] = {
        "status": "unknown", "n": n, "edges": sum(degrees) // 2,
        "max_degree": max(degrees, default=0), "omega": None,
        "chi": None, "reed_bound": None, "gap": None,
        "coloring": None, "clique": None, "elapsed_seconds": None,
    }

    def finish() -> dict[str, Any]:
        if result["omega"] is not None:
            result["reed_bound"] = (result["max_degree"] + result["omega"] + 2) // 2
        if result["omega"] is not None and result["chi"] is not None:
            _checked_witnesses(matrix, result)
            result["gap"] = result["chi"] - result["reed_bound"]
            result["status"] = "exact"
        result["elapsed_seconds"] = time.monotonic() - started
        return result

    # These elementary cases have matching explicit clique/coloring bounds.
    if not result["edges"]:
        result.update(omega=int(n > 0), chi=int(n > 0),
                      clique=[0] if n else [], coloring=[0] * n)
        return finish()
    if time.monotonic() >= deadline:
        return finish()

    clique_model = cp_model.CpModel()
    included = [clique_model.NewBoolVar(f"v{i}") for i in range(n)]
    for i in range(n):
        for j in range(i):
            if not matrix[i][j]:
                clique_model.Add(included[i] + included[j] <= 1)
    clique_model.Maximize(sum(included))
    remaining = deadline - time.monotonic()
    if remaining <= 0:
        return finish()
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = remaining
    solver.parameters.num_search_workers = workers
    solver.parameters.random_seed = 0
    status = solver.Solve(clique_model)
    if status != cp_model.OPTIMAL:
        return finish()
    clique = [i for i in range(n) if solver.Value(included[i])]
    result.update(omega=len(clique), clique=clique)

    coloring = _greedy_coloring(matrix)
    upper = max(coloring, default=-1) + 1
    if upper == len(clique):
        result.update(chi=upper, coloring=coloring)
        return finish()
    if time.monotonic() >= deadline:
        return finish()

    color_model = cp_model.CpModel()
    colors = [color_model.NewIntVar(0, upper - 1, f"color{i}") for i in range(n)]
    for i in range(n):
        for j in range(i):
            if matrix[i][j]:
                color_model.Add(colors[i] != colors[j])
    # Color permutations can always label this clique 0, 1, ..., omega-1.
    for color, vertex in enumerate(clique):
        color_model.Add(colors[vertex] == color)
    maximum = color_model.NewIntVar(len(clique) - 1, upper - 1, "maximum_color")
    color_model.AddMaxEquality(maximum, colors)
    color_model.Minimize(maximum)
    remaining = deadline - time.monotonic()
    if remaining <= 0:
        return finish()
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = remaining
    solver.parameters.num_search_workers = workers
    solver.parameters.random_seed = 0
    status = solver.Solve(color_model)
    if status == cp_model.OPTIMAL:
        result.update(chi=solver.Value(maximum) + 1,
                      coloring=[solver.Value(color) for color in colors])
    return finish()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="JSON with adjacency and optional verification claims")
    parser.add_argument("--time-limit", type=float, default=60.0)
    parser.add_argument("--workers", type=int, default=1)
    args = parser.parse_args()
    try:
        data = json.loads(args.path.read_text())
        result = verify_graph(data["adjacency"], args.time_limit, args.workers)
        claims = data.get("verification", data)
        mismatches = {
            key: {"claimed": claims[key], "computed": result[key]}
            for key in ("n", "edges", "max_degree", "omega", "chi", "reed_bound", "gap")
            if key in claims and claims[key] is not None and result[key] != claims[key]
        }
        if mismatches:
            result["claim_mismatches"] = mismatches
        print(json.dumps(result, indent=2))
        return 0 if result["status"] == "exact" and not mismatches else 1
    except (KeyError, ValueError, TypeError, OSError) as exc:
        parser.exit(2, f"verification error: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
