"""Rigorous interval/residue scan of NONINTEGER smooth critical 5/6 values.

All mathematical comparisons use integers or exact Fractions. Floating
point is used only for elapsed-time reports. A candidate not decided by
the configured digits and safe exact-fallback range aborts the scan.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from fractions import Fraction
from pathlib import Path


class Incomplete(RuntimeError):
    pass


def logarithm_interval(integer, terms=120):
    """Exact atanh-series enclosure of log(integer), for integer>1.

    With z=(integer-1)/(integer+1), the omitted positive tail after m
    terms is at most 2*z**(2*m+1)/((2*m+1)*(1-z*z)).
    """
    z = Fraction(integer - 1, integer + 1)
    square, term, lower = z * z, z, Fraction()
    for j in range(terms):
        lower += 2 * term / (2 * j + 1)
        term *= square
    remainder = 2 * term / ((2 * terms + 1) * (1 - square))
    return lower, lower + remainder


def independent_candidate_count(limit):
    """Telescoping count, independently certified by rational log bounds.

    Put alpha=log_2(3), beta=log_3(2). The two counts at depth n are
    floor(n*alpha+3+alpha)-floor(n*alpha) and
    floor(n*beta+1+3*beta)-floor(n*beta). Summing from1 through N gives
    4*N+floor((N+1)*alpha)+sum(floor((N+j)*beta),j=1..3)-3.
    Each floor below must agree at both rational interval endpoints.
    """
    low2, high2 = logarithm_interval(2)
    low3, high3 = logarithm_interval(3)

    def certified_floor(multiplier, lower, upper):
        lo, hi = multiplier * lower, multiplier * upper
        first, last = lo.numerator // lo.denominator, hi.numerator // hi.denominator
        if first != last:
            raise Incomplete("logarithm intervals do not certify a counting floor")
        return first

    alpha = certified_floor(limit + 1, low3 / high2, high3 / low2)
    beta = sum(certified_floor(limit + j, low2 / high3, high2 / low3)
               for j in (1, 2, 3))
    return 4 * limit + alpha + beta - 3


def exact_orbit(p, u, s, n):
    value = Fraction(p**u, s**n)
    for step in range(1, n + 1):
        digit = value.numerator * pow(value.denominator, -1, 5) % 5
        value = (value - digit) * Fraction(6, 5)
        if value < 0 or value > 24:
            return None, step
    assert value.denominator == 1
    return value.numerator, n


class RatioStream:
    """Maintain lo <= scale*p**u/s**n <= hi and its residue modulo 5**K."""

    def __init__(self, p, s, scale, modulus):
        self.p, self.s = p, s
        self.scale, self.modulus = scale, modulus
        self.inverse_s = pow(s, -1, modulus)
        self.lo = self.hi = scale
        self.residue = 1
        self.u = self.n = 0
        self.comparison_fallbacks = 0

    def _greater_than_one(self):
        if self.lo > self.scale:
            return True
        if self.hi <= self.scale:
            return False
        self.comparison_fallbacks += 1
        return self.p**self.u > self.s**self.n

    def advance(self):
        self.n += 1
        self.lo //= self.s
        self.hi = (self.hi + self.s - 1) // self.s
        self.residue = self.residue * self.inverse_s % self.modulus
        while not self._greater_than_one():
            self.lo *= self.p
            self.hi *= self.p
            self.residue = self.residue * self.p % self.modulus
            self.u += 1

    def candidates(self):
        lo, hi, residue, u = self.lo, self.hi, self.residue, self.u
        upper = 24 * self.scale
        while True:
            if lo > upper:
                break
            if hi > upper:
                self.comparison_fallbacks += 1
                if self.p**u > 24 * self.s**self.n:
                    break
            yield (self.p, u, self.s, self.n), lo, hi, residue
            lo *= self.p
            hi *= self.p
            residue = residue * self.p % self.modulus
            u += 1


class IntervalClassifier:
    """Enclose every canonical state and use only certified rejections.

    If lo<=scale*x<=hi, the next enclosure uses floor on the lower
    endpoint and ceil on the upper endpoint after the affine map
    x -> 6*(x-digit)/5. Integer (z+4)//5 is ceil(z/5), even for z<0.
    If x=R modulo5**r, then 6*((R-digit)//5) represents the next state
    modulo5**(r-1), because R-digit is an integer multiple of5.
    """

    def __init__(self, bits=256, digits=100, exact_fallback_max_depth=1000):
        self.bits, self.digits = bits, digits
        self.scale = 1 << bits
        self.upper = 24 * self.scale
        self.moduli = [5**i for i in range(digits + 1)]
        self.fallback_limit = exact_fallback_max_depth
        self.exact_fallbacks = []

    def classify(self, key, lo, hi, residue):
        p, u, s, n = key
        remaining = self.digits
        for step in range(1, min(n, self.digits) + 1):
            digit = residue % 5
            lo = 6 * (lo - digit * self.scale) // 5
            hi = (6 * (hi - digit * self.scale) + 4) // 5
            remaining -= 1
            residue = ((residue - digit) // 5) * 6 % self.moduli[remaining]
            if hi < 0 or lo > self.upper:
                return None, step
        # No undecided candidate is silently counted as critical. The few
        # genuine low-degree survivors are checked by independent Fractions.
        if n > self.fallback_limit:
            raise Incomplete(f"unresolved high-depth candidate {key}")
        result = exact_orbit(p, u, s, n)
        self.exact_fallbacks.append(key)
        return result


def small_crosscheck(bits, digits, limit=100):
    classifier = IntervalClassifier(bits, digits)
    modulus = classifier.moduli[-1]
    streams = [RatioStream(2, 3, classifier.scale, modulus),
               RatioStream(3, 2, classifier.scale, modulus)]
    observed = []
    for n in range(1, limit + 1):
        for stream in streams:
            stream.advance()
            for key, lo, hi, residue in stream.candidates():
                p, u, s, depth = key
                value = Fraction(p**u, s**depth)
                assert lo <= classifier.scale * value <= hi
                assert residue == pow(p, u, modulus) * pow(pow(s, depth, modulus), -1, modulus) % modulus
                result = classifier.classify(key, lo, hi, residue)
                assert result == exact_orbit(*key), (key, result, exact_orbit(*key))
                observed.append(key)
    expected = []
    for n in range(1, limit + 1):
        for p, s in [(2, 3), (3, 2)]:
            denominator, numerator, u = s**n, 1, 0
            while numerator <= denominator:
                numerator *= p
                u += 1
            while numerator <= 24 * denominator:
                expected.append((p, u, s, n))
                numerator *= p
                u += 1
    assert observed == expected
    assert len(observed) == independent_candidate_count(limit)
    return dict(depth=limit, candidates=len(observed),
                comparison_fallbacks=sum(s.comparison_fallbacks for s in streams))


def source_catalogues(paths):
    catalogues = []
    for path in paths:
        result = {}
        start, completed_depth = 1, 0
        for line in Path(path).read_text().splitlines():
            row = json.loads(line)
            if row.get("kind") == "metadata":
                start = row.get("start", 1)
            if row.get("kind") in ("progress", "complete"):
                completed_depth = max(completed_depth, row["depth"])
            if row.get("kind") == "critical":
                key = (row["numerator_prime"], row["numerator_exponent"],
                       row["denominator_prime"], row["denominator_exponent"])
                assert key not in result or result[key] == row["terminal"]
                result[key] = row["terminal"]
        if completed_depth < start:
            raise ValueError(f"comparison source has no completed coverage: {path}")
        catalogues.append((path, start, completed_depth, result))
    return catalogues


def run(args):
    check = small_crosscheck(args.bits, args.digits)
    print(json.dumps(dict(kind="crosscheck", **check)), flush=True)
    classifier = IntervalClassifier(args.bits, args.digits)
    streams = [RatioStream(2, 3, classifier.scale, classifier.moduli[-1]),
               RatioStream(3, 2, classifier.scale, classifier.moduli[-1])]
    total = max_reject = 0
    hits = {}
    digest = hashlib.sha256()
    started = time.monotonic()
    with open(args.output, "w") as output:
        output.write(json.dumps(dict(kind="metadata", limit=args.limit,
                                     bits=args.bits, residue_digits=args.digits,
                                     interval="1 < x <= 24", exact=True,
                                     candidate_class="noninteger {2,3}-smooth",
                                     small_crosscheck=check)) + "\n")
        for n in range(1, args.limit + 1):
            for stream in streams:
                stream.advance()
                for key, lo, hi, residue in stream.candidates():
                    terminal, steps = classifier.classify(key, lo, hi, residue)
                    total += 1
                    digest.update((",".join(map(str, key)) + ":" + str(terminal)
                                   + ":" + str(steps) + "\n").encode())
                    if terminal is None:
                        if steps > max_reject:
                            max_reject = steps
                            output.write(json.dumps(dict(
                                kind="rejection_record", candidate=list(key),
                                rejection_step=steps)) + "\n")
                    else:
                        hits[key] = terminal
                        p, u, s, depth = key
                        row = dict(kind="critical", numerator_prime=p,
                                   numerator_exponent=u, denominator_prime=s,
                                   denominator_exponent=depth, terminal=terminal)
                        output.write(json.dumps(row) + "\n")
                        output.flush()
            if n % args.progress == 0 or n == args.limit:
                report = dict(kind="progress", depth=n, candidates=total,
                              critical=len(hits), max_reject_steps=max_reject,
                              comparison_fallbacks=sum(s.comparison_fallbacks for s in streams),
                              exact_orbit_fallbacks=len(classifier.exact_fallbacks),
                              current_maximum_stream_interval_width=max(s.hi-s.lo for s in streams),
                              elapsed_seconds=round(time.monotonic()-started, 3))
                output.write(json.dumps(report) + "\n")
                output.flush()
                print(json.dumps(report), flush=True)
        if args.compare:
            for path, start, covered, catalogue in source_catalogues(args.compare):
                end = min(args.limit, covered)
                expected = {key: value for key, value in catalogue.items()
                            if start <= key[3] <= end}
                observed = {key: value for key, value in hits.items()
                            if start <= key[3] <= end}
                assert observed == expected, dict(
                    source=path, start=start, end=end,
                    missing=list(expected.keys()-observed.keys()),
                    added=list(observed.keys()-expected.keys()))
        expected_count = independent_candidate_count(args.limit)
        assert total == expected_count
        complete = dict(kind="complete", depth=args.limit, candidates=total,
                        independently_counted_candidates=expected_count,
                        critical=len(hits), max_reject_steps=max_reject,
                        comparison_fallbacks=sum(s.comparison_fallbacks for s in streams),
                        exact_orbit_fallbacks=len(classifier.exact_fallbacks),
                        sha256=digest.hexdigest(), compared_sources=args.compare,
                        elapsed_seconds=round(time.monotonic()-started, 3))
        output.write(json.dumps(complete) + "\n")
        print(json.dumps(complete), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=500000)
    parser.add_argument("--bits", type=int, default=256)
    parser.add_argument("--digits", type=int, default=100)
    parser.add_argument("--progress", type=int, default=10000)
    parser.add_argument("--output", required=True)
    parser.add_argument("--compare", nargs="*", default=[])
    args = parser.parse_args()
    if args.limit < 1 or args.bits < 32 or args.digits < 1 or args.progress < 1:
        parser.error("require positive limit/digits/progress and at least32 interval bits")
    run(args)


if __name__ == "__main__":
    main()
