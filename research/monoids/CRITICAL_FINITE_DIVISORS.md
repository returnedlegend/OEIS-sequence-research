# Finite divisors and effective irreducibility from critical carry prefixes

Let `S=N_0[a/b]`, where `1<a<b` and `gcd(a,b)=1`. The theorem below gives
a finite, reproducible certificate that every critical element of `S` has
finitely many actual multiplicative divisors. These certificates have been
completed for **every reduced parameter with `b<=30` and at least two
distinct denominator primes: 87 parameter pairs**.

In particular this proves finite actual divisors for every critical element
of `N_0[5/6]`, and gives a terminating atom decision algorithm throughout
that monoid. It does **not** decide whether noncritical elements admit
atomic factorizations, or whether noncritical targets have finitely many
atom divisors. Thus global atomicity and IDF for `5/6` remain unresolved.

The arguments are self-contained and the finite searches are exhaustive,
not samples of numerical inputs. The `5/6` calculation and algorithm were
independently reproduced in this workspace. Novelty relative to the full
discussion or current literature has not been verified; no novelty claim
is made.

## 1. Canonical critical tails

Put `t=a/b`, `d=b-a`, and

    K=floor((a-1)/d),
    M=a*(K+1)-1.

For an element `x` of `S`, let `n` be the least nonnegative integer for
which `x*b^n` is integral. Its canonical polynomial has coefficients below
`a` at indices `0,...,n-1`, and a nonnegative integral terminal `c_n`.
Membership and criticality are effective: canonical membership succeeds
exactly when that terminal is nonnegative, and

    x is critical  iff  c_n<=M.

[CRITICAL_BOUNDED_FACTORIZATIONS.md](CRITICAL_BOUNDED_FACTORIZATIONS.md)
proves these statements and the following facts used here:

* A critical element has bounded factorizations into arbitrary nonunits
  and therefore has an atomic factorization.
* Every representation of a critical element has leading coefficient at
  most `M`.
* With at least two denominator primes, every noncritical element starts
  an infinite proper divisor chain and is reducible.

If `c_n<a`, the bounded-coefficient polynomial is the unique nonnegative
polynomial representation of `x`. Otherwise, after at most one step the
integral terminal map `T(c)=b*floor(c/a)` reaches a fixed state `b*m`, with
`1<=m<=K`. If `k` is the first index of that fixed state, then `k<=n+1`.
At every degree `D>=k`, the canonical polynomial `F_D` has leading
coefficient `b*m`, and every coefficient at indices `k,...,D-1` equals
`d*m<a`.

## 2. A finite reversed-prefix certificate

For every `1<=m<=K` and `1<=j<=m`, enumerate all unordered integer pairs
`(u,v)` satisfying

    u*v=b*j,  u,v>=2,
    gcd(u,b)>1, gcd(v,b)>1,
    b does not divide u and b does not divide v.          (1)

Start reversed factor coefficient lists `A=(u)`, `B=(v)` and carry
`h=m-j`. At depth `l>=1`, choose a new carry `h'` in `{0,...,h}` and new
factor coefficients `alpha,beta` in `{0,...,a-1}` satisfying

    u*beta + v*alpha + sum_(i=1)^(l-1) A_i*B_(l-i)
       = d*m+a*h-b*h'.                                  (2)

Append the coefficients and replace `h` by `h'`. This is a finite
branching tree. If every such tree becomes empty by some depth `H`, the
complete calculation is a **prefix certificate** of depth `H` for `(a,b)`.
An unfinished or resource-capped search is not a certificate.

The implementation uses depth-first search, recording the exact number
of surviving states at each depth. A child uniquely determines its parent,
so these counts equal the full breadth-first state counts. Depth-first
search avoids storing an entire level. No floating-point arithmetic is
used.

## 3. The finite-divisor theorem

**Theorem.** If `(a,b)` has a prefix certificate of depth `H`, every
critical element of `S` has finitely many actual multiplicative divisors.

Here is an explicit bound. Choose a prime `ell` dividing `a`, put
`e=v_ell(a)`, and for a nonzero critical `x` define

    n=min{n>=0 : x*b^n is integral},
    X=the part of the reduced numerator of x supported outside {p:p|b},
    r=floor(v_ell(x)/e),
    B=x*t^(-r),
    L=n+max(H, floor(log_a X), floor(log_2 B)).           (3)

Every factorization `x=y*z` into nonunits has

    deg(A_y)+deg(A_z)<=L,                               (4)

where `A_y,A_z` are the minimal canonical polynomials of its factors.

**Proof.** Every divisor `y` of `x` has `v_ell(y)<=v_ell(x)`. Some
monomial in a nonnegative expression for `y` must have `ell`-adic valuation
at most `v_ell(x)`, and therefore degree at most `r`. Consequently
`y>=t^r`. The same argument applied to the cofactor gives `y<=B`. In
particular `B>=1`.

If one factor is an integer, each of its denominator-prime valuations is
at most `floor(log_2 B)`. Dividing `x` by that integer increases its
minimal denominator degree by at most this amount. This gives (4).

Suppose a noninteger factor has leading canonical coefficient coprime to
`b`, and degree `s`. Its numerator after clearing the denominator by
`b^s` is coprime to `b`, divides `X`, and is at least `a^s`. Thus
`s<=floor(log_a X)`. Its denominator is exactly `b^s`, so the cofactor's
minimal denominator degree is at most `n`. Again (4) follows.

If the terminal of `x` is below `a`, uniqueness makes the formal product
of its factor polynomials equal its canonical polynomial, giving total
degree `n`. We may therefore assume a positive fixed tail `b*m` occurs.
In the remaining case both factors are noninteger and their leading
coefficients are not coprime to `b`. Minimal denominator degree means the
cleared numerator of each factor is not divisible by `b`. Reduction
modulo `b` shows the same for its leading coefficient.

Let `G=A_y*A_z` and `D=deg G`. If `D` is before the fixed tail, then
`D<=n`. Otherwise normalize `G` by nonnegative carries. With `h_i` the
carry after index `i` and `h_(-1)=0`,

    G_i=(F_D)_i+a*h_i-b*h_(i-1)   (i<D),
    G_D=b*m-b*h_(D-1).

Thus `G_D=b*j` for some `1<=j<=m`, and its two leading coefficients
satisfy (1). In the constant tail `(F_D)_i=d*m<a`, nonnegativity gives

    h_(i-1)<=floor((d*m+a*h_i)/b)<=h_i.

The second inequality holds because `d*m<b`. Reading the two canonical
factors backwards therefore gives exactly recurrence (2); their other
coefficients lie in `{0,...,a-1}`. Zero coefficients beyond a factor's
degree cause no exception. If `D>=k+H`, at least `H` tail positions would
survive, contrary to the certificate. Hence `D<=k+H-1<=n+H`, proving (4).

Finally, the outside-denominator numerator of a divisor is a divisor of
`X`. Bound (4) bounds every negative denominator-prime valuation, and the
real bound `B` then bounds all remaining positive valuations. There are
only finitely many rational candidates. Canonical membership of the
candidate and its cofactor decides which are actual divisors. QED.

For parameters with a certificate and at least two denominator primes,
the following properties of an individual nonzero `x` are equivalent:

* `x` is critical;
* lengths of its factorizations into arbitrary nonunits are bounded;
* `x` has finitely many actual divisors;
* no infinite proper divisor chain starts at `x`.

This is a statement about **individual elements**, not global IDF or
global atomicity.

## 4. The full certificate for 5/6

For `a=5,b=6`, the fixed terminals are `6,12,18,24`. The possible leading
pairs in (1) are `(j,u,v)=(1,2,3),(2,3,4),(3,2,9),(4,3,8)`.
The complete state counts, including depth zero and the final empty
level, are:

| m | j | leading pair | state counts |
|---|---|---|---|
|1|1|2,3|1,0|
|2|1|2,3|1,1,1,1,0|
|2|2|3,4|1,0|
|3|1|2,3|1,2,3,4,2,0|
|3|2|3,4|1,1,1,0|
|3|3|2,9|1,0|
|4|1|2,3|1,2,6,10,8,3,0|
|4|2|3,4|1,2,3,2,0|
|4|3|2,9|1,1,1,1,0|
|4|4|3,8|1,0|

Thus `H=6` suffices. If `x` is `2,3`-smooth, an integer divisor is at
most `24`, so the simpler bound `deg(A_y)+deg(A_z)<=n+6` applies.
For arbitrary critical `x`, formula (3) becomes

    E=v_5(x),  B=x*(6/5)^E,
    L=n+max(6, floor(log_5 X), floor(log_2 B)).

The certificate proves that the following are atoms, despite having
nonunique polynomial representations:

    81/8, 243/16, 2187/256, 531441/65536, 2048/243,
    274877906944/31381059609 = 2^38/3^22.

Their minimal canonical terminals are respectively `9,9,9,9,8,22`.
Each has exactly the two actual divisors `1` and itself. These conclusions
use complete finite divisor searches, rather than a denominator search
stopped at a guessed cutoff. They do not assert that this is the complete
global smooth atom list.

## 5. All parameters with denominator at most 30

[cyclic_prefix_certificates.json](cyclic_prefix_certificates.json) is the
compact table of all 87 parameter certificates. Each row records `a,b`,
the fixed-tail bound `K`, certificate depth, number of leading-pair cases,
maximum level size, total nodes, and a SHA-256 digest of all exact
per-case state counts. The case `K=0` is included: all critical values
then have unique bounded-coefficient representations and need no prefix
search.

Some of the more demanding consecutive cases are:

| a/b | leading-pair cases | depth H | largest level |
|---|---:|---:|---:|
|5/6|10|6|10|
|9/10|47|9|51|
|11/12|142|11|270|
|13/14|117|12|261|
|14/15|168|13|942|
|17/18|418|17|2451|
|19/20|550|17|9142|
|20/21|400|15|12711|
|21/22|363|20|23120|
|23/24|1155|16|46948|
|25/26|545|21|57878|
|29/30|2181|21|450036|

The initial breadth-first search for `29/30` reached a storage cap in
eleven cases. The depth-first search subsequently completed **every**
case; only the completed calculation is used in this table and theorem.
No assertion of universal termination for arbitrary `a,b` is made.

## 6. Exact divisor, atom, and factorization algorithms

[cyclic_critical.py](cyclic_critical.py) first computes a prefix certificate
for its requested parameter. If any search exceeds its configured cap,
it raises `PrefixSearchIncomplete` and supplies no finite-divisor claim.

For a critical input, compute (3). For each `N|X` and each denominator
prime `p` with `e_p=v_p(b)`, enumerate exponents in the finite interval

    -e_p*L <= u_p <= floor(log_p(B*(b/p^e_p)^L)).

Test the candidates `N*product_p p^u_p` and their cofactors by exact
canonical membership. This produces all actual divisors, not merely atom
divisors. The logarithms in these bounds are computed by integer powers
and rational comparisons.

An input is an atom exactly when it is critical, is not `1`, and its
complete divisor set is `{1,x}`. Noncritical inputs are reducible by the
principal-congruence construction, so this gives a terminating global
irreducibility test for every parameter having a completed certificate.

For critical inputs, the program also identifies every atom divisor and
enumerates all atomic factorizations up to ordering. It uses the proved
length bound `Omega(X)+floor(log_2 M)`. It deliberately does not claim to
enumerate atomic factorizations of a noncritical input.

Examples:

    python research/monoids/cyclic_critical.py 5 6 2187/256 25
    python research/monoids/cyclic_critical.py 5 6 8 9 --factorizations
    python research/monoids/cyclic_critical.py 9 10 256/25

The last input is a smooth atom with unique polynomial
`7+4X^2`, even though its rational value is `(16/5)^2`. Thus a rational
perfect-power value alone does not imply reducibility in the semiring.

Verification and complete reproduction:

    python research/monoids/check_cyclic_critical.py
    python research/monoids/check_cyclic_critical.py --all-certificates

The first command independently reproduces 199 prefix cases by
breadth-first enumeration, checks exact membership reconstructions,
complete divisor lists, nonunique-polynomial atoms, critical atomic
factorizations, and rejection of incomplete searches. The second also
recomputes every one of the 87 certificates and checks the compact
manifest, including all state-count hashes. To deliberately regenerate
that manifest, use `--write-certificates`.

## 7. Restriction on a hypothetical infinite prefix branch

This observation helps identify the remaining general-termination issue;
it is not a proof of universal termination.

In an infinite branch, the decreasing integer carry sequence stabilizes.
Put `H_l=m-h_l`. Then `H_l` is bounded and nondecreasing, so

    C(z)=(1-z)*sum_(l>=0) H_l*z^l

is a nonnegative integer polynomial with `C(0)=j`, `C(1)<=m`. The limiting
reversed factor series satisfy

    A(z)*B(z)=(b-a*z)*C(z)/(1-z).                       (5)

Both have nonnegative integer coefficients; their nonconstant
coefficients are below `a`, and neither constant is divisible by `b`.
The product coefficients are eventually the constant

    (b-a)*C(1) <= (b-a)*m <= a-1 < b <= A(0)*B(0).

Neither factor can be rational. If one were rational, so would the other
be. A bounded integer sequence satisfying a fixed rational recurrence is
eventually periodic: there are finitely many possible integer state
vectors, each with a uniquely determined successor. For a common period
`N`, write `A=P/(1-z^N)`, `B=Q/(1-z^N)` with `P,Q` integral polynomials.
Equation (5) implies

    (1-z)*P*Q=(b-a*z)*C(z)*(1-z^N)^2.

The primitive linear polynomial `b-a*z` divides neither `1-z` nor
`1-z^N`, because its positive root exceeds `1`. Hence it divides `P` or
`Q` over the integers, forcing `b` to divide `A(0)` or `B(0)`, a
contradiction.

A genuine infinite obstruction would therefore require two nonrational
bounded integer series with the special rational product (5). Ordinary
binary-digit partition factorizations show that nonrational nonnegative
factors of rational series do exist. Ruling out the more restrictive
case (5), or finding an obstruction, remains open in this work.
