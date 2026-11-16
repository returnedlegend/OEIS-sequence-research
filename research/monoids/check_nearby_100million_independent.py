"""Independent verification of the nearby-family certificate through10^8.

Uses explicit integer polynomial coefficients and one-step Taylor/Hensel
lifts, followed by integer J/n^k word trees. It does not import the primary
modular-word/rational-state checker. Resource caps raise an error; they are
never interpreted as closed trees. The manifest is read-only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction
from itertools import product
from math import gcd
from pathlib import Path


def polynomial_value(coefficients, x, modulus):
    result = 0
    for coefficient in reversed(coefficients):
        result = (result * x + coefficient) % modulus
    return result


def hensel_word_roots(depth):
    if depth < 1:
        raise ValueError('positive depth required')
    nodes = [((3, 7), 1)]  # H_1(n)=3+7n, root1 modulo5.
    modulus = 5
    for length in range(1, depth):
        next_modulus = 5 * modulus
        inverse_derivative = pow(7 * pow(3, length, 5) % 5, -1, 5)
        children = []
        for coefficients, root in nodes:
            base_coefficients = tuple(3 * c for c in coefficients)
            base_value = 3 * polynomial_value(coefficients, root, next_modulus) % next_modulus
            assert base_value % modulus == 0
            lift = (-(base_value // modulus) * inverse_derivative) % 5
            ordinary_root = root + lift * modulus
            # Ordinary digits0 and1 have the same root at this depth,
            # but different polynomials must be retained for later lifts.
            for top in (0, next_modulus):
                child = base_coefficients + (top,)
                assert polynomial_value(child, ordinary_root, next_modulus) == 0
                children.append((child, ordinary_root))
            top = 7 * modulus
            value = (base_value + top * pow(root, length + 1, next_modulus)) % next_modulus
            assert value % modulus == 0
            lift = (-(value // modulus) * inverse_derivative) % 5
            r_root = root + lift * modulus
            child = base_coefficients + (top,)
            assert polynomial_value(child, r_root, next_modulus) == 0
            children.append((child, r_root))
        nodes = children
        modulus = next_modulus
    return len(nodes), sorted({root for _, root in nodes})


def small_brute_crosscheck():
    depth = 5
    modulus = 5**depth
    brute = set()
    for n in range(1, modulus, 5):
        for word in product(range(3), repeat=depth - 1):
            value = 7 * n + 3
            for length, digit in enumerate(word, start=2):
                if digit == 0:
                    addend = 0
                elif digit == 1:
                    addend = pow(5 * n, length, modulus)
                else:
                    addend = 7 * n * pow(5 * n, length - 1, modulus)
                value = (3 * value + addend) % modulus
            if value == 0:
                brute.add(n)
    assert set(hensel_word_roots(depth)[1]) == brute


def power_of_five(n):
    while n > 1 and n % 5 == 0:
        n //= 5
    return n == 1


def newline_hash(values):
    return hashlib.sha256(''.join(f'{n}\n' for n in values).encode()).hexdigest()


def integer_word_tree(n, max_nodes, max_depth):
    """A state is the already reduced rational J/n^depth."""
    assert n >= 4 and gcd(n, 105) == 1
    stack = [(1, 1, 0)]
    states = set()
    deepest = 0
    while stack:
        numerator, denominator, depth = stack.pop()
        if len(states) >= max_nodes or depth > max_depth:
            raise RuntimeError(f'closure search capped at n={n}')
        assert gcd(numerator, denominator) == 1
        state = (numerator, denominator)
        # Canonical word uniqueness prohibits merged words or cycles.
        assert state not in states, (n, state)
        states.add(state)
        deepest = max(deepest, depth)
        next_denominator = n * denominator
        if numerator % 5 == 0:
            base = 3 * numerator // 5
            stack.append((base, next_denominator, depth + 1))
            stack.append((next_denominator + base, next_denominator, depth + 1))
        r_numerator = 7 * next_denominator + 3 * numerator
        if r_numerator % 5 == 0:
            stack.append((r_numerator // 5, next_denominator, depth + 1))
    return states, deepest


def verify(manifest, max_nodes=1_000_000, max_depth=1000):
    limit, depth = manifest['limit'], manifest['depth']
    modulus = 5**depth
    assert 4 <= limit < modulus, 'residue cover requires limit<5^depth'
    assert manifest['modulus'] == modulus
    small_brute_crosscheck()
    word_count, roots = hensel_word_roots(depth)
    candidates = [n for n in roots if 4 <= n <= limit and gcd(n, 21) == 1 and not power_of_five(n)]
    assert word_count == manifest['word_count']
    assert len(roots) == manifest['root_count']
    assert newline_hash(roots) == manifest['root_sha256']
    assert len(candidates) == manifest['candidate_count']
    assert newline_hash(candidates) == manifest['candidate_sha256']
    triples = []
    digest = hashlib.sha256()
    state_count = maximum_states = maximum_depth = 0
    histogram = Counter()
    for n in candidates:
        states, deepest = integer_word_tree(n, max_nodes, max_depth)
        count = len(states)
        triples.append([n, count, deepest])
        state_count += count
        maximum_states = max(maximum_states, count)
        maximum_depth = max(maximum_depth, deepest)
        histogram[str(deepest)] += 1
        digest.update(f'{n}\n'.encode())
        for numerator, denominator in sorted(states, key=lambda x: Fraction(*x)):
            digest.update(f'{numerator}/{denominator}\n'.encode())
    assert triples == manifest['certificates']
    assert state_count == manifest['certificate_state_count']
    assert digest.hexdigest() == manifest['certificate_sha256']
    assert maximum_states == manifest['maximum_states']
    assert maximum_depth == manifest['maximum_depth']
    assert dict(histogram) == manifest['depth_histogram']
    powers = 0
    power = 5
    while power <= limit:
        powers += 1
        power *= 5
    admissible = limit - limit // 3 - limit // 7 + limit // 21 - 2 - powers
    return dict(admissible=admissible, candidates=len(candidates), states=state_count,
                maximum_states=maximum_states, maximum_depth=maximum_depth,
                certificate_sha256=digest.hexdigest())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path,
                        default=Path(__file__).with_name('nearby_100million_manifest.json'))
    parser.add_argument('--max-nodes', type=int, default=1_000_000)
    parser.add_argument('--max-depth', type=int, default=1000)
    args = parser.parse_args()
    result = verify(json.loads(args.manifest.read_text()), args.max_nodes, args.max_depth)
    print('Independent integer-polynomial/Taylor and J/n^k word-tree verification passed:')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
