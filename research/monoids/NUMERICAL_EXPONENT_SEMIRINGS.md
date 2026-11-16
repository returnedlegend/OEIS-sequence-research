# IDF and non-atomic semirings with a numerical semigroup of exponents

The result below extends the cyclic block-condition family to genuinely
nonredundant pairs of contracting generators. Its novelty relative to the
full discussion and attached PDFs remains unverified.

Let H be a numerical semigroup: an additive submonoid of N_0 containing0
whose complement is finite. Write c_H for its conductor, so every integer
at least c_H is in H, and let m be its least positive member. Let

    t=a/b,   gcd(a,b)=1,   a>=2,
    P={p:p|b},   |P|>=2,
    a<p^(v_p(b)) for every p in P.                          (1)

Put

    M=N_0[t^h:h in H] minus {0},   R=Z[1/b],
    C_m=(a^m-1)/(1-t^m),   D=b/rad(b).

Then M is IDF and non-atomic. In particular, for coprime positive integers
i,j, the pair(t^i,t^j) belongs to the requested IDF/non-atomic family.
The pair is genuinely nonredundant whenever neither i nor j divides the
other. The statement includes H=N_0 as the earlier cyclic theorem.

## 1. Real conductor, units, and perturbations

The semiring N_0[t^m] is contained in M and has ambient localization R.
Its cyclic conductor gives

    R intersect [C_m,infinity) subset M.                    (2)

The units of M are {1}. Indeed M is contained in N_0[t], which has trivial
units. Every P-smooth M-element is at least1: an element below1 has no
constant term, so its valuation at every prime dividing a is positive.

There are distinct P-smooth elements u_L in M tending to1 from above,
with u_L-1 in a^(mL)R. Choose two different primes in P and take suitable
powers congruent to1 modulo a^(mL). Their multiplicative group is dense.
Choose u_L in

    1+C_m*t^(mL) < u_L < 1+(C_m+1)*t^(mL).

Then (u_L-1)/t^(mL) belongs R and exceeds C_m, hence belongs M by (2).
Since t^(mL) belongs M, u_L belongs M.

If an element x of M has an expression

    x=f(t)+c*t^j,

where f has nonnegative coefficients supported on H, j in H, and integer
c>C_m, set

    z_L=(x/u_L-f(t))/t^j.

For mL>=j, the congruence puts z_L in R. It tends to c>C_m, so eventually
z_L belongs M. This factors x into the nonunits u_L and x/u_L, omitting
at most one index where the latter could equal1. Consequently every
polynomial expression for an M-atom has all coefficients at most floor(C_m).

## 2. All sufficiently high coefficients of atoms are below a

Condition (1) implies b>a^2, hence b>2a. Suppose a polynomial expression
for an M-atom has a coefficient at least a at some exponent j>=c_H.
Using

    a*t^j=b*t^(j+1)

preserves support in H and exposes a coefficient at least b at degree j+1.
Continuing to carry the largest multiple of a at each successive degree
replaces a coefficient c>=b by at least

    b*floor(c/a) >= (b/a-1)*c.

The multiplier b/a-1 exceeds1. Thus the exposed coefficient eventually
exceeds C_m, contradicting section1. We conclude:

    Every atom expression has coefficient <a at every degree >=c_H.  (3)

Only the finitely many lower-degree positions may have the larger bound
floor(C_m).

## 3. The least exponent of an atom is bounded

Let h be the least exponent occurring in an expression for an atom. If
h>=c_H+m+1, every exponent k in the expression satisfies k-m>=c_H+1,
so k-m belongs H. Factoring out t^m leaves another M-element with no
constant term. Its valuation at each prime dividing a is positive, so
it is a nonunit. This contradicts atomicity.

Therefore every atom admits, and in fact every expression has, a least
exponent satisfying

    h<=H_0:=c_H+m.                                         (4)

This slightly loose bound avoids exceptional endpoint cases such as the
atom t when H=N_0.

## 4. IDF

Fix x in M. Let X be the part of its reduced numerator supported outside P.
Consider an atom divisor beta with a polynomial expression of degree n.
If n<c_H, there are only finitely many possibilities: the degree is bounded
and every coefficient is bounded by floor(C_m).

If n>=c_H, write

    beta=N/b^n,
    N=sum_(i=0)^n c_i*a^i*b^(n-i).

The leading coefficient is positive and below a by (3). At each p in P,
its term c_n*a^n has valuation below v_p(b), and every other term is
 divisible by b. Hence

    v_p(N)=v_p(c_n)<v_p(b).

Thus the P-supported part of N divides D. Since beta divides x in M and
its cofactor belongs R, the outside-P part of N divides X. Consequently

    N divides D*X.                                         (5)

If h is its least exponent, (4) gives

    N>=a^h*b^(n-h)>=b^(n-H_0).

Together with (5), this bounds n by H_0+floor(log_b(DX)). There are finitely
many possible N and n, and therefore finitely many possible atom values.
Units are trivial, so M is IDF.

This is a proof of finiteness, not an asserted general algorithm for testing
irreducibility in every such semiring. Finite candidate lists for atoms do
not automatically supply an irreducibility oracle.

## 5. Non-atomicity and atomless elements

The IDF result implies that only finitely many P-smooth atoms exist in M.
Here is a direct justification without choosing any fixed divisor first:
for high-degree atoms use X=1 in (5) and the degree bound above; low-degree
expressions are already finite. Every such atom is strictly greater than1.

Choose u_L from section1 closer to1 than all these finitely many atoms.
Then u_L has no atom divisor. Indeed, any atom divisor and its cofactor
must both be P-smooth, since outside-P valuations are nonnegative on M
and sum to zero on u_L. Both are at least1, so an atom divisor cannot
exceed u_L. The chosen gap makes this impossible.

Thus M is non-atomic. Equivalently one can note that infinitely many u_L
divide one fixed integer B>2C_m, by the conductor, whereas atomic plus IDF
would imply finitely many divisor classes. The direct argument above
also proves the stronger existence of atomless nonunits.

## 6. The especially simple semigroup H=<2,3>

Here H={0,2,3,4,...}, c_H=2 and m=2. Every P-smooth atom must be an integer.
To see this, a P-smooth atom expression has a positive constant term:
otherwise every term has positive valuation at any prime dividing a.
If its degree n>=2, (5) with X=1 gives N<=D<b, whereas the positive
constant term gives N>=b^n, a contradiction. Degree below2 means degree0,
because1 is not in H. Such an integer atom must be an ordinary prime.

It follows that EVERY P-smooth element of M strictly between1 and2 has
no atom divisor, irrespective of which integer primes are actually atoms.

### A small explicit two-generator pair

Take t=2/15. Then

    q=t^2=4/225,   r=t^3=8/3375.

The theorem proves

    N_0[4/225,8/3375] minus {0} is IDF and non-atomic.

The element

    h=125/81=1+3*q+1550*q^2                              (6)

belongs even to N_0[q], is supported on the denominator primes3,5, and
lies between1 and2. By the preceding argument, h has no atom divisor
in the full two-generator monoid.

Neither generator is redundant. The polynomial X^2, respectively X^3,
has coefficients below a=2 and hence is the unique nonnegative polynomial
representing t^2, respectively t^3. A polynomial in t^3 cannot formally
equal X^2, nor can a polynomial in t^2 equal X^3.

### A composite-numerator version

For t=6/175 the same theorem applies to(t^2,t^3). One explicit atomless
element is

    h=5^10/7^8=9765625/5764801,
    h=1+26*q+29*q^2+23*q^3+347434995625*q^4,
    q=t^2.

Alternatively, (h-1)/q=69458750/117649 belongs R and exceeds
C_2=35/(1-36/30625), so conductor membership already gives a short
certificate. The displayed polynomial identity is exact.

## 7. Scope for two generators

For positive coprime i,j, H=<i,j> is a numerical semigroup, so the theorem
applies to N_0[t^i,t^j]. If their gcd is d>1, write i=d*i',j=d*j' and use
t'=t^d. The block condition persists:

    a^d<(p^(v_p(b)))^d=p^(v_p(b^d)).

Therefore the conclusion actually holds for EVERY positive integer pair
i,j, with no coprimality restriction, whenever t satisfies (1).
The nonredundancy criterion remains that neither exponent divides the other.
