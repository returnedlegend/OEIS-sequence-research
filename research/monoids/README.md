# Rational semiring multiplicative monoids: checked partial results

The problem asks which rational pairs give an atomic, non-IDF multiplicative
monoid, and which give an IDF, non-atomic one. **The full classification is
not solved here. No atomic, non-IDF example in the requested family has been
proved in these notes.**

The proofs and algorithms below are independently checked partial results.
Novelty relative to the complete AoPS discussion and its PDF attachments
has not been verified. Live access remains blocked; see
[SOURCE_STATUS.md](SOURCE_STATUS.md) for the supplied sources and attribution.

## Density-one classification in an infinite mixed family

For `n>=4`, `gcd(n,21)=1`, and at least two prime divisors of `5n`, put
`M_n=N_0[3/(5n),7/5]^*`. Every such monoid is non-atomic, and **a relative
density-one set of these parameters is proved IDF**. The proof uses simple
root lifting and digit-word counting; it does not extrapolate a finite search.
Among parameters up to `N`, at most `N^(log_5 3)` remain uncertified by the
specified finite-depth procedure. No exceptional non-IDF parameter is asserted
to exist, and the original `n=2` example remains outside the theorem.

See [DENSITY_ONE_NEARBY_IDF.md](DENSITY_ONE_NEARBY_IDF.md).
The exact computation in
[NEARBY_IDF_THROUGH_100_MILLION.md](NEARBY_IDF_THROUGH_100_MILLION.md)
settles **every admissible parameter through 100,000,000**: all 57,142,844
such monoids are IDF and non-atomic. Independent implementations exhaust
every necessary graph; this is not a truncated height search.
[TERNARY_PARAMETER_DENSITY_EXTENSION.md](TERNARY_PARAMETER_DENSITY_EXTENSION.md)
extends this to every fixed `r=A/p` with prime `p>3`, `p<A<2p`, and
`A=2p mod3`, under its stated coprimality and denominator-support conditions.
[COMPOSITE_DENOMINATOR_DENSITY_ONE.md](COMPOSITE_DENOMINATOR_DENSITY_ONE.md)
also covers fixed composite denominators, including `r=5/4`, when every
maximal denominator prime-power block exceeds 3.
[ARBITRARY_NUMERATOR_DENSITY_ONE.md](ARBITRARY_NUMERATOR_DENSITY_ONE.md)
extends the construction to every numerator `a>=3`, with the additional
small-prime coprimality condition stated there. It also classifies exactly
which positive integers admit atomic factorizations in those families.

## Explicit IDF, non-atomic families

| Family | Concrete example | Stronger conclusion |
|---|---|---|
| Five-digit family, every `m>=2` | `(5/6^m,7/6)` | At `m=2`, the sole denominator-supported atom is 3/2 and 2 is atomless. For `m>=3`, no denominator-supported atoms exist. |
| Seven-digit family, every `m>=2` | `(7/60^m,61/60)` | The integers 2, 3, and 5 have no atom divisor. |
| Boolean forcing, without denominator-block restrictions | `(5/1296,7/6)` | Both 2 and 3 have no atom divisor; only 1 among positive integers has an atomic factorization. |
| Independent mixed generators with a finite positive basis | `(3/1225,37/35)` | The integer 5 has no atom divisor. |
| Independent mixed generators with numerator 2 | `(2/225,3377/3375)` | Both 3 and 5 have no atom divisor. |
| A family adjacent to the unresolved mixed pair | `(3/20,7/5)` | Both 2 and 5 have no atom divisor; no integer greater than 1 has an atomic factorization. |
| Two nonredundant contracting powers | `(4/225,8/3375)` | `125/81=1+3*(4/225)+1550*(4/225)^2` has no atom divisor. |
| Reciprocal generators with composite numerator | `(6/175,175/6)` | `49/25=1+28*(6/175)` has no atom divisor. |

The family with a finite positive basis is proved in
[INDEPENDENT_MIXED_IDF_FAMILY.md](INDEPENDENT_MIXED_IDF_FAMILY.md).
It covers `q=a/b^m`, `r=A/b^k>1` when `gcd(aA,b)=gcd(m,k)=1`, the denominator
has at least two prime factors, every maximal prime-power factor of `b`
exceeds `a`, and `r^m` belongs to `N_0[q]`. Explicit genuinely independent,
nonredundant constructions exist for **every numerator `a>=2`**.

[NEARBY_TERNARY_IDF_FAMILY.md](NEARBY_TERNARY_IDF_FAMILY.md) proves the
corresponding claims for `(3/(5n),7/5)` under explicit arithmetic conditions.
It deliberately excludes `n=2`, the original unresolved IDF example.
[NEARBY_TERNARY_CARRY_CERTIFICATES.md](NEARBY_TERNARY_CARRY_CERTIFICATES.md)
removes the earlier congruence exclusion for every admissible `n<=10000`,
using 1,142 complete finite graphs. Each graph proves a statement at all
heights for its parameter. General termination for all `n` is not claimed.

[FIVE_SIX_MIXED_IDF_FAMILY.md](FIVE_SIX_MIXED_IDF_FAMILY.md) proves the
entire first row. Its small carry graphs also give full atom and
factorization algorithms. At the excluded boundary `m=1`, the integer 2
is an atom; this does not classify that monoid.

[DIGIT_PRIME_CARRY_IDF_CERTIFICATES.md](DIGIT_PRIME_CARRY_IDF_CERTIFICATES.md)
proves the seven-digit family with complete finite graphs for its small
parameters and an analytic argument for the remaining ones. The broader
[PRIMITIVE_RESIDUE_MIXED_IDF_FAMILY.md](PRIMITIVE_RESIDUE_MIXED_IDF_FAMILY.md)
provides further fixed-generator families and exact factorization algorithms.

[NUMERICAL_EXPONENT_SEMIRINGS.md](NUMERICAL_EXPONENT_SEMIRINGS.md) proves
IDF and non-atomicity for semirings generated by a numerical semigroup of
powers of `t=a/b`, under the denominator-block condition. In particular,
it covers every pair `(t^i,t^j)` with positive exponents; neither generator
is redundant when neither exponent divides the other.

Earlier cyclic and reciprocal constructions appear in
[PRIME_POWER_DENOMINATOR_FAMILIES.md](PRIME_POWER_DENOMINATOR_FAMILIES.md)
and [IDF_NONATOMIC_FAMILY.md](IDF_NONATOMIC_FAMILY.md).

The stronger [BOOLEAN_MIXED_IDF_FAMILY.md](BOOLEAN_MIXED_IDF_FAMILY.md)
removes every denominator-block comparison: an identity `2=r+Kq` with
`K` above the cyclic conductor forces all atom basis coefficients to be
0 or 1. It supplies independent, nonredundant IDF/non-atomic examples for
every numerator `a>=3` and every prescribed set of at least two denominator
primes coprime to `a`, including supports entirely below `a`.

## A general reciprocal transfer theorem

For every reduced `1<a<b`, put `S=N_0[a/b]` and `T=N_0[a/b,b/a]`.
Then **S is IDF if and only if T is IDF**, and atomicity of S implies
atomicity of T. When `a` is prime, atomicity is equivalent as well.

[RECIPROCAL_TRANSFER_AND_GENERAL_FAMILY.md](RECIPROCAL_TRANSFER_AND_GENERAL_FAMILY.md)
gives the proof, including the nontrivial unit group and the arbitrary
composite-numerator case. [RECIPROCAL_ALGORITHM.md](RECIPROCAL_ALGORITHM.md)
documents exact finite atom and factorization algorithms for the proved
denominator-block family.

## Critical elements and the 5/6 case

[CRITICAL_BOUNDED_FACTORIZATIONS.md](CRITICAL_BOUNDED_FACTORIZATIONS.md)
proves that every bounded canonical digit orbit gives bounded lengths of
nonunit factorizations, and hence an atomic factorization. With at least
two denominator primes, a noncritical element starts an infinite proper
divisor chain.

[CRITICAL_FINITE_DIVISORS.md](CRITICAL_FINITE_DIVISORS.md) strengthens this
to **finite actual divisors** using exact finite carry certificates. All
87 reduced parameters with denominator at most 30 and at least two
denominator primes have complete certificates. In particular, this gives
a terminating atom decision algorithm for every rational input at `5/6`.

These are local statements about elements. They do not decide whether
every element of `N_0[5/6]` has an atomic factorization, or whether each
noncritical target has finitely many atom divisors.

Several infinite arithmetic families also have symbolic depth-one certificates.
[CRITICAL_IDF_HEIGHT_REDUCTION.md](CRITICAL_IDF_HEIGHT_REDUCTION.md)
identifies the remaining global question exactly: IDF is equivalent to
finiteness of each critical class with fixed numerator part outside the
denominator primes. This reduction may overlap the credited discussion.
Further symbolic constructions cover arbitrarily many denominator primes.
[check_cyclic_k1.py](check_cyclic_k1.py) independently certifies every
reduced `K=1` parameter with denominator at most 5000 and at least two
denominator primes; this finite parameter
range is not a universal termination proof.

[SMOOTH_CRITICAL_5_6_SCAN.md](SMOOTH_CRITICAL_5_6_SCAN.md) records the exact
finite search for denominator-supported atoms, global certificates for the
22 atoms found, and an explicit member below 2 whose possible atom divisors
must lie beyond the completed search range. This is a finite exclusion,
not a resolution of atomicity at 5/6.

## Exact algorithms for the two unresolved IDF examples

| Pair | Proved and implemented here | Still unresolved |
|---|---|---|
| `(2/5,2/3)` | Terminating membership; exact atom descriptions; all complete atomic factorizations of any input form a finite, computable list. | IDF |
| `(3/10,7/5)` | Membership; atom decision; all complete atomic factorizations of any input form a finite, computable list. | IDF |

See [BINARY_PAIR_ATOMIC_FACTORIZATIONS.md](BINARY_PAIR_ATOMIC_FACTORIZATIONS.md),
[PAIR_3_10_ATOM_ALGORITHM.md](PAIR_3_10_ATOM_ALGORITHM.md), and
[PAIR_3_10_FACTORIZATION_ALGORITHM.md](PAIR_3_10_FACTORIZATION_ALGORITHM.md).
The finite lists concern complete factorizations. They need not contain
every atom divisor whose cofactor lacks an atomic factorization.

[BINARY_ATOMIC_INTEGERS_FINITE.md](BINARY_ATOMIC_INTEGERS_FINITE.md) gives a
computer-assisted classification: the positive integers at most `10^14`
admitting atomic factorizations in `N_0[2/5,2/3]^*` are exactly
`1,11,...,11^13`, each with a unique atomic factorization. A sharpening
covers every integer below `2^47`. The required finite binary-word
certificates are reproduced by independent exact implementations. No
all-integer classification is claimed.

The non-atomicity of both pairs was already reported in the supplied
discussion and is credited there. The original reductions are recorded in
[PAIR_2_5_2_3.md](PAIR_2_5_2_3.md) and [PAIR_3_10_7_5.md](PAIR_3_10_7_5.md).

Exact carry graphs exclude many prescribed degree gaps at **all absolute
heights**, but only a finite range of gaps has been checked. These
computations do not settle IDF. See
[BINARY_RATIO_GAP_SEARCH.md](BINARY_RATIO_GAP_SEARCH.md),
[BINARY_IDF_RESTRICTIONS.md](BINARY_IDF_RESTRICTIONS.md), and
[PAIR_3_10_RATIO_AUTOMATON.md](PAIR_3_10_RATIO_AUTOMATON.md).

## A broader family of contracting pairs

[MOBIUS_PAIR_NORMAL_FORMS.md](MOBIUS_PAIR_NORMAL_FORMS.md) treats
`q=a/b<1/2`, `r=a/(b-a)`. If a maximal prime-power factor of `b` exceeds
`a`, the monoid is non-atomic, yet every input has an effectively finite
list of complete atomic factorizations. The generic implementation also
decides membership and atomhood. IDF is not settled by this theorem.

For `(4/9,4/5)`, the explicit element `531441/390625=3^12/5^8` has no
atomic factorization. The implementation and independent checks include
nonconstant periodic digit cycles, which must be rejected as nonmembers.

The separate
[COMPLEMENTARY_CRITICAL_FACTORIZATIONS.md](COMPLEMENTARY_CRITICAL_FACTORIZATIONS.md)
treats complementary pairs for every integer endpoint `C>=3`. Actual
divisors of a critical element are exactly evaluations of the formal
divisors of its canonical polynomial. One large denominator block suffices
for non-atomicity and finite complete factorization lists; global IDF remains
a separate question. The prime-endpoint refinements are retained in
[PRIME_COMPLEMENT_ENDPOINT_HEIGHT.md](PRIME_COMPLEMENT_ENDPOINT_HEIGHT.md).

[ONE_BLOCK_MIXED_ATOMIC_FACTORIZATIONS.md](ONE_BLOCK_MIXED_ATOMIC_FACTORIZATIONS.md)
extends the one-block argument to a positive mixed basis, again distinguishing
complete atomic factorizations from arbitrary atom divisors.

## Other proved reductions

- [MIXED_TWO_PRIME_FAMILY.md](MIXED_TWO_PRIME_FAMILY.md): an atomic, IDF
  mixed family, including nontrivial unit groups.
- [TWO_SMALL_GENERATORS.md](TWO_SMALL_GENERATORS.md): real conductors and
  localization results for two contracting generators.
- [STRONGER_CYCLIC_REDUCTIONS.md](STRONGER_CYCLIC_REDUCTIONS.md): the
  one-good-denominator-block non-atomicity criterion and uniqueness tools.
- [LIMITS_OF_CONDUCTOR_ARGUMENTS.md](LIMITS_OF_CONDUCTOR_ARGUMENTS.md):
  counterexamples to a proposed abstract conductor argument; these are
  not asserted to be finitely generated rational semirings.

## Reproduce the exact checks

From the repository root:

```sh
python research/monoids/check_reciprocal.py
python research/monoids/check_binary_pair.py
python research/monoids/check_pair_3_10.py
python research/monoids/check_binary_ratio_gap.py
python research/monoids/check_cyclic_critical.py
python research/monoids/check_new_idf_families.py
python research/monoids/check_mobius_pair.py
python research/monoids/check_prime_complementary.py
python research/monoids/check_complementary_family.py
python research/monoids/check_density_one_certificates.py
python research/monoids/check_composite_density.py
python research/monoids/check_arbitrary_numerator_density.py
python research/monoids/check_nearby_100million.py
python research/monoids/check_nearby_100million_independent.py
python research/monoids/check_binary_atomic_integers.py
python research/monoids/check_binary_valuation_mitm.py
python research/monoids/check_smooth_critical_5_6.py
python research/monoids/check_small_smooth_5_6.py
```

Add `--all-certificates` to the cyclic check to regenerate all 87 carry
certificates, including their recorded state-count hashes. Resource caps
are reported as incomplete searches, never as proofs of nonexistence.
