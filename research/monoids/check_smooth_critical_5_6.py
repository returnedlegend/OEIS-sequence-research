"""Audit finite smooth critical-orbit records and global atom certificates.

This reruns the first 100 depths with independent Fraction arithmetic and
checks every recorded atom using the proved global critical-divisor bound.
It does not rerun the archived large-depth scans. See the companion note
for the full reproduction commands and the distinction between those checks.
"""
from fractions import Fraction
import hashlib
import json
from pathlib import Path

try:
    from .cyclic_critical import actual_divisors, critical, prefix_certificate
    from .verify_smooth_critical_5_6_intervals import independent_candidate_count
except ImportError:
    from cyclic_critical import actual_divisors, critical, prefix_certificate
    from verify_smooth_critical_5_6_intervals import independent_candidate_count


HERE = Path(__file__).resolve().parent


def independent_critical(x):
    """Fraction-based canonical orbit, independent of the scan's integer loop."""
    while x.denominator != 1:
        digit = x.numerator * pow(x.denominator, -1, 5) % 5
        x = (x - digit) * Fraction(6, 5)
        if not 0 <= x <= 24:
            return False
    return 0 <= x <= 24


def independent_candidates(limit):
    for depth in range(1, limit + 1):
        for numerator_prime, denominator_prime in ((2, 3), (3, 2)):
            denominator = denominator_prime**depth
            numerator = 1
            while numerator <= denominator:
                numerator *= numerator_prime
            while numerator <= 24 * denominator:
                yield Fraction(numerator, denominator)
                numerator *= numerator_prime


def smooth_integer(n):
    for prime in (2, 3):
        while n % prime == 0:
            n //= prime
    return n == 1


def check():
    manifest = json.loads((HERE / 'smooth_critical_5_6_manifest.json').read_text())
    hits, expected_start, total = [], 1, 0
    for item in manifest['segments']:
        content = (HERE / item['file']).read_bytes()
        assert hashlib.sha256(content).hexdigest() == item['sha256']
        rows = [json.loads(line) for line in content.splitlines()]
        first, last = rows[0], rows[-1]
        assert first['kind'] == 'metadata' and first['exact'] is True
        # The original first segment predates the optional --start argument.
        assert first.get('start', 1) == expected_start
        assert last['kind'] == 'complete' and last['depth'] == first['limit']
        segment_hits = [row for row in rows if row['kind'] == 'critical']
        assert len(segment_hits) == last['critical']
        assert last['candidates'] == item['candidates']
        total += last['candidates']
        hits.extend(segment_hits)
        expected_start = last['depth'] + 1
    assert expected_start == manifest['maximum_depth'] + 1
    assert total == manifest['candidate_count']

    certificates = json.loads(
        (HERE / 'smooth_critical_5_6_noninteger_certificates.json').read_text()
    )
    recorded_values = set()
    for row in hits:
        value = Fraction(row['numerator_prime']**row['numerator_exponent'],
                         row['denominator_prime']**row['denominator_exponent'])
        assert 1 < value <= 24 and independent_critical(value)
        recorded_values.add(value)
    assert len(hits) == len(recorded_values) == len(certificates) == 31
    assert max(row['denominator_exponent'] for row in hits) == 22

    effective_depth = manifest['maximum_depth']
    effective_count = total
    interval_manifest = json.loads(
        (HERE / 'smooth_critical_5_6_interval_manifest.json').read_text()
    )
    for item in interval_manifest['runs']:
        content = (HERE / item['file']).read_bytes()
        assert hashlib.sha256(content).hexdigest() == item['file_sha256']
        rows = [json.loads(line) for line in content.splitlines()]
        first, last = rows[0], rows[-1]
        assert first['kind'] == 'metadata' and first['exact'] is True
        assert last['kind'] == 'complete'
        assert first['limit'] == last['depth'] == item['maximum_depth']
        assert last['candidates'] == item['candidate_count']
        assert independent_candidate_count(last['depth']) == last['candidates']
        interval_hits = [row for row in rows if row['kind'] == 'critical']
        assert len(interval_hits) == last['critical'] == 31
        values = {
            Fraction(row['numerator_prime']**row['numerator_exponent'],
                     row['denominator_prime']**row['denominator_exponent'])
            for row in interval_hits
        }
        assert values == recorded_values
        if last['depth'] > effective_depth:
            effective_depth = last['depth']
            effective_count = last['candidates']

    candidates = tuple(independent_candidates(100))
    independent_hits = {x for x in candidates if independent_critical(x)}
    assert len(candidates) == 748
    assert independent_hits == recorded_values

    # This finite certificate proves that the following divisor enumerations
    # are complete at every possible height, not merely within the scan range.
    assert prefix_certificate(5, 6).depth == 6
    atoms = set()
    for row in certificates:
        value = Fraction(row['value'])
        assert value in recorded_values and critical(5, 6, value)
        divisors = actual_divisors(5, 6, value)
        assert tuple(map(str, divisors)) == tuple(row['divisors'])
        atom = divisors == (Fraction(1), value)
        assert atom == row['is_atom']
        if atom:
            atoms.add(value)
    assert len(atoms) == 20
    integer_critical = [n for n in range(2, 25) if smooth_integer(n)]
    assert len(integer_critical) == 10
    integer_atoms = {
        Fraction(n) for n in integer_critical
        if actual_divisors(5, 6, Fraction(n)) == (Fraction(1), Fraction(n))
    }
    assert integer_atoms == {Fraction(2), Fraction(3)}
    atoms |= integer_atoms
    assert len(atoms) == 22 and min(atoms) == 2
    print(f'Passed: {effective_count:,} archived candidates through depth '
          f'{effective_depth:,}; independent first-100-depth scan; '
          'all 31 noninteger critical values; 22 global atom certificates.')
    print('No claim is made about smooth atoms beyond the archived depth.')


if __name__ == '__main__':
    check()
