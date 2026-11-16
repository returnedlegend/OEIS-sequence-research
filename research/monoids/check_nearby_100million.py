"""Regenerate the complete nearby-family IDF certificate through 100,000,000.

This checker uses modular digit-word evaluations and exact Fraction closures.
The companion independent checker uses explicit polynomials and integer trees.
A state cutoff is an error, never a successful certificate.
"""
from fractions import Fraction
from hashlib import sha256
import json
from math import gcd
from pathlib import Path

if __package__:
    from .nearby_integral_carry import certificate, verify
else:
    from nearby_integral_carry import certificate, verify


def word_numerator_mod(n, word, modulus):
    h, power = 1, 1
    for digit in word:
        if digit == 0:
            h = 3*h
        elif digit == 1:
            h = 3*h + power*5*n
        elif digit == 2:
            h = 3*h + 7*n*power
        else:
            raise ValueError('invalid digit')
        h %= modulus
        power = power*5*n % modulus
    return h


def retained_word_roots(depth):
    if depth < 1:
        raise ValueError('positive depth required')
    nodes = [(bytes([2]), 1)]
    modulus = 5
    for _ in range(1, depth):
        next_modulus = 5*modulus
        children = []
        for word, root in nodes:
            for digit in range(3):
                child = word + bytes([digit])
                lifts = [root+j*modulus for j in range(5)
                         if word_numerator_mod(root+j*modulus, child,
                                               next_modulus) == 0]
                assert len(lifts) == 1
                children.append((child, lifts[0]))
        nodes, modulus = children, next_modulus
    return sorted({root for _, root in nodes}), len(nodes), modulus


def integer_list_hash(values):
    return sha256(''.join(f'{n}\n' for n in values).encode()).hexdigest()


def check(path=None):
    path = Path(path) if path else Path(__file__).with_name('nearby_100million_manifest.json')
    manifest = json.loads(path.read_text())
    limit, depth = manifest['limit'], manifest['depth']
    assert limit == 100_000_000 and depth == 12
    roots, word_count, modulus = retained_word_roots(depth)
    assert limit < modulus
    assert modulus == manifest['modulus']
    assert word_count == manifest['word_count'] == 3**(depth-1)
    assert len(roots) == manifest['root_count']
    assert integer_list_hash(roots) == manifest['root_sha256']
    candidates = [n for n in roots if 4 <= n <= limit and gcd(n, 21) == 1]
    assert len(candidates) == manifest['candidate_count']
    assert integer_list_hash(candidates) == manifest['candidate_sha256']
    assert [row[0] for row in manifest['certificates']] == candidates
    digest = sha256()
    total_states, max_states, max_depth = 0, 0, 0
    histogram = {}
    for n, expected_count, expected_depth in manifest['certificates']:
        result = certificate(n, max_states=10_000)
        if result is None:
            raise RuntimeError(f'inconclusive closure cutoff at n={n}')
        states, _ = result
        assert verify(n, states)
        assert len(states) == expected_count
        largest_denominator = max(x.denominator for x in states)
        denominator, actual_depth = 1, 0
        while denominator < largest_denominator:
            denominator *= n
            actual_depth += 1
        assert denominator == largest_denominator
        assert actual_depth == expected_depth
        digest.update(f'{n}\n'.encode())
        for x in states:
            digest.update(f'{x.numerator}/{x.denominator}\n'.encode())
        total_states += len(states)
        max_states = max(max_states, len(states))
        max_depth = max(max_depth, actual_depth)
        histogram[str(actual_depth)] = histogram.get(str(actual_depth), 0) + 1
    assert digest.hexdigest() == manifest['certificate_sha256']
    assert total_states == manifest['certificate_state_count']
    assert max_states == manifest['maximum_states']
    assert max_depth == manifest['maximum_depth']
    assert histogram == manifest['depth_histogram']
    return {'limit':limit, 'candidate_count':len(candidates),
            'exact_closure_states':total_states, 'maximum_depth':max_depth,
            'status':'all admissible parameters certified'}


if __name__ == '__main__':
    print(json.dumps(check(), sort_keys=True))
