# Contracting Möbius pairs: normal forms and finite atomic factorizations

**Provenance and scope.** These arguments were derived during the research
session and independently audited within the session. Novelty has not been
checked against the literature or the full November 9 source. The special
case (2/5,2/3) is already known to be non-atomic from the user-supplied
discussion, which credits BakedPotatoz; the surrounding classification is
attributed to Mardcelo. None of the results below resolves IDF.

Let

    a >= 2, b > 2a, gcd(a,b) = 1, p = b-a,
    q = a/b, r = a/p = q/(1-q), h = b/p = 1+r,
    S = N_0[q,r], R = Z[1/(bp)], C = (a-1)b/p.

## 1. A real conductor

Every x in R with x >= C belongs to S. Equality follows from C=(a-1)h.
For x>C, choose c in {0,...,a-1} with x-c in aR and replace x by
(x-c)/q. Then

    x'-C >= q^(-1)(x-C).

Denominator factors from b disappear after finitely many steps, leaving
only factors from p. Continue until x reaches the cyclic conductor
(a-1)p/(p-a) of N_0[r], then reconstruct the original x. Here p>a, so
r<1 and that cyclic conductor applies.

## 2. Bounded formal series for atoms

Since b and p are coprime and both exceed 1, R has at least two denominator
primes. The standard dense congruence-unit construction gives positive
P-smooth nonunits u_L approaching 1, with u_L-1 in a^L R.

An exposed polynomial coefficient greater than C therefore forces
reducibility. Any coefficient at least a can be carried using

    a*q^i*r^j = b*q^(i+1)*r^j.

Since b>C, every atom has no polynomial representation with a coefficient
at least a.

Use T=N_0[X,X/(1-X)] as the formal model. Any formal-series coefficient at
least a can be exposed in a finite positive T-expression using finite
geometric expansions. Thus every atom has formal coefficients in
{0,...,a-1}. A T-series is eventually polynomial in the coefficient index;
boundedness makes it eventually constant. Conversely, every eventually
constant nonnegative integer series belongs to T.

## 3. Uniqueness

Suppose F has coefficients in {0,...,a-1} and is a rational generating
function whose denominator is a product of powers of cyclotomic
polynomials. If G in T satisfies G(q)=F(q), then

    G-F = (bX-a)H,

where H is an integer formal series of at most polynomial growth. Clear
denominators and apply Gauss's lemma to obtain this assertion.

Write its coefficient equation as

    g_j-f_j = b*h_(j-1)-a*h_j.

A first positive h_j is impossible, since it would make the right side
at most -a. Thus h_j<=0 for every j. If u_j=-h_j>=1, then

    a*u_(j+1) >= b*u_j-f_(j+1) >= (b-a+1)*u_j.

The factor (b-a+1)/a exceeds 1, contradicting polynomial growth. Hence
H=0.

In particular, bounded eventually constant series are uniquely represented
in S. Such a nonunit series evaluates to an atom exactly when it is
formally irreducible in T. The only atom with zero constant coefficient
is q.

For an eventually constant series F with positive constant coefficient and
eventual value c>=1, any nontrivial factorization has exactly one infinite
factor: write F=A*B with A finite. Then

    A(1) * tail(B) = c.

Two infinite factors in T would have unbounded convolution coefficients:
each factor is bounded by a constant multiple of F, so each has a
positive eventual constant value. Therefore eventual value 1 automatically gives an atom.
For c>1, possible finite factors A can be tested by A(1)|c and divisibility
of (1-X)F, with the quotient series required to be nonnegative. There are
finitely many candidates: degree(A)<=degree((1-X)F), and the coefficients
of A have sum at most c.

## 4. A terminating membership algorithm

We have q*S = S intersect aR. Indeed, the constant coefficient of an
S-element in aR is divisible by a; replace each a by bq, and use
r=q(1+r) for every nonconstant monomial.

Consequently, if c is the residue of x modulo a in {0,...,a-1}, then

    x in S iff x>=c and (x-c)/q in S.

For a rational input, reject negative values and denominators containing
primes outside bp. Accept 0 or x>=C. Otherwise iterate this digit step,
rejecting if x<c, and store the visited states.

After denominator factors from b disappear, the denominator is supported
on p and never increases. The unresolved states lie in a fixed bounded
rational grid. Thus either the algorithm terminates or a state repeats.

A constant digit cycle has value x=c/(1-q)=ch and belongs to S. A
nonconstant cycle produces an eventually periodic, nonconstant digit
series F. If x belonged to S, the uniqueness argument above would identify
F with a T-series. But a bounded T-series is eventually constant. Thus
nonconstant cycles are nonmembers.

This gives a membership decision procedure. For q=4/9, C=27/5 and the
constant cycles below C are h=9/5 and 2h=18/5. For q=2/5, C=h, so its
constant cycle is already at the acceptance threshold.

## 5. Finite-polynomial uniqueness for all q<1

Even without b>2a, every finite polynomial F with coefficients less than
a is uniquely represented in T. The first-positive-coefficient argument
still forces h_j<=0. Once u_j=-h_j>=1,

    a*u_(j+1) >= b*u_j-f_(j+1) > 0,

so a negative coefficient cannot disappear. Beyond degree(F), the growth
factor b/a>1 contradicts polynomial growth. Therefore H=0.

Consequently, finite bounded-coefficient polynomial atoms remain atoms for
Möbius pairs whose second generator r may exceed 1 as well.

## 6. A non-atomic family

Continue with b>2a. Suppose some maximal prime power ell^e dividing b
satisfies ell^e>a. Then S minus {0} is non-atomic.

For a nonconstant finite digit polynomial F of degree n, the numerator
over b^n is congruent to d_n*a^n modulo ell^e. Since
1<=d_n<a<ell^e, its ell-adic valuation is less than e. Consequently
v_ell(F(q))<0.

For an eventually constant digit series with eventual value c>=1, let
i be its last index with d_i != c. Its value has numerator

    N = p sum_(j=0)^i d_j a^j b^(i-j) + c a^(i+1)

over p*b^i. Modulo ell^e this numerator is

    a^(i+1)*(c-d_i).

The difference is nonzero and has magnitude less than a<ell^e, so
v_ell(N)<e. If i>=1, its evaluated value again has negative ell-adic
valuation. If i=0 and the constant coefficient is positive, the value
is d_0+c*r >= 1+r=h. Pure constant tails have value c*h>=h.

The remaining atoms are q and positive constant primes less than a.
The former has negative ell-adic valuation; the latter have value at
least 2>h. Thus every atom smaller than h has nonpositive ell-adic
valuation.

There are P-smooth nonunits u in S with 1<u<h and v_ell(u)>0.
To construct them, choose a prime s dividing p=b-a, put T=phi(a^L),
and choose positive integers m,n such that

    1+C*q^L < ell^(T*m)/s^(T*n) < 1+(C+1)*q^L.

Such choices exist by irrationality of log(ell)/log(s), with both
exponents arbitrarily large. The congruence modulo a^L and the conductor
place u in S. For large L it lies below h.

Every atom in a factorization of u would itself be P-smooth. Every
P-smooth nonunit in S exceeds 1: an element below 1 has zero constant
coefficient and is divisible, in R, by every prime dividing a. Hence
each atomic factor of u would be smaller than h and have nonpositive
ell-adic valuation, contradicting v_ell(u)>0.

In particular, this proves non-atomicity for every contracting Möbius
pair with b a prime power, and more generally whenever a maximal prime
power factor of b exceeds a. It does not decide IDF.

### An explicit example for (4/9,4/5)

Let q=4/9 and r=4/5. The element

    x=531441/390625=3^12/5^8

lies between 1 and h=9/5. A completely explicit positive representation is

    x = 1+q^2+q^4+3q^5+3q^6+2q^7
        +q^8*(2+r^2+2r^3+2r^4+3r^5+2r^6+2r^7+126r^8).

The identity was checked using exact rational arithmetic. Taking ell=3,
e=2 proves that x has no atomic factorization. Equivalently, the first
five canonical q-digits are [1,0,1,0,1], and the remaining state is
2791791/390625>C=27/5.

## 7. Finite complete atomic factorizations throughout this family

Assume the hypothesis of Section 6, and fix ell^e dividing b with
ell^e>a. Put

    s=floor(log_ell(a-1)), so 0<=s<e.

Every atom other than q has positive constant coefficient and therefore
exceeds 1. Partition these atoms into two kinds.

The exceptional atoms are finite constants, the pure-tail atom h, and
endpoints whose last deviation has index 0. This is a finite set. Every
exceptional atom has value at least h: constants are at least 2>h, and
an index-0 endpoint is d_0+c*r>=1+r=h. Its ell-adic valuation is at most
e. For h the valuation is e; for constants and index-0 endpoints it is
at most s.

Every other atom is either a finite digit polynomial of degree n>=1 or
an endpoint with last deviation index i>=1. The valuation computations
in Section 6 sharpen to

    v_ell(alpha)<=s-en, or v_ell(alpha)<=s-ei,

respectively. In particular, every such atom contributes at least e-s
units of negative ell-adic valuation.

Now fix a nonzero x in S, choose any prime t dividing a, and define

    Q=floor(v_t(x)/v_t(a)),
    Y=x/q^Q,
    H=max{j>=0 : h^j<=Y},
    B=eH-v_ell(x).

These quantities are finite and exact. In particular Y>=1: in a positive
polynomial representation of x, some monomial has t-adic valuation at
most v_t(x), hence total degree at most Q. Since r>q, this monomial has
value at least q^Q, and positivity gives x>=q^Q.

In any atomic factorization, q occurs at most Q times. If its actual
multiplicity is m, the product of the other atoms is x/q^m<=Y. Since
each exceptional atom is at least h and every other remaining atom
exceeds 1, the number of exceptional atoms is at most H. Their total
positive ell-adic contribution is consequently at most eH.

Balancing valuations shows that the total negative ell-adic contribution,
including the q factors, is at most B. If B<0, no atomic factorization
exists. Otherwise each nonexceptional atom has degree or last-deviation
index at most

    D=floor((B+s)/e),

and the number of such nonexceptional atoms is at most

    floor(B/(e-s)).

Thus every atomic factorization has length at most

    Q+H+floor(B/(e-s)).

The coefficient alphabet is finite, so bounded degree/index gives only
finitely many possible atoms. Together with the exceptional atoms and q,
this proves that x has only finitely many complete atomic factorizations.

This is also effective. Membership is decided by Section 4. Enumerate
finite digit polynomials and eventually constant digit series up to D,
add the finite exceptional list, and apply the formal atom tests in
Section 3. Enumerate q-multiplicities from 0 through Q and products of
the remaining finite list. Every other atom exceeds 1, so each exponent
loop terminates by the real product bound. Retain exactly products equal
to x.

For a fixed q-count m, a sharper bound uses

    Y_m=x/q^m,
    H_m=max{j>=0 : h^j<=Y_m},
    B_m=eH_m-v_ell(x)-em.

Values Y_m<1 or B_m<0 give no factorizations with that q-count. Otherwise
replace B,H by B_m,H_m in the corresponding remaining-factor bounds.

### Corollaries

The submonoid generated by all atoms is an FFM. It is atomic by definition;
its atoms are precisely the original atoms, and its factorizations are
the complete atomic factorizations just proved finite.

Nevertheless, an element of this atomic submonoid can have infinitely
many divisors in S that admit no atomic factorization. Choose j with
h^j>C. The near-one elements u_L constructed in Section 6 have no atomic
factorization, and eventually

    h^j/u_L>C.

The quotient lies in R, so the conductor puts it in S. Thus infinitely
many distinct u_L divide the atomic element h^j.

This statement concerns arbitrary divisors, not atom divisors. It does
not establish either IDF or non-IDF.

## 8. A remaining IDF reduction under stronger denominator hypotheses

Suppose, in addition, that every maximal prime-power factor of both b
and p=b-a exceeds a. Then every fixed element has only finitely many
nonpolynomial atom divisors.

Indeed, for a nonconstant-tail endpoint with last deviation index i,
its numerator N from Section 6 has bounded valuations at every prime
in P. At a prime ell dividing b, its valuation is v_ell(c-d_i), bounded
by floor(log_ell(a-1)). At a prime z dividing p, reduction modulo the
full z-power dividing p gives

    N == c*a^(i+1),

so v_z(N)=v_z(c), again bounded by floor(log_z(a-1)). These valuations
are strictly below the corresponding denominator-block exponents.

If the endpoint divides a fixed x, the part of N outside P divides the
fixed outside-P numerator part of x. Consequently N is bounded. Since
its value is N/(p*b^i)>1, the index i is bounded as well. The pure-tail
atom h contributes only one additional possibility.

Therefore IDF reduces exactly to finiteness of finite digit-polynomial
atom values with a fixed outside-P numerator part. Formal irreducibility
can again be dropped: every such polynomial factors into bounded-digit
polynomial atoms, and no nonconstant factor can occur more than a-1 times
(the coefficient at its least positive exponent would otherwise exceed
a-1). Constant prime factors also have uniformly bounded multiplicities.
A finite atom list would therefore produce only finitely many bounded
polynomials.

Conversely, infinitely many finite digit-polynomial atoms whose outside-P
numerator parts divide a fixed integer M all divide one fixed element
T*M, where T is any integer greater than C^2. Their values are at most C,
and (T*M)/alpha belongs to R and exceeds C, so the conductor applies.

This gives an exact restricted-digit finiteness problem, not a resolution
of it. Both (2/5,2/3) and (4/9,4/5) satisfy these stronger denominator
hypotheses.

## 9. Exact implementation and checks

`mobius_pair_factorizations.py` is a standalone Python implementation using
only the standard library. `MobiusPair(a,b)` supplies exact membership,
canonical bounded-series forms, and global atom tests for every contracting
pair in this note. Its complete-factorization routine requires the good
denominator block from Sections 6 and 7. Candidate or traversal limits raise
`InconclusiveError`; exhausting a limit never reports nonmembership,
reducibility, or absence of factorizations.

Examples, run from this directory:

    python mobius_pair_factorizations.py 4 9 531441/390625
    python mobius_pair_factorizations.py 4 9 250/81 --atom
    python mobius_pair_factorizations.py 4 9 10
    python check_mobius_pair.py

The first input is certified to have no atomic factorization by its negative
valuation budget. The second is the atom `(2+2X+X^2)(4/9)=250/81`. For the
third, the complete output consists of exactly

    10 = 3*(10/3) = (9/5)^2*(250/81).

Other small complete examples in the same semiring are

    4 = 2^2 = (4/9)*3^2,
    6 = 2*3 = (9/5)*(10/3).

These examples exercise the variable number of q factors; in the binary
special case that number was fixed by the 2-adic valuation.

Nonconstant cycles really occur. For `(a,b)=(5,11)`, the input `25/24`
has canonical states

    25/24 -> 55/24 -> 121/24 -> 55/24,

and digits `0` followed by the repeating pair `0,4`. Its bounded rational
series is `4X^2/(1-X^2)`, which is not eventually constant. Hence `25/24`
is not in `N_0[5/11,5/6]`, despite belonging to its ambient localization.

The check script compares 3,107 states with an independently implemented
reverse-reachability grid algorithm, verifies 2,187 directly generated
semiring elements, tests constant and nonconstant cycles, checks signed
polynomial division in the endpoint atom test, reconstructs the displayed
factorizations, and compares 16 complete binary factorization sets with
the separate binary implementation. All checks passed. The source proofs,
rather than these finite tests, establish the global guarantees.
