# A finite smooth-atom obstruction at 5/6

Let `S=N_0[5/6]`. This note records a completed exact finite search and
global certificates for the atoms it finds. It does **not** decide whether
`S minus {0}` is atomic or IDF. Novelty relative to the supplied discussion
and its inaccessible attachments is unverified.

## The completed range

The completed range currently reaches denominator depth **20,000,000**,
covering **149,555,035** noninteger candidates. The original large-integer
implementation covers depths 1 through 500,000; an independent exact
interval-and-residue implementation reproduces that range and extends it.
Denominator depth means the smallest `n` such that the reduced denominator
divides `6^n`.

Every positive `{2,3}`-smooth member of S is at least 1. Indeed, a member
below 1 is divisible by `q=5/6` in S, and hence has positive 5-adic valuation.
Such a valuation is impossible for a `{2,3}`-smooth rational. Every atom
is critical, by the perturbation argument, so every smooth atom lies in
`(1,24]`. Apart from integers, all candidates therefore have one of the forms

    2^u/3^n or 3^u/2^n, with 1 < value <= 24.

The scan examines every candidate in this interval at each recorded depth.
It finds exactly 31 noninteger critical elements, all at depths at most 22.
There are also ten smooth critical integers greater than 1:

    2, 3, 4, 6, 8, 9, 12, 16, 18, 24.

The complete divisor algorithm from
[CRITICAL_FINITE_DIVISORS.md](CRITICAL_FINITE_DIVISORS.md), with its depth-six
carry certificate at 5/6, proves which of these elements are atoms. These
atom decisions are global: they exclude divisors at every possible height,
not merely divisors in the scanned range.

There are exactly 22 smooth atoms within the completed depth range. Two are
the integers 2 and 3. The remaining twenty are specified by the following
exponent pairs `(u,n)`:

| Form | Exponent pairs |
|---|---|
| `2^u/3^n` | `(3,1), (8,3), (9,4), (11,5), (13,6), (15,7), (16,8), (17,9), (24,13), (38,22)` |
| `3^u/2^n` | `(2,1), (3,2), (4,3), (5,4), (6,6), (7,8), (8,9), (10,12), (12,16), (13,17)` |

In particular, all these atoms are at least 2. No conclusion is drawn about
smooth atoms beyond the completed depth.

## Why the scan is exact

At denominator depth n, write a candidate as `N/6^n`. Since `6^n=1 mod 5`,
its canonical digit is exactly `d=N mod 5`. Subtracting the digit and
dividing by 5/6 replaces the numerator and denominator by

    N <- (N-d*6^n)/5,    6^n <- 6^(n-1).

The numerator division is exact. Reject immediately if the new value is
negative or exceeds 24. After n steps, the remaining value is an integer;
it is critical exactly when it lies in `[0,24]`. The integer map
`k -> 6*floor(k/5)` preserves that interval. Candidate endpoints and all
orbit comparisons use integer arithmetic.

The archived JSONL files record the search intervals, every hit, progress
counts, and a final completion record. Their SHA-256 digests appear in
[smooth_critical_5_6_manifest.json](smooth_critical_5_6_manifest.json) and
[smooth_critical_5_6_interval_manifest.json](smooth_critical_5_6_interval_manifest.json).
The complete noninteger divisor lists are in
[smooth_critical_5_6_noninteger_certificates.json](smooth_critical_5_6_noninteger_certificates.json).

The faster independent verifier maintains integers `lo,hi` with
`lo <= 2^256*x <= hi` and the exact residue of x modulo a large power of 5.
After reading digit d, it updates the enclosure by rounding
`6*(lo-d*2^256)/5` downward and `6*(hi-d*2^256)/5` upward. The residue update
`6*((residue-d)/5)` loses exactly one base-5 digit. It rejects only when the
whole enclosure lies outside `[0,24]`. Low-depth survivors are checked with
independent Fraction arithmetic; an unresolved high-depth candidate aborts
the scan instead of producing a completion certificate.

The enumeration maintains similarly directed intervals for the two streams
`2^u/3^n` and `3^u/2^n`, normalizing to the first value above 1 at each depth.
Any comparison that straddles a boundary is resolved by exact integer powers.
No such boundary fallback occurred in the completed twenty-million-depth run;
its only 31 exact-orbit fallbacks were the 31 critical hits. Every other
candidate left the critical interval within 104 digit steps. The longest
rejection, at `3^12190423/2^19321360`, was independently checked using the
original large-integer arithmetic; it exits below zero at step 104. The
audit is recorded in
[smooth_critical_5_6_last_rejection_audit.json](smooth_critical_5_6_last_rejection_audit.json).

There is also an independent total-count certificate. With
`alpha=log_2(3)` and `beta=log_3(2)`, the exact number of candidates through
depth N is

    4N + floor((N+1)*alpha)
       + floor((N+1)*beta) + floor((N+2)*beta) + floor((N+3)*beta) - 3.

For the first stream, the number at depth n is
`3+floor((n+1)*alpha)-floor(n*alpha)`; for the second it is
`1+floor((n+3)*beta)-floor(n*beta)`. Both sums telescope. Exact rational
logarithm intervals certify every displayed floor, so the independent count
uses no floating-point decisions.

## A concrete unresolved element below all these atoms

Define, by its prime exponents,

    h = 2^2364816678866 / 3^1492033204438.

[check_small_smooth_5_6.py](check_small_smooth_5_6.py) proves, using exact
rational bounds for logarithms and modular exponentiation, that

    1.91 < h < 1.93,
    h = 1 + (5/6)^18*z, with z in Z[1/6] and 24 < z < 25.

The conductor 24 therefore puts h in S. Its first 18 canonical digits lead
to z, so it is noncritical and reducible.

If an atom alpha divides h in S, its numerator has no prime factor outside
`{2,3}`, since outside-prime valuations cannot cancel. Its cofactor is also
smooth and therefore at least 1, giving `alpha <= h < 2`. Consequently any
atom divisor of h must have denominator depth **strictly beyond the completed
scan range**. In particular, an atomic factorization of h, if one exists,
must use atoms of denominator depth greater than **20,000,000**.

This is a finite exclusion statement. It proves neither that h has no atom
divisor nor that h lacks an atomic factorization. Proving that every smooth
atom is at least 2, without a depth cutoff, would prove non-atomicity using h;
that unrestricted assertion remains unproved here.

## Reproduction

From the repository root:

```sh
python research/monoids/check_smooth_critical_5_6.py
python research/monoids/check_small_smooth_5_6.py
```

The first command checks archive integrity, reruns all 748 candidates through
depth 100 with independent Fraction arithmetic, and regenerates every listed
global divisor certificate. It does not rerun the full large-depth search.

To reproduce the faster complete twenty-million-depth verification:

```sh
python research/monoids/verify_smooth_critical_5_6_intervals.py --limit 20000000 --digits 200 --progress 100000 --output /tmp/smooth_5_6_intervals.jsonl
```

This took about 798 seconds in the research workspace. To reproduce the two
original large integer-arithmetic segments, which are much slower:

```sh
python research/monoids/scan_smooth_critical_5_6.py --limit 100000 --output /tmp/smooth_5_6_first.jsonl
python research/monoids/scan_smooth_critical_5_6.py --start 100001 --limit 500000 --output /tmp/smooth_5_6_second.jsonl
```

Compare the exact candidates, hits, and completion counts; elapsed times vary
between machines. A truncated output without its completion record does not
certify the requested range.
