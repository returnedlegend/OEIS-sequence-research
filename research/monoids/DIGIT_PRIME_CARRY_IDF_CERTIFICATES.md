# Prime-carry certificates for finite-digit IDF theorems

This note removes the valuation-separation hypothesis from the primitive-
residue family whenever finite exact carry certificates are available. It
also proves N_0[7/60^m,61/60] minus{0} is IDF and non-atomic for EVERY m>=2,
improving the direct valuation argument's sufficient threshold m>=6.
Novelty relative to the full discussion remains unverified.

## 1. Finite digits without denominator separation

Keep the primitive-residue setup and the first two carry/conductor
inequalities from PRIMITIVE_RESIDUE_MIXED_IDF_FAMILY.md, but replace its
third sufficient inequality by the exact requirement that every digit carry
(d_i+d_j-d_(i+j))/q and(d_i*d_j-d_(ij))/q belongs N_0[q]. These finitely
many memberships are decidable by the cyclic digit algorithm. Omit the
valuation-separation inequality. Thus ell>=3 is prime, q=ell/b^m, R=Z[1/b], |P(b)|>=2, r>1 has
primitive nonzero residue modulo ell, D={0,1,r,...,r^(ell-2)}, and

    S=disjoint-union_(d in D)(d+qS),
    C=max(D)/(1-q)<2, r^(ell-1)>C,
    R intersect(C,infinity) subset S.                     (1)

Every atom has a finite D-word expression, by the same excessive-block
perturbation: a block containing r^(ell-1) exceeds C, as does a block with
two nonzero monomials. The finite-word assertion for atoms therefore needs
no denominator-depth or cycle assumption.

## 2. All critical S-elements are finite words: a positive-block argument

Let P_N(x) be the canonical N-digit prefix and F(x)=lim P_N(x) for x in S.
Besides the usual multiplicative inequality, the same prefix-congruence
argument proves

    F(x+y)<=F(x)+F(y),  F(q^i*x)=q^i*F(x),  0<=F(x)<=C.    (2)

For the first inequality, x+y and P_N(x)+P_N(y) have the same first N
digits, whose sum is at most P_N(x)+P_N(y). The second follows from i
initial zero digits. Criticality (all tails bounded by C) is equivalent
to F(x)=x, and the multiplicative inequality makes it divisor-closed.

Suppose a critical S-element had a polynomial representation with a
q-degree block c>C. Write x=G+q^i*c, with G,c in S. Then(2) gives

    F(x)<=F(G)+q^i*F(c)<G+q^i*c=x,

a contradiction. Thus EVERY polynomial q-block of a critical S-element
is at most C. The two exclusions in section1 force every block to be a
digit in D, proving that every critical S-element is a finite D-word.
This rules out nonzero bounded canonical cycles inside S without having
to enumerate a potentially large residual grid.

## 3. Exact membership with possible canonical cycles

Let H bound the b-depth of the digits. A canonical step from depth h has
successor depth at most max(0,max(h,H)-m). Therefore all states at most C
lie in a finite set of bounded denominator and bounded real value.

Canonical iteration rejects negative states, accepts nonnegative integers
and states STRICTLY above C, and rejects a repeated nonzero bounded state.
The last rejection is valid by section2: a member in a bounded cycle would
be critical, hence a finite word whose canonical orbit reaches0. This gives
exact terminating membership even when denominator depth can stall.

Strictness matters: after dropping denominator separation, C might itself
belong R but not S. In that event its maximal-digit fixed orbit is rejected;
it must not be accepted just because it equals the real threshold.

## 4. Finite prime-carry certificates

Fix p|b and write v_p(q)=-e<0. Put

    mu=min{v_p(d): d in D, d!=0},  T=mu+e.

If v_p(x)<T, then v_p(qx)<mu, so every digit prefix has

    v_p(d+qx)=v_p(x)-e<T.                                 (3)

This is an absorbing lower-valuation region. A finite word whose valuation
is at least T must therefore be built entirely above that threshold,
starting from a nonzero digit with valuation at least T.

A p-certificate is a finite set E_p of positive rationals such that:

* it contains every nonzero digit d with v_p(d)>=T;
* every member has valuation at least T;
* for every x in E_p and d in D, either v_p(d+qx)<T or d+qx belongs E_p.

All these conditions are finite exact rational checks. They imply the
all-height bound

    v_p(x)<=M_p=max(0,T-1,max_{z in E_p} v_p(z))            (4)

for every positive critical S-element. An empty E_p is permitted, omitting
its maximum. A search that hits a state-count cutoff is inconclusive;
only a fully closed and independently verified set is used as a theorem.

## 5. IDF, atomlessness near1, and all factorization algorithms

Suppose a certificate exists at every denominator prime, and put

    W=product_(p|b) p^M_p.

For fixed x, let X be its numerator with denominator-prime factors removed.
Every atom divisor other than q is greater than1, and (4) bounds its reduced
numerator by divisibility into W*X. Its P-smooth denominator is therefore at
most its numerator. This finite list, together with q, proves IDF.

In particular there are only finitely many possible P-smooth atoms: their
numerators divide W and their denominators are at most their numerators.
All of them exceed1. Near-one P-smooth elements of S exist by the usual dense
congruence construction h=1+q^L*y with y>C. Choose such an h smaller than
every candidate smooth atom greater than1. Any atom divisor of h would be
smooth, because outside-P valuations cannot cancel; its smooth cofactor is
at least1, forcing the atom to be at most h. This is impossible. Therefore
there are atomless elements arbitrarily close to1, and S is non-atomic.
If W=1, there are no smooth atoms at all, so every nonunit smooth element
is atomless.

For a critical x, every divisor y is critical, has numerator dividing W*X,
and satisfies y>=q^(v_ell(y))>=q^(v_ell(x)). Thus all divisors are in the
finite list with P-smooth denominator at most numerator/q^(v_ell(x)).
Exact membership filters the list and decides irreducibility. Noncritical
members have a tail>C and are perturbably reducible. This gives a complete
atom oracle, then complete atom-divisor lists. The q-copy count is v_ell(x)
in any atomic factorization, while all other atom factors exceed1; a finite
real-product bound gives all atomic factorizations.

## 6. Application: every pair(7/60^m,61/60), m>=2

Take ell=7, b=60, r=61/60. Its residue3 modulo7 is primitive. The digit set
is{0,1,r,r^2,r^3,r^4,r^5}. The smallest positive digit carry difference is

    eta=(61^6-60^6)/60^6=4864374361/46656000000.

All three carry/conductor inequalities already hold at m=2 and remain true
as m grows. Thus(1)–(3) apply for every m>=2, and every atom is a finite word.
The direct valuation-separation theorem covers all m>=6.

For m=2,3,4,5 use the exact certificates in the accompanying JSON. Since
v_p(r)=-v_p(60), their thresholds are T_p=(m-5)*v_p(60). The sizes are

| m | p=2 | p=3 | p=5 |
|---|---|---|---|
|2|32|17|17|
|3|4|3|3|
|4|2|2|2|
|5|1|1|1|

Every listed set is closed under ALL retained digit prefixes. Their maximum
valuations are0, so W=1. This proves IDF, non-atomicity, and atomlessness of
every nonunit{2,3,5}-smooth element for all these parameters as well.
At p=3 and p=5 the only nonnegative-valuation state is1, so every atom has
negative valuations there. Hence no positive integer greater than1 admits
an atomic factorization, for every m>=2.

The smallest new pair is

    q=7/3600, r=61/60.

Both generators are atoms. The additional atom

    q+r^2=233/225

has2-adic valuation0; it is the only nonunit critical state of nonnegative
2-adic valuation at m=2. The complete atom oracle certifies its atomhood.
The integers2,3,5 are atomless, while7 has q as its sole atom divisor and
has no atomic factorization. This pair has denominator blocks4,3,5 all
below the numerator7, and the residue3 of r excludes the Boolean forcing
identity2=r+Kq with K in R.

The same certificate implementation also covers the earlier pair(5/36,7/6):
its exceptional small carry25/6=30q passes the exact membership check even
though it falls below the cyclic conductor. It also covers(3/230,7/5) by
using ell=3,b=230,m=1; its5-certificate is exactly the six-state nearby-family
certificate. Thus these examples instantiate one common proof and algorithm.
The original pair(3/10,7/5) still fails the strict conductor-below2 condition.

## 7. Reproducibility and attribution

The finite certificates are stored in primitive_7_60_carry_certificates.json.
The helper digit_prime_carry.py independently verifies the seed, threshold,
and closure conditions. The class in certified_primitive_residue.py combines
these certificates with exact membership, atom, and factorization algorithms.

The prefix method builds on ppdppd's supplied October24 argument; the
conductor and smooth-perturbation methods build on the earlier discussion.
The finite closed graphs are proofs of all-height valuation bounds, rather
than finite-height numerical evidence. No general termination theorem for
an arbitrary prime-carry search is claimed.
