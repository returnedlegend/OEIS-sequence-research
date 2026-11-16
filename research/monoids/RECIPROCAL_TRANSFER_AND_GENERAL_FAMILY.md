# Reciprocal localization: general transfer theorems and the arbitrary-numerator family

These are independently derived results. Their novelty relative to the full
AoPS discussion and its unavailable PDF attachments has not been established.
The proofs below do not use finite computations.

Throughout let t=a/b in lowest terms, with 1<a<b, and put

    S=N_0[t],   T=N_0[t,t^(-1)],   R=Z[1/b].

All monoids below omit zero. Let A be the set of primes dividing a, P the set
of primes dividing b, and e_ell=v_ell(a) for ell in A. The sets A and P are
disjoint. Write e=(e_ell)_(ell in A).

## Main conclusions

1. S is IDF if and only if T is IDF, for every reduced 1<a<b.
2. If S is atomic, then T is atomic. No converse is claimed in general.
3. If a is prime, the map has the stronger product description
   S ~= N_0 x H and T ~= Z x H (multiplicative t-powers in the first
   coordinate), so both atomicity and IDF are equivalent between S and T.
4. If a=ell^s is a prime power, every S-atom other than t admits no
   factorization into more than s nonunits of T. The general proof gives an
   explicit uniform bound for arbitrary a.
5. T has finitely many divisor classes for every element if and only if b is
   a prime power. Equivalently, T is both atomic and IDF if and only if b is
   a prime power.
6. Suppose |P|>=2 and a<p^(v_p(b)) for every p in P. Then T is IDF and
   non-atomic for **arbitrary a>1**, removing the prime-power numerator
   restriction from the earlier reciprocal theorem. There are explicit
   finite atom-divisor bounds and a terminating factorization algorithm.

The IDF equivalence does not decide the still-unresolved examples by itself.
For instance it identifies the cyclic and reciprocal IDF questions at5/6,
but does not answer them.

## 1. Units and exact division by t

The units of S are {1}; the units of T are exactly t^Z. For completeness,
the only nonnegative Laurent-polynomial expression for1 at t is the constant
1. A negative exponent would already contribute more than1. If there are no
negative exponents, a positive constant term forces the entire expression
to be the constant1. If the constant term is zero, every term has positive
ell-adic valuation for any ell|a, so their sum cannot be1. Multiplying
expressions for inverse elements now forces each expression to be a single
monomial of coefficient1. The S assertion follows by restricting exponents.

There is an exact identity

    tS = S intersect aR.                                      (1)

One inclusion is immediate. For the other, write x=sum c_i t^i in S. Modulo
aR, one has x=c_0. Since aR intersect Z=aZ, membership x in aR gives
c_0=a*k with k>=0. Therefore

    x=t*(b*k+sum_{i>=1} c_i t^(i-1))

belongs tS. Iterating (1) gives t^m S=S intersect a^m R.

It follows that

    S = {x in T : v_ell(x)>=0 for every ell in A}.             (2)

Indeed write x=t^(-m)s with s in S and m>=0. If all the stated valuations
are nonnegative, s belongs a^m R, hence t^m S, so x belongs S.

For z in T define

    nu(z)=min_{ell in A} floor(v_ell(z)/e_ell),
    z^circ=t^(-nu(z))*z.                                     (3)

Then z^circ belongs S but not tS. It is the unique associate of z with this
property. Its valuation vector is nonnegative and has at least one
coordinate strictly below e_ell. Also z^circ>=1: an S-element below1 has
zero constant coefficient and therefore lies in tS.

The element t is an S-atom. One proof uses uniqueness of bounded-coefficient
polynomial expressions: X has coefficients below a, so a numerical
factorization of t forces the formal product to be X, with a unit factor.
Every S-atom other than t lies in S minus tS and hence is already normalized
by (3). The only S-elements that become units in T are t^n, n>=0.

## 2. A family of multiplicative valuation bounds

For every ell in A put

    J_ell(z)=z^(e_ell)*t^(-v_ell(z)),   z in T.                (4)

This is rational, multiplicative, invariant under t^Z, and satisfies

    J_ell(z)>=1, with equality exactly when z is a unit.       (5)

To prove this, write z as a finite sum of Laurent monomials, repeating terms
to absorb positive integer coefficients. If m is the least exponent, then

    z>=t^m,    v_ell(z)>=e_ell*m.

Since 0<t<1, these inequalities give z>=t^(v_ell(z)/e_ell). Equality is
possible only for a single monomial of coefficient1: any expression with
at least two monomials gives z>t^m. Taking the e_ell-th power proves (5).

Fix x in T. For a divisor d of x, normalize gamma=d^circ. Its cofactor
remains in T because normalization uses a unit. Hence

    1<=J_ell(gamma)<=J_ell(x).

Since gamma>=1 and v_ell(gamma)>=0,

    t^(-v_ell(gamma))<=J_ell(gamma)<=J_ell(x).                 (6)

Define the finite integer

    M_ell(x)=max{m>=0 : t^(-m)<=J_ell(x)}.                    (7)

Exact rational comparisons compute it. Every normalized divisor has
valuation vector in the finite box

    V(x)={v in product_[ell in A] {0,...,M_ell(x)}:
          min_ell floor(v_ell/e_ell)=0}.                      (8)

Moreover gamma^(e_ell)<=J_ell(x), so normalized divisors also have a uniform
real upper bound. These observations apply to arbitrary divisors, not only
atoms, and require no prime-power assumption on a.

## 3. T-atoms lift to S-atoms

Let alpha be a T-atom and gamma=alpha^circ. Suppose gamma=u*v were a
factorization into S-nonunits. Since alpha is a T-atom, one factor, say u,
must be a T-unit. As u belongs S, u=t^j with j>=1. This puts gamma in tS,
contrary to its normalization. Thus gamma is an S-atom other than t.

Distinct S-atoms other than t cannot become associates in T. Indeed, if
u=t^k v with k>0, u has the nontrivial S-factorization t*(t^(k-1)v);
if k<0, interchange u and v. Thus k=0 and u=v.

## 4. An elementary uniform factorization-length bound

Put p_0=min A. Fix an S-atom u!=t and consider a factorization

    u=z_1*...*z_m

into T-nonunits, with m>=2. Replace every z_i by its normalized associate
gamma_i=z_i^circ in S minus tS. For some integer K,

    product_i gamma_i=t^K*u.

Since u is normalized and the product belongs S, K>=0. In fact K>=1:
if K=0, the displayed identity is already a nontrivial S-factorization
of u.

Every gamma_i must have positive valuation at at least one prime ell|a.
Otherwise its A-valuations are all zero, and the T-element u/gamma_i has
all A-valuations nonnegative. By (2), u/gamma_i belongs S. Both gamma_i
and this cofactor are T-nonunits (the cofactor is associate to the product
of the other z_j), hence S-nonunits, contradicting irreducibility of u.

Write any S-polynomial representation gamma_i=c_0+sum_{j>=1}c_j*t^j.
Its constant coefficient is positive because gamma_i is not in tS.
The nonconstant terms lie in aR. If v_ell(gamma_i)>0, then ell divides
c_0, so gamma_i>=c_0>=ell>=p_0. Consequently

    p_0^m <= product_i gamma_i = t^K*u <= t*u.               (9)

Thus every nontrivial T-factorization of u into nonunits has length at most
floor(log_(p_0)(t*u)). In particular all lengths, including the trivial
one-factor expression, are bounded by max(1,floor(log_(p_0)(t*u))).

The conductor C=(a-1)b/(b-a) from section5 gives u<=b*C, so the uniform
bound

    B=max(1,floor(log_(p_0)(a*C)))                           (10)

works for EVERY S-atom other than t, independently of the element it divides.
Integer logarithms here mean exact comparison with integer powers, not
floating-point arithmetic.

Every such u therefore factors into T-atoms: choose a factorization with
maximum possible length; a nonatom factor could be split to increase that
length. In particular, every S-atom other than t is an atomic element of T.
It follows that

    S atomic => T atomic.                                  (11)

If S is atomic, factor the numerator s of any t^(-n)s in T into S-atoms;
the copies of t become units, and each remaining factor has a T-atomic
factorization as just proved.

The same argument shows that an S-atom u<p_0^2/t remains a T-atom. If a
is prime, the stronger statement in section6 applies to every S-atom
other than t.

### An independent sharper bound for prime-power a

If a=ell^s, normalized valuations are residues0,...,s-1. Any sequence of
more than s residues has a nonempty proper subsequence summing to0 modulo s:
apply the prefix-sum/pigeonhole argument to its first s terms. For a
T-factorization of an S-atom u!=t, normalize its factors to gamma_i in S
with those residues. The product of the selected factors has valuation
k*s, and its complement has valuation k'*s+v_ell(u), with k,k'>=0.
Divide by t^k and t^k', respectively. Identity (1) puts both resulting
nonunits in S, and their product is u, a contradiction. Thus every S-atom
other than t has T-factorization length at most s. One may use the smaller
of s and the uniform bound (10).

The prime-power bound can be sharp: for t=4/5, the element5 is an S-atom
because every5-smooth S-element is a nonnegative power of5. In T it has
factorization5=t^(-1)*2^2 of length2. More generally, for t=ell^s/p with s>=2 and
p a prime greater than ell^s, the S-atom p becomes t^(-1)*ell^s in T,
with s copies of the T-atom ell.

## 5. IDF is equivalent before and after reciprocal localization

### T IDF implies S IDF

Fix x in S. If T is IDF, only finitely many T-atom classes divide x. Every
S-atom u!=t dividing x factors in T into at most B of those classes, by
section4. There are finitely many products of length at most B from a
finite set of classes. Distinct S-atoms do not become associates by
section3. Thus x has finitely many S-atom divisors; t adds at most one.
This proves S is IDF.

### S IDF implies T IDF

The usual cyclic conductor is

    C=(a-1)b/(b-a),    R intersect [C,infinity) subset S.      (12)

For example, induct on the denominator exponent of y=N/b^n>=C, choosing
c in {0,...,a-1} with y-c in aR. The quotient (y-c)/t has one fewer
allowed denominator exponent and remains at least C.

Every S-atom has real value at most b*C. Indeed, if u>b*C, then u/b>C
belongs S by (12), and u=b*(u/b) is a factorization into S-nonunits.
Here b>1 and C>1.

Fix x in T. Every T-atom divisor normalizes to an S-atom gamma by section3.
Let X be the part of the reduced numerator of x supported outside A union P.
For each ell in A use the integer M_ell(x) in (7), and put

    L_0=X*product_[ell in A] ell^(M_ell(x)).                  (13)

The part of gamma's reduced numerator supported outside P divides L_0.
Indeed, valuations outside A union P are nonnegative throughout T and
bounded above by those of x; the remaining primes outside P are controlled
by (6).

Choose an integer B divisible by L_0 with B>=b*C^2. Then B/gamma belongs R,
and since gamma<=b*C,

    B/gamma>=C.

The conductor puts B/gamma in S. Thus ALL normalized T-atom divisors of x
are S-atom divisors of this one fixed B. If S is IDF, there are only finitely
many such atoms. This proves T is IDF and finishes the equivalence.

## 6. A direct product when the numerator is prime

Suppose a=ell is prime and put H={x in S:v_ell(x)=0}. Identity (1) shows
every x in S has a unique expression

    x=t^(v_ell(x))*h,   h in H.

The set H is a multiplicative monoid. Thus S is isomorphic to N_0 x H,
with addition of exponents in the first coordinate; T is isomorphic to
Z x H. Consequently atomicity and IDF are both equivalent between S and T.
This applies, in particular, to t=5/6; it is a reduction, not an answer to
its unresolved atomicity question.

## 7. Finitely many divisor classes exactly for prime-power b

Suppose P={p}. Fix x in T and normalize every divisor gamma using (3).
Its A-valuations lie in the finite box V(x), and its outside-(A union P)
numerator part divides X. Therefore

    gamma=N*p^j

with only finitely many possible positive integers N coprime to p. Also
1<=gamma<=U(x) for a finite upper bound from section2. This bounds j for
each N, yielding finitely many normalized divisors. Hence T has finitely
many divisor classes, and is atomic and IDF.

Suppose |P|>=2. Choose distinct p,q in P. For L>=1 let E_L=phi(a^L). The
group generated by p^(E_L) and q^(E_L) is dense in the positive reals and
all its elements are congruent to1 modulo a^L R. Choose h_L in that group
with

    1+C*t^L < h_L < 1+(C+1)*t^L.

Then (h_L-1)/t^L belongs R and exceeds C, so h_L belongs S by (12). The
h_L are P-smooth and tend to1 from above; pass to a distinct subsequence.
For an integer B>2C, eventually B/h_L belongs R and exceeds C, so h_L
are divisors of B in both S and T. They are pairwise nonassociate in T:
all have zero valuation at every ell|a, whereas t^k has valuation k*e_ell.
Thus B has infinitely many divisor classes.

An atomic IDF cancellative commutative monoid has finitely many divisor
classes for each element. To see this, factorization exponent vectors over
its finite set of atom-divisor classes form an antichain in N_0^m; Dickson's
lemma makes that set finite, and every divisor is a subproduct of one of
those factorizations. Therefore T cannot be both atomic and IDF when
|P|>=2. Together with the preceding paragraph, this proves the claimed
characterization.

## 8. The reciprocal IDF/non-atomic family for arbitrary numerators

Assume now |P|>=2 and a<p^(f_p) for every p in P, where f_p=v_p(b). Set

    D=product_[p in P] p^(f_p-1)=b/rad(b).

Then b>a^2, so C<a. The near-one elements h_L in section7 imply that any
polynomial expression with a coefficient at least a is reducible in T:
for beta=f(t)+a*t^j, the quantity

    z_L=(beta/h_L-f(t))/t^j

belongs R for L>=j and tends to a>C. Eventually z_L belongs S and gives
a factorization. Discreteness of the unit group t^Z makes both factors
nonunits after omitting finitely many indices. Thus every T-atom has a
normalized representative

    beta=sum_(i=0)^n c_i*t^i,  0<=c_i<a,  c_0,c_n>0.         (14)

Write beta=N/b^n. Then N>=b^n. At each p in P, the leading term in N is
c_n*a^n and all other terms are divisible by b. Since c_n<a<p^(f_p),

    v_p(N)=v_p(c_n)<f_p.                                   (15)

Fix x in T and use M_ell(x),X as above. The numerator of every normalized
atom divisor satisfies

    N | L(x),
    L(x)=D*X*product_[ell in A] ell^(M_ell(x)).              (16)

Hence every atom-divisor class appears in the finite candidate list

    {N/b^n : N|L(x), 0<=n<=floor(log_b N)}.

In particular its number of atom-divisor classes is at most

    sum_[N|L(x)] (1+floor(log_b N)).                         (17)

This proves IDF with no prime-power restriction on a.

### Direct atomless elements

Let

    delta=min(2, min_[ell in A] t^(-1/e_ell)) >1.

Take a P-smooth h in S with 1<h<delta, for example a sufficiently late
h_L. Suppose an atom divides h in T and normalize it to beta in (14).
For each ell in A, (6) gives

    t^(-v_ell(beta))<=J_ell(beta)<=J_ell(h)=h^(e_ell)<1/t.

Thus v_ell(beta)=0. Outside A union P the valuations of beta also vanish,
since beta divides the smooth h. Consequently N is supported only on P,
and (15) gives N<=D<b. As N>=b^n, necessarily n=0. The atom beta is a
nonunit integer, hence at least2. But then

    J_ell(beta)=beta^(e_ell)>=2^(e_ell)>h^(e_ell),

contradicting divisibility. Therefore h has no atom divisor in T. This
proves non-atomicity directly, without using atomic+IDF implies finiteness.

## 9. Constructive extension of the reciprocal algorithm

All the preceding bounds are effective in the block-condition family.
Replace the old prime-power numerator bound by (16). Enumerate its divisors
N and exponents n with b^n<=N. For beta=N/b^n:

1. Apply exact cyclic membership and obtain its canonical polynomial.
2. Require positive constant coefficient and all coefficients below a.
3. Test formal irreducibility in N_0[X].
4. Test x/beta in T using the exact Laurent-membership algorithm.

Bounded-coefficient polynomial expressions are unique even among Laurent
expressions: clear negative powers and apply divisibility by bX-a to the
difference, using the first positive and last negative coefficient argument.
Thus formal irreducibility is equivalent to T-irreducibility for the
retained polynomials. Formula (14) and (16) prove enumeration completeness.
Normalization (3) ensures exactly one representative per associate class.

For atomic factorizations, choose ANY ell_0|a and use J_ell0. It is rational,
multiplicative and greater than1 on every atom, so the exponent of each
listed atom is bounded by successive exact comparisons of its J-powers
with J_ell0(x). Enumerate the finite exponent vectors and retain those whose
residual is exactly t^k for an integer k. Compute the candidate k from any
one numerator valuation and check the rational equality; equality of J-values
alone is insufficient. This produces every atomic factorization up to
associates and ordering, or certifies that none exists.

## 10. An explicit example with a non-prime-power numerator

Take a=6, b=175=5^2*7 and t=6/175. Both maximal prime-power blocks25 and7
exceed6, so the general theorem proves

    N_0[6/175,175/6] minus {0} is IDF and non-atomic.

Here A={2,3} and e_2=e_3=1, so delta=2. The simple rational

    h=49/25=1+28*t

belongs S, is supported on denominator primes5,7, and satisfies1<h<2.
It therefore has no atom divisor in T by section8. This is an explicit
example beyond the earlier prime-power numerator hypothesis.

The same witness works for every t=6/b with b=5^m*7^n, m>=2,n>=1:

    49/25=1+(4*b/25)*t.

All these reciprocal monoids are IDF and have this atomless element.

## 11. Quantitative IDF transfer in the reverse direction

If T is IDF and x in S has N atom-divisor classes in T, the number of
S-atoms dividing x is at most

    binomial(N+B,B),

where B is the uniform bound (10). Indeed the non-t S-atoms correspond
injectively to products of at most B of the N available T-atom classes.
There are binomial(N+B,B)-1 nonempty commutative products in this inclusive
counting bound, and t adds at most one. This remains a valid bound if some
products represent the same class.

The elementary proof in section4 supersedes an earlier Dickson-lemma
argument and needs neither an ineffective bound nor a lattice computation.

## 12. A weaker hypothesis still forces reciprocal non-atomicity

Suppose |P|>=2 and

    a<p^(v_p(b)) for at least one p in P.                   (19)

Then T is non-atomic. In particular, atomicity of either S or T requires

    a>max_[p|b] p^(v_p(b)).

The assertion for S was already established in STRONGER_CYCLIC_REDUCTIONS.md;
here is the additional reciprocal argument.

Because another denominator prime exists, (19) gives b>2a. Hence C<b.
Any coefficient at least a in a polynomial expression can be carried by
 a*t^j=b*t^(j+1), exposing a coefficient at least b>C. The perturbation
argument from section8, with b in place of a, makes that element reducible
in T. Thus all normalized T-atoms have coefficients below a, even though
the all-primes block hypothesis of section8 is no longer assumed.

Fix p satisfying (19), and choose another prime s|b. The ratios

    p^(phi(a^L)*m)/s^(phi(a^L)*n),  m,n positive integers,

are dense in the positive reals. This follows from irrational rotation,
and the exponents may be taken arbitrarily large and positive. Choose h_L
in the interval used in section7 from this restricted set. It is in S,
is P-smooth, tends to1, and satisfies v_p(h_L)>0.

Choose h=h_L with1<h<delta, where delta is as in section8. Suppose h has an
atomic factorization in T. Normalize its atomic factors to beta_i and write

    h=t^k*product_i beta_i.

For every ell|a, the bound J_ell(beta_i)<=J_ell(h)<1/t forces
v_ell(beta_i)=0, exactly as in section8. Since v_ell(h)=0 as well, k=0.
Thus the beta_i multiply to h<2. Each beta_i is a nonunit polynomial with
positive constant coefficient, so1<beta_i<2. It cannot be an integer;
its polynomial degree n_i is positive.

Put f=v_p(b). Its numerator over b^(n_i) has leading term c_(n_i)*a^(n_i)
with v_p(c_(n_i))<f, while all other terms are divisible by p^f. Hence

    v_p(beta_i)=v_p(c_(n_i))-n_i*f<0.

Their product cannot have positive p-adic valuation. This contradicts the
choice of h, and proves non-atomicity.

This proof does not show that the selected h has no atom divisor, nor does
it decide IDF under the weaker hypothesis (19).

### An exact finite certificate at t=7/18

For t=7/18, the block3^2=9 exceeds7, whereas the other block2 does not.
The theorem therefore proves that both N_0[7/18] and N_0[7/18,18/7] are
non-atomic. A concrete witness is

    h=3^2448/2^3879,
    h=1+4*t^2+2*t^3+t^4*y,
    y=(h-1-4*t^2-2*t^3)/t^4.

Exact rational arithmetic gives y in Z[1/18], y>108/11=C, and1<h<2.
For orientation only, h is approximately1.9837108702 and y approximately
11.4177560649. The conductor certifies h in S, using only the four-digit
prefix(1,0,4,2); no thousands-digit expansion needs to be stored. Its
positive3-adic valuation and the preceding argument exclude every atomic
factorization in T. IDF is not determined by this certificate.
