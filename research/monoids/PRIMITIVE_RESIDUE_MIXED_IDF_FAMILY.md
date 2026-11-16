# Primitive-residue digit families with IDF and non-atomicity

This theorem is independently derived from the finite-digit method used
for N_0[5/6^m,7/6]. Novelty relative to the supplied discussion and the
literature has not been established. The denominator ring is allowed to
contain primes dividing the numerator of the second generator.

## Exact hypotheses

Let ell>=3 be prime, let b>=2 be coprime to ell and have at least two
distinct prime divisors, and write R=Z[1/b], P={p:p|b}. Choose r in R with

    r>1, r^(ell-2)<2,
    r mod ell R a primitive element of F_ell^*.

In particular r is a unit modulo ell and is nonintegral. Put

    D={0,1,r,r^2,...,r^(ell-2)}, Dmax=r^(ell-2).

Label each digit by its residue in F_ell. For each pair of digits let
delta_add=d_i+d_j-d_(i+j) and delta_mul=d_i*d_j-d_(ij), with residues
interpreted modulo ell. Every such delta is nonnegative. Let eta be the
minimum of the finitely many positive deltas.

Choose an integer m>=1, put q=ell/b^m, and impose the following finite,
exactly checkable inequalities:

    q<1-Dmax/2,
    q<1-1/r,
    eta/q >= (ell-1)/(1-q),                              (1)

and, for every p in P with e_p=v_p(b),

    m*e_p > (ell-2)*abs(v_p(r)).                         (2)

All these conditions hold for every sufficiently large m. Define

    S=N_0[q,r], C=Dmax/(1-q)<2.

**Theorem.** The multiplicative monoid S minus{0} is IDF and non-atomic,
with trivial unit group. No positive integer greater than1 has an atomic
factorization. Exact membership, criticality, atoms, all atom divisors,
and all atomic factorizations admit terminating finite algorithms.
The pair q,r is multiplicatively independent and nonredundant.

If r has numerator coprime to b in reduced form, there are no P-smooth
atoms, so every nonunit P-smooth S-element is atomless. In the general
ambient-ring case, the P-smooth atom set is exactly{r} when r is P-smooth,
and is empty otherwise.

## 1. Why the digit carries are nonnegative

The powers1,r,...,r^(ell-2) represent every nonzero residue exactly once.
For two nonzero digits, their sum is at least2, while every digit is below2;
thus the sum delta is strictly positive. A pair involving0 is immediate.

For products, if their exponent sum is below ell-1, the matching digit is
exactly their product. Otherwise reduction of the exponent modulo ell-1
gives a positive difference of the form

    r^j*(r^(ell-1)-1).

Thus eta exists and is positive. By the cyclic conductor
C_0=(ell-1)/(1-q), condition(1) puts every nonzero carry delta/q in
N_0[q]. The set D+qS is therefore closed under addition and multiplication,
contains0,1,q,r, and equals S. Distinct digit residues give the exact
disjoint decomposition

    S = disjoint-union_(d in D)(d+qS).                   (3)

In particular qS=S intersect ell R.

## 2. Canonical termination and the smaller conductor

For x in R choose its residue digit d(x) and set tau(x)=(x-d(x))/q.
Condition(2) implies that every digit has b-depth at most m. A nonintegral
state of depth h therefore has successor depth at most

    max(0,max(h,m)-m)<h.

Canonical iteration reaches an integer, so exact membership is decidable:
reject negative tails; a nonnegative integral terminal is in S; and (3)
proves completeness for S-elements.

Since every digit is at most Dmax,

    tau(x)-C >= (x-C)/q.

An x>C remains positive under iteration and eventually reaches C_0, whose
membership is known. Therefore R intersect(C,infinity) is contained in S.
In fact C is not in R: if it were, tau(C)=C because C-Dmax=qC and the
digit residues are distinct. This would be a nonintegral fixed state
(1<C<2), contradicting the strict depth decrease. Hence

    R intersect[C,infinity) subset S.                   (4)

Call x critical if its entire canonical orbit stays in[0,C]. The strict
depth decrease and C<2 show that these are exactly the finite D-words,
equivalently the members with first integral terminal0 or1.

## 3. Atoms use finite digit words

Near-one P-smooth congruence perturbations apply because |P|>=2. A
representation x=F+c*q^i*r^j with c in R and c>C is reducible: choose
P-smooth h in S approaching1 and congruent to1 modulo enough powers of
ell and the numerator of r; then

    (x/h-F)/(q^i*r^j)

belongs R and remains above C. Formula(4) gives a nontrivial factorization.

By(1), r^(ell-1)>C. Thus an atom cannot have an r-power at least ell-1 in
any q-degree block. Two nonzero monomials in the same block have total
value at least2>C and are likewise forbidden. Every atom consequently
has a finite D-word representation and is critical.

Every positive S-element below1 lies in qS, because all nonzero digits
are at least1. Its ell-adic valuation is positive, so it cannot be a unit.
A unit and its inverse are both at least1, proving that the only unit is1.
Cancellation then shows q is an atom, and every other atom is greater
than1 and has ell-adic valuation0.

The element r is also always an atom. Since r<2, the q-free block of any
polynomial representing r can only be0,1, or r: two nonzero monomials
exceed r, as does every power r^j with j>=2. Its residue g>=2 excludes0
and1, forcing the block r and leaving no other positive term. Thus Y is
the unique polynomial representation of r and is irreducible.

## 4. Highest-degree valuation separation

For p in P, write v=v_p(r). Digit valuations range between

    Vmin=min(0,(ell-2)*v), Vmax=max(0,(ell-2)*v).

Condition(2) says m*e_p>Vmax-Vmin. In a finite D-word with highest
q-degree N>=1, the highest term has valuation at most -m*e_p*N+Vmax.
Every lower term has valuation at least -m*e_p*(N-1)+Vmin, which is
strictly larger. Hence there is no cancellation, and

    v_p(x)=-m*e_p*N+v_p(d_N)<0                         (5)

for every p in P. A degree-zero critical value is one of the digits r^j.
The only possible nonunit atom of degree zero is r itself, because
r^j=r*r^(j-1) for j>=2.

Thus every atom other than possibly r has strictly negative valuation
at every denominator prime. For all positive critical values, including
degree-zero ones, positive p-adic valuations are bounded by Vmax.

## 5. IDF and failure of atomicity

Fix x in S and let X be the part of its reduced numerator supported
outside P. An atom divisor alpha other than q and r has reduced numerator
N coprime to b by(5). Outside-P valuations cannot cancel in the cofactor,
so N divides X. Since alpha>1, its P-smooth denominator B satisfies B<N.
There are finitely many possibilities. Adjoining q and r proves IDF.

Because1<r<2 and r is nonintegral, there is an actual denominator prime
p_0 in P with v_(p_0)(r)<0. Every atom has negative valuation at p_0,
including the possible exception r. Therefore no positive integer greater
than1 can be a product of atoms. This proves non-atomicity.

For a P-smooth atom other than q,r, its reduced numerator would be1, so
its value would be below1, impossible. The atom q is not P-smooth because
ell is outside P. Thus r is the only smooth atom when it is P-smooth, and
otherwise there are none. If the reduced
numerator of r is coprime to b, then r is not P-smooth either, proving the
stronger atomlessness assertion.

## 6. Complete finite algorithms

The canonical-prefix inequality attributed to ppdppd in the user-supplied
October24 discussion gives a divisor-closed critical set; that method is
not claimed as new here.
For clarity, if P_N(x) is the first N-digit partial sum and F(x) its limit,
then xy-P_N(x)P_N(y) belongs q^N S, hence the two products have the same
first N digits. Thus F(xy)<=F(x)F(y)<=xy. Also F(x)>0 for x>0, and
criticality is equivalent to F(x)=x. It follows that every divisor of a
critical element is critical.

Put

    W=product_(p in P) p^(max(0,(ell-2)*v_p(r))).

If y divides a critical x, its reduced numerator divides W*X. Repeatedly
using qS=S intersect ell R gives y>=q^(v_ell(y))>=q^(v_ell(x)). Therefore
every such divisor lies in the finite list

    {N/B : N divides W*X, B is P-smooth,
           B<=N*q^(-v_ell(x))}.

Exact membership of y and x/y filters the actual divisors. A noncritical
member has a canonical tail>C and is reducible by perturbation; a critical
member has the finite divisor test. This is a complete atom oracle.

For arbitrary x, filter q,r and the finite list N/B with N|X and B<=N
using that oracle and cofactor membership. This gives all atom divisors.
In any atomic factorization the number of q factors is exactly v_ell(x),
since all other atoms have ell-adic valuation0. After removing those
copies, every remaining atom is greater than1 and belongs to a finite
list. Its smallest value supplies an exact real-product length bound.
Finite multiset enumeration therefore decides and lists every complete
atomic factorization, including an empty list for a non-atomic element.

## 7. Independence, nonredundancy, and examples

In a multiplicative relation q^u*r^v=1, the ell-adic valuation forces u=0,
and r>1 then forces v=0. Thus the pair is multiplicatively independent.
The least residue of r modulo ell is a primitive element, hence an integer
g>=2. Since r<2, the cyclic membership digit test excludes r from N_0[q].
Also q<1 excludes q from N_0[r].

The family5/6^m,7/6 fits with ell=5,b=6 and primitive residue2. The uniform
valuation inequalities above give m>=4; the separate finite carry
certificates sharpen this to m>=2.

An example whose second-generator residue is NOT2 is

    ell=7, b=60, r=61/60, q=7/60^m, m>=6.

Here r mod7=3 is primitive, r^5<2, and the denominator blocks4,3,5 are all
below7. The positive carry and conductor inequalities are satisfied already
at m=6 and remain valid as m increases. Boolean forcing from an identity
2=r+Kq with K in R is unavailable because r has residue3 rather than2.
The theorem nevertheless proves IDF, non-atomicity, and atomlessness of
all nonunit{2,3,5}-smooth elements.

For the ambient-ring variant, ell=3,b=10,r=7/5 satisfies the conditions
for every m>=2, yielding q=3/10^m. The second generator has zero valuation
at2, so treating it as a finite exceptional atom is necessary; requiring
its reduced numerator and denominator both to use every prime of b would
unnecessarily exclude this example.

More generally, fix ell and any denominator-prime support P disjoint from
ell. Let B_0 be the product of these primes and take b=B_0^t sufficiently
large. Choose a primitive residue g and an integer s satisfying

    s=1 mod B_0,  s=(g-1)b mod ell,  1<=s<=ell*B_0.

Then r=(b+s)/b is reduced, has primitive residue g, and approaches1 as t
increases; hence r^(ell-2)<2 eventually. All sufficiently large m then
satisfy(1)-(2). This is an existence construction with exactly the chosen
denominator-prime support, not a claim of novelty for that existence fact.
