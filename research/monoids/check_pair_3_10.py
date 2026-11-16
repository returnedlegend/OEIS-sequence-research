"""Exact checks for the (3/10, 7/5) membership and factorization algorithms.

Run from any directory with this script's path. Use --gap-limit 10000 to
reproduce the all-depth endpoint-ratio exclusion in the accompanying note.
These finite checks exercise the implementations; the general theorems
are proved in the Markdown notes and are not inferred from these tests.
"""

import argparse
from fractions import Fraction
from itertools import combinations_with_replacement, product

if __package__:
    from .critical_pair_atoms import (
        Q, RGEN, atom_status, binary_polynomial, canonical, is_atom, member,
    )
    from .critical_pair_factorizations import atomic_factorizations
    from .endpoint_ratio_automaton import find
else:
    from critical_pair_atoms import (
        Q, RGEN, atom_status, binary_polynomial, canonical, is_atom, member,
    )
    from critical_pair_factorizations import atomic_factorizations
    from endpoint_ratio_automaton import find


def reconstruct(record):
    q_exponent, two_exponent, others = record
    value = Q ** q_exponent * 2 ** two_exponent
    for atom in others:
        value *= atom
    return value


def factor_multiset(record):
    q_exponent, two_exponent, others = record
    return tuple(sorted((Q,) * q_exponent + (Fraction(2),) * two_exponent + others))


def check_membership_and_atoms():
    # Positive polynomial expressions are independent membership witnesses.
    witnessed = set()
    for i, j, k in product(range(4), repeat=3):
        witnessed.add(Q ** i + RGEN ** j + Q ** k * RGEN)
    assert all(member(value) for value in witnessed)

    # Values below 1 with v_3=0 cannot belong to S. The unsupported prime
    # in 2/3 gives a separate denominator rejection.
    for value in (Fraction(1, 2), Fraction(7, 10), Fraction(2, 3), Fraction(5, 4)):
        assert not member(value), value
    assert member(0) and member(1)
    assert not is_atom(0) and not is_atom(1)

    known_atoms = (Q, RGEN, Fraction(2), Fraction(13, 10), Fraction(8, 5), Fraction(59, 50))
    assert all(is_atom(value) for value in known_atoms)

    # The exact endpoint theorem supplies a large, independently specified
    # family, including many different canonical-prefix shapes.
    endpoints = set()
    for degree in range(1, 7):
        for first in (Fraction(1), RGEN):
            for rest in product((Fraction(0), Fraction(1), RGEN), repeat=degree - 1):
                digits = (first,) + rest
                value = sum((digit * Q ** i for i, digit in enumerate(digits)),
                            Fraction(0)) + 2 * Q ** degree
                endpoints.add(value)
                belongs, critical, _, terminal = canonical(value)
                assert belongs and critical and terminal == 2
                assert is_atom(value)

    # Formal products are proper nonunit factorizations, whether or not
    # their values remain critical.
    for i, j in product(range(1, 6), repeat=2):
        value = (1 + Q ** i) * (1 + Q ** j)
        assert member(value) and not is_atom(value)
        status, _, witness = atom_status(value)
        assert not status
        if witness is not None:
            assert witness[0] * witness[1] == value
            assert all(member(factor) and factor != 1 for factor in witness)

    # Exhaust the small binary input family for the conversion helper.
    for degree in range(1, 8):
        for interior in product((0, 1), repeat=degree - 1):
            coefficients = (1,) + interior + (1,)
            numerator = sum(c * 3 ** i * 10 ** (degree - i)
                            for i, c in enumerate(coefficients))
            assert binary_polynomial(numerator, degree) == coefficients
    return len(witnessed), len(endpoints), known_atoms


def check_factorizations(known_atoms):
    # Every generated two- or three-atom product must recover its generating
    # multiset; every enumerated factorization must reconstruct exactly.
    products_checked = set()
    for length in (2, 3):
        for factors in combinations_with_replacement(known_atoms, length):
            value = Fraction(1)
            for atom in factors:
                value *= atom
            records = atomic_factorizations(value)
            assert tuple(sorted(factors)) in {factor_multiset(r) for r in records}
            assert len(records) == len({factor_multiset(r) for r in records})
            for record in records:
                assert reconstruct(record) == value
                assert all(is_atom(atom) for atom in factor_multiset(record))
            products_checked.add(value)

    assert atomic_factorizations(1) == [(0, 0, ())]
    for value in range(2, 21):
        records = atomic_factorizations(value)
        is_power_of_two = value & (value - 1) == 0
        assert bool(records) == is_power_of_two
        if records:
            assert len(records) == 1

    # Two formally different binary factorizations of the six-term
    # geometric polynomial give an exhaustive nonunique example.
    value = Fraction(142753, 100000)
    expected = {
        tuple(sorted((Fraction(139, 100), Fraction(1027, 1000)))),
        tuple(sorted((Fraction(13, 10), Fraction(10981, 10000)))),
    }
    actual = {factor_multiset(r) for r in atomic_factorizations(value)}
    assert actual == expected
    return len(products_checked)


def check_ratio_automaton(gap_limit):
    # A known accepted pair tests reconstruction and orientation.
    witness = find(80, 59)
    assert Fraction(witness['x']) == Fraction(8, 5)
    assert Fraction(witness['y']) == Fraction(59, 50)
    assert find(59, 80)['length'] == 2
    # The boundary pair 2,8/5 is intentionally excluded by the flags.
    assert find(4, 5).get('no_path') and find(5, 4).get('no_path')

    denominator = 1
    maximum = (0, 0, 0)
    for gap in range(1, gap_limit + 1):
        denominator *= 5
        for exponent in (denominator.bit_length() - 1, denominator.bit_length()):
            result = find(1 << exponent, denominator)
            assert result.get('no_path'), (exponent, gap, result)
            if result['states'] > maximum[0]:
                maximum = (result['states'], exponent, gap)
    return maximum


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--gap-limit', type=int, default=100)
    args = parser.parse_args()
    if args.gap_limit < 0:
        parser.error('--gap-limit must be nonnegative')
    members, endpoints, atoms = check_membership_and_atoms()
    products_checked = check_factorizations(atoms)
    maximum = check_ratio_automaton(args.gap_limit)
    print(f'Passed: {members} positive membership witnesses, {endpoints} endpoint atoms, '
          f'{products_checked} generated atomic products, and the exhaustive two-factorization example.')
    print(f'All-depth ratio exclusion passed for gaps 1..{args.gap_limit}; '
          f'maximum reachable graph (states, exponent, gap) = {maximum}.')


if __name__ == '__main__':
    main()
