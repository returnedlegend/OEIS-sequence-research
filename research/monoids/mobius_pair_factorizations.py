"""Exact algorithms for N_0[a/b, a/(b-a)] with b>2a and gcd(a,b)=1.

Membership and atom tests apply to every such pair. Complete atomic
factorizations are enumerated when some prime-power block ell**e || b
exceeds a. This does not decide IDF. See MOBIUS_PAIR_NORMAL_FORMS.md.
All optional resource limits raise InconclusiveError when exhausted.
"""

import argparse
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
import json
from math import gcd


class InconclusiveError(RuntimeError):
    """A resource limit was reached; no negative mathematical claim follows."""


class _Budget:
    def __init__(self, limit, description):
        if limit is not None and limit < 0:
            raise ValueError("resource limits must be nonnegative or None")
        self.limit, self.description, self.used = limit, description, 0

    def tick(self):
        if self.limit is not None and self.used >= self.limit:
            raise InconclusiveError(f"{self.description} limit {self.limit} reached")
        self.used += 1


def _factor_integer(n):
    factors = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            factors[p] = factors.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def _valuation(x, prime):
    x = Fraction(x)
    if not x:
        raise ValueError("zero has no finite valuation")
    result = 0
    numerator, denominator = abs(x.numerator), x.denominator
    while numerator % prime == 0:
        result += 1
        numerator //= prime
    while denominator % prime == 0:
        result -= 1
        denominator //= prime
    return result


def _trim(coefficients):
    result = list(coefficients)
    while result and result[-1] == 0:
        result.pop()
    return result


def _polynomial_quotient(dividend, divisor):
    """Exact division in Z[X], allowing signed coefficients; None on failure."""
    remainder, divisor = _trim(dividend), _trim(divisor)
    if not divisor:
        raise ZeroDivisionError("zero polynomial")
    if len(remainder) < len(divisor):
        return [] if not remainder else None
    quotient = [0] * (len(remainder) - len(divisor) + 1)
    while remainder and len(remainder) >= len(divisor):
        shift = len(remainder) - len(divisor)
        coefficient, residue = divmod(remainder[-1], divisor[-1])
        if residue:
            return None
        quotient[shift] = coefficient
        for j, value in enumerate(divisor):
            remainder[shift + j] -= coefficient * value
        remainder = _trim(remainder)
    return _trim(quotient) if not remainder else None


def _finite_atom(coefficients, budget):
    """Irreducibility in N_0[X] for a polynomial with positive constant."""
    f = _trim(coefficients)
    if not f or not f[0]:
        raise ValueError("positive constant coefficient required")
    if len(f) == 1:
        return f[0] > 1 and _factor_integer(f[0]) == {f[0]: 1}
    content = 0
    for coefficient in f:
        content = gcd(content, coefficient)
    if content > 1:
        return False
    # In a nonconstant factorization, some factor has degree at most n/2.
    # If its constant is g0, its partner's constant is h0=f0/g0, so
    # coefficientwise 0<=g_i<=f_i/h0.
    for degree in range(1, (len(f) - 1) // 2 + 1):
        for g0 in range(1, f[0] + 1):
            if f[0] % g0:
                continue
            h0 = f[0] // g0
            ranges = [range(f[i] // h0 + 1) for i in range(1, degree)]
            ranges.append(range(1, f[degree] // h0 + 1))
            for rest in product(*ranges):
                budget.tick()
                quotient = _polynomial_quotient(f, (g0,) + rest)
                if quotient is not None and all(c >= 0 for c in quotient):
                    return False
    return True


def _weak_compositions(total, count):
    """Iterative generator; no recursion-depth dependence on degree."""
    pending = [(total, count, ())]
    while pending:
        remaining, slots, prefix = pending.pop()
        if slots == 1:
            yield prefix + (remaining,)
        else:
            for first in range(remaining, -1, -1):
                pending.append((remaining - first, slots - 1, prefix + (first,)))


@dataclass(frozen=True)
class NormalForm:
    """F=sum(prefix[j]*X**j)+tail*X**len(prefix)/(1-X)."""
    prefix: tuple
    tail: int


class MobiusPair:
    def __init__(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("a and b must be integers")
        if a < 2 or b <= 2 * a or gcd(a, b) != 1:
            raise ValueError("require a>=2, b>2a, and gcd(a,b)=1")
        self.a, self.b, self.p = a, b, b - a
        self.q, self.r = Fraction(a, b), Fraction(a, b - a)
        self.h, self.conductor = Fraction(b, b - a), Fraction((a - 1) * b, b - a)
        self.a_factors, self.b_factors = _factor_integer(a), _factor_integer(b)
        self.denominator_primes = tuple(_factor_integer(b * (b - a)))
        self.good_blocks = tuple((ell, e) for ell, e in self.b_factors.items()
                                 if ell**e > a)

    def _in_ring(self, value):
        denominator = Fraction(value).denominator
        for prime in self.denominator_primes:
            while denominator % prime == 0:
                denominator //= prime
        return denominator == 1

    def _digit(self, value):
        return value.numerator * pow(value.denominator, -1, self.a) % self.a

    def contains(self, value, max_steps=100000):
        """Decide semiring membership, including zero."""
        current = Fraction(value)
        if current < 0 or not self._in_ring(current):
            return False
        budget, seen = _Budget(max_steps, "membership states"), set()
        while 0 < current < self.conductor:
            budget.tick()
            if current in seen:
                return False  # A nonconstant cycle cannot be a T-series.
            seen.add(current)
            coefficient = self._digit(current)
            if current < coefficient:
                return False
            following = (current - coefficient) / self.q
            if following == current:
                return True  # The constant-tail series coefficient/(1-X).
            current = following
        return True

    def digits(self, value, max_steps=100000):
        """Return its bounded eventually constant form, or None if none exists.

        A member with a coefficient >=a need not have such a form. Thus
        None here is not itself a nonmembership assertion.
        """
        current = Fraction(value)
        if current < 0 or not self._in_ring(current):
            return None
        budget, seen, digits = _Budget(max_steps, "digit states"), {}, []
        while current:
            budget.tick()
            if current > self.conductor:
                return None
            if current in seen:
                start = seen[current]
                cycle = digits[start:]
                if len(set(cycle)) != 1:
                    return None
                tail, prefix = cycle[0], digits[:start]
                while prefix and prefix[-1] == tail:
                    prefix.pop()
                return NormalForm(tuple(prefix), tail)
            seen[current] = len(digits)
            coefficient = self._digit(current)
            if current < coefficient:
                return None
            digits.append(coefficient)
            current = (current - coefficient) / self.q
        return NormalForm(tuple(_trim(digits)), 0)

    def evaluate(self, normal_form):
        """Evaluate a NormalForm exactly."""
        value, power = Fraction(0), Fraction(1)
        for coefficient in normal_form.prefix:
            value += coefficient * power
            power *= self.q
        return value + normal_form.tail * power / (1 - self.q)

    def _normal_form_atom(self, form, budget):
        f, tail = form.prefix, form.tail
        constant = f[0] if f else tail
        if not constant:
            return tail == 0 and f == (0, 1)
        if not tail:
            return _finite_atom(f, budget)
        if tail == 1:
            return True
        # For an infinite factorization F=G*H, exactly one factor G is
        # finite; G(1) divides the eventual coefficient tail. Put
        # P=(1-X)F. Then G divides P in Z[X], and H=P/G/(1-X) is
        # nonnegative iff all partial sums of P/G are nonnegative.
        p = [tail] if not f else [f[0]] + [f[i] - f[i - 1] for i in range(1, len(f))] + [tail - f[-1]]
        degree = len(p) - 1
        for coefficient_sum in range(2, tail + 1):
            if tail % coefficient_sum:
                continue
            for g0 in range(1, coefficient_sum + 1):
                if p[0] % g0:
                    continue
                tails = [()] if degree == 0 and g0 == coefficient_sum else (
                    _weak_compositions(coefficient_sum - g0, degree) if degree else [])
                for other in tails:
                    budget.tick()
                    quotient = _polynomial_quotient(p, (g0,) + tuple(other))
                    if quotient is None:
                        continue
                    partial, nonnegative = 0, True
                    for coefficient in quotient:
                        partial += coefficient
                        if partial < 0:
                            nonnegative = False
                            break
                    if nonnegative and partial > 0:
                        return False
        return True

    def is_atom(self, value, max_steps=100000, max_checks=100000):
        """Decide atomhood globally, using uniqueness of bounded forms."""
        value = Fraction(value)
        if value <= 0 or value == 1:
            return False
        form = self.digits(value, max_steps=max_steps)
        if form is None:
            return False
        return self._normal_form_atom(form, _Budget(max_checks, "formal factor checks"))

    def factorization_candidates(self, value, max_candidates=100000, max_steps=100000):
        """Finite candidate atoms for complete factorizations, plus proof bounds.

        This is not claimed to list every atom divisor of value.
        """
        x = Fraction(value)
        if x <= 0 or not self.contains(x, max_steps=max_steps):
            raise ValueError("value must be a nonzero member of this semiring")
        if not self.good_blocks:
            raise ValueError("complete enumeration requires a prime-power block ell**e || b exceeding a")
        q_bound = min(_valuation(x, t) // exponent for t, exponent in self.a_factors.items())
        y = x / self.q**q_bound
        h_bound, power = 0, self.h
        while power <= y:
            h_bound += 1
            power *= self.h
        choices = []
        for ell, e in self.good_blocks:
            s, power = 0, ell
            while power <= self.a - 1:
                s += 1
                power *= ell
            negative_budget = e * h_bound - _valuation(x, ell)
            degree_bound = (negative_budget + s) // e
            choices.append((degree_bound, ell, e, s, negative_budget))
        degree_bound, ell, e, s, negative_budget = min(choices)
        bounds = {"ell": ell, "e": e, "s": s, "q_exponent_bound": q_bound,
                  "h_exponent_bound": h_bound, "negative_valuation_budget": negative_budget,
                  "degree_bound": degree_bound,
                  "atomic_length_bound": q_bound + h_bound + negative_budget // (e - s)}
        if negative_budget < 0:
            return [], bounds
        budget, atoms = _Budget(max_candidates, "candidate/formal-factor checks"), set()

        def examine(form):
            budget.tick()
            atom = self.evaluate(form)
            if atom <= 1 or atom > y or not self._in_ring(x / atom):
                return
            if self._normal_form_atom(form, budget):
                atoms.add(atom)

        # Degree-zero finite forms and index-zero endpoints are exceptional;
        # include them even when no positive degree is allowed.
        for constant in range(2, self.a):
            examine(NormalForm((constant,), 0))
        examine(NormalForm((), 1))
        for degree in range(1, degree_bound + 1):
            for constant in range(1, self.a):
                for middle in product(range(self.a), repeat=degree - 1):
                    for leading in range(1, self.a):
                        examine(NormalForm((constant,) + middle + (leading,), 0))
        for index in range(max(0, degree_bound) + 1):
            for tail in range(1, self.a):
                if index == 0:
                    for constant in range(1, self.a):
                        if constant != tail:
                            examine(NormalForm((constant,), tail))
                else:
                    for constant in range(1, self.a):
                        for middle in product(range(self.a), repeat=index - 1):
                            for last in range(self.a):
                                if last != tail:
                                    examine(NormalForm((constant,) + middle + (last,), tail))
        bounds["candidate_and_formal_checks"] = budget.used
        return sorted(atoms), bounds

    def factorizations(self, value, max_candidates=100000, max_nodes=1000000, max_steps=100000):
        """Enumerate all atomic factorizations as sorted tuples of rationals."""
        x = Fraction(value)
        atoms, bounds = self.factorization_candidates(x, max_candidates=max_candidates, max_steps=max_steps)
        if bounds["negative_valuation_budget"] < 0:
            return []
        budget, answers = _Budget(max_nodes, "factorization nodes"), []
        for q_count in range(bounds["q_exponent_bound"] + 1):
            pending = [(0, x / self.q**q_count, ())]
            while pending:
                budget.tick()
                index, remainder, factors = pending.pop()
                if remainder < 1 or not self._in_ring(remainder):
                    continue
                if remainder == 1:
                    answers.append((self.q,) * q_count + factors)
                    continue
                if index == len(atoms):
                    continue
                atom, power, repeated = atoms[index], Fraction(1), ()
                while power <= remainder:
                    budget.tick()
                    pending.append((index + 1, remainder / power, factors + repeated))
                    power *= atom
                    repeated += (atom,)
        return sorted(answers)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    parser.add_argument("x", help="rational value, for example 531441/390625")
    parser.add_argument("--membership", action="store_true")
    parser.add_argument("--atom", action="store_true")
    parser.add_argument("--max-candidates", type=int, default=100000)
    parser.add_argument("--max-nodes", type=int, default=1000000)
    parser.add_argument("--max-steps", type=int, default=100000)
    args = parser.parse_args()
    pair, x = MobiusPair(args.a, args.b), Fraction(args.x)
    try:
        if args.membership:
            answer = {"x": str(x), "in_semiring": pair.contains(x, args.max_steps)}
        elif args.atom:
            answer = {"x": str(x), "is_atom": pair.is_atom(x, args.max_steps, args.max_candidates)}
        else:
            atoms, bounds = pair.factorization_candidates(x, args.max_candidates, args.max_steps)
            factorizations = pair.factorizations(x, args.max_candidates, args.max_nodes, args.max_steps)
            answer = {"x": str(x), "bounds": bounds,
                      "factorization_candidates": [str(atom) for atom in atoms],
                      "factorizations": [[str(atom) for atom in factors] for factors in factorizations]}
    except InconclusiveError as error:
        answer = {"x": str(x), "status": "inconclusive", "reason": str(error)}
    print(json.dumps(answer, indent=2))


if __name__ == "__main__":
    main()
