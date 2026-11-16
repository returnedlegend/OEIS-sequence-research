# Exact gap exclusions for binary values at 2/5

This is a finite computational result, not a proof of IDF. Novelty has not
been checked. The packaged exact script is `binary_ratio_gap_search.py`. The initial
200,000-gap run used the equivalent scratch implementation
`/tmp/search_cantor_ratios.py`; its run log is
`/tmp/cantor_ratio_search_200000.log`.

Let q=2/5. Suppose F,G are distinct finite binary polynomials with constant
and leading coefficients 1, and their evaluated values have the same
numerator part supported outside {3,5}. They cannot have the same degree:
then their values would differ by a power of 3, but both lie in [1,5/3),
so the power is 1 and uniqueness of bounded polynomial evaluation gives
F=G. Interchange them if necessary and write n=deg(F)>m=deg(G), L=n-m. Their reduced
numerators are M*3^u and M*3^v, respectively, so

    F(q)/G(q) = A/B,  A=3^K, B=5^L, K=u-v.

Because every such value lies in [1,5/3),

    3/5 < A/B < 5/3.

For L>=1 this forces K>0. There is at most one such K for each L, since
the ratio of the upper to lower endpoint is 25/9<3. The script finds K
using only integer comparisons: first require 5A>3B, then check 3A<5B.

For coefficients f_j,g_j, define the remaining evaluated difference

    e_j = sum_(i>=j) (B*f_i-A*g_i) q^(i-j).

Then e_0=0 and

    e_(j+1) = (5/2)(e_j-B*f_j+A*g_j).

Every e_j is an integer. Indeed the recurrence places it in Z[1/2], while
its finite tail expression places it in Z[1/5], and these rings intersect
in Z. Every e_j for j>=1 is divisible by 5. Set z_j=e_j/5. Because
f_0=g_0=1, the initial state is

    z_1=(A-B)/2.

All subsequent states lie in the finite integer interval

    -A/3 <= z <= B/3,

and satisfy

    z'=(5z-B*f+A*g)/2,  f,g in {0,1}.

Parity leaves exactly two potential transitions:

- if z is even: 5z/2 and (5z+A-B)/2;
- if z is odd: (5z-B)/2 and (5z+A)/2.

Discard transitions outside the interval. Once both polynomials end, the
state is 0. Thus a necessary condition for such F,G is that 0 be reachable
from (A-B)/2 in this finite directed graph. It is also sufficient: any
finite path to 0 records finite binary digit strings starting with 1,
which give the required evaluated equality. Trimming terminal zero digits
recovers the degree difference L because the reduced denominators of F(q)
and G(q) are 5^n and 5^m.

Using closed interval endpoints is harmless: it can only add states.
In fact a path to zero still gives actual finite polynomials, so an added
endpoint cannot create a spurious equality.

## Run result

The exact search over all L=1,...,200000 found:

- 185,989 real-admissible pairs (L,K);
- no path from the initial state to 0;
- no directed cycle reachable from the initial state;
- at most 1,836 reachable states for any pair;
- maximum BFS shortest-distance from an initial state 62.

The last statistic is not a claim about the longest path in a graph with
merged branches. The packaged implementation separately computes longest
path lengths for acyclic graphs.

No search cap was reached. The run took approximately 277 seconds.

Consequently, any two distinct finite binary polynomials whose evaluated
values share the same numerator part outside {3,5} have degree difference
greater than 200,000.

The conclusion is uniform in their individual degrees and in M. It is
stronger than checking all polynomials up to a maximum degree, but it does
not rule out infinitely many solutions with successively larger gaps.

## Why finite-prefix tests need not settle the infinite problem

The archimedean size restriction and a prescribed residue modulo 2^r can
be met by suitable ratios 3^K/5^L with K,L>0. Thus increasingly long
surviving prefixes are not unexpected. A uniform finiteness proof needs
more than extrapolating from the small graphs observed in finite runs.

An elementary additional obstruction is

    2^L = 3^K (mod 5), or L = 3K (mod 4),

from the leading binary coefficients. This rejects many ratios before
the graph search. The current implementation does not rely on this
shortcut; it searches all real-admissible ratios.

## Small reproducer

    python binary_ratio_gap_search.py --max-gap 10000
    python check_binary_ratio_gap.py

The first command uses exact integers and finishes quickly. It excludes
all 10,000 gaps, with 9,299 real-admissible ratios and at most 449 reachable
states per ratio. The script reports an explicit inconclusive status if
its state cap is reached and never treats that case as an exclusion.

The finite graph proof and the original search were independently audited.
The audit also checked all 4,096 ordered ratios from binary polynomials
through degree 6 and independently compared 676 odd numerator/denominator
pairs up to 51, reconstructing every returned witness exactly.
