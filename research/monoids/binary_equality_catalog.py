"""Independent all-match catalog using ordinary right masks, not Gray code."""
import argparse
import json


def catalog_degree(degree):
    if degree < 1:
        raise ValueError('degree must be positive')
    modulus = 3**degree
    left_count = max(m for m in range(degree)
                     if (5**m - 2**m) // 3 < modulus)
    maximum = (5**left_count - 2**left_count) // 3
    right_count = degree - 1 - left_count
    if right_count > 24:
        raise RuntimeError('inconclusive: right-mask cap exceeded')
    factor = 2 * 5**(degree - left_count)
    inverse = pow(factor, -1, modulus)
    endpoint = 5**degree + 2**degree
    weights = [2**i * 5**(degree - i) for i in range(left_count + 1, degree)]
    matches = []
    for mask in range(1 << right_count):
        right_sum = sum(weight for bit, weight in enumerate(weights)
                        if mask & (1 << bit))
        value = -(endpoint + right_sum) * inverse % modulus
        if value > maximum:
            continue
        digits = []
        for remaining in range(left_count - 1, -1, -1):
            if value > (5**(remaining + 1) - 2**(remaining + 1)) // 3:
                break
            digit = value % 2
            value -= digit * 5**remaining
            if value < 0:
                break
            value //= 2
            digits.append(digit)
        if len(digits) != left_count or value:
            continue
        coefficients = [1] + digits + [(mask >> bit) & 1 for bit in range(right_count)] + [1]
        numerator = sum(c * 2**i * 5**(degree - i)
                        for i, c in enumerate(coefficients))
        assert numerator % modulus == 0
        valuation, outside = 0, numerator
        while outside % 3 == 0:
            valuation += 1
            outside //= 3
        matches.append({'coefficients': coefficients, 'numerator': str(numerator),
                        'v3': valuation, 'outside_part': str(outside)})
    assert len({tuple(row['coefficients']) for row in matches}) == len(matches)
    return {'degree': degree, 'threshold': degree, 'left_digits': left_count,
            'right_digits': right_count, 'subsets_checked': 1 << right_count,
            'matches': matches}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('start', type=int)
    parser.add_argument('stop', type=int)
    arguments = parser.parse_args()
    if not 1 <= arguments.start <= arguments.stop:
        parser.error('require 1<=start<=stop')
    for degree in range(arguments.start, arguments.stop + 1):
        print(json.dumps(catalog_degree(degree)), flush=True)
