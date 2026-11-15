"""Reproducible exact checks for N_0[2/5,2/3] membership/factorizations."""

from fractions import Fraction
from itertools import product

from binary_pair_factorizations import H, Q, R, factorizations, in_binary_pair


def main():
    monomials = [Fraction(1), Q, R, Q**2, Q*R, R**2]
    generated_count = 0
    for coefficients in product(range(3), repeat=len(monomials)):
        value = sum((c*m for c, m in zip(coefficients, monomials)), Fraction())
        assert in_binary_pair(value)
        generated_count += 1

    for value in [Fraction(-1), Fraction(1, 2), Fraction(1, 3), Fraction(1, 5),
                  Fraction(3, 5), Fraction(27, 25), Fraction(25, 21)]:
        assert not in_binary_pair(value)

    for value in [Fraction(2), Fraction(3), Fraction(5), Fraction(9, 5), Fraction(125, 81)]:
        assert not factorizations(value)["factorizations"]

    # An independently specified identity between four known atoms.
    # (1+X)(1+X^2/(1-X)) = (1+X^3)/(1-X).
    answer = factorizations(Fraction(133, 75))
    atom_values = [candidate["value"] for candidate in answer["factorization_candidates"]]
    found = {
        tuple(sorted((atom_values[i], exponent)
                     for i, exponent in enumerate(record["atom_exponents"]) if exponent))
        for record in answer["factorizations"]
    }
    assert found == {
        tuple(sorted([("7/5", 1), ("19/15", 1)])),
        tuple(sorted([("5/3", 1), ("133/125", 1)])),
    }

    reconstruction_count = 0
    for value in [Fraction(1), Q, Q**3, H, H**4, Fraction(7, 5), Fraction(29, 25),
                  Fraction(39, 25), Fraction(891, 625), Fraction(19, 15),
                  Fraction(83, 75), Fraction(113, 75), (1+Q)*(1+Q**3),
                  Q**2*H**3*(1+Q)**2*Fraction(19, 15)]:
        answer = factorizations(value)
        assert answer["factorizations"]
        atoms = [Fraction(candidate["value"]) for candidate in answer["factorization_candidates"]]
        for record in answer["factorizations"]:
            reconstructed = Q**record["q_exponent"]
            length = record["q_exponent"]
            for atom, exponent in zip(atoms, record["atom_exponents"]):
                reconstructed *= atom**exponent
                length += exponent
            assert reconstructed == value
            assert length <= answer["bounds"]["atomic_length_bound"]
            reconstruction_count += 1

    print(f"Passed: {generated_count} generated semiring values, explicit nonmembers, "
          "non-atomic witnesses, a two-factorization identity, and "
          f"{reconstruction_count} factorization reconstructions.")


if __name__ == "__main__":
    main()
