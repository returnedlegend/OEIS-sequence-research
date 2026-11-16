"""Exact modular subset-sum search for binary f(2/5) with v_3(N)>degree(f).

Here N=5**n*f(2/5), and the constant and leading coefficients are 1.
Splitting the n-1 free digits gives O(2**(n/2)) search and storage.
No floating-point arithmetic participates in a mathematical decision.
"""

import argparse
import json
from time import monotonic


class InconclusiveError(RuntimeError):
    """The requested computation exceeds its explicit resource bound."""


def gray_sums(weights, modulus):
    """Yield (subset residue, subset mask) for every subset exactly once."""
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    weights = tuple(weight % modulus for weight in weights)
    current = 0
    yield 0, 0
    for index in range(1, 1 << len(weights)):
        lowbit = index & -index
        weight = weights[lowbit.bit_length() - 1]
        gray = index ^ (index >> 1)
        if gray & lowbit:
            current += weight
            if current >= modulus:
                current -= modulus
        else:
            current -= weight
            if current < 0:
                current += modulus
        yield current, gray


def check_degree(degree, exponent=None, max_half_bits=24):
    """Find a binary numerator divisible by 3**exponent, or exclude all.

    The default exponent=degree+1 tests the conjectured degree bound.
    A different exponent supports exact positive-control tests, such as
    degree=4, exponent=4, which finds the known numerator891.
    Exhausting the half-size cap raises InconclusiveError.
    """
    if degree < 1:
        raise ValueError("degree must be positive")
    exponent = degree + 1 if exponent is None else exponent
    if exponent < 1:
        raise ValueError("valuation threshold must be positive")
    if max_half_bits < 0:
        raise ValueError("max_half_bits must be nonnegative")
    left_count = (degree - 1) // 2
    right_count = degree - 1 - left_count
    if right_count > max_half_bits:
        raise InconclusiveError(f"half-size {right_count} exceeds cap {max_half_bits}")

    modulus = 3**exponent
    weights = [2**i * 5**(degree - i) % modulus for i in range(1, degree)]
    left, right = weights[:left_count], weights[left_count:]
    target = -(5**degree + 2**degree) % modulus
    started = monotonic()
    residues = {value for value, _ in gray_sums(left, modulus)}
    result = {
        "degree": degree, "valuation_threshold": exponent,
        "modulus": str(modulus), "left_subsets": 1 << left_count,
        "left_residues": len(residues), "right_subsets": 1 << right_count,
    }
    for right_checked, (right_sum, right_mask) in enumerate(gray_sums(right, modulus), 1):
        complement = target - right_sum
        if complement < 0:
            complement += modulus
        if complement not in residues:
            continue

        left_mask = next(mask for value, mask in gray_sums(left, modulus)
                         if value == complement)
        coefficients = (
            [1] + [(left_mask >> i) & 1 for i in range(left_count)]
            + [(right_mask >> i) & 1 for i in range(right_count)] + [1]
        )
        numerator = sum(c * 2**i * 5**(degree - i)
                        for i, c in enumerate(coefficients))
        if numerator % modulus:
            raise AssertionError("exact witness reconstruction failed")
        valuation, remaining = 0, numerator
        while remaining % 3 == 0:
            valuation += 1
            remaining //= 3
        result.update(
            threshold_match=True, violates_degree_bound=(valuation > degree),
            coefficients=coefficients, numerator=str(numerator), v3=valuation,
            outside_part=str(remaining), right_checked=right_checked,
            seconds=round(monotonic() - started, 3),
        )
        return result

    result.update(threshold_match=False, right_checked=1 << right_count,
                  seconds=round(monotonic() - started, 3))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("start", type=int)
    parser.add_argument("stop", type=int)
    parser.add_argument("--offset", type=int, default=1,
                        help="valuation threshold is degree+offset (default1)")
    parser.add_argument("--max-half-bits", type=int, default=24)
    arguments = parser.parse_args()
    if not 1 <= arguments.start <= arguments.stop:
        parser.error("require 1<=start<=stop")
    for degree in range(arguments.start, arguments.stop + 1):
        try:
            result = check_degree(degree, degree + arguments.offset, arguments.max_half_bits)
        except InconclusiveError as error:
            print(json.dumps({"degree": degree, "status": "inconclusive", "reason": str(error)}))
            return 2
        print(json.dumps(result), flush=True)
        if result["threshold_match"]:
            break
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
