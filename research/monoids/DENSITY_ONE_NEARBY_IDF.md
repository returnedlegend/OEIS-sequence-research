# A density-one IDF theorem for the nearby ternary family

This is an asymptotic classification of an infinite one-parameter family,
not a complete classification of all rational pairs. Novelty relative to
the full online discussion remains unverified.

## Main theorem

Let

    A={n>=4: gcd(n,21)=1, 5n has at least two prime divisors},
    M_n=N_0[3/(5n),7/5] minus{0}.

For a subset of A of relative natural density ONE, M_n is IDF and non-atomic.
In fact every M_n with n in A is non-atomic: no integer greater than1 has an
atomic factorization. Only the IDF conclusion needs the density argument.

There is an explicit terminating certificate search on a density-one set
of parameters. No claim is made that it terminates for every n, or that
any exceptional parameter is non-IDF. The original n=2 pair(3/10,7/5)
is outside this theorem and remains unsettled for IDF.

## 1. The finite word tree

Write q_n=3/(5n), r=7/5, and D={0,1,r}. For all n in A the established
nearby digit theorem gives conductor C_n=r/(1-q_n)<2, finite critical
D-words, trivial units, and finite-D-word expressions for every atom.

A negative5-adic valuation is absorbing under every prefix x->d+q_n*x:
q_n*x then has valuation at most-2, below every digit's valuation.
Therefore every5-integral critical value is obtained from the terminal1
by repeatedly prefixing digits while retaining5-integrality.

If5 divides n, or if n!=1 modulo5, no first prefix is5-integral and the
tree is trivial. Otherwise the first prefix must be r, because

    r+q_n=(7n+3)/(5n)

is5-integral exactly when n=1 modulo5.

For fixed n, define a word by its CONSTRUCTION order: start at1 and read
digits d_1,...,d_L, replacing x by d_j+q_n*x at each step. Retain a word
when every intermediate value is5-integral. A finite closed prefix-word
tree is an all-height IDF certificate by NEARBY_TERNARY_CARRY_CERTIFICATES.md.
Its finitely many values contain every atom with nonnegative5-adic
valuation; all other atoms have nonpositive valuation at every denominator
prime, giving the finite numerator bound.

## 2. Polynomial numerators and progression stability

For a word w of length L define the integer polynomial H_w(n) by

    x_w(n)=H_w(n)/(5n)^L,   H_empty(n)=1.

If a new digit is appended to the construction word, the recurrences are

    digit0: H_new=3H_w,
    digit1: H_new=(5n)^(L+1)+3H_w,
    digit r: H_new=7n*(5n)^L+3H_w.                        (1)

When5 does not divide n, a word of length L is5-integral exactly when
H_w(n)=0 modulo5^L. Negative-valuation absorption ensures that final
integrality already forces integrality of all its prefixes.

Suppose a finite closed word tree for n_0 has maximum retained depth h.
To verify closure one checks every child through depth h+1. For any

    n=n_0 modulo5^(h+1),                                 (2)

all those words have exactly the same integrality status, because their
integer polynomials agree modulo5^L at every L<=h+1. Thus the SAME PREFIX-
WORD TREE is closed for every such n satisfying the hypotheses. The rational
state values change with n; it is the finite word tree that remains fixed.

This proof does not infer a height bound from shortest paths in a possibly
merged graph. The stored certificates are explicit prefix-closed word sets,
with every retained child included and every missing child checked. They
therefore control every branch through the boundary depth h+1 directly.

Exact5-adic valuations are also uniform on(2). A state with valuation t>=0
can be prefixed by zero exactly t consecutive times before leaving the tree.
Thus its original depth L satisfies L+t<=h, and the modulus5^(h+1) preserves
that exact valuation of H_w, not merely its integrality.

## 3. Explicit infinite progressions

The two-state trees give IDF and non-atomicity for every admissible n in

    n=1,6,16 modulo25.

The previously exhibited six-state n=46 tree has h=3, so it proves the same
conclusion for EVERY admissible

    n=46 modulo625.

Its maximum positive5-adic valuation remains1 throughout that progression.
These are infinite families inside the earlier omitted class n=1 modulo5.

The existing1142 finite parameter certificates yield112 distinct certified
progressions after duplicate and contained classes are removed. The
progression JSON records a representative and an explicit closed word tree
for every class. Together with n!=1 modulo5, this finite union has relative
density

    1209751876/1220703125 = 0.9910287368192

inside A. This is an exact density of a finite union of arithmetic
progressions, not a numerical estimate of the full IDF set.

## 4. Each word specifies only one parameter residue class

Every retained nonempty word begins with r, so

    H_1(n)=7n+3.

For any word of length L>=1 beginning with r, recurrence(1) gives

    H_w(n)=3^(L-1)*(7n+3) modulo5,
    H'_w(n)=7*3^(L-1) modulo5.                            (3)

The derivative is a unit modulo5. Hence H_w has exactly ONE root modulo
5^L: start from its unique root n=1 modulo5, then lift uniquely at each
stage. Explicitly, if z is a root modulo5^j, then

    H_w(z+t*5^j)=H_w(z)+t*5^j*H'_w(z) modulo5^(j+1),

so exactly one t in{0,1,2,3,4} gives the next root. This is the elementary
simple-root lifting argument; no distribution conjecture is used.

There are at most3^(L-1) words of length L whose first digit is r. Therefore
the parameters admitting ANY retained word of depth L lie in at most
3^(L-1) residue classes modulo5^L. Their upper natural density is at most

    3^(L-1)/5^L = (1/5)*(3/5)^(L-1).                     (4)

Classes may coincide, which only improves this upper bound.

## 5. Density-one termination and IDF

If a prefix-word tree is infinite, it has words of arbitrarily large depth,
because each node has only three children. Its parameter therefore belongs
to the residue-class set in section4 for EVERY L. By(4), the upper natural
density of parameters with infinite trees is at most3^(L-1)/5^L for every L,
and consequently is ZERO.

Every remaining admissible parameter has a finite closed tree and hence an
IDF certificate. The admissible set A has natural density4/7: coprimality
with21 contributes(1-1/3)(1-1/7), while the excluded powers of5 have density0.
Thus the zero-density exceptional set also has relative density0 in A.
Equivalently the certified IDF/non-atomic parameters have relative density1.

The quantitative bound(4) is valid conditionally inside A as well: congruence
modulo5^L is independent of coprimality with21 by the Chinese remainder
theorem. For example, a full tree search through depth10 certifies a set of
relative density at least

    1-3^9/5^10 = 0.9979844608.

This is a proved lower bound for a finite-depth certification procedure.
It does not assert that the remaining parameters fail IDF.

There is also a power-saving finite-range bound. For N>=2 set

    k=ceil(log_5 N).

Each residue class modulo5^k contains at most one integer in[1,N]. Hence
at most3^(k-1) parameters in that interval can have a retained word of depth
k. Every other admissible parameter has a finite tree of height below k,
and is therefore explicitly certified IDF. In particular the number of
uncertified admissible parameters is at most

    3^(ceil(log_5 N)-1) <= N^(log_5 3),

where log_5(3) is approximately0.682607. This upper bound concerns failure
of this finite-depth certificate, not actual failure of IDF.

## 6. Scope and reproducibility

The short helper nearby_progressions.py constructs and independently checks
explicit closed WORD trees, then records their stable arithmetic progressions.
The attached nearby_progression_certificates.json contains the112 classes
used in section3 and exact rational density totals. Closure verification
uses rational arithmetic and explicitly tests every boundary child.

The density-one proof itself is independent of those computations: it uses
only the polynomial recurrences, unique simple-root lifting, and the
three-branch counting bound. Existing conductor, critical-orbit, and
perturbation tools come from the supplied discussion and the preceding
notes; no claim is made that those general methods originated here.
