"""Exact critical-divisor and complete atomic-factorization algorithms.

Parameters: integer C>=3, a=C+1, b>a*C, gcd(a,b)=1.
Global atom classification assumes at least two denominator primes.
Global complete-factorization enumeration additionally uses one p^e||b>C.
These algorithms do not decide global IDF.
"""
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import gcd

@lru_cache(None)
def factor_integer(n):
    if n<1:raise ValueError('positive integer required')
    out=[];p=2
    while p*p<=n:
        e=0
        while n%p==0:n//=p;e+=1
        if e:out.append((p,e))
        p=3 if p==2 else p+2
    if n>1:out.append((n,1))
    return tuple(out)

def divisors(n):
    out=[1]
    for p,e in factor_integer(n):out=[d*p**j for d in out for j in range(e+1)]
    return tuple(sorted(out))

def vp(x,p):
    x=Fraction(x)
    if x<=0:raise ValueError('positive rational required')
    n,d=x.numerator,x.denominator;v=0
    while n%p==0:n//=p;v+=1
    while d%p==0:d//=p;v-=1
    return v

def floor_log(base,x):
    x=Fraction(x)
    if base<2 or x<1:raise ValueError('require base>=2 and x>=1')
    k=0;power=Fraction(1)
    while power*base<=x:power*=base;k+=1
    return k

def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:p.pop()
    return tuple(p or [0])

def exact_nonnegative_quotient(numerator,denominator):
    n=list(trim(numerator));d=trim(denominator)
    if d==(0,):raise ZeroDivisionError
    if n==[0]:return (0,)
    if len(n)<len(d):return None
    q=[0]*(len(n)-len(d)+1)
    while len(n)>=len(d) and n!=[0]:
        if n[-1]<0 or n[-1]%d[-1]:return None
        c=n[-1]//d[-1];k=len(n)-len(d);q[k]=c
        for j,v in enumerate(d):n[j+k]-=c*v
        n=list(trim(n))
    return trim(q) if n==[0] else None

@dataclass(frozen=True)
class Complementary:
    C:int
    b:int
    def __post_init__(self):
        if self.C<3:
            raise ValueError('C must be an integer at least3')
        if self.b<=self.C*(self.C+1) or gcd(self.b,self.C+1)!=1:
            raise ValueError('require b>C*(C+1), coprime to C+1')
    @property
    def a(self):return self.C+1
    @property
    def q(self):return Fraction(self.a,self.b)
    @property
    def r(self):return self.C*(1-self.q)
    @property
    def denominator_primes(self):return factor_integer(self.b)
    def digit(self,residue):return self.r if residue==self.C else Fraction(residue)
    def denominator_depth(self,x):
        d=Fraction(x).denominator;n=0
        for p,e in self.denominator_primes:
            v=0
            while d%p==0:d//=p;v+=1
            n=max(n,(v+e-1)//e)
        return n if d==1 else None
    @lru_cache(None)
    def canonical(self,x):
        """Return (residue digits, terminal), or None for nonmembership."""
        x=Fraction(x)
        if x<0 or self.denominator_depth(x) is None:return None
        ds=[]
        while x.denominator!=1:
            if x<0:return None
            residue=x.numerator*pow(x.denominator,-1,self.a)%self.a
            ds.append(residue);x=(x-self.digit(residue))/self.q
        return (tuple(ds),int(x)) if x>=0 else None
    def member(self,x):return self.canonical(Fraction(x)) is not None
    def critical(self,x):
        out=self.canonical(Fraction(x))
        return out is not None and out[1]<=self.C
    def _critical_form(self,x):
        out=self.canonical(Fraction(x))
        if out is None or out[1]>self.C:raise ValueError('critical member required')
        ds,k=out;ordinary=[0]*(len(ds)+1);ys=[0]*len(ordinary)
        for i,d in enumerate(ds):
            if d==self.C:ys[i]=1
            else:ordinary[i]=d
        ordinary[-1]=k;e=0
        while e<len(ordinary)-1 and ordinary[e]==ys[e]==0:e+=1
        return e,trim(ordinary[e:]),trim(ys[e:]),k
    def _evaluate(self,ordinary,ys=(0,)):
        return sum((Fraction(c)*self.q**i for i,c in enumerate(ordinary)),Fraction(0))+self.r*sum((Fraction(c)*self.q**i for i,c in enumerate(ys)),Fraction(0))
    def _ordinary_divisors(self,ordinary,ys):
        """All ordinary formal divisors of a normalized Y-degree<=1 form."""
        degree=max(len(ordinary),len(ys))-1;bound=max(max(ordinary),max(ys))
        c0=gcd(ordinary[0],ys[0]);constants=divisors(c0)
        for d in range(degree+1):
            for first in constants:
                if d==0:choices=((first,),)
                else:
                    choices=((first,)+middle+(last,) for middle in product(range(bound+1),repeat=d-1) for last in range(1,bound+1))
                for g in choices:
                    qo=exact_nonnegative_quotient(ordinary,g)
                    if qo is None:continue
                    qy=exact_nonnegative_quotient(ys,g)
                    if qy is not None:yield g,qo,qy
    @lru_cache(None)
    def critical_divisors(self,x):
        x=Fraction(x)
        if x<=0:raise ValueError('positive critical member required')
        e,o,y,k=self._critical_form(x)
        if k==self.C and (factor_integer(self.C)==((self.C,1),) or any(y)):
            normalized=x/self.q**e
            return tuple(sorted({self.q**i for i in range(e+1)}|{self.q**i*normalized for i in range(e+1)}))
        normalized_divisors=set()
        for g,qo,qy in self._ordinary_divisors(o,y):
            normalized_divisors.add(self._evaluate(g))
            normalized_divisors.add(self._evaluate(qo,qy))
        return tuple(sorted({self.q**i*d for i in range(e+1) for d in normalized_divisors}))
    @lru_cache(None)
    def is_atom(self,x):
        x=Fraction(x)
        out=self.canonical(x)
        if x<=0 or out is None or x==1:return False
        if out[1]>self.C:
            if len(self.denominator_primes)<2:raise ValueError('noncritical atom test requires two denominator primes')
            return False
        if x==self.q:return True
        e,o,y,k=self._critical_form(x)
        if e:return False
        if k==self.C and (factor_integer(self.C)==((self.C,1),) or any(y)):
            return True
        for g,qo,qy in self._ordinary_divisors(o,y):
            if g!=(1,) and not(qo==(1,) and qy==(0,)):return False
        return True
    def outside_numerator(self,x):
        n=Fraction(x).numerator
        if n<=0:raise ValueError('positive rational required')
        for p,_ in self.denominator_primes:
            while n%p==0:n//=p
        return n
    def factorization_bounds(self,x,p=None):
        x=Fraction(x)
        if x<=0 or not self.member(x):raise ValueError('positive member required')
        if len(self.denominator_primes)<2:raise ValueError('two denominator primes required')
        good=[(prime,e) for prime,e in self.denominator_primes if prime**e>self.C]
        if p is not None:good=[z for z in good if z[0]==p]
        if not good:raise ValueError('a denominator prime-power block greater than C is required')
        p,e=good[0]
        A=min(vp(x,ell)//f for ell,f in factor_integer(self.a));B=x/self.q**A
        if B<1:return dict(p=p,e=e,A=A,B=B,D=-1,K=0,integer_count=0)
        J=floor_log(p,B) if p<=self.C else 0;D=J-vp(x,p)
        K=(D+floor_log(p,self.C))//e if D>=0 else 0
        return dict(p=p,e=e,A=A,B=B,D=D,K=K,integer_count=floor_log(2,B))
    def complete_atom_candidates(self,x,bounds):
        x=Fraction(x);K=bounds['K'];B=bounds['B'];ranges=[]
        for p,e in self.denominator_primes:
            upper=floor_log(p,self.C*(self.b//p**e)**K)
            ranges.append(range(-K*e,upper+1))
        out={}
        for N in divisors(self.outside_numerator(x)):
            for exps in product(*ranges):
                z=Fraction(N)
                for (p,_),w in zip(self.denominator_primes,exps):z*=Fraction(p)**w
                if z.denominator==1 or not 1<z<=min(B,self.C):continue
                if self.denominator_depth(z)>K:continue
                if self.is_atom(z) and self.member(x/z):out[z]=False
        for prime in range(2,self.C+1):
            if factor_integer(prime)==((prime,1),) and prime<=B and self.member(x/prime):out[Fraction(prime)]=True
        return tuple(sorted(out.items()))
    def atomic_factorizations(self,x,p=None):
        """Every complete factorization as (q_count, nondecreasing_other_atoms)."""
        x=Fraction(x);bd=self.factorization_bounds(x,p)
        if bd['D']<0:return ()
        atoms=self.complete_atom_candidates(x,bd);records=[]
        for j in range(bd['A']+1):
            target=x/self.q**j
            if target<1:continue
            stack=[(0,target,bd['D'],bd['integer_count'],())]
            while stack:
                start,left,nonint_budget,int_budget,factors=stack.pop()
                if left==1:records.append((j,factors));continue
                if left<1:continue
                for index in range(start,len(atoms)):
                    alpha,is_integer=atoms[index]
                    if alpha>left:break
                    if is_integer:
                        if int_budget:stack.append((index,left/alpha,nonint_budget,int_budget-1,factors+(alpha,)))
                    elif nonint_budget:
                        stack.append((index,left/alpha,nonint_budget-1,int_budget,factors+(alpha,)))
        return tuple(sorted(records))

class PrimeComplement(Complementary):
    """Compatibility class retaining the prime-C parameter check."""
    def __post_init__(self):
        super().__post_init__()
        if factor_integer(self.C)!=((self.C,1),):
            raise ValueError('C must be prime for PrimeComplement')

def main(prime_only=False):
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('C',type=int);parser.add_argument('b',type=int);parser.add_argument('values',nargs='+')
    args=parser.parse_args()
    family=PrimeComplement if prime_only else Complementary
    S=family(args.C,args.b)
    for item in args.values:
        x=Fraction(item);c=S.canonical(x)
        print(x,'canonical=',c)
        if c is not None:print('atom=',S.is_atom(x),'factorizations=',S.atomic_factorizations(x))

if __name__=='__main__':
    main()
