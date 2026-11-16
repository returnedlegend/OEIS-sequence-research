"""Verify the exact finite inputs for the atomic-integer classification."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path

from binary_equality_catalog import catalog_degree
from mobius_pair_factorizations import MobiusPair


ROOT = Path(__file__).parent


def direct_matches(degree):
    """Exhaust ordinary complete words, independently of the block method."""
    weights = [2**i * 5**(degree - i) for i in range(1, degree)]
    answers = []
    for mask in range(1 << (degree - 1)):
        coefficients = [1] + [(mask >> i) & 1 for i in range(degree - 1)] + [1]
        numerator = 5**degree + 2**degree + sum(
            weight for i, weight in enumerate(weights) if mask & (1 << i))
        if numerator % 3**degree == 0:
            answers.append(coefficients)
    return sorted(answers)


def main():
    catalog_path = ROOT / "binary_equality_catalog_1_63.jsonl"
    assert hashlib.sha256(catalog_path.read_bytes()).hexdigest() == (
        "dd875f7086046f2a6bb1e5685fad625993dc51ff7e51039b1de247aaf3f073ee")
    archived = [json.loads(line) for line in catalog_path.read_text().splitlines()]
    assert [row["degree"] for row in archived] == list(range(1, 64))
    all_matches = []
    for row in archived:
        degree = row["degree"]
        # This recomputes every catalog degree, with no early stopping.
        assert catalog_degree(degree) == row
        if degree <= 18:
            assert sorted(match["coefficients"] for match in row["matches"]) == direct_matches(degree)
        for match in row["matches"]:
            coefficients = match["coefficients"]
            numerator = sum(c * 2**i * 5**(degree - i)
                            for i, c in enumerate(coefficients))
            assert numerator == int(match["numerator"])
            assert numerator % 3**degree == 0
            all_matches.append((degree, coefficients, numerator, match["v3"]))
    assert all_matches == [(4, [1, 1, 0, 0, 1], 891, 4)]

    negatives_path = ROOT / "binary_equality_gmp_negative_degrees_1_63.jsonl"
    assert hashlib.sha256(negatives_path.read_bytes()).hexdigest() == (
        "58336ccfe8c4662efb2366e7471c58b1620075d61d9f4c12bf2ed3c1ab481043")
    negatives = [json.loads(line) for line in negatives_path.read_text().splitlines()]
    assert [row["degree"] for row in negatives] == [n for n in range(1, 64) if n != 4]
    assert all(row["valuation_threshold"] == row["degree"]
               and not row["threshold_match"]
               and row["right_checked"] == row["right_subsets"] for row in negatives)

    upper_path = ROOT / "binary_valuation_digit_search_cpp_1_100.jsonl"
    assert hashlib.sha256(upper_path.read_bytes()).hexdigest() == (
        "3af02d6766503397df103c81a8a1d46fe194a68a48c915f2e28623a965352a85")
    upper = [json.loads(line) for line in upper_path.read_text().splitlines()]
    assert [row["degree"] for row in upper] == list(range(1, 101))
    assert all(row["valuation_threshold"] == row["degree"] + 1
               and not row["threshold_match"]
               and row["right_checked"] == row["right_subsets"] for row in upper)

    assert 10**14 < 2**47
    assert 3**147 < 2**32 * 5**87
    assert 2**14 * 3**64 < 5**50
    assert 11**13 <= 10**14 < 11**14
    assert 3**147 < 5**101 < 3**148
    assert 2**47 * 3**64 < 5**64
    assert all(2**(r + 1) - 1 <= 3**r for r in range(47))
    assert 11**13 < 2**47 < 11**14

    pair = MobiusPair(2, 5)
    alpha = Fraction(891, 625)
    assert pair.is_atom(alpha) and pair.is_atom(pair.h)
    assert pair.h**4 * alpha == 11
    for exponent in range(14):
        assert pair.h**(4 * exponent) * alpha**exponent == 11**exponent <= 10**14

    print("Passed: complete equality catalog through degree 63, independent full-word "
          "checks through 18, archived GMP exclusions through 100, all exact range "
          "inequalities, and the 14 displayed integer factorizations.")


if __name__ == "__main__":
    main()
