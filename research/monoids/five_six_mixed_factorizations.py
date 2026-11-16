"""Exact atoms and atomic factorizations for N_0[5/6**m,7/6], m>=2."""
from fractions import Fraction as F
from functools import lru_cache

if __package__:
    from .nearby_ternary_factorizations import NearbyTernary
    from .reciprocal_factorizations import divisors,valuation
else:
    from nearby_ternary_factorizations import NearbyTernary
    from reciprocal_factorizations import divisors,valuation


class FiveSixMixed(NearbyTernary):
    def __init__(self,m):
        if m<2:raise ValueError('require m>=2; m1 is not covered')
        self.m=m
        self.q,self.r=F(5,6**m),F(7,6)
        self.primes=(2,3)
        self.digits=(F(0),F(1),self.r,self.r**3,self.r**2)
        self.conductor=self.r**3/(1-self.q)
        self.numerator_multiplier=3 if m==2 else 1

    @lru_cache(None)
    def canonical(self,x):
        """Return (labels,terminal), accepting the conductor as a terminal."""
        x=F(x)
        if x<0:return None
        denominator=x.denominator
        for p in self.primes:
            while denominator%p==0:denominator//=p
        if denominator!=1:return None
        labels=[];seen=set()
        while x.denominator!=1 and x<self.conductor:
            if x in seen:
                raise AssertionError('unexpected bounded cycle contradicts residual-state proof')
            seen.add(x)
            label=x.numerator*pow(x.denominator,-1,5)%5
            if x<self.digits[label]:return None
            labels.append(label)
            x=(x-self.digits[label])/self.q
        return tuple(labels),x

    @lru_cache(None)
    def critical(self,x):
        x=F(x)
        if x<=0:return False
        result=self.canonical(x)
        return result is not None and result[1] in (0,1)

    @lru_cache(None)
    def is_atom(self,x):
        x=F(x)
        if x==1 or not self.critical(x):return False
        outside=x.numerator
        for p in self.primes:
            while outside%p==0:outside//=p
        bound=self.numerator_multiplier*outside
        lower=self.q**valuation(x,5)
        for numerator in divisors(bound):
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
        candidates={self.q}
        for numerator in divisors(self.numerator_multiplier*outside):
            candidates.update(F(numerator,denominator)
                              for denominator in self.smooth_denominators(numerator))
        return tuple(sorted(y for y in candidates
                            if y!=1 and self.is_atom(y) and self.member(x/y)))

    def factorizations(self,x):
        x=F(x);atoms=self.atom_divisors(x)
        if x==1:return atoms,[()]
        qs=valuation(x,5)
        upper=x/self.q**qs
        other=[z for z in atoms if z!=self.q]
        budget=0
        if other:
            delta=min(other);assert delta>1
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


def check_prime_certificates():
    q,r=F(5,36),F(7,6)
    digits=(F(0),F(1),r,r**3,r**2)
    certificates={2:set(map(F,['1','7/6','3/2','97/54','893/486','4031/2187','63659/39366'])),
                  3:set(map(F,['1','7/6','3/2','5/24','29/24','11/8','149/96','7/4','77/48']))}
    for p,states in certificates.items():
        assert {F(1),r}<=states
        assert all(valuation(x,p)>=-1 for x in states)
        for x in states:
            for digit in digits:
                y=digit+q*x
                assert valuation(y,p)<=-2 or y in states
        assert max(valuation(x,p) for x in states)==(0 if p==2 else 1)
    return True


if __name__=='__main__':
    import argparse,json
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('m',type=int);parser.add_argument('values',nargs='+')
    args=parser.parse_args();check_prime_certificates()
    semiring=FiveSixMixed(args.m)
    for text in args.values:
        x=F(text);atoms,facts=semiring.factorizations(x)
        print(json.dumps({'m':args.m,'x':str(x),'atom_divisors':list(map(str,atoms)),
                         'atomic_factorizations':[list(map(str,f)) for f in facts]}))
