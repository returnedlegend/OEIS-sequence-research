# Density-one IDF for arbitrary numerator and fixed upper digit

This is a proof of the stated family, not a novelty claim against the full
literature or the supplied discussion. The cyclic conductor and the
near-one smooth perturbation method build on the supplied discussion;
the parameter-counting argument is explicit below. No universal IDF or
universal carry-termination claim is made.

## Statement

Fix integers a,D,A satisfying

    a>=3, gcd(a,D)=gcd(A,D)=1,
    p^(v_p(D))>a for every p|D,
    (a-2)D<A<(a-1)D,  A=-D modulo a.                 (1)

In particular D>a. Put r=A/D. An admissible parameter n satisfies

    n>=max(a,4), gcd(n,a*A*(a-2)!)=1,
    n has a prime divisor outside P(D).              (2)

Set b=Dn, q=a/b, R=Z[1/b], and S=N_0[q,r]. Its nonzero multiplicative
monoid has trivial units. For every admissible n it is non-atomic, and
the pair (q,r) is multiplicatively independent and nonredundant.

A relative-density-one subset of the admissible parameters has explicit
finite carry certificates proving IDF. More quantitatively, for N>=2,
all but at most

    (a-2) sum_[p|D] a^(ceil(log_(p^(v_p(D))) N)-1)    (3)

admissible n<=N have certificates from a specified finite-depth test.
This is at most (a-2)*omega(D)*N^theta, where

    theta=max_[p|D] log_(p^(v_p(D))) a <1.

The exceptions in (3) are uncertified parameters, not parameters proved
to fail IDF.

The positive integers having an atomic factorization are exactly:

* products of ordinary primes at most a-2, if D has a prime divisor
  greater than a-2;
* products of ordinary primes at most a-2 and of A, if every prime divisor
  of D is at most a-2.

Empty products are allowed. In particular an ordinary prime greater than
a-2 and not dividing A has no atomic factorization.

The factorial in (2) is essential to the proof as stated: it makes every
ordinary nonzero digit an s-adic unit at every prime s|n. Omitting it
invalidates both the outside-D valuation argument and the asserted
triviality of the p-integral tree when p divides n.

## 1. Exact digit decomposition and conductor

Use the a digits

    E={0,1,...,a-2,r}.

They have distinct residues modulo aR, with r representing a-1. We use
the usual cyclic conductor: every element of R at least

    C_0=(a-1)/(1-q)

belongs to N_0[q]. This follows by the ordinary residues 0,...,a-1 and
denominator-depth reduction. Since b=Dn>a^2, q<1/a and C_0<a.

For every sum or product of two digits, subtract its residue digit and
divide by q. The result belongs to N_0[q]. Here are all the needed cases.

For ordinary digit sums and products, the difference is either a
nonnegative multiple of a, or that multiple plus a-1-r. The associated
nonzero carries are integers: a/q=b, while

    (a-1-r)/q = n*((a-1)D-A)/a

is an integer at least n. For k>=1,

    (k+r-(k-1))/q=n*(A+D)/a

is an integer. For 2<=k<=a-2,

    (kr-(a-k))/q=n*(kA-(a-k)D)/a

is a positive integer. The product 1*r has zero carry. Finally

    (2r-(a-2))/q=n*(2A-(a-2)D)/a

is a positive integer, and the only potentially nonintegral carry is

    (r^2-1)/q=n*(A^2-D^2)/(aD).                     (4)

If a>=4 then r>a-2 and q<1/a give (4)>a>=C_0. If a=3,
A^2-D^2>2D and n>=4 give (4)>8/3, whereas
C_0<=32/13<8/3. Thus every carry is in N_0[q].

Consequently the union U of the sets d+qS over d in E is closed under addition and
multiplication: multiply or add two digit-plus-q expressions and use the
corresponding carry. It contains 1,q,r, so S=U. Distinct residues make
this a disjoint decomposition.

The conductor supplied by these digits is

    C=r/(1-q).

It satisfies a-2<r<C<a-1, since ((a-1)D-A) is a positive multiple of a
and n>=a. Also r^2>C. For a>=4 this follows from r>a-2>=2 and
1/(1-q)<a/(a-1)<2. For a=3 it is equivalent to

    n>3A/[D(A-D)]=3/D+3/(A-D)<=15/4<4<=n.

If x in R is written with denominator b^k, k>=1, its canonical tail
(x-d)/q is in b^(-(k-1)) Z: residue subtraction supplies divisibility by
a. Hence canonical denominator depth decreases until an integer is
reached. A tail x>=C remains >=C, so every R-element >=C belongs to S.
The equality C in R is impossible: C=An/(Dn-a), whose reduced denominator
is coprime to Dn; membership in R would make C an integer, contrary to
a-2<C<a-1.

## 2. All atoms have finite digit words

Here is the perturbation fact used below. Since P(b) has at least two
primes, for every i and epsilon>0 there is a b-smooth unit h of R such
that

    1<h<1+epsilon,  h in N_0[q],  h=1 modulo a^i R.

Indeed, choose L>=i large with C_0 q^L<epsilon. Ratios of powers of two
distinct denominator primes, with the exponents constrained to be
multiples of their orders modulo a^L, are dense in the positive reals.
Choose such a ratio in (1+C_0 q^L,1+epsilon). Then
(h-1)/q^L lies in R above C_0, proving h in N_0[q].

If x=P+q^i z with P in S and z in R greater than C, choose h as above
sufficiently near 1. Then

    x/h=P+q^i z',  z'=(x/h-P)/q^i in R,  z'>C.

Thus x/h belongs to S, and x=h*(x/h) is a proper factorization; h can be
chosen to avoid x, so the second factor is not 1. In particular no atom
can have a polynomial representation with a q-block greater than C.

A q-block is a polynomial in r with nonnegative integer coefficients.
The only such values at most C are the digits E: integer coefficients
at least a-1 exceed C, r+1>C, and r^2>C. Therefore every atom has a finite
E-word representation.

The only unit is 1: its unique polynomial representation is the constant
1, as the residue and the real bound force its degree-zero block to be
1. The same argument makes q an atom. Every element below 1 has a zero
initial block and is divisible by q; hence q is the only atom below 1.
Every other atom has positive constant digit and is greater than 1.

For each ordinary k<=a-2, the same residue/real argument shows that its
only polynomial representation is the constant k. Its atoms are exactly
the ordinary primes at most a-2. Likewise r has the unique polynomial
representation Y, so r is an atom. These are precisely the degree-zero
atoms.

## 3. Integer factorizations and unconditional non-atomicity

Let s|n with s not dividing D. By (2), s divides neither A nor any
nonzero ordinary digit. Every nonzero digit is therefore an s-adic unit,
while v_s(q)=-v_s(n)<0. A finite digit word of degree h has uniquely
smallest valuation in its highest term, giving

    v_s(word)=-h*v_s(n).

All atoms have nonpositive s-valuation. An atomic factorization of an
integer can therefore use only degree-zero atoms, namely the small
ordinary primes and r. Write such a product as u*r^j, with u supported
on primes at most a-2.

If D has a prime above a-2, integrality forces j=0. If all primes of D
are at most a-2, integrality is equivalent to D^j dividing u, and
u*r^j=A^j*(u/D^j). Conversely A=rD factors into r and the small ordinary
prime atoms. This proves the exact integer classification and
non-atomicity stated above.

For independence, any prime divisor of a has positive valuation on q
and zero valuation on r; hence q^u r^v=1 forces u=v=0. Nonredundancy
follows from q<1<r and from the residue a-1 of r: any representation in
N_0[q] would have constant coefficient at least a-1>r.

## 4. Finite carry certificates imply IDF

Fix p^e exactly dividing D. A negative p-valuation remains negative
under every prefix map x -> d+qx: qx has valuation less than -e, below
both possible digit valuations 0,...,v_p(a-2) and -e. Thus every
p-integral finite digit word starts from an ordinary terminal digit

    j in {1,...,a-2}

and all its prefixes retain p-integrality. Because j<a<p^e, the first
retained prefix must be r. If p|n, condition (2) makes every j a p-adic
unit, and qj has a deeper pole than r; there is no retained first
prefix. The closure then consists only of the finite seeds.

If the retained closure is finite for every p|D, their finite union
contains every atom with nonnegative valuation at some prime of D. At
primes of n outside D all atom valuations are nonpositive by section 3.
Consequently every atom outside this finite exceptional set has numerator
coprime to b. If it divides a fixed target x, that numerator divides the
part of the numerator of x supported outside P(b). Apart from q, every
atom exceeds 1, so its denominator is smaller than its numerator. There
are only finitely many candidates. Adding q and the finite exceptional
sets proves IDF.

## 5. Hensel roots and the density estimate

For p not dividing n, a word of length L starting from seed j has value
H_w(n)/(Dn)^L. Its forced initial r gives

    H_1=An+aj.

Subsequent ordinary prefixes d in {0,...,a-2} and the r-prefix give

    H_new=a H+d(Dn)^(L+1),
    H_new=a H+A n(Dn)^L.

For every positive length L,

    H_w = a^(L-1)(An+aj) modulo p,
    H'_w = A*a^(L-1) modulo p.

The derivative is a unit. Thus each word has exactly one root class
modulo p^(eL), by unique simple-root lifting. A retained word must belong
to that class. There are (a-2) seed choices and at most a^(L-1) words
after the forced first r. The set of parameters admitting a retained
depth-L word therefore has upper natural density at most

    (a-2)*a^(L-1)/p^(eL).

This tends to zero by (1). An infinite closure has retained words of
arbitrarily large length, so its parameter set has density zero. The
finite union over p|D still has density zero. All other admissible
parameters have finite certificates and are IDF.

The admissible set has positive density phi(F)/F, where
F=a*A*(a-2)!: removing integers supported only on P(D) removes a
density-zero set. Absolute density-zero exceptions therefore have
relative density zero. One must not assume that the Hensel moduli are
coprime to F: primes in D can divide (a-2)!. No such assumption is needed.

For the finite-N bound take L_p=ceil(log_(p^e)N). Its root modulus is at
least N, so each root class contributes at most one integer in [1,N].
The union bound gives (3). Outside the union, each integral tree has
depth less than L_p and hence is a finite, explicitly enumerable
certificate. Finally a^(ceil(log_(p^e)N)-1)<=N^(log_(p^e)a).

## 6. Examples and scope

For a=4,D=5,A=11, the fixed upper generator is 11/5, and q=4/(5n).
Admissibility requires n>=4, gcd(n,88)=1, and a prime of n outside {5}.
The only positive integers with atomic factorizations are powers of 2.
IDF holds for a relative-density-one set of these n.
The particular n=7 is certified directly: at the sole prime p=5 of D,
the complete integral closure is {1,2,17/7}. Thus the explicit pair
(4/35,11/5) is IDF and non-atomic.

For a=5,D=16,A=49, the fixed upper generator is 49/16 and q=5/(16n).
Admissibility requires n>=5, gcd(n,1470)=1, and an odd prime divisor of n.
The atomic integers are exactly 2^i*3^j*49^k. In particular 49 has the
atomic factorization (49/16)*2^4, while the integer 7 has no atomic
factorization.
At n=11 the complete 2-integral closure is {1,2,3,34/11}, giving the
explicit IDF, non-atomic pair (5/176,49/16).

The integer classification does not assert uniqueness of atomic
factorizations. For a=5,D=8,A=27,n=7, the integral closure at 2 consists
only of its seeds {1,2,3}, so (5/56,27/8) is IDF and non-atomic, while
27 has the distinct atomic factorizations 3^3 and (27/8)*2^3.

The proof neither exhibits a non-IDF admissible parameter nor proves
that every admissible parameter is IDF. The finite-tree density estimate
is the asserted conclusion.

## 7. A boundary counterexample when the factorial condition is dropped

The factorial restriction cannot simply be removed while retaining the
stated integer classification. Take a=5,D=16,A=49,n=6. Then gcd(n,aA)=1
and n has the outside denominator prime 3, but n shares primes with
(a-2)!. In S=N_0[5/96,49/16], the elements q=5/96, 2, and 3 are atoms:
their positive polynomial representations are uniquely X, 2, and 3,
respectively, by the same residue and size argument. Yet

    5 = (5/96)*3*2^5

is an atomic factorization. The integer 5 is not in the monoid generated
by 2,3,49. The failed valuation step is visible already in

    3q = 5/32,  v_3(3q)=0,

rather than the claimed negative valuation for every positive-degree
word. This example is outside the corrected theorem.

The exact checks in `check_arbitrary_numerator_density.py` cover the
composite numerators 4 and 6, the numerator-5 prime-power block case,
all digit carries, Hensel lifting for the terminal seeds, the three
explicit finite closures above, and rejection of this invalid parameter.
They supplement the proof; finite checks are not used as a substitute
for the all-depth density argument.

## 8. Finite complete atomic factorizations for every admissible parameter

This conclusion does **not** require the finite carry certificates or
IDF. For every parameter satisfying (1) and (2), every element has a
finite, effectively enumerable set of complete atomic factorizations.
This does not assert that a factorization exists, or that arbitrary
elements have only finitely many atom divisors.

Fix a prime s dividing n but not D, and put f=v_s(n). Every atom has a
canonical digit polynomial. If its q-degree is h, section 3 gives
v_s(atom)=-fh. Therefore a complete atomic factorization of x forces

    H=-v_s(x)/f

to be a nonnegative integer and forces the sum of the atoms' q-degrees
to equal H. If H fails this condition, there is no complete atomic
factorization. Otherwise every positive-degree atom belongs to the
finite list of digit words of degree at most H. The degree-zero atoms
are exactly r and the ordinary primes at most a-2.

For completeness, these finite candidates admit an exact atom test.
Let P_N(x) denote the first N canonical digits and F(x)=lim P_N(x).
The digit-prefix argument gives F(x+y)<=F(x)+F(y),
F(q^i*x)=q^i*F(x), and F(x)<=min(x,C). For subadditivity, the sum of
two N-digit prefixes differs from x+y by an element of q^N*S; taking
its canonical prefix cannot increase that sum. Passing to the limit
gives the inequality. This is the same prefix method credited to
ppdppd in the supplied discussion.

A finite digit word x has F(x)=x. If any positive polynomial
representation x=sum_i q^i*c_i(r) had a block c_i(r)>C, the preceding
inequalities would give F(x)<x, a contradiction. Every block is
therefore one of E. Each such block has its unique polynomial
representation as an ordinary constant or Y, and the canonical digits
are unique. Hence x has a unique polynomial representation in
N_0[X,Y]. Actual factorizations of x correspond exactly to formal
factorizations of that polynomial into nonunit polynomials. A finite
exhaustive test is possible: factor bidegrees are bounded by the target
bidegrees, and every coefficient of a factor is at most the largest
target coefficient, since the other nonzero factor has a positive
integer coefficient and no cancellation is possible.

Finally put delta=min({r} union {ordinary primes <=a-2})>1. At most H
positive-degree atoms occur. Their product is at least q^H, because
q is the only atom below 1. The product of the degree-zero atoms is
therefore at most x*q^(-H). If this bound is less than 1 no factorization
exists; otherwise there are at most

    H + floor(log_delta(x*q^(-H)))

atoms in a factorization. Enumerate the finite candidate multisets
within these degree and length bounds and test their products exactly.
This is a terminating mathematical algorithm; no implementation of
this general corollary is claimed here.
