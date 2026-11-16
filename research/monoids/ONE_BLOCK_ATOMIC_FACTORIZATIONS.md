# Effective finite atomic factorizations under one good denominator block

Let t=a/b be reduced, 1<a<b. Put S=N_0[t], T=N_0[t,t^{-1}], and
P={p:p|b}. Assume |P|>=2 and that for some p in P,

  a<p^f,  where f=v_p(b).

Then every element of S and of T has only finitely many atomic
factorizations up to ordering and, for T, units. These factorizations
can be enumerated by a terminating exact algorithm. An empty list
certifies failure to admit an atomic factorization. Neither monoid is
atomic under these hypotheses, so this statement must not be called
the finite-factorization-monoid property. It does not decide IDF.

## 1. The complete atom correspondence

The one-good-block argument gives b>2a and C=(a-1)/(1-t)<b. Near-one
b-smooth factors, congruent to 1 modulo high powers of a, show that
a polynomial coefficient at least a forces reducibility in both S
and T: carry a*t^j to b*t^{j+1}, then perturb the coefficient b>C.

Thus every S-atom other than t, and every normalized T-atom, has a
polynomial representation

  beta=sum_{i=0}^n c_i*t^i,
  0<=c_i<a, c_0,c_n>0.                                  (1)

Every polynomial with all coefficients below a is unique even among
nonnegative Laurent-polynomial representations. Clear negative powers
and use divisibility of a polynomial vanishing at t by bX-a; the first
positive and last negative coefficients of the quotient force a
contradiction unless the difference is zero.

Consequently (1) is an S-atom exactly when it is a T-atom, and exactly
when its formal polynomial is irreducible in N_0[X]. The S-atoms are
t together with these normalized T-atoms. The constant atoms are
precisely the ordinary integer primes less than a.

## 2. Normalization, norms, and bounded unit exponents

Let A be the primes dividing a and e_ell=v_ell(a). The exact identities

  tS=S intersect a*Z[1/b],
  S={z in T: v_ell(z)>=0 for every ell in A}

give the unique normalized associate

  z^circ=t^{-nu(z)}z,
  nu(z)=min_{ell in A} floor(v_ell(z)/e_ell).

It lies in S minus tS and is at least 1. Define

  J_ell(z)=z^{e_ell}*t^{-v_ell(z)}.

For z in T these are rational multiplicative invariants, at least 1,
and equal to 1 exactly at the units. This follows by taking the least
exponent in a nonnegative Laurent expression.

Fix x in T and consider an atomic factorization

  x=t^k*product_i beta_i

with normalized atoms beta_i as in (1). Since beta_i>=1,

  t^{-sum_i v_ell(beta_i)} <= product_i J_ell(beta_i)=J_ell(x).

Let

  M_ell=max{j>=0:t^{-j}<=J_ell(x)}.

Every unit exponent k therefore belongs to the explicitly finite
integer interval determined by

  0<=v_ell(x)-k*e_ell<=M_ell  for every ell in A.          (2)

All bounds use successive rational comparisons. For a fixed admissible
k put B_k=x*t^{-k}. The normalized factors multiply to B_k, so B_k>=1.

## 3. The good denominator prime bounds total polynomial degree

For a positive-degree normalized atom beta of degree n, write
beta=N/b^n. Its top coefficient satisfies 0<c_n<a<p^f, while every
other numerator term is divisible by p^f. Therefore

  -v_p(beta)=n*f-v_p(c_n) >= (n-1)*f+1 >= n.             (3)

Among the constant atoms, only the atom p can have positive p-adic
valuation, and it is available only if p<a. Let j be its multiplicity
in a factorization of B_k. Since all normalized factors are at least 1,

  j<=J_k:=floor(log_p B_k) if p<a,
  j=0 and J_k=0 if p>=a.

Taking p-adic valuations of the product gives

  sum_{positive-degree factors} -v_p(beta_i)
       = j-v_p(B_k) <= J_k-v_p(B_k)=:L_k.

By (3), the sum of the polynomial degrees of all nonconstant normalized
atom factors is at most L_k. A negative L_k excludes that unit exponent.
All constant atom multiplicities have total at most floor(log_2 B_k).
In particular there are finitely many atomic factorizations for each k,
and (2) permits only finitely many k.

## 4. Exact enumeration

For each integer k satisfying (2):

1. Compute B_k and L_k; skip B_k<1 or L_k<0.
2. List the integer primes below a and every polynomial (1) of degree
   between 1 and L_k. Keep a polynomial only if it is formally
   irreducible in N_0[X]. This is a finite test: any formal factor has
   positive constant coefficient and is coefficientwise bounded by
   the original polynomial. Enumerate such factors and perform exact
   polynomial division over Q[X], testing that the quotient has
   nonnegative integer coefficients.
3. Evaluate the retained atoms and enumerate their multisets whose
   product is B_k, bounding total nonconstant degree by L_k and total
   constant multiplicity by floor(log_2 B_k). Equivalently, each atom
   exponent is bounded by successive comparisons beta^j<=B_k.
4. Output x=t^k times every successful atom product.

This returns all T-factorizations up to units and ordering. To enumerate
S-factorizations for an input x in S, keep exactly the outputs with
k>=0 and replace the unit factor t^k by k copies of the S-atom t.
The atom correspondence in section 1 proves both directions.

Exact S-membership is the usual denominator-reducing digit algorithm
with digits 0,...,a-1. Exact T-membership follows by taking the largest
K>=0 with t^{-K}<=x (or K=0 if x<1), then testing t^K*x in S.

## Examples and scope

This applies to t=7/18: the block 3^2 exceeds 7, so individual atomic
factorizations can be decided and listed even though this argument
does not settle IDF. It also applies to t=3/10 via the prime 5.

The implementation is one_block_factorizations.py. For example,
at t=7/18 it returns 7=t*2*3*3 and 14=t*2*2*3*3. At t=4/15, the
element 15 has no S-atomic factorization but has the T-factorization
15=t^{-1}*2*2. This illustrates why the condition k>=0 must be imposed
when converting reciprocal outputs into cyclic factorizations.

Exact checks reconstruct every returned factorization for these examples
and recover the two factorizations of 142753/100000 at t=3/10. These
finite checks validate implementation cases; completeness is proved
by the degree and unit-exponent bounds above.

The finite atom-divisor problem is different. An atom can divide x
with a cofactor having no atomic factorization; such a divisor need
not appear in any list produced here. No IDF conclusion follows from
the finite atomic-factorization theorem alone.
