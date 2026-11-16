"""Exact Boolean-basis IDF family from BOOLEAN_MIXED_IDF_FAMILY.md.

This extends the finite-basis algorithms without a denominator-block bound.
"""
from fractions import Fraction
from itertools import product
from math import gcd, floor
from functools import lru_cache

if __package__:
    from .finite_basis_membership import FiniteBasisMixed
    from .reciprocal_factorizations import factor_integer
else:
    from finite_basis_membership import FiniteBasisMixed
    from reciprocal_factorizations import factor_integer


class BooleanMixed(FiniteBasisMixed):
    def __init__(self, a, b, m, k, numerator_r):
        if min(a,b,m,k,numerator_r) <= 0 or a < 2:
            raise ValueError('require a>=2 and positive b,m,k,A')
        if gcd(a*numerator_r,b) != 1 or gcd(m,k) != 1:
            raise ValueError('require gcd(a*A,b)=1 and gcd(m,k)=1')
        self.primes = tuple(factor_integer(b))
        if len(self.primes) < 2:
            raise ValueError('require at least two denominator primes')
        self.a,self.b,self.m,self.k = a,b,m,k
        self.q,self.r = Fraction(a,b**m),Fraction(numerator_r,b**k)
        if not 0 < self.q < 1 < self.r:
            raise ValueError('require 0<q<1<r')
        self.conductor = Fraction(a-1)/(1-self.q)
        self.carry = (2-self.r)/self.q
        if not self.in_ring(self.carry) or self.carry <= self.conductor:
            raise ValueError('require 2=r+Kq with K in R and K>C')
        if not self.cyclic_member(self.r**m):
            raise ValueError('require r**m in N_0[q]')
        powers = [self.r**j for j in range(m)]
        self.digit_coefficients = {}
        for coefficients in product(range(floor(self.conductor)+1),repeat=m):
            digit = sum((c*z for c,z in zip(coefficients,powers)),Fraction(0))
            if digit <= self.conductor:
                # If different coefficient arrays have the same value,
                # either suffices for recovering a successful expression.
                self.digit_coefficients.setdefault(digit,coefficients)
        self.digits = tuple(sorted(self.digit_coefficients))
        self.denominator_part = 1

    @lru_cache(None)
    def escape_free_expression(self, x):
        # Search all states, including integers. Strict escape is the
        # mathematical criterion; the graph also safely permits equality.
        from collections import deque
        x=Fraction(x)
        if x<0 or not self.in_ring(x):
            return None
        pending=deque([x])
        parents={x:None}
        terminal=None
        while pending:
            state=pending.popleft()
            if state>self.conductor:
                return None
            if state.denominator==1 and terminal is None:
                terminal=state
            for digit in self.digits:
                if digit>state:
                    break
                successor=(state-digit)/self.q
                if self.in_ring(successor) and successor not in parents:
                    parents[successor]=(state,self.digit_coefficients[digit])
                    pending.append(successor)
        if terminal is None:
            return None
        tail=terminal
        reversed_digits=[]
        while parents[tail] is not None:
            previous,coefficients=parents[tail]
            reversed_digits.append(coefficients)
            tail=previous
        expression=list(reversed(reversed_digits))
        expression.append((terminal.numerator,)+(0,)*(self.m-1))
        while len(expression)>1 and not any(expression[-1]):
            expression.pop()
        assert all(c in (0,1) for coefficients in expression for c in coefficients)
        return tuple(expression)

    @lru_cache(None)
    def is_atom(self,x):
        x=Fraction(x)
        if x<=0 or x==1:
            return False
        expression=self.escape_free_expression(x)
        if expression is None:
            return False
        monomials=[self.q**i*self.r**j for i in range(len(expression))
                   for j in range(self.m)]
        for coefficients in product((0,1),repeat=len(monomials)):
            candidate=sum((c*z for c,z in zip(coefficients,monomials)),Fraction(0))
            if candidate in (0,1,x):
                continue
            if self.member(x/candidate):
                return False
        return True


if __name__=='__main__':
    import argparse,json
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('a','b','m','k','numerator_r'):
        parser.add_argument(name,type=int)
    parser.add_argument('values',nargs='+')
    args=parser.parse_args()
    semiring=BooleanMixed(args.a,args.b,args.m,args.k,args.numerator_r)
    for text in args.values:
        x=Fraction(text)
        atoms,facts=semiring.factorizations(x)
        print(json.dumps({'x':str(x),'atom_divisors':list(map(str,atoms)),
                          'atomic_factorizations':[list(map(str,f)) for f in facts]}))
