# Finite atomic factorizations in mixed semirings with one good block

This is a broader finite-factorization algorithm, not an IDF theorem. It
extends the one-good-block cyclic argument to positive finite mixed bases.
Novelty relative to the full discussion remains unverified.

## Theorem

Let

    q=a/b^m in(0,1), r=A/b^k>1,
    a>=2, gcd(a*A,b)=1, gcd(m,k)=1, |P(b)|>=2,
    b^m>a^2, r^m in N_0[q].

Assume only ONE denominator prime p satisfies p^f>a, f=v_p(b).
Then S=N_0[q,r] minus{0} is non-atomic. Every element has finitely many
atomic factorizations, and all of them can be enumerated by an exact
terminating algorithm. No general IDF conclusion is asserted here.

## 1. Atom oracle

The cyclic conductor C=(a-1)/(1-q) is less than a. Near-one smooth
perturbation makes every basis coefficient at least a reducible. Thus all
atoms have coefficients below a in the basis q^i*r^j, 0<=j<m.

Such bounded arrays are unique: subtract two arrays and use the highest
denominator weight mi+kj. Its coefficient difference has magnitude less
than a<p^f and cannot cancel the lower terms, all divisible by p^f.

The finite-state membership graph, strict-escape test, and bounded-factor
argument of INDEPENDENT_MIXED_IDF_FAMILY.md sections11–14 therefore work
unchanged with this one good prime. They give a complete atom oracle.
The element q is an atom, and every other atom exceeds1.

## 2. A finite search for all atomic factorizations

Fix x in S and a numerator prime ell|a. Copies of q in any factorization
are bounded by E=floor(v_ell(x)/v_ell(a)). Enumerate their number u=0,...,E,
and let B=x/q^u be the target product of the other atoms. Discard B<1.

A noninteger atom beta with highest denominator weight n>=1 satisfies

    -v_p(beta)=n*f-v_p(d)>=n,

because its leading coefficient d satisfies0<d<a<p^f. An integer atom is
an ordinary prime below a. Among integer atoms only p can contribute positive
p-adic valuation, and its multiplicity is at most

    J=floor(log_p B) if p<a, and J=0 otherwise.

The bound is valid even if p itself is reducible and never occurs. Therefore
the sum of denominator weights of all noninteger factors is at most

    L=J-v_p(B).

If L<0 there is no factorization for this u. Otherwise enumerate all basis
arrays with coefficients below a and weights mi+kj<=L, apply the atom oracle,
and retain factors whose complementary target lies in S. This is a finite
catalog containing every possible noninteger factor. Integer-atom count is
at most floor(log_2 B), and the positive-weight factor count is at most L.
Finite enumeration now lists exactly all atomic factorizations.

The algorithm does not decide all atom divisors of x: a divisor can have a
cofactor that admits no atomic factorization and therefore never occur in
these lists. This is why no IDF inference is made.

## 3. Non-atomicity

Choose another denominator prime s!=p. The positive ratios p^M/s^N are dense
near1 after imposing arbitrarily strong congruences modulo powers of a.
Consequently there are P-smooth h in S with

    1<h<2, v_p(h)>0.

For example use h congruent1 modulo a^L and h=1+q^L*y with y>C.

Any atom appearing in a factorization of h is P-smooth, since outside-P
valuations cannot cancel. It cannot be q, whose numerator primes lie outside
P. Every other atom exceeds1, so no integer atom at least2 can occur in a
product less than2. Each remaining noninteger atom has negative p-adic
valuation by section2, contradicting v_p(h)>0. Thus h has no atomic
factorization and the monoid is non-atomic.

This argument does not assert that h has no atom divisor.

## Example and relationship to stronger special cases

The pair q=3/100,r=11/10 satisfies the one-good-block hypotheses via p=5,
although its2-block is below3. It is covered by this theorem. The separate
Boolean forcing identity2=r+30q proves the stronger IDF conclusion for this
particular pair; that extra conclusion does not follow from the present
one-good-block argument alone.
