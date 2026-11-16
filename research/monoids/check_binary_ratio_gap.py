"""Exact small checks for the binary ratio carry-graph algorithm."""

from fractions import Fraction
from itertools import product

from binary_ratio_gap_search import analyze_ratio, search


Q = Fraction(2, 5)


def check_witness(answer, ratio):
    pairs = answer["coefficient_pairs"]
    assert pairs[0] == [1, 1]
    numerator = sum((Q**j * pair[0] for j, pair in enumerate(pairs)), Fraction())
    denominator = sum((Q**j * pair[1] for j, pair in enumerate(pairs)), Fraction())
    assert numerator / denominator == ratio


def main():
    values = [Fraction(1)]
    for degree in range(1, 7):
        for middle in product((0, 1), repeat=degree-1):
            coefficients = (1, *middle, 1)
            values.append(sum((Q**j*c for j, c in enumerate(coefficients)), Fraction()))
    assert len(values) == 64
    for numerator in values:
        for denominator in values:
            ratio = numerator / denominator
            answer = analyze_ratio(ratio.numerator, ratio.denominator)
            assert answer["status"] == "witness"
            check_witness(answer, ratio)

    witness_count = 0
    for numerator in range(1, 52, 2):
        for denominator in range(1, 52, 2):
            ratio = Fraction(numerator, denominator)
            answer = analyze_ratio(numerator, denominator)
            assert answer["status"] != "inconclusive"
            if answer["status"] == "witness":
                check_witness(answer, ratio)
                witness_count += 1
    assert witness_count == 50

    capped = search(11, max_states=1)
    assert not capped["complete"]
    assert capped["obstruction"]["status"] == "inconclusive"
    result = search(10000)
    assert result["complete"] and result["excluded_through"] == 10000
    assert result["real_admissible_ratios_tested"] == 9299
    assert result["maximum_reachable_states"] == 449
    assert result["ratios_with_reachable_cycle"] == 0
    print("Passed: 4096 known binary ratios, 676 small odd ratios, exact witness "
          "reconstruction, explicit cap handling, and exclusion of 10000 gaps.")


if __name__ == "__main__":
    main()
