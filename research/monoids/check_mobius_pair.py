"""Exact regression checks for contracting Möbius-pair algorithms.

The finite-grid membership oracle propagates acceptance backwards through
the entire digit graph, independently of the implementation's orbit walk.
Other checks use explicit positive representations, formal factorization
identities, and the separately implemented binary-pair enumerator.
"""

from collections import deque
from fractions import Fraction
from itertools import product

from binary_pair_factorizations import factorizations as binary_factorizations
from mobius_pair_factorizations import InconclusiveError, MobiusPair, NormalForm


def _expect_raises(exception, operation):
    try:
        operation()
    except exception:
        return
    raise AssertionError(f"expected {exception.__name__}")


def _membership_grid(a, b, denominator):
    """Compute membership on a whole finite grid by reverse reachability."""
    conductor = Fraction((a - 1) * b, b - a)
    threshold = conductor * denominator
    last = (threshold.numerator - 1) // threshold.denominator
    inverse = pow(denominator, -1, a)
    predecessors = [[] for _ in range(last + 1)]
    accepted = {0}

    for numerator in range(1, last + 1):
        digit = numerator * inverse % a
        residual = numerator - digit * denominator
        if residual < 0:
            continue
        assert residual % a == 0
        following = b * (residual // a)
        if following > last or following == numerator:
            # The conductor, or the explicit member digit/(1-q).
            accepted.add(numerator)
        else:
            predecessors[following].append(numerator)

    pending = deque(accepted)
    while pending:
        following = pending.popleft()
        for numerator in predecessors[following]:
            if numerator not in accepted:
                accepted.add(numerator)
                pending.append(numerator)
    return last, accepted


def _binary_factorization_set(value):
    result = binary_factorizations(value)
    atoms = [Fraction(item["value"]) for item in result["factorization_candidates"]]
    answers = set()
    for record in result["factorizations"]:
        factors = [Fraction(2, 5)] * record["q_exponent"]
        for atom, exponent in zip(atoms, record["atom_exponents"]):
            factors.extend([atom] * exponent)
        answers.add(tuple(sorted(factors)))
    return answers


def main():
    grid_count = 0
    for a, b, denominator in [
        (2, 5, 15), (2, 5, 45),
        (4, 9, 45), (4, 9, 225),
        (3, 8, 40), (6, 13, 91), (5, 12, 84),
    ]:
        pair = MobiusPair(a, b)
        last, accepted = _membership_grid(a, b, denominator)
        for numerator in range(last + 1):
            value = Fraction(numerator, denominator)
            assert pair.contains(value) == (numerator in accepted), (a, b, value)
            grid_count += 1

    generated_count = 0
    for a, b in [(2, 5), (3, 8), (4, 9)]:
        pair = MobiusPair(a, b)
        monomials = [Fraction(1), pair.q, pair.r,
                     pair.q**2, pair.q * pair.r, pair.r**2]
        for coefficients in product(range(3), repeat=len(monomials)):
            value = sum((c * term for c, term in zip(coefficients, monomials)), Fraction())
            assert pair.contains(value), (a, b, coefficients)
            generated_count += 1

    binary = MobiusPair(2, 5)
    larger = MobiusPair(4, 9)
    q, r, h = larger.q, larger.r, larger.h

    # Both an immediate period-two cycle and a prefix followed by a cycle.
    for pair, value in [
        (MobiusPair(3, 13), Fraction(169, 160)),
        (MobiusPair(5, 11), Fraction(55, 24)),
        (MobiusPair(5, 11), Fraction(25, 24)),
    ]:
        assert not pair.contains(value)
        assert pair.digits(value) is None
        assert not pair.is_atom(value)

    for pair, value in [
        (binary, Fraction(-1)), (binary, Fraction(1, 2)),
        (binary, Fraction(27, 25)), (larger, Fraction(1, 7)),
    ]:
        assert not pair.contains(value)

    forms = [
        (q, NormalForm((0, 1), 0)),
        (h, NormalForm((), 1)),
        (2 * h, NormalForm((), 2)),
        (2 + r, NormalForm((2,), 1)),
        (1 + 2 * q**2 * h, NormalForm((1, 0), 2)),
        (2 + 2 * q + q**2, NormalForm((2, 2, 1), 0)),
        ((1 + q) * (2 + r), NormalForm((2, 3), 2)),
    ]
    for value, form in forms:
        assert larger.digits(value) == form, (value, form)
        assert larger.evaluate(form) == value
    assert larger.contains(4) and larger.digits(4) is None

    known_atoms = [
        q, h, Fraction(2), Fraction(3),
        Fraction(10, 3), Fraction(250, 81),
        2 + r, 3 + r,
        1 + 2 * q**2 * h, 1 + 3 * q**2 * h,
    ] + [1 + q**degree for degree in (1, 2, 3, 5)]
    for value in known_atoms:
        assert larger.is_atom(value), value
    for value in [
        Fraction(0), Fraction(1), q**2, r, 2 * h,
        2 * (1 + q), (1 + q)**2, h * (1 + q + q**2),
        # Its only possible nonconstant finite factor has a signed quotient
        # (2+X-X^2)/(1+X)=2-X, whose partial sums remain nonnegative.
        (1 + q) * (2 + r),
    ]:
        assert not larger.is_atom(value), value

    witness = Fraction(3**12, 5**8)
    explicit = (
        1 + q**2 + q**4 + 3 * q**5 + 3 * q**6 + 2 * q**7
        + q**8 * (2 + r**2 + 2 * r**3 + 2 * r**4 + 3 * r**5
                  + 2 * r**6 + 2 * r**7 + 126 * r**8)
    )
    assert explicit == witness
    assert larger.contains(witness)
    assert not larger.is_atom(witness)
    assert larger.factorizations(witness) == []
    assert larger.factorizations(5) == []

    expected = {
        Fraction(1): {()},
        Fraction(4): {(Fraction(2), Fraction(2)), (q, Fraction(3), Fraction(3))},
        Fraction(6): {(Fraction(2), Fraction(3)), (h, Fraction(10, 3))},
        Fraction(10): {
            (Fraction(3), Fraction(10, 3)),
            (h, h, Fraction(250, 81)),
        },
        r: {(q, h)},
    }
    reconstruction_count = 0
    for value, answers in expected.items():
        actual = larger.factorizations(value)
        assert len(actual) == len(set(actual)), (value, actual)
        assert set(actual) == answers, (value, actual, answers)
        _, bounds = larger.factorization_candidates(value)
        for factors in actual:
            reconstructed = Fraction(1)
            for atom in factors:
                assert larger.is_atom(atom)
                reconstructed *= atom
            assert reconstructed == value
            assert len(factors) <= bounds["atomic_length_bound"]
            reconstruction_count += 1

    prime_power = MobiusPair(3, 8)
    assert prime_power.factorizations(3) == [
        (prime_power.q, Fraction(2), Fraction(2), Fraction(2))
    ]

    binary_values = [
        Fraction(1), binary.q, binary.q**2, binary.h, binary.h**2,
        Fraction(7, 5), Fraction(29, 25), Fraction(19, 15),
        Fraction(83, 75), Fraction(113, 75), Fraction(133, 75),
        Fraction(891, 625), Fraction(2), Fraction(3), Fraction(5),
        Fraction(125, 81),
    ]
    for value in binary_values:
        assert set(binary.factorizations(value)) == _binary_factorization_set(value), value

    # A valid contracting pair without a suitable block still supports
    # membership and atom tests, but the factorization theorem does not apply.
    unsupported = MobiusPair(5, 12)
    assert unsupported.contains(unsupported.h)
    assert unsupported.is_atom(unsupported.h)
    _expect_raises(ValueError, lambda: unsupported.factorizations(unsupported.h))
    _expect_raises(ValueError, lambda: binary.factorizations(Fraction(27, 25)))
    for arguments in [(1, 3), (2, 3), (2, 4)]:
        _expect_raises(ValueError, lambda arguments=arguments: MobiusPair(*arguments))

    # Resource exhaustion must remain distinguishable from a mathematical no.
    _expect_raises(InconclusiveError, lambda: larger.contains(q, max_steps=0))
    _expect_raises(InconclusiveError, lambda: larger.is_atom(Fraction(250, 81), max_checks=0))
    _expect_raises(InconclusiveError, lambda: larger.factorizations(4, max_candidates=1))
    _expect_raises(InconclusiveError, lambda: larger.factorizations(4, max_nodes=1))

    print(
        f"Passed: {grid_count} independent finite-grid membership checks, "
        f"{generated_count} generated values, explicit cycles and normal forms, "
        f"{len(known_atoms)} known atoms, {reconstruction_count} exact factorization "
        f"reconstructions, {len(binary_values)} complete binary cross-checks, "
        "and resource-limit/unsupported-family checks."
    )


if __name__ == "__main__":
    main()
