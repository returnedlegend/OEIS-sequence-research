"""Exact algorithms for the primitive-residue mixed IDF family."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import gcd

if __package__:
    from .nearby_ternary_factorizations import NearbyTernary
    from .finite_basis_membership import FiniteBasisMixed
    from .reciprocal_factorizations import divisors,factor_integer,valuation
else:
    from nearby_ternary_factorizations import NearbyTernary
    from finite_basis_membership import FiniteBasisMixed
    from reciprocal_factorizations import divisors,factor_integer,valuation


class PrimitiveResidueMixed(NearbyTernary):
    def __init__(self,ell,b,m,r):
        r=F(r)
        if ell<3 or factor_integer(ell)!={ell:1}:
            raise ValueError('ell must be an odd prime')
        if b<2 or m<1 or gcd(ell,b)!=1:
            raise ValueError('require b>=2,m>=1,gcd(ell,b)=1')
        blocks=factor_integer(b)
        if len(blocks)<2:
            raise ValueError('require at least two denominator primes')
        self.a,self.b,self.m=ell,b,m
        self.primes=tuple(blocks)
        self.q,self.r=F(ell,b**m),r
        denominator=r.denominator
        for p in self.primes:
            while denominator%p==0:denominator//=p
        if denominator!=1 or r<=1 or r**(ell-2)>=2:
            raise ValueError('require r in R, r>1, r**(ell-2)<2')
        values={0:F(0)}
        for j in range(ell-1):
            value=r**j
            residue=value.numerator*pow(value.denominator,-1,ell)%ell
            if residue in values:
                raise ValueError('r must have primitive nonzero residue modulo ell')
            values[residue]=value
        self.digits=tuple(values[i] for i in range(ell))
        maximum=max(self.digits)
        deltas=[z for i,j in product(range(ell),repeat=2)
                for z in (self.digits[i]+self.digits[j]-self.digits[(i+j)%ell],
                          self.digits[i]*self.digits[j]-self.digits[i*j%ell])]
        assert all(z>=0 for z in deltas)
        self.minimum_carry=min(z for z in deltas if z>0)
        if not (self.q<1-maximum/2 and self.q<1-1/r and
                self.minimum_carry/self.q>=F(ell-1)/(1-self.q)):
            raise ValueError('finite carry/conductor inequalities do not hold')
        if any(m*e<=(ell-2)*abs(valuation(r,p)) for p,e in blocks.items()):
            raise ValueError('strict denominator valuation separation does not hold')
        self.conductor=maximum/(1-self.q)
        self.numerator_multiplier=1
        for p in self.primes:
            self.numerator_multiplier*=p**max(0,(ell-2)*valuation(r,p))

    @lru_cache(None)
    def canonical(self,x):
        x=F(x)
        if x<0:return None
        denominator=x.denominator
        for p in self.primes:
            while denominator%p==0:denominator//=p
        if denominator!=1:return None
        labels=[]
        while x.denominator!=1:
            label=x.numerator*pow(x.denominator,-1,self.a)%self.a
            if x<self.digits[label]:return None
            labels.append(label)
            x=(x-self.digits[label])/self.q
        return tuple(labels),x.numerator

    @lru_cache(None)
    def is_atom(self,x):
        x=F(x)
        if x==1 or not self.critical(x):return False
        if x==self.q:return True
        if self.member(x/self.q):return False
        outside=x.numerator
        for p in self.primes:
            while outside%p==0:outside//=p
        lower=self.q**valuation(x,self.a)
        for numerator in divisors(self.numerator_multiplier*outside):
            for denominator in self.smooth_denominators(numerator/lower):
                candidate=F(numerator,denominator)
                if candidate in (1,x):continue
                if self.member(candidate) and self.member(x/candidate):return False
        return True

    @lru_cache(None)
    def atom_divisors(self,x):
        x=F(x)
        if not self.member(x):raise ValueError('input is outside the nonzero monoid')
        outside=x.numerator
        for p in self.primes:
            while outside%p==0:outside//=p
        candidates={self.q,self.r}
        for numerator in divisors(outside):
            candidates.update(F(numerator,denominator)
                              for denominator in self.smooth_denominators(numerator))
        return tuple(sorted(y for y in candidates
                            if y!=1 and self.is_atom(y) and self.member(x/y)))

    factorizations=FiniteBasisMixed.factorizations


if __name__=='__main__':
    import argparse,json
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('ell','b','m'):parser.add_argument(name,type=int)
    parser.add_argument('r');parser.add_argument('values',nargs='+')
    args=parser.parse_args()
    semiring=PrimitiveResidueMixed(args.ell,args.b,args.m,F(args.r))
    for text in args.values:
        x=F(text);atoms,facts=semiring.factorizations(x)
        print(json.dumps({'x':str(x),'atom_divisors':list(map(str,atoms)),
                         'atomic_factorizations':[list(map(str,f)) for f in facts]}))
