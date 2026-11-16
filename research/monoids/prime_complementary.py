"""Compatibility entry point for the prime-C complementary subfamily.

The implementation now lives in complementary_family.py, whose general
Complementary class also permits composite C>=3. PrimeComplement retains
the original prime-C parameter check.
"""
if __package__:
    from .complementary_family import (
        Complementary, PrimeComplement, divisors, exact_nonnegative_quotient,
        factor_integer, floor_log, main, trim, vp,
    )
else:
    from complementary_family import (
        Complementary, PrimeComplement, divisors, exact_nonnegative_quotient,
        factor_integer, floor_log, main, trim, vp,
    )

if __name__ == '__main__':
    main(prime_only=True)
