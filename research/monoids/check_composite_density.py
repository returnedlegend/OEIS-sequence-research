"""Exact carry and Hensel-lifting checks for composite denominator density."""
from fractions import Fraction as F
from itertools import product
from math import gcd

if __package__:
    from .reciprocal_factorizations import factor_integer
    from .certified_primitive_residue import CertifiedPrimitive
else:
    from reciprocal_factorizations import factor_integer
    from certified_primitive_residue import CertifiedPrimitive


def polynomial(D,A,n,word):
    h,derivative=1,0
    for depth,label in enumerate(word,1):
        h*=3;derivative*=3
        if label==1:
            h+=(D*n)**depth
            derivative+=depth*D**depth*n**(depth-1)
        elif label==2:
            h+=A*D**(depth-1)*n**depth
            derivative+=A*depth*D**(depth-1)*n**(depth-1)
    return h,derivative


def check():
    checks=0
    for D,A in [(4,5),(5,7),(7,8),(7,11),(35,37),(35,43),(20,31),(25,26)]:
        blocks=factor_integer(D)
        assert gcd(3*A,D)==1 and D<A<2*D and (A-2*D)%3==0
        assert all(p**e>3 for p,e in blocks.items())
        n=4
        while gcd(n,3*A)!=1 or set(factor_integer(n))<=set(blocks):n+=1
        q,r=F(3,D*n),F(A,D)
        C0=2/(1-q);C=r/(1-q)
        assert C0<=F(32,13)<F(8,3)<(r*r-1)/q
        assert C<2 and r*r>C
        for value in ((2-r)/q,(1+r)/q,(2*r-1)/q):
            assert value>=0 and value.denominator==1
        checks+=1
        for p,e in blocks.items():
            for depth in range(1,5):
                for tail in product(range(3),repeat=depth-1):
                    word=(2,)+tail
                    root=(-3*pow(A,-1,p))%p;modulus=p
                    for precision in range(1,e*depth):
                        lifts=[root+t*modulus for t in range(p)
                               if polynomial(D,A,root+t*modulus,word)[0]%(p*modulus)==0]
                        assert len(lifts)==1
                        root=lifts[0];modulus*=p
                    h,derivative=polynomial(D,A,root,word)
                    assert h%p**(e*depth)==0
                    assert derivative%p==(A*3**(depth-1))%p!=0
                    checks+=1
    semiring=CertifiedPrimitive(3,28,1,F(5,4))
    assert semiring.atom_divisors(F(2))==()
    assert semiring.atom_divisors(F(7))==()
    assert semiring.is_atom(F(3,28)) and semiring.is_atom(F(5,4))
    checks+=3
    print(f'Passed {checks} exact composite-denominator carry/lifting checks.')


if __name__=='__main__':check()
