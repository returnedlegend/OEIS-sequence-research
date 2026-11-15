"""Exact finite atom/divisor algorithm for the reciprocal family.

Hypotheses: a>1, gcd(a,b)=1, at least two primes divide b,
and every maximal prime-power factor of b exceeds a. See
RECIPROCAL_TRANSFER_AND_GENERAL_FAMILY.md. Fractions and comparisons are exact.
The exhaustive polynomial factor test favors clarity over large inputs.
"""
from fractions import Fraction
from itertools import product
from math import gcd, isqrt
import argparse
import json


def factor_integer(n):
    if n < 1:
        raise ValueError("Expected a positive integer")
    factors = {}
    p = 2
    while p <= isqrt(n):
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def valuation(x, p):
    x = Fraction(x)
    if x <= 0:
        raise ValueError("Valuation requires a positive rational")
    n, d, v = x.numerator, x.denominator, 0
    while n % p == 0:
        n //= p
        v += 1
    while d % p == 0:
        d //= p
        v -= 1
    return v


def divisors(n):
    result = [1]
    for p, e in factor_integer(n).items():
        result = [d * p**j for d in result for j in range(e + 1)]
    return sorted(result)


def cyclic_digits(x, a, b):
    """Canonical finite nonnegative polynomial at a/b, or None."""
    x = Fraction(x)
    if x < 0:
        return None
    d = x.denominator
    while d > 1:
        common = gcd(d, b)
        if common == 1:
            return None
        d //= common
    coefficients = []
    while x.denominator != 1:
        c = (x.numerator * pow(x.denominator, -1, a)) % a
        if x < c:
            return None
        coefficients.append(c)
        x = (x - c) * b / a
    coefficients.append(x.numerator)
    while len(coefficients) > 1 and coefficients[-1] == 0:
        coefficients.pop()
    return tuple(coefficients)


def in_reciprocal(x, a, b):
    x = Fraction(x)
    if x <= 0:
        return False
    inverse = Fraction(b, a)
    threshold, k = inverse, 0
    while threshold <= x:
        k += 1
        threshold *= inverse
    return cyclic_digits(x * Fraction(a, b)**k, a, b) is not None


def polynomial_quotient(f, g):
    """Return an integer nonnegative quotient, or None."""
    remainder = list(f)
    quotient = [0] * (len(f) - len(g) + 1)
    for shift in range(len(quotient) - 1, -1, -1):
        coefficient, residue = divmod(remainder[shift + len(g) - 1], g[-1])
        if residue or coefficient < 0:
            return None
        quotient[shift] = coefficient
        for j, value in enumerate(g):
            remainder[shift + j] -= coefficient * value
    if any(remainder):
        return None
    return tuple(quotient)


def formal_atom(f):
    """Irreducibility in N_0[X], for f with positive constant term."""
    if not f or f[0] <= 0 or f == (1,):
        return False
    content = 0
    for c in f:
        content = gcd(content, c)
    if len(f) == 1:
        return len(factor_integer(f[0])) == 1 and next(iter(factor_integer(f[0]).values())) == 1
    if content > 1:
        return False
    # If f=g*h with positive constants, g_i <= f_i since h_0>=1.
    # At least one factor has degree at most half the degree of f.
    for degree in range(1, (len(f) - 1) // 2 + 1):
        for constant in divisors(f[0]):
            for leading in divisors(f[-1]):
                if leading > f[degree]:
                    continue
                for middle in product(*(range(f[i] + 1) for i in range(1, degree))):
                    g = (constant, *middle, leading)
                    if polynomial_quotient(f, g) is not None:
                        return False
    return True


class ReciprocalFamily:
    def __init__(self, a, b):
        numerator_factors, denominator_factors = factor_integer(a), factor_integer(b)
        if a < 2 or gcd(a, b) != 1:
            raise ValueError("a must be greater than one and coprime to b")
        if len(denominator_factors) < 2 or any(p**e <= a for p, e in denominator_factors.items()):
            raise ValueError("b needs >=2 prime factors, with each maximal prime power >a")
        self.a, self.b = a, b
        self.numerator_factors = numerator_factors
        self.ell, self.s = next(iter(numerator_factors.items()))
        self.t = Fraction(a, b)
        self.primes = set(denominator_factors) | set(numerator_factors)
        self.denominator_bound = 1
        for p, e in denominator_factors.items():
            self.denominator_bound *= p**(e - 1)

    def unit_exponent(self, x):
        x = Fraction(x)
        exponent, residue = divmod(valuation(x, self.ell), self.s)
        return exponent if residue == 0 and self.t**exponent == x else None

    def norm(self, x):
        # The s-th power of the real norm I; rational and exact.
        x = Fraction(x)
        return x**self.s / self.t**valuation(x, self.ell)

    def atom_divisors(self, x):
        x = Fraction(x)
        if not in_reciprocal(x, self.a, self.b):
            raise ValueError("x is not a nonzero element of the reciprocal semiring")
        outside = x.numerator
        for p in self.primes:
            while outside % p == 0:
                outside //= p
        bound = self.denominator_bound * outside
        for ell, exponent in self.numerator_factors.items():
            norm = x**exponent / self.t**valuation(x, ell)
            threshold, valuation_bound = 1 / self.t, 0
            while threshold <= norm:
                valuation_bound += 1
                threshold /= self.t
            if len(self.numerator_factors) == 1:
                valuation_bound = min(valuation_bound, exponent - 1)
            bound *= ell**valuation_bound
        atoms, candidate_bound = set(), 0
        for numerator in divisors(bound):
            denominator = 1
            while denominator <= numerator:
                candidate_bound += 1
                beta = Fraction(numerator, denominator)
                coefficients = cyclic_digits(beta, self.a, self.b)
                if (coefficients and coefficients[0] > 0
                        and max(coefficients) < self.a and formal_atom(coefficients)
                        and in_reciprocal(x / beta, self.a, self.b)):
                    atoms.add(beta)
                denominator *= self.b
        return sorted(atoms), candidate_bound

    def factorizations(self, x):
        x = Fraction(x)
        atoms, candidate_bound = self.atom_divisors(x)
        norms = [self.norm(alpha) for alpha in atoms]
        answers = []

        pending = [(0, x, self.norm(x), [])]
        while pending:
            index, remainder, remaining_norm, exponents = pending.pop()
            if index == len(atoms):
                exponent = self.unit_exponent(remainder)
                if exponent is not None:
                    answers.append({"unit_power": exponent, "atom_exponents": exponents})
                continue
            power, norm_power, multiplicity = Fraction(1), Fraction(1), 0
            children = []
            while norm_power <= remaining_norm:
                children.append((index + 1, remainder / power, remaining_norm / norm_power,
                                 exponents + [multiplicity]))
                power *= atoms[index]
                norm_power *= norms[index]
                multiplicity += 1
            pending.extend(reversed(children))
        return {"a": self.a, "b": self.b, "x": str(x),
                "normalized_atom_divisors": [str(alpha) for alpha in atoms],
                "candidate_bound": candidate_bound, "factorizations": answers}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    parser.add_argument("x", help="positive rational, e.g. 243/128")
    arguments = parser.parse_args()
    family = ReciprocalFamily(arguments.a, arguments.b)
    print(json.dumps(family.factorizations(Fraction(arguments.x)), indent=2))


if __name__ == "__main__":
    main()
