# An IDF/non-atomic family adjacent to (3/10,7/5)

This is a separate parameter family; it does not settle IDF for the original
pair(3/10,7/5). Novelty relative to the full discussion is unverified.

## Theorem

Let n be a positive integer satisfying

    n>2,   gcd(n,21)=1,
    5n has at least two distinct prime divisors,
    n is not congruent to1 modulo5.                        (1)

Put

    q=3/(5n),   r=7/5,   S=N_0[q,r],   R=Z[1/(5n)],
    P={p:p|5n}.

Then S minus {0} is IDF and non-atomic. More strongly:

* every atom has strictly negative5-adic valuation;
* every atom has nonpositive valuation at every prime in P;
* there are no P-smooth atoms, so every nonunit P-smooth S-element has no
  atom divisor;
* no positive integer greater than1 admits an atomic factorization.

For example n=4 gives the genuinely mixed, multiplicatively independent,
nonredundant pair

    (q,r)=(3/20,7/5).

Its monoid is IDF and non-atomic, and both2 and5 have no atom divisor.
The case n=2 is exactly the original pair(3/10,7/5); the proof deliberately
excludes it, and its IDF status is not claimed here.

## 1. An exact digit system

Let D={0,1,r}. Since gcd(n,3)=1, the ideal qR equals3R, and the digits have
distinct residues0,1,2 modulo3R. Write d for the least positive residue
of n modulo3, so d is1 or2, and put

    K=n*(8n-5d)/3.

This is a nonnegative integer. Direct identities give

    1+1 = r+nq,
    1+r = 4nq,
    r+r = 1+3nq,
    r^2 = 1+dq+Kq^2.                                      (2)

They show D+qS is closed under addition and multiplication. It contains
0,1,q,r and is contained in S, hence

    S=qS disjoint-union (1+qS) disjoint-union (r+qS).        (3)

Consequently, if d(x) is the digit with x=d(x) modulo3R, then

    x in S iff (x-d(x))/q in S.                            (4)

## 2. A conductor strictly below2

Set

    C=r/(1-q)=7n/(5n-3).

The assumptions imply n>=4, so

    1<r<C<=28/17<2<1+r,
    r^2=49/25>C.                                          (5)

Every x in R with x>=C belongs S. Represent x=N/(5n)^L. For L>=1,
choosing d(x) in D and dividing by q reduces the allowed denominator
exponent by one: the digit denominator5 divides5n, and the congruence
cancels the numerator factor3. Moreover

    (x-d(x))/q >= (C-r)/q = C.

Induction ends at a nonnegative integer and proves

    R intersect [C,infinity) subset S.                     (6)

The units are {1}. Every positive P-smooth S-element is at least1:
if x<1, a polynomial expression cannot contain a term of q-degree0,
since r>1; every remaining term has positive3-adic valuation. A unit
and its inverse are P-smooth and hence both at least1.

## 3. Perturbing an excessive block

Because |P|>=2, choose P-smooth h_L tending to1 from above with
h_L-1 in3^L R and

    1+Cq^L<h_L<1+(C+1)q^L.

The standard dense congruence subgroup construction and (6) give h_L in S.
If x=F+q^i*c with F in S, c in R and c>C, then for L>=i,

    z_L=(x/h_L-F)/q^i

belongs R and tends to c>C. Eventually z_L is in S by (6), so
x=h_L*(F+q^i*z_L) is a nontrivial factorization after avoiding h_L=x.
Thus an atom cannot have any such block c>C in a polynomial expression.

## 4. Every atom has a finite digit expression with digits0,1,r

Consider a nonnegative polynomial expression for an atom alpha. A monomial
q^i*r^j with j>=2 is impossible: r^j>=r^2>C, so section3 applies to that
entire block. Thus the expression has r-degree at most1. Group it by
q-degree, with coefficients A_i+B_i*r.

By (5), any A_i>=2, any B_i>=2, or simultaneous A_i,B_i>=1 makes this
coefficient greater than C. Consequently every atom has an expression

    alpha=sum_(i=0)^N d_i*q^i,
    d_i in{0,1,r},   d_N!=0.                               (7)

An atom below1 must be q: (3) forces its first digit to0, giving
alpha=q*y with y in S; atomicity then forces y=1. Hence every atom other
than q is at least1.

## 5. Valuations at primes dividing n other than5

Fix p|n with p!=5. The assumption gcd(n,21)=1 ensures p divides neither3
nor7. Thus each nonzero digit in (7) is a p-adic unit, while

    v_p(q)=-v_p(n)<0.

The highest-index term has the unique least valuation. Therefore

    v_p(alpha)=-N*v_p(n)<=0.                              (8)

## 6. The5-adic valuation is always negative

Put f=v_5(5n)>=1. The nonzero digit valuations are v_5(1)=0 and
v_5(r)=-1.

If the highest digit d_N is r, its term has valuation-fN-1 and the
minimum is unique, so v_5(alpha)=-fN-1<0.

Suppose d_N=1. The case N=0 is the unit1, so N>=1. The highest term has
valuation-fN. If f>=2, every lower term has larger valuation, giving
v_5(alpha)=-fN<0.

If f=1, the only possible competing term is rq^(N-1). When present,
combine it with q^N:

    q^N+rq^(N-1)=q^(N-1)*(3+7n)/(5n).

The congruence assumption n!=1 modulo5 is exactly what makes3+7n nonzero
modulo5. The combined term therefore still has valuation-N; all remaining
terms have larger valuation. If the competing term is absent, the minimum
was already unique. In both cases v_5(alpha)=-N<0.

This proves the first two conclusions of the theorem.

## 7. IDF and atomless integers

Fix x in S, and let X be the part of its reduced numerator supported
outside P. Every atom alpha has reduced numerator supported outside P,
by (8) and section6. If alpha divides x, that numerator divides X, since
all outside-P valuations are nonnegative throughout S.

For alpha!=q, section4 gives alpha>=1. Write alpha=A/B in lowest terms.
Then A divides X and B<=A; also B is supported on P. There are only
finitely many such pairs(A,B). The possible exceptional atom q adds at
most one value. This proves IDF.

No atom is P-smooth. Indeed its reduced numerator would then be1. If it
is not q, its value would be at most1, contradicting alpha>=1 and the fact
that1 is a unit; q itself has numerator3 outside P. Thus a P-smooth element
has no atom divisor: any divisor atom would also be P-smooth, because
outside-P valuations cannot cancel.

Every finite product of atoms has negative5-adic valuation, whereas each
positive integer has nonnegative5-adic valuation. Hence no integer greater
than1 has an atomic factorization. In particular the monoid is non-atomic.

## 8. Why this does not answer the original n=2 case

For n=2 the same digit system has conductor C=2, exactly at the boundary.
The digit2 is no longer an excessive block, and the relation

    2=r+2q

does not expose a block greater than C. In fact2 is an atom, as established
in the supplied discussion. Its positive2-adic valuation prevents the
outside-P numerator bound used in section7. The IDF question at n=2
therefore remains open in these notes.

The congruence exclusion also matters. At n=46, for example,
q+r=65/46 is an atom with positive5-adic valuation. Indeed q+r<2 and
q+r<r^2, so the q-degree-zero portion of any polynomial representing it
is among0,1,r. Its residue modulo3R forces that portion to be r. The
remaining polynomial divided by q represents1, whose only nonnegative
polynomial representation is the constant1. Thus X+Y is the unique
polynomial representing q+r, and its formal irreducibility proves the
atom claim. The blanket nonpositive-valuation assertion therefore fails
in the omitted congruence class. No IDF claim is made for that subfamily.

## 9. Explicit identities at the smallest new example

For n=4, q=3/20 and r=7/5,

    2=r+4q,
    1+r=16q,
    2r=1+12q,
    r^2=1+q+36q^2,
    C=28/17.

All identities are exact. The generators are nonredundant: q<1 excludes
q in N_0[r], while r has least residue2 modulo3R, exceeding its real value,
so it cannot belong N_0[q]. They are multiplicatively independent because
v_7(q)=0 and v_7(r)=1, followed by q!=1. Their effective denominator primes
are2 and5, and the numerator prime3 is not effective. Thus this example
lies in the mixed independent region specified in Open Problem2.

## 10. Critical elements form a divisor-closed set

This section uses the prefix/digit-limit method explained by ppdppd in the
October24 post supplied by the user. Its application to this parameter family,
and the ensuing finite algorithms, are proved here; the method itself is not
claimed as new.

For x in S let P_N(x) be its first N canonical digits and define

    F(x)=lim_(N->infinity) P_N(x).

The prefixes increase and are bounded above by x. If x>0, then F(x)>0:
otherwise every digit would vanish, putting x in3^N R for every N, impossible
for a nonzero rational. Prefixes are determined by residue modulo3^N R, since
qR=3R. For x,y in S,

    xy-P_N(x)*P_N(y) belongs q^N S subset3^N R.

Thus the two products have the same first N digits, and

    P_N(xy)=P_N(P_N(x)*P_N(y))<=P_N(x)*P_N(y).

Taking limits gives

    F(xy)<=F(x)*F(y)<=xy.                                  (11)

Call x critical if every canonical iterate tau^j(x) lies in[0,C]. Denominator
clearing reaches a nonnegative integer; because C<2, a critical orbit reaches
0 or1, then0. Conversely every finite D-digit expression has all its suffixes
at most sum_(j>=0) r*q^j=C. Therefore the following are equivalent:

* x is critical;
* x has a finite expression with digits in D;
* F(x)=x.

For the final equivalence, an orbit leaving[0,C] has a tail c>C, while its
remaining digit sum is at most C, so F(x)<x. If xy is critical and x,y>0,
(11) forces F(x)=x and F(y)=y. Hence the critical elements are divisor-closed.
All atoms are critical by section4; alternatively a noncritical tail c>C
makes an element reducible by section3.

## 11. An exact terminating atom test

The valuation arguments in sections5 and6 apply to every nonunit finite
digit expression, not just atoms. Thus each nonunit critical element has
nonpositive valuations at all denominator primes, and strictly negative
5-adic valuation. Its reduced numerator is coprime to5n.

Every x in S satisfies

    x>=q^(v_3(x)).                                        (12)

Indeed, (3) gives x in qS exactly when v_3(x)>0. Strip precisely v_3(x)
factors q. The residual element has residue1 or2 and is at least1.

Fix critical x>0, write x=X/Y in lowest terms, and put E=v_3(x). Any divisor
y of x is critical. Its reduced numerator A divides X, since denominator
primes have nonpositive valuations on both y and x/y and all other primes
have nonnegative valuations. Also v_3(y)<=E, so (12) gives y>=q^E. Writing
y=A/B in lowest terms, we obtain

    A divides X,   B is P-smooth,   B<=A/q^E.               (13)

This is a finite, explicitly enumerable list containing EVERY divisor of x.
For each candidate, use the canonical membership test on y and x/y. Excluding
y=1 and y=x, the existence of a surviving candidate is exactly reducibility.
If no candidate survives, x is an atom. A noncritical x is already reducible,
and1 is a unit. This gives an exact terminating atom test on the whole monoid.
It also shows every critical element has only finitely many divisors and hence
is atomic, despite non-atomicity of the full monoid.

The element q is an atom: in q=yz, at least one factor is below1, hence is a
multiple of q by (3); cancellation then makes the other factor a unit.

## 12. All atom divisors and all atomic factorizations

For an arbitrary x in S, remove all primes in P from its numerator to obtain
X. Section7 gives the complete finite atom-candidate list

    {q} union {A/B: A divides X, B is P-smooth, B<=A}.

Apply the atom test of section11 and check x/(A/B) in S. The resulting list
is precisely the atom-divisor set of x.

Every atom has integer5-adic valuation at most -1. Consequently an atomic
factorization of x has length at most -v_5(x). Enumerate nondecreasing lists
from the finite atom-divisor set, retaining only products equal to x and
pruning whenever the remaining cofactor leaves S. This is a terminating
algorithm for ALL atomic factorizations, including certification that no
such factorization exists. For x=1 the only factorization is empty.

The implementation nearby_ternary_factorizations.py uses only exact integer
and rational arithmetic. For n=4 it gives:

| x | complete atom-divisor set | all atomic factorizations |
|---|---|---|
|2|empty|none|
|3|{3/20}|none|
|5|empty|none|
|7|{7/5}|none|
|7/5|{7/5}|7/5|
|31/20|{31/20}|31/20|
|49/25|{7/5}|(7/5)^2|
|21/100|{3/20,7/5}|(3/20)(7/5)|

These finite outputs illustrate the proved algorithms; they are not being
used as a substitute for the all-height proofs above.
