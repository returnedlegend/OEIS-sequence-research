# Density-one IDF with a fixed composite denominator

This extends the prime-denominator density theorem. Novelty relative to
the full discussion and literature remains unverified. It does not assert
universal termination of the carry search or IDF for every parameter.

## Theorem and hypotheses

Fix integers D,A satisfying

    D>=4, gcd(3,D)=1, gcd(A,D)=1,
    D<A<2D, A=2D modulo3,
    p^(v_p(D))>3 for every prime p dividing D.             (1)

In particular a2-adic denominator block is allowed provided its exponent
is at least2. Fix r=A/D. For integers n with

    n>=4, gcd(n,3A)=1,
    n has at least one prime divisor outside D,            (2)

put q=3/(Dn) and M_n=N_0[q,r] minus{0}.

Every M_n in(2) is non-atomic: no positive integer greater than1 has an
atomic factorization. A subset of these parameters of relative natural
density ONE has finite carry certificates proving IDF. Hence the IDF
parameters themselves have relative density1. All pairs are multiplicatively
independent and nonredundant.

For N>=2, all but at most

    sum_[p|D] 3^(ceil(log_(p^(v_p(D))) N)-1)                (3)

admissible parameters n<=N have explicit finite-depth IDF certificates.
In particular this is at most omega(D)*N^theta, where

    theta=max_[p|D] log_(p^(v_p(D))) 3 <1.

The bound counts parameters not certified by that particular finite-depth
procedure; it does not count monoids known to fail IDF.

## 1. Uniform ternary digits and non-atomicity

Let R=Z[1/(Dn)] and use digits{0,1,r}, whose residues modulo3R are0,1,2.
Their four nontrivial carries after division by q are

    n*(2D-A)/3,
    n*(D+A)/3,
    n*(2A-D)/3,
    n*(A^2-D^2)/(3D).

The first three are nonnegative integers. The last is in R and exceeds
8/3, since A^2-D^2>2D and n>=4. On the other hand q<=3/16, so the cyclic
conductor2/(1-q) is at most32/13<8/3. Thus every carry is in N_0[q], giving
the exact disjoint digit decomposition

    S=qS disjoint-union(1+qS) disjoint-union(r+qS).

The conductor C=r/(1-q) satisfies C<2:2D-A is a positive multiple of3,
so n*(2D-A)>6. Also

    3A/[D(A-D)]=3/D+3/(A-D)<=15/4<4<=n,

so r^2>C. Canonical denominators clear in finitely many steps because the
digit denominator D divides Dn. Consequently the critical elements are
finite digit words, and excessive-block perturbations put every atom in
that class. Units are trivial, q is the only atom below1, and the other
atoms exceed1.

Choose a prime s|n with s not dividing D. Hypothesis(2) also gives s not
dividing3A, so every nonzero digit is an s-adic unit. A finite word of degree
h has v_s=-h*v_s(n). An atomic factorization of an integer would therefore
use only degree-zero atoms, whose only nonunit candidate is r. Its positive
powers are nonintegral because r has a genuine denominator. This proves
non-atomicity and the asserted integer-factorization exclusion for every
admissible n, independently of IDF.

## 2. One carry tree for each denominator prime

Fix p|D and e=v_p(D). If v_p(x)<0, then v_p(qx)<-e, below both nonzero
digit valuations0 and-e. Negative valuation is therefore absorbing under
all prefix maps d+qx.

Every p-integral critical element is generated from terminal1 by prefixes
that retain p-integrality. If p|n, all prefixes of1 immediately have negative
valuation, so the integral closure is{1}. If p does not divide n, the first
retained prefix must be r, and

    r+q=(A*n+3)/(D*n)

is p-integral exactly when A*n+3 is divisible by p^e.

Suppose this retained closure is finite for every p|D. Their finite union
contains every atom having nonnegative valuation at any prime dividing D.
At every other denominator prime s|n, s not dividing D, highest-degree
valuation is nonpositive as in section1. Thus an atom outside this finite
exception set has reduced numerator coprime to Dn. For any fixed target x,
that numerator divides the target's outside numerator; because every atom
other than q exceeds1, its denominator is at most its numerator. This is
a finite list. Adding q and the finite exceptions proves IDF.

## 3. Unique polynomial roots and density one

For p not dividing n, a construction word of length L starting from1 has
value H_w(n)/(Dn)^L, where H_w is an integer polynomial. Its first retained
digit r gives H_1=A*n+3. Later recurrences are

    H_new=3H,
    H_new=(Dn)^(L+1)+3H,
    H_new=A*n*(Dn)^L+3H.

For every word of positive length L beginning with r,

    H_w=3^(L-1)*(A*n+3) modulo p,
    H'_w=A*3^(L-1) modulo p,

and the derivative is a unit because p divides neither3 nor A. Therefore
H_w has exactly one root modulo p^(eL), by successive unique simple-root
lifts. A retained depth-L word must lie in that root class.

There are at most3^(L-1) words after the forced initial r. Hence parameters
with a retained depth-L word at p have upper density at most

    3^(L-1)/p^(eL).

Condition(1) makes this tend to0. Parameters with an infinite p-integral
closure have retained words at every depth, so they form a zero-density
set. Taking the finite union over p|D preserves density0. Every remaining
admissible parameter has all the finite closures required by section2,
and is IDF.

The admissible set has density phi(3A)/(3A)>0: integers coprime to3A have
that density, while integers supported only on the finite prime set P(D)
have density0. Thus the exceptional set has relative density0 as well.
The moduli p^(eL) are coprime to3A, so the same density estimates hold
conditionally on admissibility by the Chinese remainder theorem.

For the finite-range bound, use L_p=ceil(log_(p^e) N). Each root class modulo
p^(eL_p) contains at most one integer in[1,N]. A union bound over the at most
3^(L_p-1) word classes at each p gives(3). Outside that union every relevant
tree has finite bounded depth, yielding explicit certificates.

## 4. A new denominator4 instance and scope

Take D=4,A=5, so r=5/4 and q=3/(4n). The only block is2^2=4>3. For n>=4,
gcd(n,15)=1, and n having an odd prime divisor, the theorem gives non-atomicity
for every n and IDF for a relative-density-one set. The finite-range
exception bound is

    3^(ceil(log_4 N)-1) <= N^(log_4 3).

The first integral prefix can occur only when5n+3=0 modulo4, namely
n=1 modulo4. Every other residue class has a trivial closure and is
immediately IDF. This includes the concrete independent pair(3/28,5/4).

The3-adic valuation proves independence, and r has residue2>r modulo3R,
which proves nonredundancy. As in the prime case, no conclusion is drawn
about whether any remaining parameter actually fails IDF or has an infinite
tree. The prefix/conductor methods build on the supplied discussion; the
root-counting proof is given explicitly rather than asserting novelty
against unavailable source documents.
