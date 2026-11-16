# Complete finite-range classification through 100 million

For every integer

\[
4\le n\le100\,000\,000,\qquad
\gcd(n,21)=1,\qquad |\mathcal P(5n)|\ge2,
\]

the monoid

\[
\mathbb N_0\!\left[\frac3{5n},\frac75\right]^*
\]

is **IDF and non-atomic**. Its only positive integer admitting an atomic
factorization is 1. There are 57,142,844 admissible parameter values in
this interval.

This is an all-height statement for every parameter in a finite interval.
The computation does not infer termination from a search cutoff: every
necessary finite graph was exhausted and its outgoing edges were checked.
It leaves the original pair `(3/10,7/5)`, corresponding to `n=2`, outside
its scope. Novelty relative to the complete online discussion remains
unverified.

## 1. Reduction to a small exceptional list

Use the digit system and critical-word results proved in
[NEARBY_TERNARY_IDF_FAMILY.md](NEARBY_TERNARY_IDF_FAMILY.md), the finite
5-integral closure criterion in
[NEARBY_TERNARY_CARRY_CERTIFICATES.md](NEARBY_TERNARY_CARRY_CERTIFICATES.md),
and the Hensel argument in
[DENSITY_ONE_NEARBY_IDF.md](DENSITY_ONE_NEARBY_IDF.md).

Parameters outside `n ≡ 1 (mod 5)` already have the finite closure `{1}`.
For a remaining parameter, a nontrivial 5-integral word must start from
1 and apply the digit `r=7/5` first. If its length is `L`, write its value
as `H_w(n)/(5n)^L`. The first numerator is `7n+3`; appending a digit
`0,1,r` gives, respectively,

\[
3H_w(n),\qquad
3H_w(n)+(5n)^{L+1},\qquad
3H_w(n)+7\cdot5^L n^{L+1}.
\]

Every such polynomial has derivative congruent to
`7·3^(L−1)` modulo 5, so it has exactly one root modulo `5^L`.
A retained word of length 12 therefore forces the parameter into one
of the root classes of the `3^11=177,147` first-`r` words.

There are exactly **53,872 distinct root classes** modulo
`5^12=244,140,625`. Since this modulus exceeds 100 million, each class
has at most one positive representative in the requested interval.
Exactly **12,626** representatives satisfy `n≥4` and `gcd(n,21)=1`.
Every other admissible parameter has no retained word of length 12,
so its 5-integral tree has depth less than 12 and is finite.

## 2. Exhaustion of every exceptional tree

All 12,626 remaining trees were exhausted. Together they contain
**531,249 states**. The largest tree has 509 states, at `n=1,116,071`;
the greatest depth is 32, at `n=60,908,186`.

The finite-closure criterion consequently proves IDF for every
remaining parameter. The unconditional non-atomicity and integer
factorization result follow from the cited nearby-family theorem.

Two separate implementations agreed on every root class and every
rational state:

* Modular evaluation of digit words, testing all five Hensel lifts,
  followed by exact rational graph closure.
* Explicit integer coefficient polynomials with the derivative lift,
  followed by an integer word-tree calculation.

For the second method, write a retained depth-`L` state as `J/n^L`.
The three possible child numerators over `n^(L+1)` are

\[
\frac{3J}{5},\qquad n^{L+1}+\frac{3J}{5},\qquad
\frac{7n^{L+1}+3J}{5},
\]

and a child is retained exactly when its displayed numerator is an
integer. The hypotheses make these fractions reduced. Canonical digit
uniqueness prevents distinct retained words from representing the same
state. Both implementations exhaust the stack or queue before accepting.

## 3. Reproducible certificate

[nearby_100million_manifest.json](nearby_100million_manifest.json) stores
the complete exceptional parameter list with each tree's size and depth,
plus aggregate checksums. It avoids storing the 64 MB rational-state
listing: both checkers reconstruct all states exactly.

Run either independent method:

```sh
python research/monoids/check_nearby_100million.py
python research/monoids/check_nearby_100million_independent.py
```

The sorted root-list SHA-256 is
`7dbf178314412619f31e35c59c1d7a118fc9e962bf25004f159a507ff71c130d`.
The sorted candidate-list SHA-256 is
`b21541b168bfb125ece2365ddf8d297589592879897591f12fb8c445c3c02805`.
The complete state-list SHA-256 is
`7b6ebe5bdbb5b8baab20b02f529549e9b799bf89df31c25f9735266848874256`.
For the last hash, visit parameters in increasing order, write `n` and a
newline, then write each state in increasing rational order as
`numerator/denominator` and a newline. The checkers verify these hashes,
the complete parameter list, all per-tree counts and depths, and the
aggregate statistics.

The hashes are reproducibility checks; the proof relies on the exact
root enumeration and complete finite closures, not on the hashes alone.
