"""Exact finite-state membership for the independent mixed IDF family.

See INDEPENDENT_MIXED_IDF_FAMILY.md, sections11–15. This decides
semiring membership, atoms, atom divisors, and all atomic factorizations.
"""
from collections import deque
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import gcd
import argparse
import json

if __package__:
    from .reciprocal_factorizations import divisors, factor_integer, valuation
else:
    from reciprocal_factorizations import divisors, factor_integer, valuation


class FiniteBasisMixed:
    def __init__(self, a, b, m, k, numerator_r):
        if min(a, b, m, k, numerator_r) <= 0 or a < 2:
            raise ValueError("require a>=2 and b,m,k,A positive")
        if gcd(a*numerator_r, b) != 1 or gcd(m, k) != 1:
            raise ValueError("require gcd(a*A,b)=1 and gcd(m,k)=1")
        blocks = factor_integer(b)
        if len(blocks) < 2 or any(p**e <= a for p, e in blocks.items()):
            raise ValueError("require at least two denominator primes and every prime-power block>a")
        self.a, self.b, self.m, self.k = a, b, m, k
        self.primes = tuple(blocks)
        self.q = Fraction(a, b**m)
        self.r = Fraction(numerator_r, b**k)
        if not 0 < self.q < 1 < self.r:
            raise ValueError("require 0<q<1<r")
        self.conductor = Fraction(a-1)/(1-self.q)
        if not self.cyclic_member(self.r**m):
            raise ValueError("require r**m in N_0[q]")
        # Digits above C can never be chosen at an unaccepted state x<C.
        powers = [self.r**j for j in range(m)]
        self.digit_coefficients = {}
        for coefficients in product(range(a), repeat=m):
            digit = sum((c*z for c, z in zip(coefficients, powers)), Fraction(0))
            if digit < self.conductor:
                assert digit not in self.digit_coefficients
                self.digit_coefficients[digit] = coefficients
        self.digits = tuple(sorted(self.digit_coefficients))
        self.denominator_part = 1
        for prime, exponent in blocks.items():
            self.denominator_part *= prime**(exponent-1)


    @lru_cache(None)
    def in_ring(self, x):
        denominator = Fraction(x).denominator
        for p in self.primes:
            while denominator % p == 0:
                denominator //= p
        return denominator == 1

    @lru_cache(None)
    def cyclic_member(self, x):
        x = Fraction(x)
        if x < 0 or not self.in_ring(x):
            return False
        while x.denominator != 1:
            digit = x.numerator*pow(x.denominator, -1, self.a) % self.a
            if x < digit:
                return False
            x = (x-digit)/self.q
        return True

    @lru_cache(None)
    def member(self, x):
        x = Fraction(x)
        if x < 0 or not self.in_ring(x):
            return False
        pending = deque([x])
        seen = {x}
        while pending:
            state = pending.popleft()
            if state.denominator == 1 or state >= self.conductor:
                return True
            for digit in self.digits:
                if digit > state:
                    break
                successor = (state-digit)/self.q
                if self.in_ring(successor) and successor not in seen:
                    seen.add(successor)
                    pending.append(successor)
        return False

    @lru_cache(None)
    def escape_free_expression(self, x):
        """Unique bounded basis array, or None for nonmembers/escaping states.

        Unlike membership, this search continues from integer states. A
        reachable tail>C proves reducibility by the smooth perturbation lemma.
        """
        x = Fraction(x)
        if x < 0 or not self.in_ring(x):
            return None
        pending = deque([x])
        parents = {x: None}
        terminal = None
        while pending:
            state = pending.popleft()
            if state > self.conductor:
                return None
            # Under the theorem hypotheses C does not belong R.
            assert state != self.conductor
            if state.denominator == 1 and terminal is None:
                terminal = state
            for digit in self.digits:
                if digit > state:
                    break
                successor = (state-digit)/self.q
                if self.in_ring(successor) and successor not in parents:
                    parents[successor] = (state, self.digit_coefficients[digit])
                    pending.append(successor)
        if terminal is None:
            return None
        tail = terminal
        reversed_digits = []
        while parents[tail] is not None:
            previous, coefficients = parents[tail]
            reversed_digits.append(coefficients)
            tail = previous
        expression = list(reversed(reversed_digits))
        expression.append((terminal.numerator,)+(0,)*(self.m-1))
        while len(expression) > 1 and not any(expression[-1]):
            expression.pop()
        return tuple(expression)

    @lru_cache(None)
    def is_atom(self, x):
        x = Fraction(x)
        if x <= 0 or x == 1:
            return False
        expression = self.escape_free_expression(x)
        if expression is None:
            return False
        height = len(expression)-1
        monomials = [self.q**i*self.r**j
                     for i in range(height+1) for j in range(self.m)]
        for coefficients in product(range(self.a), repeat=len(monomials)):
            candidate = sum((c*z for c, z in zip(coefficients, monomials)), Fraction(0))
            if candidate in (0, 1, x):
                continue
            if self.member(x/candidate):
                return False
        return True

    @lru_cache(None)
    def atom_divisors(self, x):
        x = Fraction(x)
        if x <= 0 or not self.member(x):
            raise ValueError('input must belong to the nonzero monoid')
        outside = x.numerator
        for prime in self.primes:
            while outside % prime == 0:
                outside //= prime
        atoms = set()
        if self.member(x/self.q):
            assert self.is_atom(self.q)
            atoms.add(self.q)
        for numerator in divisors(self.denominator_part*outside):
            denominator = 1
            while denominator <= numerator:
                candidate = Fraction(numerator, denominator)
                if candidate != 1 and self.is_atom(candidate) and self.member(x/candidate):
                    atoms.add(candidate)
                denominator *= self.b
        return tuple(sorted(atoms))

    def factorizations(self, x):
        x = Fraction(x)
        atoms = self.atom_divisors(x)
        if x == 1:
            return atoms, [()]
        ell, exponent = next(iter(factor_integer(self.a).items()))
        q_budget = valuation(x, ell)//exponent
        upper_product = x/self.q**q_budget
        other_atoms = tuple(atom for atom in atoms if atom != self.q)
        other_budget = 0
        if other_atoms:
            delta = min(other_atoms)
            assert delta > 1
            power = delta
            while power <= upper_product:
                other_budget += 1
                power *= delta
        pending = [(0, x, q_budget, other_budget, ())]
        answers = []
        while pending:
            start, remaining, qs, others, chosen = pending.pop()
            if remaining == 1:
                answers.append(chosen)
                continue
            for index in range(start, len(atoms)):
                atom = atoms[index]
                q_cost = int(atom == self.q)
                other_cost = 1-q_cost
                if qs < q_cost or others < other_cost:
                    continue
                cofactor = remaining/atom
                if self.member(cofactor):
                    pending.append((index, cofactor, qs-q_cost,
                                    others-other_cost, chosen+(atom,)))
        return atoms, answers


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('a', 'b', 'm', 'k', 'numerator_r'):
        parser.add_argument(name, type=int)
    parser.add_argument('values', nargs='+')
    parser.add_argument('--factorizations', action='store_true')
    args = parser.parse_args()
    semiring = FiniteBasisMixed(args.a, args.b, args.m, args.k, args.numerator_r)
    for text in args.values:
        x = Fraction(text)
        result = {'q': str(semiring.q), 'r': str(semiring.r),
                  'x': str(x), 'member': semiring.member(x),
                  'cyclic_member': semiring.cyclic_member(x)}
        if args.factorizations and x > 0 and result['member']:
            atoms, facts = semiring.factorizations(x)
            result['atom_divisors'] = list(map(str, atoms))
            result['atomic_factorizations'] = [list(map(str, f)) for f in facts]
        print(json.dumps(result))


if __name__ == '__main__':
    main()
