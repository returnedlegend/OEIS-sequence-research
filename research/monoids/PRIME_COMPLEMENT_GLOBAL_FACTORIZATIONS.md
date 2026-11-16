# A global finite atomic-factorization algorithm for a prime complementary endpoint

The one-large-block theorem and algorithm now extend to all integer C>=3;
see [COMPLEMENTARY_CRITICAL_FACTORIZATIONS.md](COMPLEMENTARY_CRITICAL_FACTORIZATIONS.md).
This note retains the prime-C specialization and its endpoint height links.

This note extends the critical-element results in
PRIME_COMPLEMENT_CRITICAL_ALGORITHM.md. It makes no novelty claim. The
user-supplied source already contains complementary-generator families:
Mardcelo's October 20 result assumes q=a/b, r=(a-1)(1-q), b>=a^2-1,
and every maximal denominator prime-power block at least a, and proves
IDF and nonatomicity. The theorem here uses only one large block for
finite complete atomic-factorization sets and nonatomicity; it does not
claim IDF when some other block is smaller. The full PDFs were not
available for comparison.

Assume throughout

    C>=3 is prime, a=C+1, gcd(a,b)=1, b>a*C,
    q=a/b, r=C*(1-q), R=Z[1/b], S=N_0[q,r],
    b has at least two distinct prime divisors.

The critical-element theorem proves terminating membership and atom
algorithms, and describes every atom: q is the only atom below1; all
other atoms are normalized critical values in(1,C]. Every normalized
endpoint terminating at C is an atom, while every other critical value
has a unique polynomial representation.

Suppose there is a prime p with

    p^e exactly divides b and p^e>C.                 (1)

The following conclusions hold:

* S is nonatomic, with an explicit terminating search for a witness.
* Every individual nonzero S-element has finitely many complete atomic
  factorizations; all of them can be found by a terminating exact algorithm.
* Criticality, finiteness of actual divisors, and bounded lengths of
  arbitrary nonunit factorizations are equivalent for individual elements.
* These statements do not decide IDF for noncritical targets.

## 1. A denominator valuation shared by all nonconstant atoms

Let alpha be an atom other than q or an ordinary integer. Write its
canonical expansion with minimal b-denominator depth n>=1 and integral
terminal k in{0,...,C}. If k>0 and the preceding digit is ordinary,
clearing b^n gives a numerator of p-adic valuation exactly v_p(k): all
earlier contributions are divisible by p^e, while the top term is k*a^n.

If the preceding digit is r, its denominator also contributes at this
depth. The top two terms instead sum to

    a^(n-1)*[a*k+C*(b-a)]
      =a^n*(k-C)+C*b*a^(n-1).

Here k<C: if k=C, that preceding tail would already be the integer
r+q*C=C, contradicting minimal canonical depth. Thus the relevant
valuation is v_p(C-k). In either case the nonzero integer k or C-k is
at most C<p^e, so

    v_p(alpha)=v_p(k)-n*e<0, or
    v_p(alpha)=v_p(C-k)-n*e<0, respectively.         (2)

If k=0, the final nonzero digit must be r: an ordinary last digit would
already have been an integral terminal. Its contribution after clearing
b^n is C*(b-a)*a^(n-1), so the same argument gives

    v_p(alpha)=v_p(C)-n*e<0.                        (3)

Consequently, if d=-v_p(alpha), then

    n <= floor((d+floor(log_p C))/e).               (4)

The only integer atoms are the ordinary primes at most C. Integers below
C have their unique constant polynomial representation, and C itself is
an endpoint atom.

## 2. Nonatomicity from one large block

Let s be another prime dividing b. For any L, taking the exponents to be
multiples of a common multiplicative-order exponent modulo a^L gives
b-smooth rationals

    h=p^u/s^v, u,v>0, h-1 in a^L*R,

dense on the positive real axis. Density follows from the irrationality
of log(p)/log(s). Choose L with C*q^L<1, then choose such an h with

    1+C*q^L<h<2.

The element c=(h-1)/q^L belongs R and exceeds C. The conductor therefore
shows that h=1+q^L*c belongs S. Moreover v_p(h)>0, and h has zero valuation
at every prime dividing a.

If h had an atomic factorization, q could not occur: it has positive
valuation at every prime dividing a, and all S-elements have nonnegative
valuations there. Every remaining atom is greater than1. Since h<2, no
integer atom could occur. But every remaining nonconstant atom has
negative p-adic valuation by (2)-(3), contradicting v_p(h)>0. Thus h is
nonatomic.

This is constructive: enumerate positive exponents u,v satisfying the
congruences until the displayed interval holds. Density proves that this
finite search eventually succeeds.

## 3. Explicit bounds for every complete atomic factorization

Fix x in S\{0}. For each prime ell dividing a, every S-element has
nonnegative ell-adic valuation. Define

    A=min_{ell|a} floor(v_ell(x)/v_ell(a)),
    B=x*q^(-A).

The number j of q factors in any atomic factorization lies in{0,...,A}.
After removing them, the product of its remaining atoms is at most B.
If B<1 there is no atomic factorization.

Let

    J=floor(log_p B) if p<=C, and J=0 if p>C,
    D=J-v_p(x).

Here J bounds the multiplicity of the integer atom p; if p>C that atom
does not exist. Valuations in any complete atomic factorization give

    sum_{nonconstant alpha !=q} -v_p(alpha)
       = multiplicity(p)-e*j-v_p(x)
       <= D.                                      (5)

If D<0 there is no atomic factorization. Otherwise at most D nonconstant
atoms other than q occur, and (4) bounds every such atom's denominator
 depth by

    K=floor((D+floor(log_p C))/e).                   (6)

The total number of integer atoms is at most floor(log_2 B). Together
with j<=A, these give a finite uniform length bound for every complete
atomic factorization of this particular x.

## 4. An exact finite candidate and factorization algorithm

Let X be the part of x's reduced numerator supported outside the prime
divisors of b. For an atom divisor alpha, its numerator outside those
primes divides X, since every element of S has nonnegative valuation at
all primes outside b.

Enumerate each divisor N of X and each tuple of valuations w_l for primes
l^f exactly dividing b, within

    -K*f <= w_l <= floor(log_l(C*(b/l^f)^K)).        (7)

Form alpha=N*product l^w_l and retain nonintegral values in(1,min(B,C)]
that the atom oracle accepts and whose minimal b-depth is at most K. This includes
all nonconstant atoms allowed by (6). Include also the finitely many
integer primes at most min(B,C) that divide x in S. Every enumeration
bound is finite and uses exact integer powers and rational comparisons.

Finally enumerate j in{0,...,A}, multisets of at most D nonconstant
candidate atoms, and multisets of at most floor(log_2 B) integer atoms.
Keep exactly those whose product, multiplied by q^j, equals x. This gives
all complete atomic factorizations, up to order, and terminates. The unit
1 has its empty factorization. An empty output for a nonunit certifies
that the element is nonatomic.

The algorithm does not bound all atom divisors: an atom with a nonatomic
cofactor is not required to obey the complete-factorization budget (5).
This is exactly why the theorem is not an IDF proof.

## 5. A small concrete example beyond the all-block hypothesis

Take

    q=4/15, r=11/5, C=3, p^e=5>3.

The other denominator block is3<4, so this parameter does not meet the
all-block hypothesis quoted above. The witness

    h=125/81
     =1+q+r*q^2+q^3+20*q^4

belongs S and lies between1 and2. It has v_2(h)=0 and v_5(h)=3>0.
No q factor can occur in an atomic factorization, integer atoms2 and3
are too large, and every other atom has negative5-adic valuation.
Therefore h has no atomic factorization. Nevertheless every element of
this S has only finitely many complete atomic factorizations, and the
algorithm above decides and enumerates them. Its global IDF status is
not settled here.

Two further small witnesses illustrate that the good block may be a
higher prime power:

| C,b | q,r | Nonatomic element in(1,2) |
|---|---|---|
|5,35|6/35,29/7|49/25=1+2q+21q^2|
|7,63|8/63,55/9|81/49=1+4q+9q^2|

In the second row the good block is3^2>7, although the prime3 is itself
an integer atom. It cannot occur in a factorization of the displayed
element because that element is less than2. The same monoid also shows
why the global algorithm must allow the q multiplicity to vary:

    8=2*2*2=q*3*3*7.

The exact algorithm finds these two factorizations and no others.

An infinite subfamily outside the quoted all-block hypothesis is obtained
by taking any primes C>=3 and P>C+1 and setting b=C*P. Then

    q=(C+1)/(C*P),  r=(C*P-C-1)/P.

The P-block is greater than C while the C-block is less than a=C+1.
Every member of this parameter family is therefore nonatomic and has
finite complete atomic-factorization sets, with the same exact algorithms.
Again, no global IDF conclusion is asserted.

For this b=C*P subfamily,
[PRIME_COMPLEMENT_ENDPOINT_HEIGHT.md](PRIME_COMPLEMENT_ENDPOINT_HEIGHT.md)
reduces IDF exactly to fixed-outside-numerator endpoint heights. All
nonendpoint critical values have an elementary degree bound at fixed
outside numerator; every remaining endpoint candidate is already an
atom. The height condition itself remains unresolved.

## 6. Atomic witnesses for any possible IDF failure

The critical atom classification also gives a short conditional witness,
without assuming (1). If IDF fails, infinitely many atom divisors of one
target share the same numerator outside the primes of b. Choose one such
atom alpha_0. All these atoms alpha lie in(1,C], their ratios belong R,
and

    C^2*alpha_0/alpha >= C*alpha_0>C.

Thus every alpha divides the single element C^2*alpha_0, which has an
explicit atomic factorization C*C*alpha_0 of length3. Under (1), the
finite complete-factorization theorem implies that all but finitely many
of these cofactors are nonatomic. This is a witness reduction, not an
assertion that such an infinite family exists.
