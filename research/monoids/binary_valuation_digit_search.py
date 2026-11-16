"""Exact table-free search for binary numerators divisible by a power of 3.

The left block is short enough that its entire value lies below the
modulus. Each right subset determines one candidate left value, which
is decoded exactly instead of looking it up in a stored subset table.
See BINARY_VALUATION_SEARCH.md for the completeness proof.
"""

import argparse
import json
from time import monotonic

from binary_valuation_mitm import InconclusiveError, gray_sums


def check_degree(degree, exponent=None, max_right_bits=30):
    """Find/exclude all binary degree-n numerators divisible by 3**exponent.

    Both endpoint digits are 1. The default exponent=n+1 tests v3(N)>n.
    Resource exhaustion raises InconclusiveError, never a false exclusion.
    """
    exponent = degree + 1 if exponent is None else exponent
    if degree < 1 or exponent < 1:
        raise ValueError("positive degree and valuation threshold required")
    if max_right_bits < 0:
        raise ValueError("max_right_bits must be nonnegative")
    modulus = 3**exponent

    # A_m=(5**m-2**m)/3 is the maximum m-digit block value.
    left_count, maximum, two_power = 0, 0, 1
    maxima = [0]
    while left_count < degree - 1:
        following = 5 * maximum + two_power
        if following >= modulus:
            break
        left_count += 1
        maximum = following
        maxima.append(maximum)
        two_power *= 2
    right_count = degree - 1 - left_count
    if right_count > max_right_bits:
        raise InconclusiveError(f"right block has {right_count} bits, exceeding cap {max_right_bits}")

    inverse = pow(2 * 5**(degree - left_count), -1, modulus)
    target = -(5**degree + 2**degree) * inverse % modulus
    weights = [2**i * 5**(degree - i) * inverse % modulus
               for i in range(left_count + 1, degree)]
    five_powers = [5**j for j in range(left_count)]
    started, decoded = monotonic(), 0
    result = {
        "degree": degree, "valuation_threshold": exponent,
        "left_digits": left_count, "right_digits": right_count,
        "right_subsets": 1 << right_count, "modulus": str(modulus),
        "left_maximum": str(maximum),
    }
    for checked, (residue, mask) in enumerate(gray_sums(weights, modulus), 1):
        value = target - residue
        if value < 0:
            value += modulus
        if value > maximum:
            continue
        decoded += 1
        left_digits = []
        for j in range(left_count - 1, -1, -1):
            if value > maxima[j + 1]:
                break
            digit = value & 1
            value -= digit * five_powers[j]
            if value < 0:
                break
            value //= 2
            left_digits.append(digit)
        if len(left_digits) != left_count or value:
            continue

        coefficients = (
            [1] + left_digits + [(mask >> j) & 1 for j in range(right_count)] + [1]
        )
        numerator = sum(c * 2**i * 5**(degree - i)
                        for i, c in enumerate(coefficients))
        if numerator % modulus:
            raise AssertionError("exact witness reconstruction failed")
        valuation, outside = 0, numerator
        while outside % 3 == 0:
            valuation += 1
            outside //= 3
        result.update(
            threshold_match=True, violates_degree_bound=(valuation > degree),
            coefficients=coefficients, numerator=str(numerator), v3=valuation,
            outside_part=str(outside), right_checked=checked,
            decoded_candidates=decoded, seconds=round(monotonic() - started, 3),
        )
        return result

    result.update(threshold_match=False, right_checked=1 << right_count,
                  decoded_candidates=decoded, seconds=round(monotonic() - started, 3))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("start", type=int)
    parser.add_argument("stop", type=int)
    parser.add_argument("--offset", type=int, default=1,
                        help="valuation threshold is degree+offset (default 1)")
    parser.add_argument("--max-right-bits", type=int, default=30)
    arguments = parser.parse_args()
    if not 1 <= arguments.start <= arguments.stop:
        parser.error("require 1<=start<=stop")
    for degree in range(arguments.start, arguments.stop + 1):
        try:
            result = check_degree(degree, degree + arguments.offset, arguments.max_right_bits)
        except InconclusiveError as error:
            print(json.dumps({"degree": degree, "status": "inconclusive", "reason": str(error)}))
            return 2
        print(json.dumps(result), flush=True)
        if result["threshold_match"]:
            break
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
