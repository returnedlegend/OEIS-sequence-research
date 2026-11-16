"""Exhaustive deterministic carry-prefix certificates when K=1.

The default run covers every reduced parameter with b<=5000 and at least
two denominator primes. It independently checks small cases against the
general search, then reproduces cyclic_k1_certificates.json exactly.
--write-manifest deliberately regenerates that compact certificate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from math import gcd, isqrt
from pathlib import Path

if __package__:
    from .cyclic_critical import PrefixSearchIncomplete, prefix_certificate
else:
    from cyclic_critical import PrefixSearchIncomplete, prefix_certificate


def proper_pairs(b: int) -> list[tuple[int, int]]:
    return [(u, b // u) for u in range(2, isqrt(b) + 1) if b % u == 0]


def has_two_primes(b: int) -> bool:
    remainder = b
    for p in range(2, isqrt(b) + 1):
        if remainder % p == 0:
            while remainder % p == 0:
                remainder //= p
            return remainder != 1
    return False


def deterministic_path(
    a: int, b: int, u: int, v: int, max_depth: int = 200
) -> tuple[int, tuple[int, ...], tuple[int, ...]]:
    """Return the first empty depth and the unique surviving prefix.

    Preconditions: K=1, uv=b, gcd(u,v)=1, and u,v>=2. A cap raises an
    explicit incomplete-search exception; it never certifies termination.
    """
    assert (a - 1) // (b - a) == 1 and u * v == b and gcd(u, v) == 1
    inverse = pow(v, -1, u)
    left, right = [u], [v]
    for depth in range(1, max_depth + 1):
        cross = sum(left[i] * right[depth - i] for i in range(1, depth))
        target = b - a - cross
        if target < 0:
            return depth, tuple(left), tuple(right)
        alpha = target * inverse % u
        remainder = target - v * alpha
        if remainder < 0:
            return depth, tuple(left), tuple(right)
        beta = remainder // u
        # target<uv gives uniqueness; K=1 also gives u,v<a.
        assert 0 <= alpha < u < a and 0 <= beta < v < a
        left.append(alpha)
        right.append(beta)
    raise PrefixSearchIncomplete(f"K=1 path cap reached for {(a, b, u, v)}")


def independent_small_check() -> int:
    checked = 0
    for b in range(6, 101):
        if not has_two_primes(b):
            continue
        for a in range(b // 2 + 1, 2 * b // 3 + 1):
            if gcd(a, b) != 1:
                continue
            rows = []
            for u, v in proper_pairs(b):
                death = 1 if gcd(u, v) > 1 else deterministic_path(a, b, u, v)[0]
                rows.append((1, 1, u, v, (1,) * death + (0,)))
                checked += 1
            assert tuple(rows) == prefix_certificate(a, b).rows
    try:
        deterministic_path(11, 21, 3, 7, max_depth=1)
    except PrefixSearchIncomplete:
        pass
    else:
        raise AssertionError("a capped K=1 path was accepted as a certificate")
    return checked


def scan(max_denominator: int) -> dict:
    histogram: Counter[int] = Counter()
    digest = hashlib.sha256()
    parameter_count = denominator_count = coprime_cases = 0
    noncoprime_cases = two_cases = 0
    records: list[dict] = []
    maximum_depth = 0
    for b in range(6, max_denominator + 1):
        if not has_two_primes(b):
            continue
        parameters = [
            a for a in range(b // 2 + 1, 2 * b // 3 + 1) if gcd(a, b) == 1
        ]
        if not parameters:
            continue
        denominator_count += 1
        parameter_count += len(parameters)
        pairs = proper_pairs(b)
        for a in parameters:
            for u, v in pairs:
                if gcd(u, v) > 1:
                    noncoprime_cases += 1
                    death, left, right = 1, (u,), (v,)
                elif u == 2:
                    # d=b-a is odd and d<v, so d is not 2*beta+v*alpha.
                    assert (b - a) % 2 == 1 and b - a < v
                    two_cases += 1
                    death, left, right = 1, (u,), (v,)
                else:
                    coprime_cases += 1
                    death, left, right = deterministic_path(a, b, u, v)
                histogram[death] += 1
                digest.update(f"{a},{b},{u},{v},{death}\n".encode())
                if death > maximum_depth:
                    maximum_depth = death
                    records.append(
                        dict(a=a, b=b, u=u, v=v, depth=death,
                             left=list(left), right=list(right))
                    )
    return dict(
        max_denominator=max_denominator,
        denominator_count=denominator_count,
        parameter_count=parameter_count,
        prefix_case_count=sum(histogram.values()),
        noncoprime_cases=noncoprime_cases,
        coprime_two_cases=two_cases,
        explicit_coprime_cases=coprime_cases,
        maximum_depth=maximum_depth,
        death_depth_counts={str(k): v for k, v in sorted(histogram.items())},
        sha256=digest.hexdigest(),
        depth_records=records,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-denominator", type=int, default=5000)
    parser.add_argument("--write-manifest", action="store_true")
    args = parser.parse_args()
    if args.max_denominator < 6:
        parser.error("--max-denominator must be at least 6")
    if args.write_manifest and args.max_denominator != 5000:
        parser.error("the committed manifest covers exactly b<=5000")
    checked = independent_small_check()
    result = scan(args.max_denominator)
    manifest = Path(__file__).with_name("cyclic_k1_certificates.json")
    if args.write_manifest:
        manifest.write_text(json.dumps(result, indent=2) + "\n")
    elif args.max_denominator == 5000:
        assert result == json.loads(manifest.read_text()), "manifest mismatch"
    print(
        f"Passed {checked} independent general-search comparisons; "
        f"certified {result['parameter_count']} parameters through "
        f"b={args.max_denominator}, {result['prefix_case_count']} prefix cases, "
        f"maximum empty depth {result['maximum_depth']}."
    )


if __name__ == "__main__":
    main()
