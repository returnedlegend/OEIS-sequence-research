"""Exact regression checks for the new IDF families and one-block algorithm.

The all-height completeness arguments are in the accompanying manuscripts;
these checks target implementation boundaries and reconstruct finite outputs.
"""
from fractions import Fraction as F
from itertools import product
from math import prod

if __package__:
    from .finite_basis_membership import FiniteBasisMixed
    from .nearby_ternary_factorizations import NearbyTernary
    from .one_block_factorizations import OneBlockSemiring
    from .reciprocal_factorizations import factor_integer
else:
    from finite_basis_membership import FiniteBasisMixed
    from nearby_ternary_factorizations import NearbyTernary
    from one_block_factorizations import OneBlockSemiring
    from reciprocal_factorizations import factor_integer


def check():
    count = 0
    for n in (4, 8, 10, 13, 17, 20, 23):
        semiring = NearbyTernary(n)
        values = {sum((d*semiring.q**i for i, d in enumerate(ds)), F(0))
                  for ds in product(semiring.digits, repeat=2)}-{0}
        for x in values:
            assert semiring.member(x) and semiring.critical(x)
            atoms, facts = semiring.factorizations(x)
            assert facts
            assert semiring.is_atom(x) == (x != 1 and facts == [(x,)])
            for factors in facts:
                assert prod(factors, start=F(1)) == x
                assert all(semiring.is_atom(a) and a in atoms for a in factors)
            count += 1
        for p in semiring.primes:
            assert semiring.atom_divisors(F(p)) == ()
            assert semiring.factorizations(F(p))[1] == []
            count += 1

    for params in [(3,35,2,1,37), (4,35,2,1,37), (5,77,2,1,78),
                   (6,77,2,1,79), (2,15,2,3,3377)]:
        semiring = FiniteBasisMixed(*params)
        assert semiring.member(semiring.r) and not semiring.cyclic_member(semiring.r)
        for i, j in product(range(4), repeat=2):
            x = semiring.q**i*semiring.r**j
            assert semiring.member(x) and semiring.member(1+x+semiring.q*x)
            count += 1
        for x in [F(1), F(2), F(3), semiring.q, semiring.r,
                  semiring.q*semiring.r, semiring.r**2]:
            atoms, facts = semiring.factorizations(x)
            for factors in facts:
                assert prod(factors, start=F(1)) == x
                assert all(semiring.is_atom(z) and z in atoms for z in factors)
            assert semiring.is_atom(x) == (x != 1 and facts == [(x,)])
            if x in (semiring.q, semiring.r, semiring.q*semiring.r, semiring.r**2):
                assert facts
            count += 1
        for p in semiring.primes:
            assert semiring.atom_divisors(F(p)) == ()
            count += 1

    # Membership accepts integer2 immediately, but the atom escape search
    # must continue and discover2=r+385q for this mixed example.
    semiring = FiniteBasisMixed(3, 35, 2, 1, 37)
    assert F(2) == semiring.r+385*semiring.q
    assert semiring.member(F(2)) and not semiring.is_atom(F(2))
    assert semiring.atom_divisors(F(2)) == ()
    count += 1

    for a, b in [(3,35), (4,35), (5,77), (6,77), (7,143), (8,143)]:
        s = (-2*b) % a
        semiring = FiniteBasisMixed(a,b,2,1,b+s)
        actual = [j for j in range(2,a+3) if semiring.is_atom(F(j))]
        expected = [j for j in range(2,a//2+1) if factor_integer(j) == {j:1}]
        assert actual == expected
        count += 1

    for a, b, x in [(7,18,F(7)), (7,18,F(14)), (4,15,F(15)),
                    (3,10,F(142753,100000))]:
        semiring = OneBlockSemiring(a,b)
        for reciprocal in (False, True):
            records = semiring.factorizations(x, reciprocal=reciprocal)
            for k, factors in records:
                assert semiring.t**k*prod(factors,start=F(1)) == x
                assert reciprocal or k >= 0
            if (a,b,x) == (4,15,F(15)):
                assert bool(records) == reciprocal
            if (a,b) == (3,10):
                assert len(records) == 2
            count += 1
    print(f'Passed {count} exact research regression checks.')


if __name__ == '__main__':
    check()
