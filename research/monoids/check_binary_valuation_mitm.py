"""Independent exact checks for both binary valuation searches.

Pass --gmp-binary PATH to include an independently compiled C++ backend.
The default checks require only the Python standard library.
"""

import argparse
import json
from pathlib import Path
from random import Random
import subprocess
import sys

from binary_valuation_mitm import InconclusiveError, check_degree, gray_sums
from binary_valuation_digit_search import check_degree as check_degree_table_free


def valuation_three(number):
    exponent = 0
    while number % 3 == 0:
        number //= 3
        exponent += 1
    return exponent


def direct_numerators(degree):
    """Ordinary mask enumeration, independent of the Gray-code search."""
    weights = [2**i * 5**(degree - i) for i in range(1, degree)]
    endpoints = 5**degree + 2**degree
    return [endpoints + sum(weight for bit, weight in enumerate(weights)
                            if mask & (1 << bit))
            for mask in range(1 << len(weights))]


def verify_witness(result):
    degree = result["degree"]
    digits = result["coefficients"]
    assert len(digits) == degree + 1 and digits[0] == digits[-1] == 1
    assert set(digits) <= {0, 1}
    numerator = sum(digit * 2**i * 5**(degree - i)
                    for i, digit in enumerate(digits))
    exponent = valuation_three(numerator)
    assert numerator == int(result["numerator"])
    assert exponent == result["v3"] >= result["valuation_threshold"]
    assert int(result["outside_part"]) == numerator // 3**exponent
    assert result["violates_degree_bound"] == (exponent > degree)


def expect_error(error_type, callback):
    try:
        callback()
    except error_type:
        return
    raise AssertionError(f"expected {error_type.__name__}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gmp-binary", type=Path)
    arguments = parser.parse_args()
    random = Random(20261116)
    gray_checks = 0
    for size in range(13):
        for _ in range(20):
            modulus = random.randint(1, 1000)
            weights = [random.randint(-4 * modulus, 4 * modulus) for _ in range(size)]
            rows = list(gray_sums(weights, modulus))
            assert len(rows) == 1 << size
            assert {mask for _, mask in rows} == set(range(1 << size))
            for residue, mask in rows:
                expected = sum(weight for bit, weight in enumerate(weights)
                               if mask & (1 << bit)) % modulus
                assert residue == expected
            gray_checks += 1

    threshold_checks = 0
    positive_controls = 0
    for degree in range(1, 19):
        numerators = direct_numerators(degree)
        max_valuation = max(map(valuation_three, numerators))
        thresholds = range(1, degree + 2) if degree <= 14 else [degree + 1]
        for threshold in thresholds:
            result = check_degree(degree, exponent=threshold)
            assert result["modulus"] == str(3**threshold)
            assert result["threshold_match"] == (max_valuation >= threshold)
            if result["threshold_match"]:
                verify_witness(result)
                assert int(result["numerator"]) in numerators
                positive_controls += 1
            else:
                assert result["right_checked"] == result["right_subsets"]
            table_free = check_degree_table_free(degree, exponent=threshold)
            assert table_free["threshold_match"] == (max_valuation >= threshold)
            left_count = table_free["left_digits"]
            maximum = (5**left_count - 2**left_count) // 3
            assert int(table_free["left_maximum"]) == maximum < 3**threshold
            if left_count < degree - 1:
                assert (5**(left_count + 1) - 2**(left_count + 1)) // 3 >= 3**threshold
            if table_free["threshold_match"]:
                verify_witness(table_free)
                assert int(table_free["numerator"]) in numerators
            else:
                assert table_free["right_checked"] == table_free["right_subsets"]
            if arguments.gmp_binary:
                compiled = json.loads(subprocess.check_output(
                    [str(arguments.gmp_binary), str(degree), str(degree), str(threshold - degree)],
                    text=True,
                ))
                for key, value in table_free.items():
                    if key != "seconds":
                        assert compiled[key] == value, (key, compiled, table_free)
                if compiled["threshold_match"]:
                    verify_witness(compiled)
            threshold_checks += 1

    equality = check_degree(4, exponent=4)
    assert equality["coefficients"] == [1, 1, 0, 0, 1]
    assert equality["numerator"] == "891" and equality["v3"] == 4
    assert not equality["violates_degree_bound"]
    assert not check_degree(4)["threshold_match"]
    assert check_degree_table_free(4, exponent=4)["numerator"] == "891"
    assert not check_degree_table_free(4)["threshold_match"]

    expect_error(ValueError, lambda: list(gray_sums([1], 0)))
    expect_error(ValueError, lambda: check_degree(0))
    expect_error(ValueError, lambda: check_degree(4, exponent=0))
    expect_error(ValueError, lambda: check_degree(4, max_half_bits=-1))
    expect_error(InconclusiveError, lambda: check_degree(4, max_half_bits=0))
    expect_error(ValueError, lambda: check_degree_table_free(0))
    expect_error(ValueError, lambda: check_degree_table_free(4, exponent=0))
    expect_error(ValueError, lambda: check_degree_table_free(4, max_right_bits=-1))
    expect_error(InconclusiveError, lambda: check_degree_table_free(10, max_right_bits=0))
    script = Path(__file__).with_name("binary_valuation_mitm.py")
    completed = subprocess.run(
        [sys.executable, str(script), "4", "4", "--max-half-bits", "0"],
        check=False, capture_output=True, text=True,
    )
    assert completed.returncode == 2
    assert json.loads(completed.stdout)["status"] == "inconclusive"
    table_script = Path(__file__).with_name("binary_valuation_digit_search.py")
    completed = subprocess.run(
        [sys.executable, str(table_script), "10", "10", "--max-right-bits", "0"],
        check=False, capture_output=True, text=True,
    )
    assert completed.returncode == 2
    assert json.loads(completed.stdout)["status"] == "inconclusive"
    if arguments.gmp_binary:
        completed = subprocess.run(
            [str(arguments.gmp_binary), "10", "10", "1", "0"],
            check=False, capture_output=True, text=True,
        )
        assert completed.returncode == 2 and "inconclusive" in completed.stderr
    print(f"Passed: {gray_checks} independent Gray-code checks, "
          f"{threshold_checks} exact threshold comparisons through degree18 for both Python backends, "
          f"{positive_controls} reconstructed positive controls, equality891, and resource/error checks."
          + (f" GMP backend agrees on all {threshold_checks} threshold cases." if arguments.gmp_binary else ""))


if __name__ == "__main__":
    main()
