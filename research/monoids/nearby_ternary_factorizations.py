"""Exact atoms and factorizations for N_0[3/(5n),7/5].

Requires n>2, gcd(n,21)=1, at least two denominator primes, and n!=1 mod5.
See NEARBY_TERNARY_IDF_FAMILY.md for completeness and termination proofs.
"""
from fractions import Fraction
from functools import lru_cache
from math import gcd
import argparse
import json

if __package__:
    from .reciprocal_factorizations import divisors, factor_integer, valuation
else:
    from reciprocal_factorizations import divisors, factor_integer, valuation


class NearbyTernary:
    def __init__(self, n):
        if n <= 2 or gcd(n, 21) != 1 or n % 5 == 1:
            raise ValueError("require n>2, gcd(n,21)=1, and n not congruent to1 modulo5")
        self.n = n
        self.base = 5*n
        self.primes = tuple(factor_integer(self.base))
        if len(self.primes) < 2:
            raise ValueError("require at least two distinct denominator primes")
        self.q = Fraction(3, self.base)
        self.r = Fraction(7, 5)
        self.conductor = self.r/(1-self.q)
        self.digits = (Fraction(0), Fraction(1), self.r)

    @lru_cache(None)
    def canonical(self, x):
        """Return digit labels and terminal integer, or None for nonmembership."""
        x = Fraction(x)
        if x < 0:
            return None
        denominator = x.denominator
        for p in self.primes:
            while denominator % p == 0:
                denominator //= p
        if denominator != 1:
            return None
        labels = []
        while x.denominator != 1:
            label = x.numerator*pow(x.denominator, -1, 3) % 3
            digit = self.digits[label]
            if x < digit:
                return None
            labels.append(label)
            x = (x-digit)/self.q
        return tuple(labels), x.numerator

    @lru_cache(None)
    def member(self, x):
        x = Fraction(x)
        return x > 0 and self.canonical(x) is not None

    @lru_cache(None)
    def critical(self, x):
        x = Fraction(x)
        result = self.canonical(x)
        return x > 0 and result is not None and result[1] in (0, 1)

    @lru_cache(None)
    def smooth_denominators(self, limit):
        limit = Fraction(limit)
        if limit < 1:
            return ()
        results = []

        def generate(index, value):
            if index == len(self.primes):
                results.append(value)
                return
            p = self.primes[index]
            while value <= limit:
                generate(index+1, value)
                value *= p

        generate(0, 1)
        return tuple(sorted(results))

    @lru_cache(None)
    def is_atom(self, x):
        x = Fraction(x)
        if x == 1 or not self.critical(x):
            return False
        # Every divisor of a critical element is critical. Its numerator
        # divides x.numerator and its value is at least q**v_3(x).
        assert gcd(x.numerator, self.base) == 1
        lower = self.q**valuation(x, 3)
        for numerator in divisors(x.numerator):
            for denominator in self.smooth_denominators(numerator/lower):
                divisor = Fraction(numerator, denominator)
                if divisor in (1, x):
                    continue
                if self.member(divisor) and self.member(x/divisor):
                    return False
        return True

    def atom_divisors(self, x):
        x = Fraction(x)
        if not self.member(x):
            raise ValueError("input is outside the nonzero monoid")
        outside = x.numerator
        for p in self.primes:
            while outside % p == 0:
                outside //= p
        atoms = set()
        if self.member(x/self.q):
            assert self.is_atom(self.q)
            atoms.add(self.q)
        for numerator in divisors(outside):
            for denominator in self.smooth_denominators(numerator):
                candidate = Fraction(numerator, denominator)
                if candidate == 1:
                    continue
                if self.is_atom(candidate) and self.member(x/candidate):
                    atoms.add(candidate)
        return tuple(sorted(atoms))

    def factorizations(self, x):
        x = Fraction(x)
        atoms = self.atom_divisors(x)
        if x == 1:
            return atoms, [()]
        budget = -valuation(x, 5)
        if budget <= 0:
            return atoms, []
        weights = tuple(-valuation(atom, 5) for atom in atoms)
        assert all(weight >= 1 for weight in weights)
        answers = []

        pending = [(0, x, budget, ())]
        while pending:
            start, remaining, available, chosen = pending.pop()
            if remaining == 1:
                answers.append(chosen)
                continue
            if available <= 0:
                continue
            for index in range(start, len(atoms)):
                if weights[index] > available:
                    continue
                cofactor = remaining/atoms[index]
                if self.member(cofactor):
                    pending.append((index, cofactor, available-weights[index],
                                    chosen+(atoms[index],)))

        return atoms, answers


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n", type=int)
    parser.add_argument("values", nargs="+")
    args = parser.parse_args()
    monoid = NearbyTernary(args.n)
    for value in args.values:
        x = Fraction(value)
        atoms, facts = monoid.factorizations(x)
        print(json.dumps({"n": args.n, "x": str(x),
                          "atom_divisors": list(map(str, atoms)),
                          "atomic_factorizations": [list(map(str, f)) for f in facts]}, indent=2))


if __name__ == "__main__":
    main()
