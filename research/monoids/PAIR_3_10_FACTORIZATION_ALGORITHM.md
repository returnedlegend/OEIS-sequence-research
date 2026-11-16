# Finite atomic factorizations at (3/10,7/5), with an exact algorithm

Source status: the canonical digits and conductor were reported by ppdppd
on October 16, and non-atomicity and the integer factorization result on
October 24, in the discussion excerpt supplied by the user. See
[SOURCE_STATUS.md](SOURCE_STATUS.md). The inaccessible draft PDFs have not
been checked; no novelty claim is made for the additional reductions or
algorithms here. IDF for this pair remains unresolved.

Let q=3/10, r=7/5, and S=N_0[q,r]. Every nonzero S-element has only
finitely many factorizations into atoms, up to ordering. Some elements
have none, so this is not a claim that S is an atomic or finite
factorization monoid. It also does not settle IDF: an atom divisor with
a non-atomic cofactor need not occur in any atomic factorization.

The algorithm below decides whether each S-element has an atomic
factorization and enumerates all such factorizations. It uses exact
integer and rational arithmetic. No complexity claim is intended.

## 1. Atom valuations

The complete atom description in PAIR_3_10_ATOM_ALGORITHM.md gives:

* q is the only atom below 1, and v_3(q)=1.
* Every other atom is critical and lies in [1,2], with v_3=0.
* 2 is the only atom with v_5=0.
* For every atom alpha other than q and 2, the least exponent d with
  denominator(alpha) dividing 10^d satisfies d=-v_5(alpha)>=1.

For the last statement, examine the highest critical digit after
collapsing a trailing r immediately before terminal 2. A highest
ordinary digit 1 or terminal 2 at q-degree d has 5-adic valuation -d;
a highest r at q-degree d-1 has valuation -d. The 2-adic valuation in
each case is at least -d, so this is also the minimal 10-denominator
degree. The constant ordinary atom is 2; the generator r has degree 1
in this denominator sense despite having q-degree zero.

Canonical division also gives the exact identity

  q*S = S intersect 3*Z[1/10].

Indeed a value divisible by 3 in Z[1/10] has canonical digit zero, and
the membership algorithm shows that division by q stays in S. The
opposite inclusion is immediate.

## 2. Uniform bounds for a fixed input

Fix x in S minus {0}, and set

  e=v_3(x),   y=x/q^e.

The preceding identity shows y belongs S, v_3(y)=0, and y>=1. Every
atomic factorization of x contains exactly e copies of q; its other
factors form an atomic factorization of y.

If v_5(y)>0, y has no atomic factorization, since every remaining atom
has nonpositive 5-adic valuation. Otherwise put n=-v_5(y)>=0. In any
atomic factorization of y, the positive denominator degrees of its
atoms other than 2 sum exactly to n. There are therefore at most n
such factors, each with degree at most n. The multiplicity of 2 is
at most

  K=floor(log_2 y),

because every other factor is at least 1. Thus every atomic
factorization of x has length at most e+n+K.

All possible non-2 atoms have denominator dividing 10^n and value in
[1,2), so they lie in a finite rational grid. This already proves
finiteness of the atomic factorizations.

## 3. A smaller explicit candidate list

Let X be the part of y's reduced numerator supported outside {2,5}.
The outside numerator M of every atom in a factorization divides X.
For each M|X and each d in {1,...,n}, there is exactly one integer u
for which

  1 <= M*2^u/5^d < 2.

Compute this u by repeatedly multiplying or dividing the rational
M/5^d by 2. Test the resulting value alpha with the terminating atom
algorithm and, optionally, retain it only if y/alpha belongs S.

This list contains every non-2 atom in any atomic factorization of y.
It has at most n*tau(X) entries before rejection. Some retained atoms
may divide y with a non-atomic cofactor; the final product test handles
this distinction.

## 4. Enumeration

For every integer k from 0 through K and every multiset of retained
atoms alpha_i whose degrees sum to n, test the exact equality

  y = 2^k * product_i alpha_i.

Keep precisely the successful multisets, and prepend e copies of q.
All loops are finite: each atom degree is positive, so a multiset has
at most n members. Conversely every atomic factorization satisfies
all the bounds and is retained. The unit has the empty factorization;
an empty output for a nonunit certifies that it has no atomic
factorization.

The separate implementation critical_pair_factorizations.py imports
the atom predicate from critical_pair_atoms.py. It enumerates
multisets in nondecreasing order using an explicit stack, avoiding a
recursion through the entire candidate list.

For example, 3 and 5 have no atomic factorizations, whereas

  24/25 = q * 2 * (8/5),
  91/50 = (13/10) * (7/5)

are atomic factorizations. Removing the forced q from 3 leaves 10,
whose positive 5-adic valuation certifies failure of atomicity.

A nonunique example, with exactly two atomic factorizations, is

  142753/100000 = (139/100)*(1027/1000)
               = (13/10)*(10981/10000).

This comes from the formal identity

  (1+X+X^2)*(1+X^3)=(1+X)*(1+X^2+X^4)

at X=q. The exact algorithm certifies that all four displayed factors
are atoms and that the two listed factorizations are exhaustive.

## Scope

This is a complete per-element algorithm for atomic-factorization
existence and enumeration. It does not enumerate all atom divisors
and does not prove or disprove IDF of S.
