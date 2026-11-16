"""An exact, compact membership certificate for a huge smooth rational below 2.

The rational is represented by its prime exponents. Its atomic factorization
status is NOT decided here. No floating-point arithmetic is used.
"""
from fractions import Fraction


NUMERATOR_EXPONENT = 2364816678866
DENOMINATOR_EXPONENT = 1492033204438


def log_interval(x, terms=100):
    """Rational bounds from log(x)=2*sum y^(2j+1)/(2j+1), y=(x-1)/(x+1)."""
    x = Fraction(x)
    if x < 1:
        low, high = log_interval(1 / x, terms)
        return -high, -low
    y = (x - 1) / (x + 1)
    power = y
    partial = Fraction(0)
    for j in range(terms):
        partial += 2 * power / (2 * j + 1)
        power *= y * y
    remainder = 2 * power / ((2 * terms + 1) * (1 - y * y))
    return partial, partial + remainder


def check():
    u, v = NUMERATOR_EXPONENT, DENOMINATOR_EXPONENT
    k = 18
    modulus = 5**k
    assert pow(2, u, modulus) == pow(3, v, modulus)
    two = log_interval(2)
    three = log_interval(3)
    lower = u * two[0] - v * three[1]
    upper = u * two[1] - v * three[0]
    assert lower > log_interval(Fraction(191, 100))[1]
    assert upper < log_interval(Fraction(193, 100))[0]
    q = Fraction(5, 6)
    assert 1 + 24 * q**k < Fraction(191, 100)
    assert Fraction(193, 100) < 1 + 25 * q**k < 2
    # Thus h=1+q^18*z, with z in Z[1/6] and 24<z<25.
    # The conductor 24 places z, and hence h, in N_0[5/6].
    print("Exact certificate passed: 1.91 < 2^%d/3^%d < 1.93; "
          "h=1+(5/6)^18*z with z in Z[1/6] and 24<z<25."
          % (u, v))
    print("Atomicity and existence of atom divisors of h remain undecided.")


if __name__ == "__main__":
    check()
