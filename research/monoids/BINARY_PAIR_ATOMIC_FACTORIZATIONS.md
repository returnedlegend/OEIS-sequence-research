# Membership and all atomic factorizations for N_0[2/5,2/3]

Put q=2/5, r=2/3, h=5/3, S=N_0[q,r], and R=Z[1/15].
This note uses the independently audited atom classification in
PAIR_2_5_2_3.md. It does not resolve IDF. Novelty has not been checked.

Nevertheless, membership in S is decidable by a terminating exact
algorithm, and **every element has only finitely many atomic
factorizations, all effectively enumerable**. Some elements have none.
This does not make S an atomic monoid or an FFM.

The implementation is `binary_pair_factorizations.py`, which reuses the
exact polynomial helpers in `reciprocal_factorizations.py`.

## 1. A terminating membership algorithm

We know R intersect [h,infinity) is contained in S. Also

    q*S = S intersect 2R.

For the nontrivial inclusion, write x in S as a nonnegative polynomial in
q and r. If x is in 2R, its constant coefficient is even. Every constant
2 is q*5, and every nonconstant monomial is divisible by q in S because
r=q(1+r). Thus x/q is in S.

For x in R with 0<x<h, let c be its residue modulo 2, represented by 0 or
1. If c=0, the displayed equality gives x in S iff x/q in S. If c=1,
any S-representation has an odd constant coefficient. Since x<h<2, that
coefficient must be exactly 1. Thus x<1 is impossible, and otherwise
x is in S iff (x-1)/q is in S.

The algorithm is therefore:

1. Reject negative x or denominators having primes outside {3,5}.
2. Accept x=0 or x>=h.
3. Otherwise put c=x mod 2 in {0,1}. Reject if x<c; replace x by (x-c)/q
   if x>=c, and repeat.

All operations are on rational numbers. Here x mod 2 is simply the parity
of its reduced numerator, since its denominator is odd.

### Termination

Each digit step reduces a positive exponent of 5 in the denominator by
one, and no step increases the exponent of 3 in the denominator. After
finitely many steps, any unresolved state has the form y=N/3^d in lowest
terms, with 0<y<h.

First suppose d>=2 and put m=3^d. A digit step stays in [0,h] only if
the residue a=N mod m is even and at most 2m/3. Indeed, the only possible
representatives in [0,hm] are a and a+m. The lower one can continue only
when it is even and at most 2m/3; the upper one can continue only when
it is odd, which likewise requires even a and a<=2m/3.

The residue at the next step is (5/2)a modulo 3^d. The element 5/2 has
order 3^(d-1) modulo 3^d, because

    v_3(5^j-2^j)=1+v_3(j)

by the elementary lifting-the-exponent identity. It therefore generates
the principal-unit subgroup. Since N is coprime to 3, its orbit visits
every residue in its fixed nonzero class modulo 3, including an odd
residue. At that point an unresolved digit step is impossible. The
algorithm must have accepted or rejected by then.

For d=1, the only possible persistent residue is 2 modulo 3. Its only
unresolved state is 2/3, which maps directly to h. For d=0, the only
positive unresolved integer is 1, which maps to 0. Thus the algorithm
terminates in every case. A safe bound on the number of steps is

    e + 1 + 3^max(d-1,0),

where the original reduced denominator is 3^d*5^e. This is a termination
bound, not an efficiency claim.

## 2. Atom data needed for the factorization bounds

The atoms are:

- q, with v_2(q)=1;
- h, with v_3(h)=-1 and v_5(h)=1;
- finite binary polynomial atoms beta=N/5^n, n>=1, where
  N=M*3^k, gcd(M,30)=1, k>=0, and 1<beta<h;
- other binary endpoint atoms alpha=N/(3*5^i), i>=1, where
  gcd(N,30)=1 and 1<alpha<h.

All atoms except q have 2-adic valuation zero. For a finite binary atom,
v_3(beta)=k; for an endpoint other than h, v_3(alpha)=-1. Every endpoint
other than h has a nontrivial numerator part outside {2,3,5}.

An endpoint has the unique canonical form

    alpha=f(q)+q^i*r,

where f is binary, f(0)=1, and deg(f)<i. Conversely every such expression
is an atom. A finite binary f(q), with f(0)=1 and deg(f)>0, is an atom
exactly when f is formally irreducible in N_0[X].

## 3. Explicit bounds for any atomic factorization

Fix x in S minus {0}. Define

    E=v_2(x),
    y=x/q^E,
    W=the numerator part of x supported outside {2,3,5},
    Omega=sum of the prime-factor multiplicities of W,
    H=max{j>=0 : h^j<=y}.

The equality q*S=S intersect 2R shows y is in S. It has 2-adic valuation
zero, so y>=1. All quantities above are therefore well-defined. H is
computed by exact repeated multiplication, not floating-point logarithms.

In any atomic factorization:

1. q occurs exactly E times.
2. h occurs at most H times, because all remaining factors exceed 1.
3. Other endpoint atoms occur at most Omega times: each consumes at least
   one prime factor of W.
4. If the finite binary atom factors have 3-adic valuations k_1,...,k_t,
   then the 3-adic valuation balance gives

       sum k_j = v_3(x) + (# h factors) + (# other endpoint factors)
               <= K := v_3(x)+H+Omega.

If K<0, there is no atomic factorization. Otherwise every finite binary
atom appearing has numerator M*3^k with M|W and 0<=k<=K. Its denominator
5^n is bounded by 5^n<M*3^k. Every other endpoint appearing has numerator
N|W and 3*5^i<N. These are finite, explicit candidate lists.

The possible degree n for a fixed finite numerator is actually unique:
1<N/5^n<h, an interval whose endpoint ratio is smaller than 5.

There is also a bound on atomic factorization length. Finite binary atoms
whose outside numerator part is 1 have k>=1, so their number is at most
sum k_j. All other atoms except q and h consume a prime factor of W, so
their total number is at most Omega. Hence, whenever a factorization
exists, its length is at most

    E + v_3(x) + 2H + 2Omega.

## 4. Complete finite enumeration

The algorithm generates all candidates allowed by Section 3:

- h, if H>=1;
- N/(3*5^i) with N|W and 1<N/(3*5^i)<h, retaining precisely those for
  which N/(3*5^i)-q^i*r has a binary q-polynomial representation of
  degree less than i and constant coefficient 1;
- M*3^k/5^n with M|W, 0<=k<=K, and 1<M*3^k/5^n<h, retaining precisely
  those with a binary q-polynomial representation that is formally
  irreducible.

The polynomial membership and irreducibility tests are the exact finite
algorithms already documented in RECIPROCAL_ALGORITHM.md. Every retained
candidate is an actual atom. The list can include atoms that do not
participate in a factorization of x; it is only a finite superset for
this purpose, not a claimed complete list of all atom divisors of x.

Finally enumerate products of these finitely many candidates, with q
fixed at exponent E. All candidates exceed 1, so the real size bound
on the remaining product makes every exponent loop finite. Retain exactly
the products equal to x. This returns every atomic factorization and
only atomic factorizations.

There is no conflict with the open IDF question: infinitely many atom
divisors, if they exist, can have cofactors admitting no atomic
factorization. Such atom divisors would never occur in this finite list
of complete factorizations.

## 5. Small explicit consequences

Both 3 and 5 have W=1 and K=3. Thus their only possible finite binary
atom numerators are 1,3,9,27. The only value in the requisite interval
with positive degree is 27/25; its canonical digit test fails because

    27/25 = 1 + q*(1/5),

and 1/5 has odd numerator but is below 1. There are no other endpoints
because W=1. Powers of h cannot equal 3 or 5, so neither integer admits
an atomic factorization. Since 2=q*5 and q is the only atom of positive
2-adic valuation, 2 has no atomic factorization either.

This does not say those integers have no atom divisors. In particular,
3=h*(9/5), and 9/5=1+2q lies in S.

The earlier witness 125/81 has E=0, H=0, W=1 and K=-4, so the valuation
budget immediately rules out an atomic factorization.

Example commands:

    python binary_pair_factorizations.py 19/15
    python binary_pair_factorizations.py 3
    python binary_pair_factorizations.py 27/25 --membership

No claim about the novelty of these consequences is made.

## 6. A checked nonunique factorization

The algorithm returns exactly the following two atomic factorizations:

    133/75 = (7/5)*(19/15) = (5/3)*(133/125).

They arise from the formal identity

    (1+X)*(1+X^2/(1-X)) = (1+X^3)/(1-X).

All four factors are atoms by the exact classification. More generally,
for every d,m>=1, the binary eventually-1 series

    E_(d,m)(X)=(1-X^d+X^(2d)-...+X^(2md))/(1-X)

is an endpoint atom, and

    (1+q^d)*E_(d,m)(q) = h*(1+q^((2m+1)d))

gives two atomic factorizations. This supplies an infinite family of
nonunique factorizations, not infinitely many factorizations of a fixed
element.

`check_binary_pair.py` checks generated semiring values, explicit
nonmembers, the non-atomic witnesses, the displayed two-factorization
identity, and exact reconstruction of returned factorizations.

## 7. An equivalent form of a sufficient, unproved IDF conjecture

Consider the assertion

    v_3(sum_(j=0)^n c_j 2^j5^(n-j)) <= n

for every finite binary polynomial with c_0=c_n=1. This assertion is
unproved. If true, it would imply IDF, since a fixed outside numerator
part M would satisfy M>= (5/3)^n.

There is a precise structural reformulation: the assertion holds if and
only if every positive integer admitting an atomic factorization is
coprime to 30.

If f(q)=M*3^k/5^n has k>n, then f(q) has an atomic factorization by
formal polynomial factorization. Multiplying by atoms gives the three
atomic integers

    f(q)*h^n       = M*3^(k-n),
    f(q)*q*h^(n+1) = 2M*3^(k-n-1),
    f(q)*h^(n+1)   = 5M*3^(k-n-1).

Conversely, in any atomic factorization of a positive integer I, adding
the 2-, 3-, and 5-adic valuation equations gives

    v_2(I)+v_3(I)+v_5(I)
      = sum_(finite binary factors) (k_j-n_j)
        -sum_(other endpoint factors) (i_j+1).

If I has a prime factor in {2,3,5}, the left side is positive, so some
finite binary atom has k_j>n_j. The atomwise bound and the bound for all
finite binary polynomials are equivalent, because formal factorizations
add degrees and 3-adic valuations.

Equality cases do occur. The binary atom f=1+X+X^4 has

    f(q)=891/625=11*3^4/5^4,
    11=h^4*f(q).

Thus 11 admits an atomic factorization even though 2,3,5 do not.

A counterexample to the conjectured valuation bound would not by itself
disprove IDF; it would invalidate this particular sufficient criterion.
