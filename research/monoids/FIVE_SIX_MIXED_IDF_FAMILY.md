# The family N_0[5/6^m,7/6] is IDF and non-atomic for every m>=2

These results are independently proved below. Novelty relative to the full
online discussion has not been established. The cyclic monoid N_0[5/6]
and the mixed pair(5/6,7/6) are not settled by this theorem.

## Theorem

For every integer m>=2, put q=5/6^m, r=7/6, and S_m=N_0[q,r]. Then the
multiplicative monoid S_m minus{0} is IDF and non-atomic, with trivial units.
The only positive integer admitting an atomic factorization is1.

For m>=3 there are no{2,3}-smooth atoms, so both2 and3 are atomless.
For m=2 the unique{2,3}-smooth atom is3/2=q+r^2. The integer2 is atomless,
while3=(3/2)*2 has an atom divisor but no atomic factorization.

All atom divisors and all atomic factorizations are decidable by finite,
exact algorithms. In particular the example(5/36,7/6) is covered, despite
both denominator primes being smaller than the numerator5.

## 1. A five-digit system

Let R=Z[1/6]. Use digits in residue order modulo5R:

    d_0=0, d_1=1, d_2=r, d_3=r^3, d_4=r^2.

At m=2, the carries for unordered nonzero digit pairs are as follows. The
sum carry is(d_i+d_j-d_(i+j mod5))/q; the product carry is
(d_i*d_j-d_(ij mod5))/q.

| i,j | sum carry | product carry |
|---|---|---|
|1,1|6|0|
|1,2|25/6|0|
|1,3|53/6|0|
|1,4|17|0|
|2,2|7|0|
|2,3|119/6|221/36|
|2,4|11|0|
|3,3|47/3|10829/1296|
|3,4|77/6|1547/216|
|4,4|49/6|221/36|

The cyclic conductor is C_0=4/(1-q)=144/31. Every nonzero carry in the
table exceeds C_0 except25/6, and25/6=30q belongs S_2. Pairs involving0
are immediate. Thus D+qS_2 is closed under addition and multiplication,
contains the generators, and equals S_2.

For general m>=2 every table carry is multiplied by6^(m-2). The cyclic
conductor decreases with m, so the large carries still belong N_0[q]. The
exceptional carry is an integer25*6^(m-3) when m>=3. Therefore, for EVERY
m>=2,

    S_m=disjoint-union_(d in D)(d+qS_m).                   (1)

The disjointness follows from the distinct residues modulo5R.

## 2. A conductor below2 and critical words

Put

    C_m=r^3/(1-q)<=343/186<2.

For the canonical map tau(x)=(x-d(x))/q,

    tau(x)-C_m >= (x-C_m)/q.

Thus any x in R strictly above C_m eventually reaches the larger cyclic
conductor C_0 under iteration; all preceding iterates remain positive.
Reverse application of(1) proves x belongs S_m. The boundary C_m is not in
R: for m=2 its denominator has the outside prime31; for m=3 the outside
factor is211; and for m>=4 the coprime-to6 denominator6^m-5 exceeds343.
Consequently

    R intersect[C_m,infinity) subset S_m.                 (2)

A near-one smooth perturbation shows that any representation containing a
q-degree block c>C_m is reducible. Also

    r^4>C_m,

because r*(1-q)>=217/216>1. Hence an atom cannot use an r-power at least4.
Within each q-degree block, two nonzero monomials would contribute at least2,
which also exceeds C_m. Every atom therefore has a finite D-digit expression.
An atom below1 must be q, since every S_m-element below1 lies in qS_m.

Call x critical when every canonical iterate lies in[0,C_m]. For m>=3,
denominator6-depth drops by m against digit depths at most3, so a bounded
orbit reaches a nonnegative integer, necessarily0 or1. For m=2 the depth
can stall at1, which needs an explicit check. The bounded residual states
are k/6, k=0,...,11, with the following canonical successors:

    0,-6,-6,-47/6,-5,6,0,0,-11/6,1,12,6.

Only0,1,7/6,3/2 survive bounded and nonnegative, and they all reach0
(3/2 goes to1). There is no nontrivial surviving cycle. Therefore critical
elements are EXACTLY the finite D-words, for every m>=2.

## 3. Criticality is inherited by divisors

Let P_N(x) be the first N canonical digits and F(x)=lim P_N(x). The standard
prefix argument from the supplied discussion gives

    F(xy)<=F(x)*F(y)<=xy.

Indeed xy-P_N(x)P_N(y) belongs q^N S_m subset5^N R, so the two products
have the same first N digits. Also F(x)>0 for x>0. Criticality is equivalent
to F(x)=x: bounded tails tend to0 after multiplication by q^N; a tail above
C_m has digit sum strictly smaller than itself. Thus every divisor of a
critical element is critical. This uses the prefix method attributed to
ppdppd in the supplied October24 discussion, rather than claiming that
method as new.

## 4. Two finite prime-carry certificates at m=2

Fix p=2 or3. Here v_p(q)=-2 and every digit has valuation at least-3.
If v_p(x)<=-2, then qx has valuation at most-4, strictly below every nonzero
digit. Therefore prefixing any digit keeps the valuation at most-2.

It follows that every critical value with v_p>=-1 is obtained from seeds
{1,r} by prefix maps x->d+qx that retain v_p>=-1. The other possible top
digits r^2,r^3 already have valuations below this threshold and cannot
recover. The following finite sets are closed under EVERY retained image:

    E_2={1,7/6,3/2,97/54,893/486,4031/2187,63659/39366},

    E_3={1,7/6,3/2,5/24,29/24,11/8,149/96,7/4,77/48}.

For p=2 the complete retained edges are

    1 --d_4--> 3/2
    3/2 --d_3--> 97/54
    97/54 --d_3--> 893/486
    893/486 --d_3--> 4031/2187
    4031/2187 --d_4--> 63659/39366.

For p=3 they are

    1 --d_4--> 3/2
    7/6 --d_3--> 7/4
    3/2 --d_0--> 5/24
    3/2 --d_1--> 29/24
    3/2 --d_2--> 11/8
    11/8 --d_4--> 149/96
    7/4 --d_4--> 77/48.

Every omitted image has valuation at most-2. These are exact rational
identities and divisibility checks, so the certificates apply at ALL heights.
The largest2-adic valuation in E_2 is0, and the largest3-adic valuation in
E_3 is1. Consequently EVERY positive critical element satisfies

    v_2(x)<=0,   v_3(x)<=1.                               (3)

Moreover the only nonunit critical element with v_2(x)=0 is4031/2187,
which has negative3-adic valuation.

## 5. The simpler valuation argument for all m>=3

For m=3, a suffix with negative p-adic valuation remains negative under
every prefix, for p=2,3: qx has valuation at most-4, below the digit minimum-3.
Only the top digit1 has nonnegative valuation. From1, the only potentially
cancelling prefix is r^3+q, and

    r^3+q=(343+5)/216=29/18,

which has negative valuation at both2 and3. All other prefixes have unique
least valuation from q. Thus every nonunit critical value has strictly
negative valuations at both denominator primes.

For m>=4 even this possible tie disappears: q has valuation at most-4,
whereas every digit has valuation at least-3. The same conclusion follows.

## 6. IDF and complete finite divisor bounds

Fix x in S_m and remove the prime factors2 and3 from its numerator to obtain
X. An atom divisor alpha!=q is greater than1. At m=2, (3) implies that its
reduced numerator divides3X. At m>=3, section5 makes that numerator divide X.
In either case its denominator is2,3-smooth and at most its numerator.
This is a finite list; adjoining the possible atom q proves IDF.

For a critical x every divisor is critical. Also qS_m=S_m intersect5R,
by(1), so every y in S_m satisfies y>=q^(v_5(y)). Hence a divisor y of a
critical x has numerator dividing3X (or X when m>=3) and denominator at
most numerator/q^(v_5(x)). Enumerating this finite list and testing exact
membership of y and x/y decides irreducibility. A noncritical element is
already reducible by perturbation. Thus the finite atom-divisor candidate
list can be completely filtered, not merely bounded.

Copies of q in an atomic factorization are bounded by v_5(x); every other
atom in the finite divisor list exceeds1. A real-product bound therefore
gives finite enumeration of all atomic factorizations.

## 7. Smooth atoms and non-atomicity

Positive{2,3}-smooth elements of S_m are at least1: an element below1 is a
multiple of q and has positive5-adic valuation. This also shows the unit
group is trivial.

At m=2, a critical smooth element lies in[1,C_2] and, by(3), has the form
2^u*3^v with u<=0,v<=1. The only possibilities are1 and3/2. The latter
belongs S_2 since3/2=q+r^2. Any nonunit divisor of it must be smooth and
critical, hence equal3/2; therefore3/2 is an atom and is the only smooth
atom. It does not divide2 because4/3 is not in S_2: its residue modulo5
selects the digit r^3>4/3. Thus2 is atomless. The integer3 cannot be a
product of smooth atoms, since no positive power of3/2 is an integer.

In fact no integer greater than1 has any atomic factorization. At m=2,
nonnegative2-adic valuation forces every factor atom to have2-adic valuation0.
The only possible nonunit critical value of that valuation is4031/2187,
whose3-adic valuation is negative; its positive powers are not integers.
At m>=3 every atom already has negative valuations at both2 and3.

For m>=3 there are no smooth atoms at all: both prime valuations would be
negative, making a smooth atom smaller than1, which is impossible. Thus
both2 and3 are atomless. This completes the theorem.

## 8. The boundary m=1 changes the atoms

For q=5/6,r=7/6, the integer2 is an atom. To prove this, consider any
nonnegative polynomial representing2. Its q-degree-zero part is a sum of
powers of r bounded by2. The only possibilities with residue2 modulo5R are
the constant2 and the single monomial r: powers r^2,r^3,r^4 have residues
4,3,1, respectively; r^5>2; and any sum involving r and another nonzero
monomial exceeds2. If the constant part is2, all remaining terms vanish.
If it is r, the remaining part is q, and dividing by q gives the unique
constant representation of1. Hence the only polynomial representations of2
are the constant2 and X+Y. Both are irreducible in N_0[X,Y], so a numerical
factorization would have a unit factor.

The element3/2 is not in this m=1 semiring. Its q-degree-zero part, bounded
by3/2 and with residue4 modulo5R, would have to be r^2. The remaining
quotient by q is1/6, which cannot belong S: an element below1 lies in qS
and has positive5-adic valuation, whereas1/6 has valuation0.

Thus the behavior of these two concrete elements is completely determined:

| parameter | integer2 | rational3/2 |
|---|---|---|
|m=1|atom|not in the semiring|
|m=2|atomless|atom|
|m>=3|atomless|atomless|

For the last row,3/2=r^2+6^(m-2)*q belongs S_m and is smooth, while there
are no smooth atoms. This sharp boundary for these elements does not
classify atomicity or IDF of the full m=1 monoid; those remain unproved here.
