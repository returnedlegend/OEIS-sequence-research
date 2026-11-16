"""Primitive-residue algorithms with finite prime-carry certificates.

Unlike the analytic class, this permits overlapping denominator valuations.
A cutoff in closure search is inconclusive, never a negative theorem.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product

if __package__:
    from .primitive_residue_factorizations import PrimitiveResidueMixed
    from .digit_prime_carry import closure,verify,upper_bound
    from .reciprocal_factorizations import divisors,factor_integer,valuation
else:
    from primitive_residue_factorizations import PrimitiveResidueMixed
    from digit_prime_carry import closure,verify,upper_bound
    from reciprocal_factorizations import divisors,factor_integer,valuation


class CertifiedPrimitive(PrimitiveResidueMixed):
    def __init__(self,ell,b,m,r,certificates=None,max_states=10000):
        r=F(r)
        # Bootstrap the parameter-independent digit data through the already
        # validated analytic constructor, at a sufficiently large exponent.
        bootstrap=m
        while True:
            try:
                super().__init__(ell,b,bootstrap,r)
                break
            except ValueError as error:
                message=str(error)
                if message not in ('finite carry/conductor inequalities do not hold',
                                   'strict denominator valuation separation does not hold'):
                    raise
                bootstrap+=1
        self.m=m;self.q=F(ell,b**m)
        maximum=max(self.digits)
        if not (self.q<1-maximum/2 and self.q<1-1/r):
            raise ValueError('finite carry/conductor inequalities do not hold')
        for i,j in product(range(ell),repeat=2):
            for delta in (self.digits[i]+self.digits[j]-self.digits[(i+j)%ell],
                          self.digits[i]*self.digits[j]-self.digits[i*j%ell]):
                if not self.cyclic_member(delta/self.q):
                    raise ValueError('a digit carry is outside the cyclic semiring')
        self.conductor=maximum/(1-self.q)
        if certificates is None:
            certificates=[]
            for p in self.primes:
                record=closure(self.q,self.digits,p,max_states)
                if record is None:
                    raise ValueError('prime-carry search cutoff: mathematically inconclusive')
                certificates.append(record)
        if sorted(record['prime'] for record in certificates)!=sorted(self.primes):
            raise ValueError('require exactly one certificate for each denominator prime')
        if not all(verify(self.q,self.digits,record) for record in certificates):
            raise ValueError('invalid prime-carry certificate')
        self.certificates=tuple(certificates)
        self.numerator_multiplier=1
        for record in certificates:
            self.numerator_multiplier*=record['prime']**upper_bound(record)

    @lru_cache(None)
    def cyclic_member(self,x):
        x=F(x)
        if x<0:return False
        denominator=x.denominator
        for p in self.primes:
            while denominator%p==0:denominator//=p
        if denominator!=1:return False
        while x.denominator!=1:
            digit=x.numerator*pow(x.denominator,-1,self.a)%self.a
            if x<digit:return False
            x=(x-digit)/self.q
        return True

    @lru_cache(None)
    def canonical(self,x):
        x=F(x)
        if x<0:return None
        denominator=x.denominator
        for p in self.primes:
            while denominator%p==0:denominator//=p
        if denominator!=1:return None
        labels=[];seen=set()
        while x.denominator!=1 and x<=self.conductor:
            if x in seen:return None
            seen.add(x)
            label=x.numerator*pow(x.denominator,-1,self.a)%self.a
            if x<self.digits[label]:return None
            labels.append(label)
            x=(x-self.digits[label])/self.q
        return tuple(labels),x

    @lru_cache(None)
    def atom_divisors(self,x):
        x=F(x)
        if not self.member(x):raise ValueError('input is outside the nonzero monoid')
        outside=x.numerator
        for p in self.primes:
            while outside%p==0:outside//=p
        candidates={self.q,self.r}
        for numerator in divisors(self.numerator_multiplier*outside):
            candidates.update(F(numerator,denominator)
                              for denominator in self.smooth_denominators(numerator))
        return tuple(sorted(y for y in candidates
                            if y!=1 and self.is_atom(y) and self.member(x/y)))


if __name__=='__main__':
    import argparse,json
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('ell','b','m'):parser.add_argument(name,type=int)
    parser.add_argument('r');parser.add_argument('values',nargs='+')
    args=parser.parse_args()
    semiring=CertifiedPrimitive(args.ell,args.b,args.m,F(args.r))
    for text in args.values:
        x=F(text);atoms,facts=semiring.factorizations(x)
        print(json.dumps({'x':str(x),'atom_divisors':list(map(str,atoms)),
                         'atomic_factorizations':[list(map(str,f)) for f in facts]}))
