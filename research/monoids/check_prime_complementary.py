"""Meaningful exact checks for prime complementary endpoint algorithms."""
from fractions import Fraction as F
from itertools import product
if __package__:
    from .prime_complementary import PrimeComplement
else:
    from prime_complementary import PrimeComplement


def endpoint_checks(S,max_depth):
    count=0
    for depth in range(max_depth+1):
        for ds in product(range(S.C+1),repeat=depth):
            if ds and ds[0]==0:continue
            x=F(S.C)
            for d in reversed(ds):x=S.digit(d)+S.q*x
            assert S.is_atom(x),(S,x)
            assert S.critical_divisors(x)==tuple(sorted((F(1),x))),(S,x)
            # q is not globally prime when a is composite, so this
            # explicit endpoint divisor theorem is a substantive check.
            z=S.q**2*x
            expected=tuple(sorted({S.q**i for i in range(3)}|{S.q**i*x for i in range(3)}))
            assert S.critical_divisors(z)==expected
            count+=1
    return count


def main():
    membership=endpoints=products=0
    for C,b in [(3,15),(5,35),(7,63),(11,143)]:
        S=PrimeComplement(C,b)
        for i,j in product(range(3),repeat=2):
            for c,d in [(1,1),(2,3),(C,C+1)]:
                x=c*S.q**i+d*S.r**j
                assert S.member(x),(C,b,x)
                membership+=1
        endpoints+=endpoint_checks(S,2 if C>3 else 3)
        assert S.is_atom(S.q) and S.is_atom(S.r) and S.is_atom(F(C))
        assert S.member(F(S.a)/S.q)
        assert not S.member(F(2)/S.q) # a even composite, denominator2 remains.
        assert not S.member(F(S.a//2)/S.q)
        for alpha in (F(C),S.r,1+S.q):
            n=0
            while True:
                hole=C-(C-F(1,b))*S.q**n
                if hole>1 and alpha*hole>=C:break
                n+=1
            assert not S.member(hole)
            assert S.member(alpha*hole) and S.member(alpha*hole*hole)
        # Integer atoms and q shifts exercise positive good-prime budget.
        for x,known in [(F(1),(0,())),(F(3),(0,(F(3),))),
                        (S.q*3,(1,(F(3),))),
                        (F(6),(0,(F(2),F(3))))]:
            records=S.atomic_factorizations(x)
            assert known in records,(C,b,x,records)
            for n,atoms in records:
                value=S.q**n
                for a in atoms:value*=a;assert S.is_atom(a)
                assert value==x
            products+=1
    S=PrimeComplement(3,15)
    h=F(125,81)
    assert h==1+S.q+S.r*S.q**2+S.q**3+20*S.q**4
    assert S.member(h) and not S.is_atom(h)
    assert S.atomic_factorizations(h)==()
    small_atoms=(F(2),F(3),S.r,1+S.q,1+S.C*S.q)
    for i,j in product(range(len(small_atoms)),repeat=2):
        for exponent in (0,1):
            x=S.q**exponent*small_atoms[i]*small_atoms[j]
            expected=(exponent,tuple(sorted((small_atoms[i],small_atoms[j]))))
            assert expected in S.atomic_factorizations(x),(x,expected)
            products+=1
    q=S.q
    f1=(1+q+q*q,1+q**3)
    f2=(1+q,1+q*q+q**4)
    x=f1[0]*f1[1]
    assert x==f2[0]*f2[1]
    expected={(0,tuple(sorted(f1))),(0,tuple(sorted(f2)))}
    assert set(S.atomic_factorizations(x))==expected
    # q^2 has no positive-size atom factors despite composite a.
    assert S.atomic_factorizations(q*q)==((2,()),)
    # Here the good block is 3^2, and the integer atom3 has positive
    # good-prime valuation. The q multiplicity genuinely varies.
    T=PrimeComplement(7,63)
    assert T.atomic_factorizations(F(8))==(
        (0,(F(2),F(2),F(2))),
        (1,(F(3),F(3),F(7))),
    )
    # A preceding r contributes at the same denominator depth as the
    # terminal4: the effective coefficient is4-C=-3, with3-valuation1.
    tail_atom=T.r+4*T.q
    assert tail_atom==F(139,21) and T.is_atom(tail_atom)
    assert T.atomic_factorizations(tail_atom)==((0,(tail_atom,)),)
    assert F(81,49)==1+4*T.q+9*T.q*T.q
    assert T.member(F(81,49)) and T.atomic_factorizations(F(81,49))==()
    print(f'Passed {membership} positive polynomial membership witnesses, {endpoints} endpoint/divisor checks, {products} generated atomic products, the nonatomic125/81 witness, and an exact two-factorization target.')

if __name__=='__main__':main()
