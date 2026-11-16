"""Enumerate all atomic factorizations in N_0[3/10,7/5], exactly.

This can return an empty list for a non-atomic element. It does not
enumerate all atom divisors, whose finiteness remains the IDF question.
"""

from fractions import Fraction
if __package__:
    from .critical_pair_atoms import Q, divisors, is_atom, member, outside_numerator
else:
    from critical_pair_atoms import Q, divisors, is_atom, member, outside_numerator


def vp(x, p):
    x = Fraction(x)
    if x <= 0:
        raise ValueError("positive rational required")
    numerator, denominator = x.numerator, x.denominator
    answer = 0
    while numerator % p == 0:
        numerator //= p
        answer += 1
    while denominator % p == 0:
        denominator //= p
        answer -= 1
    return answer


def in_binary_window(x):
    """Return (2**u*x,u) with value in [1,2), using exact comparisons."""
    x = Fraction(x)
    exponent = 0
    while x < 1:
        x *= 2
        exponent += 1
    while x >= 2:
        x /= 2
        exponent -= 1
    return x, exponent


def possible_factor_atoms(x, depth):
    """All atoms other than 2 that could occur in a factorization of x.

    Here v_3(x)=0, and depth=-v_5(x)>=0. The returned pair is
    (atom, denominator depth). Every actual factorization atom is in
    this finite list; candidates with non-atomic cofactors may also occur.
    """
    x = Fraction(x)
    result = {}
    for m in divisors(outside_numerator(x)):
        power = 1
        for d in range(1, depth + 1):
            power *= 5
            atom, _ = in_binary_window(Fraction(m, power))
            if atom > x:
                continue
            if is_atom(atom) and member(x / atom):
                result[atom] = d
    return tuple(sorted(result.items()))


def atomic_factorizations(x):
    """Return every atomic factorization, up to ordering.

    Each record is (q_exponent, two_exponent, other_factors), where
    other_factors is a nondecreasing tuple with repetitions. The unit 1
    has the single empty factorization (0,0,()).
    """
    x = Fraction(x)
    if x <= 0 or not member(x):
        raise ValueError("input must belong to S minus {0}")
    q_exponent = vp(x, 3)
    normalized = x / Q ** q_exponent
    if normalized < 1:
        return []
    depth = -vp(normalized, 5)
    if depth < 0:
        return []
    atoms = possible_factor_atoms(normalized, depth)
    records = []
    two_exponent, power = 0, Fraction(1)
    while power <= normalized:
        target = normalized / power
        stack = [(0, depth, target, ())]
        while stack:
            start, remaining, target, factors = stack.pop()
            if remaining == 0:
                if target == 1:
                    records.append((q_exponent, two_exponent, factors))
                continue
            if target <= 1:
                continue
            for index in range(start, len(atoms)):
                atom, atom_depth = atoms[index]
                if atom > target:
                    break
                if atom_depth <= remaining:
                    stack.append((index, remaining - atom_depth,
                                  target / atom, factors + (atom,)))
        two_exponent += 1
        power *= 2
    return records


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("values", nargs="+", help="positive rational S-elements")
    args = parser.parse_args()
    for item in args.values:
        value = Fraction(item)
        records = atomic_factorizations(value)
        print(f"{value}: {len(records)} atomic factorizations")
        for q_exponent, two_exponent, factors in records:
            parts = [str(Q)] * q_exponent + ["2"] * two_exponent + [str(f) for f in factors]
            print("  " + (" * ".join(parts) if parts else "1"))
