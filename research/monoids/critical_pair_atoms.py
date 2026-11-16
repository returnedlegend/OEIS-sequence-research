"""Exact membership and atom tests for N_0[3/10, 7/5].

The atom test uses the critical-value factor theorem proved in
PAIR_3_10_CRITICAL_REDUCTION.md. This is a terminating decision procedure,
not a practical complexity claim and not an IDF decision algorithm.
"""

from fractions import Fraction
Q = Fraction(3, 10)
RGEN = Fraction(7, 5)
DIGITS = (Fraction(0), Fraction(1), RGEN)


def supported_denominator(x):
    d = x.denominator
    for p in (2, 5):
        while d % p == 0:
            d //= p
    return d == 1


def canonical(x):
    """Return (member, critical, digits, terminal).

    Digits are the residues 0,1,2, with residue 2 denoting the digit 7/5.
    The process stops at its first integer. On failure, terminal is the
    negative tail or None when the denominator has an unsupported prime.
    """
    x = Fraction(x)
    if not supported_denominator(x):
        return False, False, (), None
    digits = []
    critical = 0 <= x <= 2
    while x.denominator != 1:
        if x < 0:
            return False, False, tuple(digits), x
        residue = x.numerator * pow(x.denominator, -1, 3) % 3
        digits.append(residue)
        x = (x - DIGITS[residue]) / Q
        critical = critical and 0 <= x <= 2
    member = x >= 0
    return member, critical and member, tuple(digits), int(x)


def member(x):
    return canonical(x)[0]


def outside_numerator(x):
    n = Fraction(x).numerator
    if n <= 0:
        raise ValueError("A positive rational is required")
    for p in (2, 5):
        while n % p == 0:
            n //= p
    return n


def divisors(n):
    """All positive divisors, by elementary trial factorization."""
    factors = []
    p = 2
    while p * p <= n:
        exponent = 0
        while n % p == 0:
            n //= p
            exponent += 1
        if exponent:
            factors.append((p, exponent))
        p = 3 if p == 2 else p + 2
    if n > 1:
        factors.append((n, 1))
    result = [1]
    for p, exponent in factors:
        result = [d * p ** e for d in result for e in range(exponent + 1)]
    return sorted(result)


def binary_polynomial(numerator, degree):
    """Binary G with G(0)=1, G(3/10)=numerator/10**degree, or None.

    The caller uses numerator coprime to 10, so degree is the exact
    denominator exponent and a valid polynomial must have top digit 1.
    """
    current = numerator
    power = 10 ** degree
    coefficients = []
    for _ in range(degree):
        if current < 0:
            return None
        # Every power of 10 is 1 modulo 3.
        digit = current % 3
        if digit > 1:
            return None
        coefficients.append(digit)
        current = (current - digit * power) // 3
        power //= 10
    if current != 1:
        return None
    coefficients.append(current)
    if coefficients[0] != 1:
        return None
    return tuple(coefficients)


def binary_divisor_candidates(m):
    """Yield all nonconstant binary G(q) whose numerator divides m."""
    for n in divisors(m):
        if n == 1:
            continue
        degree, power = 1, 10
        while power <= n:
            coefficients = binary_polynomial(n, degree)
            if coefficients is not None:
                yield Fraction(n, power), coefficients
            degree += 1
            power *= 10


def proper_binary_divisor(x):
    """A witness (G(q), x/G(q), coefficients), or None.

    Correct as an exhaustive proper-factor test when x is critical and
    lies in [1,2].
    """
    x = Fraction(x)
    for value, coefficients in binary_divisor_candidates(outside_numerator(x)):
        if value >= x:
            continue
        quotient = x / value
        if member(quotient):
            return value, quotient, coefficients
    return None


def atom_status(x):
    """Return (is_atom, reason, optional_factorization_witness)."""
    x = Fraction(x)
    if x <= 0:
        return False, "outside the nonzero positive monoid", None
    belongs, critical, _, terminal = canonical(x)
    if not belongs:
        return False, "outside the monoid", None
    if x == 1:
        return False, "unit", None
    if x == Q:
        return True, "the unique atom below 1", None
    if x < 1:
        return False, "proper multiple of q", (Q, x / Q)
    if x > 2:
        return False, "above the real conductor", None
    if not critical:
        return False, "a canonical tail exceeds 2", None
    if terminal == 2:
        return True, "critical endpoint with unique highest coefficient 2", None
    witness = proper_binary_divisor(x)
    if witness is not None:
        return False, "proper ordinary binary divisor", witness[:2]
    return True, "critical with no proper ordinary binary divisor", None


def is_atom(x):
    return atom_status(x)[0]


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("values", nargs="+", help="rationals such as 8/5 or 169/100")
    arguments = parser.parse_args()
    for value in arguments.values:
        rational = Fraction(value)
        answer, reason, witness = atom_status(rational)
        print(f"{rational}: {'atom' if answer else 'not an atom'}; {reason}")
        if witness is not None:
            print(f"  factorization: {witness[0]} * {witness[1]}")
