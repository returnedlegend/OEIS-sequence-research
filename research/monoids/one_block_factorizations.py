"""Exact finite atomic factorizations for one-good-block cyclic semirings.

Requires gcd(a,b)=1, 1<a<b, at least two denominator primes, and some
prime-power factor p**v_p(b)>a. This does not decide global IDF.
"""

from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import gcd


def factor_integer(n):
    factors = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p+2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def valuation(x, p):
    x = F(x)
    n, d, result = x.numerator, x.denominator, 0
    if n <= 0:
        raise ValueError("valuation requires a positive rational")
    while n % p == 0:
        n //= p
        result += 1
    while d % p == 0:
        d //= p
        result -= 1
    return result


def floor_log(base, value):
    base, value = F(base), F(value)
    if base <= 1 or value < 1:
        raise ValueError("logarithm bounds require base>1 and value>=1")
    power, exponent = F(1), 0
    while power*base <= value:
        power *= base
        exponent += 1
    return exponent


def nonnegative_quotient(f, g):
    remainder = [F(c) for c in f]
    quotient = [F(0)]*(len(f)-len(g)+1)
    for shift in range(len(f)-len(g), -1, -1):
        coefficient = remainder[shift+len(g)-1]/g[-1]
        quotient[shift] = coefficient
        for j, value in enumerate(g):
            remainder[shift+j] -= coefficient*value
    if any(remainder):
        return None
    if any(c < 0 or c.denominator != 1 for c in quotient):
        return None
    return tuple(int(c) for c in quotient)


@lru_cache(None)
def formal_atom(f):
    if len(f) == 1:
        return f[0] >= 2 and factor_integer(f[0]) == {f[0]: 1}
    content = 0
    for c in f:
        content = gcd(content, c)
    if content > 1:
        return False
    degree = len(f)-1
    for d in range(1, degree):
        if f[d] == 0:
            continue
        ranges = [range(1, f[0]+1)]
        ranges += [range(f[i]+1) for i in range(1, d)]
        ranges += [range(1, f[d]+1)]
        for g in product(*ranges):
            h = nonnegative_quotient(f, g)
            if h is not None and h != (1,):
                return False
    return True


class OneBlockSemiring:
    def __init__(self, a, b):
        if not 1 < a < b or gcd(a, b) != 1:
            raise ValueError("require reduced 1<a<b")
        self.a, self.b, self.t = a, b, F(a, b)
        self.A, self.P = factor_integer(a), factor_integer(b)
        good = [p for p, e in self.P.items() if p**e > a]
        if len(self.P) < 2 or not good:
            raise ValueError("require two denominator primes and a good block")
        self.p = min(good, key=lambda p: (p < a, -p))
        self.constants = tuple(p for p in range(2, a)
                               if factor_integer(p) == {p: 1})

    @lru_cache(None)
    def canonical(self, x):
        x = F(x)
        if x < 0:
            return None
        if x == 0:
            return (0,)
        denominator = x.denominator
        n = 0
        for p, e in self.P.items():
            count = 0
            while denominator % p == 0:
                denominator //= p
                count += 1
            n = max(n, (count+e-1)//e)
        if denominator != 1:
            return None
        power = self.b**n
        numerator = x.numerator*(power//x.denominator)
        coefficients = []
        for _ in range(n):
            c = numerator*pow(power, -1, self.a) % self.a
            coefficients.append(c)
            numerator = (numerator-c*power)//self.a
            power //= self.b
            if numerator < 0:
                return None
        coefficients.append(numerator)
        return tuple(coefficients)

    def member(self, x, reciprocal=False):
        x = F(x)
        if x <= 0:
            return False
        if not reciprocal:
            return self.canonical(x) is not None
        exponent, power = 0, F(1)
        while power/self.t <= x:
            exponent += 1
            power /= self.t
        return self.canonical(x*self.t**exponent) is not None

    def unit_exponents(self, x):
        lower, upper = [], []
        for ell, e in self.A.items():
            v = valuation(x, ell)
            norm = x**e*self.t**(-v)
            maximum = floor_log(1/self.t, norm)
            lower.append((v-maximum+e-1)//e)
            upper.append(v//e)
        return range(max(lower), min(upper)+1)

    def factor_atoms(self, target, degree_bound):
        result = []
        for p in self.constants:
            if p <= target and self.canonical(target/p) is not None:
                result.append((F(p), 0))
        for degree in range(1, degree_bound+1):
            ranges = [range(1, self.a)]
            ranges += [range(self.a) for _ in range(degree-1)]
            ranges += [range(1, self.a)]
            denominator = self.b**degree
            for coefficients in product(*ranges):
                numerator = sum(c*self.a**i*self.b**(degree-i)
                                for i, c in enumerate(coefficients))
                value = F(numerator, denominator)
                if value > target:
                    continue
                if self.canonical(target/value) is None:
                    continue
                if formal_atom(tuple(coefficients)):
                    result.append((value, degree))
        return tuple(sorted(result))

    def factorizations(self, x, reciprocal=False):
        """Return (k, tuple(normalized atoms)); t**k is the unit/S-t part."""
        x = F(x)
        if not self.member(x, reciprocal):
            raise ValueError("input is outside the selected nonzero monoid")
        records = []
        for k in self.unit_exponents(x):
            if not reciprocal and k < 0:
                continue
            target = x*self.t**(-k)
            if target < 1:
                continue
            prime_count = floor_log(self.p, target) if self.p < self.a else 0
            degree_bound = prime_count-valuation(target, self.p)
            if degree_bound < 0:
                continue
            constant_bound = floor_log(2, target)
            atoms = self.factor_atoms(target, degree_bound)
            stack = [(0, target, degree_bound, constant_bound, ())]
            while stack:
                start, remaining, degrees, constants, factors = stack.pop()
                if remaining == 1:
                    records.append((k, factors))
                    continue
                for index in range(start, len(atoms)):
                    atom, degree = atoms[index]
                    if atom > remaining:
                        break
                    if degree > degrees or (degree == 0 and constants == 0):
                        continue
                    stack.append((index, remaining/atom, degrees-degree,
                                  constants-(degree == 0), factors+(atom,)))
        return records


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    parser.add_argument("values", nargs="+")
    parser.add_argument("--reciprocal", action="store_true")
    args = parser.parse_args()
    semiring = OneBlockSemiring(args.a, args.b)
    for text in args.values:
        x = F(text)
        records = semiring.factorizations(x, args.reciprocal)
        print(f"{x}: {len(records)} atomic factorizations")
        for k, factors in records:
            print(f"  ({semiring.t})**{k} * " +
                  (" * ".join(map(str, factors)) if factors else "1"))
