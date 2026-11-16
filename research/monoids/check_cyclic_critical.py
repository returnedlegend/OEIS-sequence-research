"""Exact checks for the critical cyclic divisor theorem and implementation.

Default checks include an independently written breadth-first certificate,
finite divisor lists, nonunique-polynomial atoms, and exact factorizations.
--all-certificates reproduces all 87 parameter certificates with b <= 30.
--write-certificates regenerates the compact manifest from the exact search.
"""

from __future__ import annotations

import argparse
import json
import random
from fractions import Fraction
from math import gcd
from pathlib import Path

from cyclic_critical import (
    PrefixSearchIncomplete,
    actual_divisors,
    atomic_factorizations,
    canonical,
    critical,
    factor_integer,
    is_atom,
    prefix_case,
    prefix_certificate,
)


MANIFEST = Path(__file__).with_name("cyclic_prefix_certificates.json")


def breadth_first_counts(a, b, m, j, u, v):
    """Independent storage and coefficient-enumeration strategy for the proof."""
    states = {((u,), (v,), m - j)}
    counts = [1]
    for depth in range(1, 50):
        following = set()
        for left, right, carry in states:
            cross = sum(left[i] * right[depth - i] for i in range(1, depth))
            for next_carry in range(carry + 1):
                target = (b - a) * m + a * carry - b * next_carry - cross
                for alpha in range(a):
                    for beta in range(a):
                        if u * beta + v * alpha == target:
                            following.add(
                                (left + (alpha,), right + (beta,), next_carry)
                            )
        states = following
        counts.append(len(states))
        if not states:
            return tuple(counts)
    raise AssertionError("independent breadth-first check did not finish")


def all_parameter_summaries():
    return [
        prefix_certificate(a, b).summary()
        for b in range(6, 31)
        if len(factor_integer(b)) >= 2
        for a in range(2, b)
        if gcd(a, b) == 1
    ]


def check_defaults():
    certificate_cases = 0
    for a, b in [(5, 6), (9, 10), (11, 12)]:
        for m, j, u, v, counts in prefix_certificate(a, b).rows:
            assert counts == breadth_first_counts(a, b, m, j, u, v)
            certificate_cases += 1
    assert certificate_cases == 199

    # Symbolically proved depth-one families, including denominators beyond30.
    for q in [7, 9, 11, 49, 81]:
        assert prefix_certificate(q + 2, 2 * q).depth == 1
        assert is_atom(q + 2, 2 * q, Fraction(q + 2, 2 * q))
    for u, v in [(3, 4), (3, 16), (5, 16), (7, 64), (9, 64)]:
        a, b = (u + 1) * v // 2 - 1, u * v
        assert gcd(a, b) == 1
        assert prefix_certificate(a, b).depth == 1
        assert is_atom(a, b, Fraction(a, b))
    for u, v in [(5, 9), (5, 11), (7, 9), (7, 11), (9, 25)]:
        a, b = u * v + u + v, 2 * u * v
        assert gcd(a, b) == 1
        assert (a - 1) // (b - a) == 1
        assert prefix_certificate(a, b).depth == 1
    for blocks in [(7,), (11, 17), (13, 17), (17, 19, 23)]:
        product = 1
        for block in blocks:
            product *= block
        total = sum(product // block for block in blocks)
        assert 6 * total <= product
        a, b = product + 2 * total, 2 * product
        assert gcd(a, b) == 1
        assert (a - 1) // (b - a) == 1
        assert prefix_certificate(a, b).depth == 1
    for blocks, weights in [
        ((11, 17), (2, 1)),
        ((7, 9, 13), (1, 1, 1)),
        ((19, 23, 29, 31), (2, 1, 1, 1)),
        ((16, 9), (2, 1)),
        ((9, 25), (2, 1)),
    ]:
        product = 1
        for block in blocks:
            product *= block
        total = sum(weight * (product // block)
                    for block, weight in zip(blocks, weights))
        assert (product + total) % 2 == 0 and 3 * total <= product
        a, b = (product + total) // 2, product
        assert gcd(a, b) == 1
        assert (a - 1) // (b - a) == 1
        assert prefix_certificate(a, b).depth == 1

    # A cap must remain an explicit incomplete result, not an empty tree.
    try:
        prefix_case(5, 6, 2, 1, 2, 3, max_depth=1)
    except PrefixSearchIncomplete:
        pass
    else:
        raise AssertionError("depth cap was accepted as a certificate")

    assert canonical(5, 6, Fraction(1, 5)) is None
    assert canonical(5, 6, Fraction(9, 4)) is None
    assert canonical(5, 6, Fraction(-1)) is None
    assert canonical(5, 6, Fraction(0)) == (0,)
    assert not is_atom(5, 6, Fraction(1))
    assert critical(5, 8, Fraction(9))
    assert not critical(5, 8, Fraction(10))

    expected_divisors = {
        Fraction(5, 6): (Fraction(5, 6), Fraction(1)),
        Fraction(2): (Fraction(1), Fraction(2)),
        Fraction(8): tuple(map(Fraction, [1, 2, "8/3", 3, 4, 8])),
        Fraction(9): tuple(map(Fraction, [1, 2, 3, "9/2", 9])),
    }
    for value, expected in expected_divisors.items():
        assert actual_divisors(5, 6, value) == expected

    # The terminal coefficients exceed4: uniqueness of bounded polynomials
    # alone cannot prove atomicity of these examples.
    nonunique_atoms = tuple(
        map(
            Fraction,
            [
                "81/8",
                "243/16",
                "2187/256",
                "531441/65536",
                "2048/243",
                "274877906944/31381059609",
            ],
        )
    )
    for atom in nonunique_atoms:
        assert canonical(5, 6, atom)[-1] >= 5
        assert actual_divisors(5, 6, atom) == (Fraction(1), atom)
        assert is_atom(5, 6, atom)
    assert is_atom(9, 10, Fraction(256, 25))
    assert canonical(9, 10, Fraction(256, 25)) == (7, 0, 4)
    assert not is_atom(5, 6, Fraction(25))
    try:
        actual_divisors(5, 6, Fraction(25))
    except ValueError:
        pass
    else:
        raise AssertionError("noncritical input received a finite divisor list")

    expected_eight = {
        (Fraction(2), Fraction(2), Fraction(2)),
        (Fraction(8, 3), Fraction(3)),
    }
    expected_nine = {
        (Fraction(2), Fraction(9, 2)),
        (Fraction(3), Fraction(3)),
    }
    assert set(atomic_factorizations(5, 6, Fraction(8))) == expected_eight
    assert set(atomic_factorizations(5, 6, Fraction(9))) == expected_nine
    assert atomic_factorizations(5, 6, Fraction(1)) == ((),)
    # Odd denominator support uses the sharper minimum-prime length bound.
    assert atomic_factorizations(7, 15, Fraction(3)) == ((Fraction(3),),)
    assert atomic_factorizations(7, 15, Fraction(6)) == (
        (Fraction(2), Fraction(3)),
    )
    assert atomic_factorizations(29, 45, Fraction(27)) == (
        (Fraction(3), Fraction(3), Fraction(3)),
    )

    # Generated polynomial values test the canonical algorithm independently
    # by reconstruction; known products must appear in complete divisor lists.
    rng = random.Random(5610)
    reconstruction_checks = 0
    for a, b in [(5, 6), (7, 10), (9, 10), (11, 12)]:
        t = Fraction(a, b)
        for _ in range(20):
            coefficients = [rng.randrange(a) for _ in range(rng.randrange(1, 5))]
            value = sum((c * t**i for i, c in enumerate(coefficients)), Fraction())
            if not value:
                continue
            digits = canonical(a, b, value)
            assert digits is not None
            assert sum((c * t**i for i, c in enumerate(digits)), Fraction()) == value
            assert critical(a, b, value)
            reconstruction_checks += 1
    for left, right in [
        (Fraction(5, 6), Fraction(1)),
        (Fraction(5, 6), Fraction(2)),
        (Fraction(8, 3), Fraction(3)),
        (Fraction(9, 2), Fraction(2)),
        (Fraction(3), Fraction(4)),
    ]:
        divisors = actual_divisors(5, 6, left * right)
        assert left in divisors and right in divisors

    print(
        f"Passed {certificate_cases} independent prefix cases, "
        f"{reconstruction_checks} canonical reconstructions, "
        "complete divisor/atom examples, factorization lists, and cap checks."
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--all-certificates", action="store_true")
    parser.add_argument("--write-certificates", action="store_true")
    args = parser.parse_args()
    check_defaults()
    if args.all_certificates or args.write_certificates:
        summaries = all_parameter_summaries()
        assert len(summaries) == 87
        if args.write_certificates:
            MANIFEST.write_text(json.dumps(summaries, indent=2) + "\n")
            print(f"Wrote {len(summaries)} complete certificate summaries to {MANIFEST.name}.")
        else:
            assert summaries == json.loads(MANIFEST.read_text())
            print(f"Reproduced all {len(summaries)} parameter certificates, including their hashes.")


if __name__ == "__main__":
    main()
