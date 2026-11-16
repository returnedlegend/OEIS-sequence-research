"""Exact finite carry-graph exclusions for binary polynomials at 2/5.

An excluded degree gap is uniform in the individual degrees and outside
numerator part. Finite ranges do not prove IDF. No floating-point
arithmetic is used. See BINARY_RATIO_GAP_SEARCH.md.
"""

import argparse
from collections import deque
from fractions import Fraction
import hashlib
import json
from pathlib import Path


def analyze_ratio(numerator, denominator, max_states=100000):
    """Decide whether finite binary F,G with F(0)=G(0)=1 have F(q)/G(q)=A/B.

    Return inconclusive if the explicitly reported state cap is exceeded.
    A witness contains coefficient pairs, in increasing degree order.
    """
    ratio = Fraction(numerator, denominator)
    if ratio <= 0:
        raise ValueError("The ratio must be positive")
    a, b = ratio.numerator, ratio.denominator
    if a % 2 == 0 or b % 2 == 0:
        return {"status": "disjoint", "states": 0, "max_bfs_distance": 0,
                "reachable_cycle": False, "longest_path": 0}
    return _analyze_odd_ratio(a, b, max_states)


def _analyze_odd_ratio(a, b, max_states):
    # The degree-gap search already has coprime odd powers of 3 and 5.
    # Avoid an unnecessary gcd of those potentially enormous integers.
    lower, upper = -(a // 3), b // 3
    start = (a - b) // 2
    if not lower <= start <= upper:
        return {"status": "disjoint", "states": 0, "max_bfs_distance": 0,
                "reachable_cycle": False, "longest_path": 0}

    pending = deque([start])
    predecessor = {start: None}
    distances = {start: 0}
    edges = {}
    max_distance = 0
    while pending:
        state = pending.popleft()
        if state == 0:
            word = []
            while predecessor[state] is not None:
                previous, f_digit, g_digit = predecessor[state]
                word.append([f_digit, g_digit])
                state = previous
            word.reverse()
            return {"status": "witness", "states": len(predecessor),
                    "max_bfs_distance": max_distance,
                    "coefficient_pairs": [[1, 1], *word]}

        if state % 2 == 0:
            choices = [(5*state // 2, 0, 0), ((5*state+a-b) // 2, 1, 1)]
        else:
            choices = [((5*state-b) // 2, 1, 0), ((5*state+a) // 2, 0, 1)]
        following = []
        for successor, f_digit, g_digit in choices:
            if lower <= successor <= upper:
                following.append(successor)
                if successor not in predecessor:
                    predecessor[successor] = (state, f_digit, g_digit)
                    distances[successor] = distances[state] + 1
                    max_distance = max(max_distance, distances[successor])
                    pending.append(successor)
        edges[state] = following
        if len(predecessor) > max_states:
            return {"status": "inconclusive", "states": len(predecessor),
                    "max_bfs_distance": max_distance}

    indegrees = {state: 0 for state in predecessor}
    for following in edges.values():
        for successor in following:
            indegrees[successor] += 1
    roots = deque(state for state, degree in indegrees.items() if degree == 0)
    longest = {start: 0}
    removed = 0
    while roots:
        state = roots.popleft()
        removed += 1
        for successor in edges[state]:
            longest[successor] = max(longest.get(successor, 0), longest.get(state, 0) + 1)
            indegrees[successor] -= 1
            if indegrees[successor] == 0:
                roots.append(successor)
    cyclic = removed < len(predecessor)
    return {"status": "disjoint", "states": len(predecessor),
            "max_bfs_distance": max_distance, "reachable_cycle": cyclic,
            "longest_path": None if cyclic else max(longest.values())}


def search(max_gap, max_states=100000):
    """Check every degree gap through max_gap; stop at a witness or cap."""
    if max_gap < 0 or max_states < 1:
        raise ValueError("Expected a nonnegative gap bound and a positive state cap")
    a = b = 1
    exponent = admissible = maximum_states = maximum_distance = cycles = 0
    digest = hashlib.sha256()
    checked = 0
    obstruction = None
    for gap in range(1, max_gap + 1):
        b *= 5
        while 5*a <= 3*b:
            a *= 3
            exponent += 1
        if 3*a >= 5*b:
            digest.update(f"{gap}:real\n".encode())
            checked = gap
            continue
        admissible += 1
        answer = _analyze_odd_ratio(a, b, max_states)
        maximum_states = max(maximum_states, answer["states"])
        maximum_distance = max(maximum_distance, answer["max_bfs_distance"])
        cycles += int(answer.get("reachable_cycle", False))
        digest.update(json.dumps([gap, exponent, answer], sort_keys=True).encode() + b"\n")
        if answer["status"] != "disjoint":
            obstruction = {"degree_gap": gap, "v3_gap": exponent, **answer}
            break
        checked = gap
    return {
        "requested_max_gap": max_gap,
        "excluded_through": checked,
        "real_admissible_ratios_tested": admissible,
        "maximum_reachable_states": maximum_states,
        "maximum_bfs_distance": maximum_distance,
        "ratios_with_reachable_cycle": cycles,
        "state_cap": max_states,
        "complete": checked == max_gap,
        "obstruction": obstruction,
        "result_digest_sha256": digest.hexdigest(),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-gap", type=int, default=1000)
    parser.add_argument("--max-states", type=int, default=100000)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    answer = search(arguments.max_gap, arguments.max_states)
    text = json.dumps(answer, indent=2) + "\n"
    if arguments.output:
        arguments.output.write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
