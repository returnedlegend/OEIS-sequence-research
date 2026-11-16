"""Exact critical-divisor and atom algorithms for cyclic rational semirings.

A finite carry-prefix certificate is proved before divisor bounds are used.
An unfinished certificate raises PrefixSearchIncomplete; a resource limit
is never treated as a successful certificate. All arithmetic is exact.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import gcd, isqrt


class PrefixSearchIncomplete(RuntimeError):
    """The configured finite search did not supply a certificate."""


def valuation(n: int, p: int) -> tuple[int, int]:
    if n <= 0:
        raise ValueError("valuation requires a positive integer")
    exponent = 0
    while n % p == 0:
        n //= p
        exponent += 1
    return exponent, n


@lru_cache(None)
def factor_integer(n: int) -> tuple[tuple[int, int], ...]:
    if n < 1:
        raise ValueError("factor_integer requires a positive integer")
    factors = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            exponent, n = valuation(n, p)
            factors.append((p, exponent))
        p += 1
    if n > 1:
        factors.append((n, 1))
    return tuple(factors)


def floor_log(base: int, x: Fraction | int) -> int:
    x = Fraction(x)
    if base < 2 or x < 1:
        raise ValueError("require base >= 2 and x >= 1")
    exponent, power = 0, Fraction(1)
    while power * base <= x:
        power *= base
        exponent += 1
    return exponent


def integer_divisors(n: int) -> tuple[int, ...]:
    divisors = [1]
    for p, exponent in factor_integer(n):
        divisors = [d * p**k for d in divisors for k in range(exponent + 1)]
    return tuple(sorted(divisors))


def _validate_parameters(a: int, b: int, *, two_primes: bool = False) -> None:
    if not 1 < a < b or gcd(a, b) != 1:
        raise ValueError("require coprime integers 1 < a < b")
    if two_primes and len(factor_integer(b)) < 2:
        raise ValueError("this algorithm requires at least two denominator primes")


def critical_threshold(a: int, b: int) -> int:
    _validate_parameters(a, b)
    return a * ((a - 1) // (b - a) + 1) - 1


@lru_cache(None)
def canonical(a: int, b: int, x: Fraction) -> tuple[int, ...] | None:
    """Return the minimal canonical polynomial, or None for nonmembership."""
    _validate_parameters(a, b)
    x = Fraction(x)
    if x < 0:
        return None
    if x == 0:
        return (0,)
    denominator, degree = x.denominator, 0
    for p, exponent in factor_integer(b):
        v, denominator = valuation(denominator, p)
        degree = max(degree, (v + exponent - 1) // exponent)
    if denominator != 1:
        return None
    denominator = b**degree
    numerator = x.numerator * (denominator // x.denominator)
    digits = []
    for _ in range(degree):
        digit = numerator * pow(denominator, -1, a) % a
        digits.append(digit)
        numerator = (numerator - digit * denominator) // a
        denominator //= b
        if numerator < 0:
            return None
    digits.append(numerator)
    return tuple(digits)


def critical(a: int, b: int, x: Fraction) -> bool:
    digits = canonical(a, b, Fraction(x))
    return digits is not None and digits[-1] <= critical_threshold(a, b)


def leading_pairs(b: int, j: int) -> tuple[tuple[int, int], ...]:
    value = b * j
    return tuple(
        (u, value // u)
        for u in range(2, isqrt(value) + 1)
        if value % u == 0
        and gcd(u, b) > 1
        and gcd(value // u, b) > 1
        and u % b
        and (value // u) % b
    )


def prefix_case(
    a: int,
    b: int,
    m: int,
    j: int,
    u: int,
    v: int,
    *,
    max_depth: int = 100,
    max_nodes: int = 100_000_000,
) -> tuple[int, ...]:
    """Count every surviving prefix at each depth, ending with a zero count.

    A child uniquely determines its parent, so depth-first counts equal the
    complete breadth-first state counts without storing an entire level.
    """
    solutions: dict[int, list[tuple[int, int]]] = {}
    # Carries can only decrease, and the convolution cross term is
    # nonnegative. Larger coefficient targets can never be reached.
    maximum_target = (b - a) * m + a * (m - j)
    for alpha in range(min(a - 1, maximum_target // v) + 1):
        maximum_beta = min(a - 1, (maximum_target - v * alpha) // u)
        for beta in range(maximum_beta + 1):
            solutions.setdefault(u * beta + v * alpha, []).append((alpha, beta))
    left, right = [u], [v]
    counts = [1] + [0] * max_depth
    visited = 0

    def visit(carry: int, depth: int) -> None:
        nonlocal visited
        visited += 1
        if visited > max_nodes:
            raise PrefixSearchIncomplete(
                f"node cap reached for {(a, b, m, j, u, v)}"
            )
        cross = sum(left[i] * right[depth - i] for i in range(1, depth))
        for next_carry in range(carry + 1):
            target = (b - a) * m + a * carry - b * next_carry - cross
            for alpha, beta in solutions.get(target, ()):
                counts[depth] += 1
                if depth == max_depth:
                    raise PrefixSearchIncomplete(
                        f"depth cap reached for {(a, b, m, j, u, v)}"
                    )
                left.append(alpha)
                right.append(beta)
                visit(next_carry, depth + 1)
                left.pop()
                right.pop()

    visit(m - j, 1)
    last_nonzero = max(i for i, count in enumerate(counts) if count)
    return tuple(counts[: last_nonzero + 2])


@dataclass(frozen=True)
class PrefixCertificate:
    a: int
    b: int
    # Each row is (m, j, u, v, counts), with counts ending in zero.
    rows: tuple[tuple[int, int, int, int, tuple[int, ...]], ...]

    @property
    def depth(self) -> int:
        return max((len(row[4]) - 1 for row in self.rows), default=0)

    def summary(self) -> dict[str, int | str]:
        encoded = json.dumps(self.rows, separators=(",", ":")).encode()
        return {
            "a": self.a,
            "b": self.b,
            "K": (self.a - 1) // (self.b - self.a),
            "depth": self.depth,
            "cases": len(self.rows),
            "max_width": max((max(row[4]) for row in self.rows), default=0),
            "nodes": sum(sum(row[4]) for row in self.rows),
            "sha256": hashlib.sha256(encoded).hexdigest(),
        }


@lru_cache(None)
def prefix_certificate(a: int, b: int) -> PrefixCertificate:
    _validate_parameters(a, b, two_primes=True)
    rows = []
    for m in range(1, (a - 1) // (b - a) + 1):
        for j in range(1, m + 1):
            for u, v in leading_pairs(b, j):
                rows.append((m, j, u, v, prefix_case(a, b, m, j, u, v)))
    return PrefixCertificate(a, b, tuple(rows))


@dataclass(frozen=True)
class DivisorBounds:
    outside_numerator: int
    valuation_degree: int
    denominator_degree: int
    real_upper_bound: Fraction
    factor_degree_bound: int


def divisor_bounds(a: int, b: int, x: Fraction) -> DivisorBounds:
    _validate_parameters(a, b, two_primes=True)
    x = Fraction(x)
    digits = canonical(a, b, x)
    if x <= 0 or digits is None:
        raise ValueError("require x in the semiring minus {0}")
    if not critical(a, b, x):
        raise ValueError("noncritical x has infinitely many actual divisors")
    height = prefix_certificate(a, b).depth
    outside = x.numerator
    for p, _ in factor_integer(b):
        _, outside = valuation(outside, p)
    ell, exponent = factor_integer(a)[0]
    numerator_valuation, _ = valuation(outside, ell)
    r = numerator_valuation // exponent
    upper = x * Fraction(b, a) ** r
    n = len(digits) - 1
    degree_bound = n + max(height, floor_log(a, outside), floor_log(2, upper))
    return DivisorBounds(outside, r, n, upper, degree_bound)


def actual_divisors(a: int, b: int, x: Fraction) -> tuple[Fraction, ...]:
    x = Fraction(x)
    bounds = divisor_bounds(a, b, x)
    primes = factor_integer(b)
    ranges = []
    for p, exponent in primes:
        upper = floor_log(
            p,
            bounds.real_upper_bound
            * (b // p**exponent) ** bounds.factor_degree_bound,
        )
        ranges.append(range(-exponent * bounds.factor_degree_bound, upper + 1))
    lower = Fraction(a, b) ** bounds.valuation_degree
    divisors = set()
    for numerator in integer_divisors(bounds.outside_numerator):
        for exponents in product(*ranges):
            candidate = Fraction(numerator)
            for (p, _), exponent in zip(primes, exponents):
                candidate *= Fraction(p) ** exponent
            if not lower <= candidate <= bounds.real_upper_bound:
                continue
            if (
                canonical(a, b, candidate) is not None
                and canonical(a, b, x / candidate) is not None
            ):
                divisors.add(candidate)
    return tuple(sorted(divisors))


def is_atom(a: int, b: int, x: Fraction) -> bool:
    _validate_parameters(a, b, two_primes=True)
    x = Fraction(x)
    if x <= 0 or canonical(a, b, x) is None:
        raise ValueError("require x in the semiring minus {0}")
    if x == 1 or not critical(a, b, x):
        return False
    return actual_divisors(a, b, x) == tuple(sorted({Fraction(1), x}))


def atom_divisors(a: int, b: int, x: Fraction) -> tuple[Fraction, ...]:
    divisors = actual_divisors(a, b, Fraction(x))
    return tuple(
        divisor
        for divisor in divisors
        if divisor != 1
        and not any(
            other not in (1, divisor)
            and canonical(a, b, divisor / other) is not None
            for other in divisors
        )
    )


def atomic_factorizations(
    a: int, b: int, x: Fraction
) -> tuple[tuple[Fraction, ...], ...]:
    """Enumerate factorizations of a critical input, up to ordering."""
    x = Fraction(x)
    bounds = divisor_bounds(a, b, x)
    atoms = atom_divisors(a, b, x)
    omega = sum(exponent for _, exponent in factor_integer(bounds.outside_numerator))
    minimum_denominator_prime = factor_integer(b)[0][0]
    length_bound = omega + floor_log(
        minimum_denominator_prime, critical_threshold(a, b)
    )
    answers = []

    def visit(remainder: Fraction, first: int, factors: tuple[Fraction, ...]) -> None:
        if remainder == 1:
            answers.append(factors)
            return
        if len(factors) == length_bound:
            return
        for i in range(first, len(atoms)):
            quotient = remainder / atoms[i]
            if canonical(a, b, quotient) is not None:
                visit(quotient, i, factors + (atoms[i],))

    visit(x, 0, ())
    return tuple(answers)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    parser.add_argument("values", nargs="*", type=Fraction)
    parser.add_argument("--factorizations", action="store_true")
    args = parser.parse_args()
    print(json.dumps(prefix_certificate(args.a, args.b).summary(), sort_keys=True))
    for x in args.values:
        digits = canonical(args.a, args.b, x)
        if x <= 0 or digits is None:
            print(f"{x}: outside the semiring minus {{0}}")
        elif not critical(args.a, args.b, x):
            print(f"{x}: noncritical, reducible, infinitely many actual divisors")
        else:
            divisors = actual_divisors(args.a, args.b, x)
            print(
                f"{x}: digits={digits}; atom={is_atom(args.a, args.b, x)}; "
                f"divisors={[str(d) for d in divisors]}"
            )
            if args.factorizations:
                print(
                    "factorizations:",
                    [[str(d) for d in fs] for fs in atomic_factorizations(args.a, args.b, x)],
                )


if __name__ == "__main__":
    main()
