"""Exact atom/factorization algorithms after a finite nearby carry certificate."""
from fractions import Fraction as F
from functools import lru_cache
from math import gcd

if __package__:
    from .nearby_ternary_factorizations import NearbyTernary
    from .nearby_integral_carry import certificate,verify
    from .reciprocal_factorizations import divisors,factor_integer,valuation
else:
    from nearby_ternary_factorizations import NearbyTernary
    from nearby_integral_carry import certificate,verify
    from reciprocal_factorizations import divisors,factor_integer,valuation


class CertifiedNearby(NearbyTernary):
    def __init__(self,n,states=None,max_states=10000):
        if n<=2 or gcd(n,21)!=1:
            raise ValueError('require n>2 and gcd(n,21)=1')
        self.n=n
        self.base=5*n
        self.primes=tuple(factor_integer(self.base))
        if len(self.primes)<2:
            raise ValueError('require at least two denominator primes')
        self.q,self.r=F(3,self.base),F(7,5)
        self.conductor=self.r/(1-self.q)
        self.digits=(F(0),F(1),self.r)
        if states is None:
            result=certificate(n,max_states)
            if result is None:
                raise ValueError('certificate search cutoff: mathematically inconclusive')
            states,_=result
        self.exceptional=tuple(sorted(set(map(F,states))))
        if not verify(n,self.exceptional):
            raise ValueError('invalid finite carry certificate')
        self.valuation_bound=max(0,max(valuation(x,5) for x in self.exceptional))

    @lru_cache(None)
    def is_atom(self,x):
        x=F(x)
        if x==1 or not self.critical(x):
            return False
        outside=x.numerator
        for p in self.primes:
            while outside%p==0:outside//=p
        numerator_bound=outside*5**self.valuation_bound
        lower=self.q**valuation(x,3)
        for numerator in divisors(numerator_bound):
            for denominator in self.smooth_denominators(numerator/lower):
                candidate=F(numerator,denominator)
                if candidate in (1,x):continue
                if self.member(candidate) and self.member(x/candidate):
                    return False
        return True

    @lru_cache(None)
    def atom_divisors(self,x):
        x=F(x)
        if not self.member(x):
            raise ValueError('input is outside the nonzero monoid')
        outside=x.numerator
        for p in self.primes:
            while outside%p==0:outside//=p
        candidates=set(self.exceptional)
        candidates.add(self.q)
        for numerator in divisors(outside):
            candidates.update(F(numerator,denominator)
                              for denominator in self.smooth_denominators(numerator))
        return tuple(sorted(y for y in candidates
                            if y!=1 and self.is_atom(y) and self.member(x/y)))

    def factorizations(self,x):
        x=F(x)
        atoms=self.atom_divisors(x)
        if x==1:return atoms,[()]
        qs=valuation(x,3)
        upper=x/self.q**qs
        other=[z for z in atoms if z!=self.q]
        budget=0
        if other:
            delta=min(other)
            assert delta>1
            power=delta
            while power<=upper:budget+=1;power*=delta
        stack=[(0,x,qs,budget,())];answers=[]
        while stack:
            start,remaining,q_left,other_left,chosen=stack.pop()
            if remaining==1:answers.append(chosen);continue
            for i in range(start,len(atoms)):
                atom=atoms[i]
                q_cost=int(atom==self.q);other_cost=1-q_cost
                if q_left<q_cost or other_left<other_cost:continue
                cofactor=remaining/atom
                if self.member(cofactor):
                    stack.append((i,cofactor,q_left-q_cost,other_left-other_cost,chosen+(atom,)))
        return atoms,answers


if __name__=='__main__':
    import argparse,json
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('n',type=int);parser.add_argument('values',nargs='+')
    args=parser.parse_args()
    semiring=CertifiedNearby(args.n)
    for text in args.values:
        x=F(text);atoms,facts=semiring.factorizations(x)
        print(json.dumps({'x':str(x),'atom_divisors':list(map(str,atoms)),
                          'atomic_factorizations':[list(map(str,f)) for f in facts]}))
