"""Exact regression checks for the new IDF families and one-block algorithm.

The all-height completeness arguments are in the accompanying manuscripts;
these checks target implementation boundaries and reconstruct finite outputs.
"""
from fractions import Fraction as F
from itertools import product
from math import prod
from pathlib import Path
import json

if __package__:
    from .finite_basis_membership import FiniteBasisMixed
    from .boolean_mixed_factorizations import BooleanMixed
    from .five_six_mixed_factorizations import FiveSixMixed,check_prime_certificates
    from .primitive_residue_factorizations import PrimitiveResidueMixed
    from .certified_primitive_residue import CertifiedPrimitive
    from .digit_prime_carry import verify as verify_prime_carry
    from .certified_nearby_factorizations import CertifiedNearby
    from .nearby_integral_carry import verify as verify_carry
    from .nearby_ternary_factorizations import NearbyTernary
    from .one_block_factorizations import OneBlockSemiring
    from .reciprocal_factorizations import factor_integer
else:
    from finite_basis_membership import FiniteBasisMixed
    from boolean_mixed_factorizations import BooleanMixed
    from five_six_mixed_factorizations import FiveSixMixed,check_prime_certificates
    from primitive_residue_factorizations import PrimitiveResidueMixed
    from certified_primitive_residue import CertifiedPrimitive
    from digit_prime_carry import verify as verify_prime_carry
    from certified_nearby_factorizations import CertifiedNearby
    from nearby_integral_carry import verify as verify_carry
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
    for params in [(5,6,4,1,7), (3,10,2,1,11), (3,10,2,1,17)]:
        semiring = BooleanMixed(*params)
        for x in [F(1), F(2), F(3), F(5), semiring.q, semiring.r,
                  semiring.q*semiring.r, semiring.r**2]:
            atoms, facts = semiring.factorizations(x)
            for factors in facts:
                assert prod(factors, start=F(1)) == x
                assert all(semiring.is_atom(z) and z in atoms for z in factors)
            if x.denominator == 1 and x > 1:
                assert facts == []
            if x in (semiring.q, semiring.r, semiring.q*semiring.r, semiring.r**2):
                assert facts
            count += 1
        for prime in semiring.primes:
            assert semiring.atom_divisors(F(prime)) == ()
            count += 1
    # Both denominator blocks are BELOW the numerator in the strongest
    # explicit example; this must not silently reuse the old block bound.
    semiring = BooleanMixed(5,6,4,1,7)
    assert semiring.r**4 == 1+221*semiring.q
    assert 2 == semiring.r+216*semiring.q
    count += 1
    check_prime_certificates()
    for m in (2,3,4):
        semiring=FiveSixMixed(m)
        values=[F(2),F(3),F(5),semiring.q,semiring.r,semiring.r**2,
                semiring.q*semiring.r]
        if m==2:values.extend([F(3,2),F(4031,2187)])
        for x in values:
            atoms,facts=semiring.factorizations(x)
            for factors in facts:
                assert prod(factors,start=F(1))==x
                assert all(semiring.is_atom(z) and z in atoms for z in factors)
            if x.denominator==1 and x>1:assert facts==[]
            else:assert facts
            count+=1
        assert semiring.atom_divisors(F(2))==()
        if m==2:assert semiring.atom_divisors(F(3))==(F(3,2),)
        else:assert semiring.atom_divisors(F(3))==()
        count+=2
    semiring=CertifiedNearby(46)
    for x in [F(2),F(5),F(23)]:
        assert semiring.atom_divisors(x)==()
        count+=1
    assert semiring.atom_divisors(F(13))==(F(65,46),)
    assert semiring.factorizations(F(13))[1]==[]
    assert semiring.is_atom(F(2155,2116))
    count+=3
    data=json.loads(Path(__file__).with_name('nearby_carry_certificates.json').read_text())
    assert len(data['certificates'])==1142
    for record in data['certificates']:
        assert verify_carry(record['n'],map(F,record['states']))
        count+=1
    for params in [(7,60,6,F(61,60)),(3,20,2,F(5,4)),(3,10,2,F(7,5))]:
        semiring=PrimitiveResidueMixed(*params)
        for x in [F(2),F(3),semiring.q,semiring.r,semiring.r**2]:
            atoms,facts=semiring.factorizations(x)
            for factors in facts:
                assert prod(factors,start=F(1))==x
                assert all(semiring.is_atom(z) and z in atoms for z in factors)
            if x.denominator==1 and x>1:assert facts==[]
            else:assert facts
            count+=1
    semiring=PrimitiveResidueMixed(3,20,2,F(5,4))
    assert semiring.atom_divisors(F(2))==(F(5,4),)
    count+=1
    data=json.loads(Path(__file__).with_name('primitive_7_60_carry_certificates.json').read_text())
    for record in data['records']:
        semiring=CertifiedPrimitive(7,60,record['m'],F(61,60),
                                    certificates=record['certificates'])
        for certificate in record['certificates']:
            assert verify_prime_carry(semiring.q,semiring.digits,certificate)
            count+=1
        assert semiring.numerator_multiplier==1
        for p in (2,3,5):
            assert semiring.atom_divisors(F(p))==()
            count+=1
    for generic,special,values in [
        (CertifiedPrimitive(5,6,2,F(7,6)),FiveSixMixed(2),[F(2),F(3),F(3,2)]),
        (CertifiedPrimitive(3,230,1,F(7,5)),CertifiedNearby(46),[F(2),F(13),F(65,46)])]:
        for x in values:
            assert generic.atom_divisors(x)==special.atom_divisors(x)
            assert set(generic.factorizations(x)[1])==set(special.factorizations(x)[1])
            count+=1
    semiring=CertifiedPrimitive(7,60,2,F(61,60))
    assert semiring.is_atom(F(233,225))
    assert F(233,225)==semiring.q+semiring.r**2
    count+=1
    print(f'Passed {count} exact research regression checks.')


if __name__ == '__main__':
    check()
