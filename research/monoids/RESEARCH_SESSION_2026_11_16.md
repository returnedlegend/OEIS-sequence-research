# Three-hour research session: verified results and limits

The requested session ran from 22:43 UTC on November 15 to 01:43 UTC on
November 16, 2026. Work was continually pushed to the `research/monoid-idf`
branch. The original rational-pair
classification remains incomplete, and no atomic, non-IDF example in the
requested two-generator family was proved.

## Strongest infinite-family result

For

\[
M_n=\mathbb N_0\!\left[\frac{3}{5n},\frac75\right]^*,\qquad
n\ge4,\quad \gcd(n,21)=1,\quad |\mathcal P(5n)|\ge2,
\]

every monoid is non-atomic, and a **relative density-one set of parameters
is proved IDF**. The certificate method leaves at most
`N^(log_5 3)` admissible parameters up to N uncertified at its prescribed
finite depth. It does not assert that those remaining monoids fail IDF.

The proof is short in principle. A retained digit word of length L gives a
polynomial congruence in n with unit derivative modulo 5, so it specifies
one residue class modulo `5^L`. There are at most `3^(L-1)` words. Parameters
with infinite retained trees lie in all these shrinking residue-class unions,
and therefore have upper natural density zero. A finite tree supplies an
all-height IDF certificate.

[DENSITY_ONE_NEARBY_IDF.md](DENSITY_ONE_NEARBY_IDF.md) gives the proof and
112 explicit infinite arithmetic progressions. The method extends to fixed
generators such as `8/7`, `11/7`, and `5/4`; see
[TERNARY_PARAMETER_DENSITY_EXTENSION.md](TERNARY_PARAMETER_DENSITY_EXTENSION.md)
and [COMPOSITE_DENOMINATOR_DENSITY_ONE.md](COMPOSITE_DENOMINATOR_DENSITY_ONE.md).
The final extension,
[ARBITRARY_NUMERATOR_DENSITY_ONE.md](ARBITRARY_NUMERATOR_DENSITY_ONE.md),
works for every numerator `a>=3` under explicit denominator-block and
coprimality hypotheses, and gives an exact classification of the positive
integers admitting atomic factorizations in those families.

## Complete finite-range classification of that family

Every one of the **57,142,844 admissible parameters `n<=100,000,000`** is
certified IDF and non-atomic. The root-class reduction leaves only 12,626
parameters requiring individual finite graphs; all of them terminate.
Two independent implementations agree on all 531,249 rational states.

[NEARBY_IDF_THROUGH_100_MILLION.md](NEARBY_IDF_THROUGH_100_MILLION.md)
contains the complete argument and reproduction commands. This is a global
IDF theorem for each parameter in a finite parameter range, rather than
evidence from bounded-height factor searches. The boundary `n=2`, namely
the original `(3/10,7/5)` pair, remains outside its scope.

The boundary is structural: the conductor `7n/(5n-3)` equals 2 at `n=2`,
where critical endpoint representations occur. For admissible `n>=4` it is
strictly below 2, and the finite-word argument applies. The larger finite
range therefore does not automatically answer the boundary problem.

## Further proved families and algorithms

The notes prove IDF and non-atomicity for every
`N_0[5/6^m,7/6]^*` with `m>=2`, and every
`N_0[7/60^m,61/60]^*` with `m>=2`. Small finite carry graphs handle the
boundary parameters; analytic estimates cover the infinite tails.
The Boolean mixed-family theorem removes denominator-block restrictions
from another broad class, with independent, nonredundant examples for
every prescribed numerator at least 3.

The complementary-family algorithm now permits every integer endpoint
`C>=3`. Actual divisors of a critical element are exactly evaluations of
formal divisors of its canonical polynomial. Under one large denominator
block, all complete atomic factorizations of every input can be enumerated.
These finite lists do not imply IDF, because a cofactor may be non-atomic.

For cyclic semirings, exact carry certificates give complete divisor
algorithms for critical elements. Symbolic families cover every prescribed
set of at least two denominator primes, and a separate exact computation
certifies 1,001,391 reduced `K=1` parameters with denominator at most 5000
and at least two denominator primes. For reduced `1<a<b`, the general
reciprocal transfer theorem proves that `N_0[a/b]^*` is IDF exactly when
`N_0[a/b,b/a]^*` is IDF, including composite numerators.

The [directory index](README.md) links each proof, its precise hypotheses,
and its exact implementation.

## Original examples: what the computations prove

For `N_0[2/5,2/3]^*`, every positive integer below `2^47` admitting an
atomic factorization is a power of 11, and its factorization is unique.
In particular the complete list below `10^14` is `1,11,...,11^13`.
The proof uses exact finite word catalogues, independently checked by
Python and GMP implementations. It does not classify all positive integers
or settle IDF. See [BINARY_ATOMIC_INTEGERS_FINITE.md](BINARY_ATOMIC_INTEGERS_FINITE.md).

For `N_0[5/6]^*`, the completed smooth critical-orbit search and its exact
scope are recorded in [SMOOTH_CRITICAL_5_6_SCAN.md](SMOOTH_CRITICAL_5_6_SCAN.md).
The exact search covers 149,555,035 candidates through denominator depth
20,000,000. There are 22 certified smooth atoms in that range, all at least 2.
An explicit smooth member h in `(1.91,1.93)` is proved to belong to the
semiring. Any atom divisor of h must have denominator depth greater than
20,000,000.
This leaves both the existence of such divisors and atomicity of h undecided.

## Source status and remaining problems

The supplied discussion already reports non-atomicity of `(2/5,2/3)` and
`(3/10,7/5)`, and provides related digit, conductor, and valuation methods.
Those are credited in the notes. The requested AoPS page still returned
proxy tunnel HTTP 403 on the final access check; the attached discussion
PDFs were unavailable. **Novelty relative to the complete discussion and
literature has not been verified.**

The original two-generator classification is not solved. In particular,
this session does not settle IDF for `(2/5,2/3)` or `(3/10,7/5)`, nor
atomicity of `N_0[5/6]^*`. Finite searches, terminating certificates for
individual parameters, and unrestricted theorems are distinguished
throughout the write-ups.
