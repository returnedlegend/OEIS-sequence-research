"""Reproducible exact checks for the reciprocal-family algorithm."""
from fractions import Fraction as Q
from itertools import product
from reciprocal_factorizations import (
    ReciprocalFamily, cyclic_digits, formal_atom, in_reciprocal,
)


def main():
    family = ReciprocalFamily(5, 144)
    witness = family.factorizations(Q(243, 128))
    assert witness["normalized_atom_divisors"] == []
    assert witness["factorizations"] == []
    assert family.factorizations(5)["factorizations"] == [
        {"unit_power": 1, "atom_exponents": [4, 2]}
    ]
    family = ReciprocalFamily(2, 15)
    square = family.factorizations(Q(17, 15)**2)
    assert square["normalized_atom_divisors"] == ["17/15"]
    assert square["factorizations"] == [{"unit_power": 0, "atom_exponents": [2]}]
    family = ReciprocalFamily(4, 225)
    assert family.norm(Q(2, 15)) == 1
    assert family.unit_exponent(Q(2, 15)) is None
    assert not in_reciprocal(Q(2, 15), 4, 225)
    assert family.factorizations(Q(9, 5))["normalized_atom_divisors"] == []
    family = ReciprocalFamily(6, 175)
    assert family.factorizations(Q(49, 25))["normalized_atom_divisors"] == []
    six = family.factorizations(6)
    assert six["normalized_atom_divisors"] == ["2", "3", "5"]
    assert six["factorizations"] == [{"unit_power": 0, "atom_exponents": [1, 1, 0]}]
    assert formal_atom((1, 1))
    assert not formal_atom((1, 2, 1))
    assert not formal_atom((1, 1, 1, 1))
    assert formal_atom((2, 0, 4, 1, 2))
    polynomial_count = associate_count = 0
    for a, b in [(2, 15), (4, 225), (5, 144), (6, 175), (10, 1323)]:
        t = Q(a, b)
        family = ReciprocalFamily(a, b)
        for cs in product(range(3), repeat=4):
            x = sum(c*t**i for i, c in enumerate(cs))
            if not x:
                continue
            digits = cyclic_digits(x, a, b)
            assert digits is not None
            assert sum(c*t**i for i, c in enumerate(digits)) == x
            polynomial_count += 1
            for k in [-2, -1, 0, 1, 2]:
                assert in_reciprocal(x*t**k, a, b)
                associate_count += 1
        for x in [Q(1), Q(2), Q(3), t, 1/t, 1+t, (1+t)**2]:
            result = family.factorizations(x)
            atoms = list(map(Q, result["normalized_atom_divisors"]))
            for record in result["factorizations"]:
                reconstructed = t**record["unit_power"]
                for atom, exponent in zip(atoms, record["atom_exponents"]):
                    reconstructed *= atom**exponent
                assert reconstructed == x
            if x in [Q(1), t, 1/t, 1+t, (1+t)**2]:
                assert result["factorizations"]
    print(f"Passed: explicit witnesses, unit distinction, formal factors, "
          f"{polynomial_count} polynomial values, {associate_count} associates, "
          "and factorization reconstruction.")


if __name__ == "__main__":
    main()
