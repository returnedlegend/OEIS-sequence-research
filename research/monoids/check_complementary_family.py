"""Exact checks including composite complementary endpoints."""
from fractions import Fraction as F
from itertools import product
if __package__:
    from .complementary_family import Complementary
else:
    from complementary_family import Complementary


def main():
    polynomial_members=0
    for C,b in [(4,21),(4,24),(4,36),(6,45),(8,77),(9,99),(10,126)]:
        S=Complementary(C,b)
        for i,j in product(range(3),repeat=2):
            for c,d in [(1,1),(2,3),(C,C+1)]:
                assert S.member(c*S.q**i+d*S.r**j)
                polynomial_members+=1
        assert S.is_atom(S.q) and S.is_atom(S.r)
        # Canonical endpoints containing Y remain atoms for composite C.
        y=S.r+C*S.q*S.q
        assert S.is_atom(y) and S.critical_divisors(y)==(F(1),y)
        # The integer endpoint's proper factors must be retained.
        integer_divisors=tuple(F(d) for d in range(1,C+1) if C%d==0)
        assert S.critical_divisors(F(C))==integer_divisors
        expected=tuple(sorted({S.q**i*d for i in range(3) for d in integer_divisors}))
        assert S.critical_divisors(S.q*S.q*C)==expected
    S=Complementary(6,45)
    q=S.q;x=1+5*q+6*q*q;factors=(1+2*q,1+3*q)
    assert x==F(1298,675) and x==factors[0]*factors[1]
    assert not S.is_atom(x) and all(S.is_atom(z) for z in factors)
    assert S.critical_divisors(x)==tuple(sorted((F(1),x,*factors)))
    assert S.atomic_factorizations(x)==((0,tuple(sorted(factors))),)
    assert S.atomic_factorizations(F(6))==((0,(F(2),F(3))),)
    assert (1,(F(3),F(3),F(5))) in S.atomic_factorizations(F(7))
    T=Complementary(4,36);q=T.q
    f1=1+2*q;f2=1+2*q*q;x=f1*f2
    assert x==1+2*q+2*q*q+4*q**3
    assert T.canonical(x)==((1,2,2),4)
    assert T.critical_divisors(x)==tuple(sorted((F(1),f1,f2,x)))
    assert T.atomic_factorizations(x)==((0,tuple(sorted((f1,f2)))),)
    h=F(243,128)
    assert h==1+q+q**3+2034*q**4
    assert T.member(h) and T.atomic_factorizations(h)==()
    # The critical theorem also applies to a single denominator prime.
    U=Complementary(4,23)
    y=U.r+4*U.q*U.q
    assert U.is_atom(y) and U.critical_divisors(y)==(F(1),y)
    # A good prime7>C makes atomic integer factorizations precisely
    # ordinary prime factorizations using primes at most C.
    V=Complementary(4,21)
    assert V.atomic_factorizations(F(18))==((0,(F(2),F(3),F(3))),)
    assert V.member(F(5)) and V.atomic_factorizations(F(5))==()
    print(f'Passed {polynomial_members} positive polynomial membership witnesses, composite endpoint/divisor cases, exact canonical factorizations, a one-prime critical case, and the nonatomic243/128 witness.')

if __name__=='__main__':main()
