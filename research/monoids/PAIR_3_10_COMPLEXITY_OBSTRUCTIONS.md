# Bounded-run finiteness and a finite-prefix obstruction at (3/10,7/5)

Source status: the canonical digits and conductor were reported by ppdppd
on October 16, and non-atomicity and the integer factorization result on
October 24, in the discussion excerpt supplied by the user. See
[SOURCE_STATUS.md](SOURCE_STATUS.md). The inaccessible draft PDFs have not
been checked; no novelty claim is made for the additional reductions or
algorithms here. IDF for this pair remains unresolved.

These are restrictions on the unresolved endpoint-atom criterion, not a
solution of IDF. Put q=3/10, r=7/5=2(1-q). A normalized endpoint atom has
a finite word

  x=sum_{i=0}^{n-1} d_i*q^i+2*q^n,
  d_i in {0,1,r}, d_0 in {1,r},

and trailing digits r before the final2 may be collapsed. The exact
endpoint-atom theorem and the reduction to fixed outside numerator M
are proved in PAIR_3_10_CRITICAL_REDUCTION.md.

## 1. Fixed M and a bounded number of digit runs give finitely many atoms

Fix M coprime to30 and a nonnegative integer K. There are only finitely
many distinct endpoint values with outside-{2,5} numerator M and with
at most K constant-digit runs in the finite prefix.

The proof uses the standard S-unit theorem in its legitimate fixed-length
form: a linear equation with fixed nonzero rational coefficients has
only finitely many nondegenerate solutions in a fixed finitely generated
multiplicative subgroup of Q^*. Here nondegenerate means that no
nonempty proper subsum of the equation, including its constant term,
vanishes.

Take a collapsed prefix with exactly k runs, k<=K, and let

  0=m_0<m_1<...<m_k=n

be its run boundaries. Let a_j in {0,1,r} be its successive run digits,
so a_j!=a_{j-1}, a_0 in {1,r}, and a_{k-1} in {0,1} after collapse.
Multiplying the endpoint expression by 1-q gives

  (1-q)*x = a_0
    +sum_{j=1}^{k-1}(a_j-a_{j-1})*q^{m_j}
    +(r-a_{k-1})*q^n.

Every displayed coefficient is nonzero and has 3-adic valuation0:
their absolute values belong to {1,r,r-1}, with r-1=2/5. The powers
of q on the right have distinct nonnegative exponents. Thus no
nonempty subset of the right-hand terms can sum to zero: its least
3-adic valuation occurs in a unique term. A proper vanishing subsum
including the left-hand term would leave a nonempty vanishing subsum
on the right. Hence the whole equation is nondegenerate.

Write x=M*2^u*5^v. Its variable S-unit part and all the powers q^{m_j}
belong to the fixed group Gamma=<2,3,5>. Divide the equation by a_0,
move the constant term to the other side, and apply the fixed-length
S-unit theorem. For a fixed run pattern (a_0,...,a_{k-1}) this leaves
only finitely many values of 2^u*5^v, and hence of x. There are only
finitely many patterns with k<=K. The constant endpoint2 is handled
separately.

Consequently any infinite fixed-M family witnessing non-IDF must have
unbounded numbers of digit transitions. This statement does not apply
the S-unit theorem to unbounded-length sums; allowing K to grow is
exactly the unresolved case.

A separate argument also excludes a fixed repeated digit block. For a
fixed block of length h, its k-fold repetition followed by the terminal2
has value x_k=A+B*q^{h*k}, with fixed rational A,B, by the geometric-sum
formula. When A and B are nonzero, the fixed-length S-unit theorem
applied to M*2^u*5^v=A+B*q^{h*k} gives only finitely many possibilities.
If B=0, the values are identical. If A=0, the values are a fixed
multiple of q^{h*k}; their 3-adic valuations cannot stay0 for infinitely
many k. The same argument applies when a fixed prefix and suffix are
attached, provided the result still has the form A+B*q^{h*k}. This
excludes such fixed-period constructions without confusing them with
bounded-run words.

## 2. Every fixed finite critical prefix is passed infinitely often

Fix M coprime to30 and a nonempty finite digit prefix d_0,...,d_{k-1}, where
all digits belong to {0,1,r} and d_0 is1 or r. Put

  P=sum_{i=0}^{k-1} d_i*q^i.

There are infinitely many rationals x=M*2^u/5^n, with u,n positive
and n arbitrarily large, whose first k canonical digits are precisely
this prefix and whose remaining real tail lies in (1,2).

The desired real interval is

  P+q^k < x < P+2*q^k.

Every remaining tail in (1,2) gives all preceding tails in [0,2], since
0<=d_i<=r and r+2q=2. The initial value is in [1,2] because its first
digit is nonzero.

The prefix P is a unit modulo3^k R. Since2 is a primitive root modulo
3^k, choose u_0>=0 so

  M*2^{u_0} == P modulo3^k R.

Let T=phi(3^k). For nonnegative i,j, the numbers

  M*2^{u_0+T*i}/5^{T*j}

have this same residue, because2^T and5^T are congruent to1 modulo3^k.
Their logarithms meet every open real interval infinitely often with
i,j arbitrarily large: log2/log5 is irrational, so the differences
i*log2-j*log5 are dense, also after imposing lower bounds on i,j.
Choose values in the displayed real interval. Then

  (x-P)/q^k belongs R and lies in (1,2).

The congruence modulo3^k makes each of the first k canonical digit
choices equal to the prescribed digit. Thus the prefix condition holds,
and n=T*j is arbitrarily large.

In particular, no fixed finite list of initial canonical-digit tests
or congruence conditions can exclude all sufficiently deep candidate
powers. This does not show that any of these candidates complete to
critical endpoints: their later digits may, and generally do, leave
[0,2]. It explains why a full proof needs control that grows with the
denominator exponent.
