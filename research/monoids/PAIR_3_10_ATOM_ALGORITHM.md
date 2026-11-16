# Exact atom decision at (3/10,7/5)

Source status: the canonical digits and conductor were reported by ppdppd
on October 16, and non-atomicity and the integer factorization result on
October 24, in the discussion excerpt supplied by the user. See
[SOURCE_STATUS.md](SOURCE_STATUS.md). The inaccessible draft PDFs have not
been checked; no novelty claim is made for the additional reductions or
algorithms here. IDF for this pair remains unresolved.

Put q=3/10, r=7/5, S=N_0[q,r], and R=Z[1/10]. This note gives a
terminating atom-decision algorithm. It does not decide IDF or give an
eventual bound for atom divisors of a fixed element. It uses the
critical-value representation theorem in PAIR_3_10_CRITICAL_REDUCTION.md;
the proof ingredients needed here are recalled below. No novelty claim
is made.

## 1. Exact membership and criticality

For y in R, choose d from {0,1,r} matching its residue modulo 3R and
replace y by (y-d)/q. Stop at the first integer. Each step lowers the
least exponent n for which the denominator divides 10^n, so the process
terminates. Negative tails certify nonmembership. Nonnegative terminal
integers certify membership through the resulting nonnegative expression.

The necessity follows from the real conductor R intersect [2,infinity)
subset S and the possible q-degree-zero polynomials of value below 2:
0,1,Y,Y^2. The selected digit is forced except for Y^2; in that case

  r^2=1+q*(16/5),

and 16/5 belongs S by the conductor. Thus canonical subtraction and
division preserve S. Denominators with primes other than 2,5 are rejected
before starting.

A value in R intersect [0,2] is called critical when every canonical
tail lies in [0,2]. Every atom other than q is a critical value in [1,2].
Indeed q is the only possible atom below 1, and a value or canonical
tail above 2 forces reducibility by the near-one smooth-factor argument
from PAIR_3_10_7_5.md. The element q is an atom because its only polynomial
expression is X: every expression for q has zero q-degree-zero part and
dividing by q gives the unique expression 1 for the unit.

## 2. Complete representations and endpoint atoms

For a critical value, the canonical digit is forced at every noninteger
tail. The possible alternative Y^2 would make the next canonical tail
at least 16/5>2. The terminal values 0 and 1 have only their constant
expressions. The expressions for 2 are precisely

  F_m(X,Y)=2X^m+Y*(1+X+...+X^{m-1}),  m>=0.

Consequently a critical value terminating at 0 or 1 has a unique
nonnegative polynomial expression. A critical value terminating at 2,
with prefix P and terminal depth n, has exactly the expressions

  P(X,Y)+X^n F_m(X,Y),  m>=0.

All these expressions have Y-degree at most 1. Every coefficient is 0
or 1 except the unique highest-X-degree coefficient, which is the pure
ordinary coefficient 2. At each X-degree the ordinary and Y
coefficients are disjoint. Every q-tail of every representation has
value at most 2.

**Every critical value in [1,2] terminating at 2 is an atom.**

In fact the following stronger formal lemma proves this immediately.
Suppose a nonnegative polynomial F(X,Y) has nonzero X-constant part,
highest-X-degree coefficient equal to the constant 2, and all lower
monomial coefficients at most 1. Then F is multiplicatively irreducible
in N_0[X,Y]. For if F=G*H, the highest-X-degree coefficients multiply
to 2, so after interchanging factors they are the constants 1 and 2.
Both X-constant parts are nonzero. If G has positive X-degree, multiply
its nonzero X-constant part by the top term of H: this creates a
coefficient at least 2 below the highest X-degree of F, a contradiction.
Thus G has X-degree zero, and its highest-X-degree coefficient being
the constant 1 means G=1.

Every endpoint-2 representation satisfies this lemma. Expanding any
factorization in S therefore forces a constant polynomial factor 1,
proving the atom assertion. The lemma also covers F_0=2.

## 3. Finite binary divisors suffice for any remaining critical value

For every critical x in [1,2], one has the equivalence

  x is reducible iff it has a proper divisor G(q),
  where G is nonconstant, binary, and G(0)=1.

The reverse implication is immediate. For the forward implication, in
any proper factorization at least one factor has an ordinary polynomial
expression, because the product has Y-degree at most 1. Both factors
have v_3=0 and are at least 1, so an ordinary factor has positive
constant term. Properness forces that constant to be 1. If this ordinary
factor has a coefficient 2, the other factor cannot contain Y or any
coefficient 2: the product would contain a coefficient at least 2 on Y,
or a coefficient at least 4. In that case the other factor is ordinary
and binary. Thus in every case a proper factorization supplies a
nonconstant ordinary binary polynomial G(X), with G(0)=1. Both it and
its cofactor are greater than 1. In particular G(q)<x.

Let M be the part of the reduced numerator of x supported outside 2,5.
For such a binary polynomial G of degree d, write

  G(q)=N/10^d,
  N=sum_{i=0}^d G_i*3^i*10^{d-i}.

The constant and top coefficients are 1. Thus N>=10^d, N is odd, and
5 does not divide N. If G(q) divides x in S, the cofactor belongs R,
so N divides M. Hence every possible binary factor occurs in the finite
list

  N/10^d,  N|M,  N>1,  1<=d<=floor(log_10 N).

To decide whether a listed number has a binary polynomial expression,
apply the ordinary cyclic digit algorithm for q=3/10: successively
choose c_i in {0,1,2} matching the current value modulo 3R and divide
the residual by q. The denominator exponent drops by one per step.
Keep the value only when its constant and highest coefficients are 1
and every coefficient is 0 or 1. This representation is unique.

For every retained value g<x, apply the exact S-membership algorithm to
x/g. Any successful test supplies a proper factorization. If all tests
fail, x is an atom. Integer factorization, divisor enumeration, and
canonical digit calculation are all elementary terminating algorithms;
no efficiency estimate is claimed.

## 4. Complete algorithm

For a positive rational x:

1. Test membership in S by section 1. Reject inputs outside S.
2. The unit 1 is not an atom, and q is an atom.
3. Other values below 1, values above 2, and noncritical values in [1,2]
   are reducible.
4. A critical value terminating at 2 is an atom by section 2.
5. For every other critical value, perform the finite binary-divisor
   search in section 3. It is an atom exactly when no proper binary
   divisor is found.

The implementation is critical_pair_atoms.py. It uses exact Python
integer and Fraction arithmetic. For example:

  python critical_pair_atoms.py 3/10 7/5 2 8/5 1417/1000 91/50 3

The values q,r,2,8/5 are atoms. The critical value 1417/1000 factors as
(13/10)*(109/100), and 91/50 factors as (13/10)*(7/5). The integer 3
is reducible and has no atomic factorization.

## 5. Consequences and limits

All endpoint-2 values in the unresolved fixed-outside-numerator IDF
criterion are atoms, so no irreducibility test is needed for those
candidates. Critical values terminating at 0 or 1 have unique polynomial
expressions and are atomic by formal polynomial factorization. This
also gives a short alternative proof that every critical value in [1,2]
is atomic.

The algorithm decides whether each individual rational is an atom. It
does not prove that a fixed numerator class has only finitely many
endpoint atoms, which remains the IDF obstruction.
