"""Exact membership and atomic factorizations for N_0[2/5, 2/3].

Every atomic-factorization set is finite, although IDF is unresolved.
The candidate list below is complete for atoms appearing in atomic
factorizations; it is NOT claimed to list every atom divisor.
See BINARY_PAIR_ATOMIC_FACTORIZATIONS.md for the proof and bounds.
"""

import argparse
from fractions import Fraction
import json

from reciprocal_factorizations import (
    cyclic_digits,
    divisors,
    factor_integer,
    formal_atom,
    valuation,
)


Q = Fraction(2, 5)
R = Fraction(2, 3)
H = Fraction(5, 3)


def _denominator_supported(x):
    denominator = Fraction(x).denominator
    for prime in (3, 5):
        while denominator % prime == 0:
            denominator //= prime
    return denominator == 1


def in_binary_pair(x):
    """Decide membership, including zero, using exact rational arithmetic."""
    current = Fraction(x)
    if current < 0 or not _denominator_supported(current):
        return False
    # q*S = S intersect 2*Z[1/15]. Below H, an odd element of S
    # must have constant coefficient exactly 1. These facts justify
    # each digit step; the denominator-orbit argument proves termination.
    while 0 < current < H:
        coefficient = current.numerator % 2
        if current < coefficient:
            return False
        current = (current - coefficient) / Q
    return True


def _outside_part(x):
    outside = Fraction(x).numerator
    for prime in (2, 3, 5):
        while outside % prime == 0:
            outside //= prime
    return outside


def factorization_candidates(x):
    """Return a proved finite superset of atoms in atomic factorizations."""
    x = Fraction(x)
    if x <= 0 or not in_binary_pair(x):
        raise ValueError("x must be a nonzero element of N_0[2/5,2/3]")

    q_exponent = valuation(x, 2)
    remaining_value = x / Q**q_exponent
    outside = _outside_part(x)
    outside_factors = factor_integer(outside)
    outside_multiplicity = sum(outside_factors.values())
    h_exponent_bound = 0
    h_power = H
    while h_power <= remaining_value:
        h_exponent_bound += 1
        h_power *= H
    binary_v3_budget = valuation(x, 3) + h_exponent_bound + outside_multiplicity

    bounds = {
        "q_exponent": q_exponent,
        "h_exponent_bound": h_exponent_bound,
        "outside_numerator": outside,
        "outside_prime_multiplicity": outside_multiplicity,
        "binary_v3_budget": binary_v3_budget,
        "atomic_length_bound": (
            q_exponent + valuation(x, 3)
            + 2 * h_exponent_bound + 2 * outside_multiplicity
        ),
    }
    if binary_v3_budget < 0:
        return [], bounds

    candidates = {}
    if h_exponent_bound:
        candidates[H] = {"value": str(H), "kind": "h"}

    outside_divisors = divisors(outside)
    endpoint_checks = 0
    for numerator in outside_divisors:
        denominator_power, degree = 5, 1
        while 3 * denominator_power < numerator:
            endpoint_checks += 1
            atom = Fraction(numerator, 3 * denominator_power)
            if atom < H:
                prefix = atom - Q**degree * R
                coefficients = cyclic_digits(prefix, 2, 5)
                if (coefficients and coefficients[0] == 1
                        and max(coefficients) <= 1 and len(coefficients) <= degree):
                    candidates[atom] = {
                        "value": str(atom), "kind": "endpoint",
                        "prefix": list(coefficients), "last_zero": degree,
                    }
            denominator_power *= 5
            degree += 1

    finite_checks = 0
    for outside_numerator in outside_divisors:
        numerator = outside_numerator
        for exponent in range(binary_v3_budget + 1):
            finite_checks += 1
            denominator_power, degree = 1, 0
            while denominator_power * 5 < numerator:
                denominator_power *= 5
                degree += 1
            if degree:
                atom = Fraction(numerator, denominator_power)
                if atom < H:
                    coefficients = cyclic_digits(atom, 2, 5)
                    if (coefficients and coefficients[0] == 1
                            and max(coefficients) <= 1 and formal_atom(coefficients)):
                        candidates[atom] = {
                            "value": str(atom), "kind": "finite_binary",
                            "polynomial": list(coefficients), "v3": exponent,
                        }
            numerator *= 3

    bounds["endpoint_candidate_checks"] = endpoint_checks
    bounds["finite_numerator_checks"] = finite_checks
    return [candidates[atom] for atom in sorted(candidates)], bounds


def factorizations(x):
    """Enumerate every atomic factorization; units are trivial."""
    x = Fraction(x)
    candidates, bounds = factorization_candidates(x)
    if bounds["binary_v3_budget"] < 0:
        return {
            "x": str(x), "bounds": bounds,
            "factorization_candidates": [], "factorizations": [],
        }
    atoms = [Fraction(candidate["value"]) for candidate in candidates]
    answers = []

    pending = [(0, x / Q**bounds["q_exponent"], [])]
    while pending:
        index, remainder, exponents = pending.pop()
        if remainder < 1 or not _denominator_supported(remainder):
            continue
        if index == len(atoms):
            if remainder == 1:
                answers.append({
                    "q_exponent": bounds["q_exponent"],
                    "atom_exponents": exponents,
                })
            continue
        power, exponent = Fraction(1), 0
        children = []
        while power <= remainder:
            children.append((index + 1, remainder / power, exponents + [exponent]))
            power *= atoms[index]
            exponent += 1
        pending.extend(reversed(children))
    return {
        "x": str(x), "bounds": bounds,
        "factorization_candidates": candidates, "factorizations": answers,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("x", help="positive rational, e.g. 125/81 or 19/15")
    parser.add_argument("--membership", action="store_true", help="only test membership")
    arguments = parser.parse_args()
    x = Fraction(arguments.x)
    answer = {"x": str(x), "in_semiring": in_binary_pair(x)} if arguments.membership else factorizations(x)
    print(json.dumps(answer, indent=2))


if __name__ == "__main__":
    main()
