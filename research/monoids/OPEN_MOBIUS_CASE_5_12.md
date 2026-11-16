# An unresolved Möbius pair: (5/12,5/7)

Put q=5/12, r=5/7, h=12/7, S=N_0[q,r], and P={2,3,7}.
This note gives exact structural restrictions and certified examples.
It does not determine atomicity or IDF, and makes no exhaustive claim
about the displayed atoms. Novelty has not been checked.

The bounded-normal-form theorem in MOBIUS_PAIR_NORMAL_FORMS.md applies
because 12>2*5. Every atom other than q has a unique positive-constant
representation with digits in {0,1,2,3,4}, either finite or eventually
constant. A bounded finite polynomial represents an atom exactly when
it is irreducible in N_0[X]. For an eventually constant form F, any
nontrivial factorization has a nonunit finite polynomial factor A with
nonnegative coefficients, and A divides (1-X)F in Z[X]. These criteria
will certify all examples below. The element h is an atom.

The sufficient non-atomicity and finite-factorization theorem in
MOBIUS_PAIR_NORMAL_FORMS.md does not apply: the maximal prime-power blocks 4 and 3 of 12 are both less
than 5. The examples below show concretely why its valuation proof fails.

## 1. Two numerator branches for finite P-unit atoms

For a bounded polynomial F of degree n>=1, with positive leading digit
d_n<=4, write

    F(q)=N/12^n,
    N=sum_(j=0)^n d_j*5^j*12^(n-j).

Modulo 12, N=d_n*5^n. Thus 6 does not divide N. If F(q) is a P-unit,
then necessarily

    N=2^u*7^w  or  N=3^v*7^w,  u,v,w>=0.

This concerns the numerator over 12^n, even if that fraction is not
reduced. It is a necessary condition, not a characterization of atoms.

## 2. Pure-power numerators for nonconstant P-unit endpoints

Let a canonical endpoint have tail c in {1,2,3,4}, last deviation at i,
and digit d_i!=c. Its numerator over 7*12^i is

    N=7*sum_(j=0)^i d_j*5^j*12^(i-j)+c*5^(i+1).

Modulo 7 this is nonzero, since c<7. Modulo 12 it satisfies

    N == 5^(i+1)*(c-d_i).

The nonzero difference c-d_i lies between -4 and 4, so 6 does not divide
N. Therefore a P-unit endpoint must have

    N=2^u or N=3^v.

Pure tails c*h are separate; only h itself is an atom among them.

## 3. Endpoints with constant digit 1 have only three possible forms

Every P-unit atom below h has constant digit 1. Any P-unit endpoint with that
constant digit satisfies

    N == 7*12^i == 2^(i+1) (mod 5),
    N == c*5^(i+1) (mod 7),
    N == 5^(i+1)*(c-d_i) (mod 12).

If N=2^u, the first congruence gives u==i+1 (mod 4). Since the value is
at least 1, N>=7 and u>=3. Substitution in the last congruence gives
c-d_i==4 (mod 12), hence c=4,d_i=0. Quadratic characters modulo 7 in
the middle congruence then force i odd.

If N=3^v, the first congruence gives v==3*(i+1) (mod 4). When i is odd,
the last congruence gives c-d_i=-3, forcing c=1,d_i=4. When i is even,
it gives c-d_i=3, allowing (c,d_i)=(3,0) or (4,1). In the middle
congruence, the parity of v makes the quadratic characters of 3^v and
5^(i+1) equal, so c must be a quadratic residue modulo 7. This excludes
c=3 and leaves only c=4,d_i=1.

Thus the necessary cases are:

- N=2^u: i odd, tail 4, last deviation digit 0;
- N=3^v: i odd, tail 1, last deviation digit 4;
- N=3^v: i even, tail 4, last deviation digit 1.

In particular tails 2 and 3 are impossible for a P-unit endpoint with
constant digit 1. The three remaining cases are not ruled out.

## 4. Explicit P-unit atoms and their certifications

The constants 2 and 3 are atoms. The following additional bounded
polynomials also represent atoms:

| Polynomial F(X) | Exact value F(5/12) |
|---|---|
| 1+4X | 8/3 |
| 3+4X | 14/3 |
| 1+3X | 9/4 |
| 4+3X | 21/4 |
| 2+X+4X^2 | 28/9 |
| 4+X+2X^2 | 343/72 |
| 3+X+3X^2 | 63/16 |
| 4+2X+3X^2+4X^3+X^4 | 117649/20736=7^6/12^4 |

The four linear polynomials are primitive and hence irreducible in
N_0[X]. The three quadratics are primitive, with respective discriminants
-31,-31,-35, so are irreducible even over Q.

For the monic quartic F=X^4+4X^3+3X^2+2X+4, any positive linear factor
would be X+e with e in {1,2,4}, but F(-e) equals 2,-4,44 respectively.
Two positive monic quadratic factors would have the form

    (X^2+aX+b)(X^2+cX+d),  a,c>=0, b,d>=1.

Their constant terms require b*d=4, while their X^2 coefficient would
require a*c+b+d=3. This is impossible because b+d>=4. A nonunit constant
factor is excluded by the leading coefficient 1. Thus F is irreducible
in N_0[X], completing every polynomial atom certification in the table.

There is also the P-unit endpoint atom

    beta=2+3*q^2/(1-q)=81/28.

Here (1-X)F=2-2X+3X^2 has discriminant -20 and coefficient gcd 1, so
admits no nonunit nonnegative finite polynomial divisor. The endpoint
criterion stated above proves that beta is an atom. By contrast,

    27/7=1+4*r=h*(1+3*q)

is reducible.

The two degree-two atoms 28/9 and 63/16 invalidate the attempted
extension of the good-block valuation bound: they have positive 2- and
3-adic valuations, respectively. The relevant leading digits are
divisible by the entire blocks 4 and 3, so cancellation can raise the
numerator valuation. One cannot simply bound it by the leading digit's
valuation without the good-block hypothesis.

## 5. Exact multiplicative relations

The displayed atoms satisfy

    h*(63/16)=3*(9/4),
    h*(28/9)=2*(8/3),
    (9/4)*(8/3)=2*3,
    h^2*(343/72)=14,
    h^4*(117649/20736)=49.

In particular 49 has the displayed atomic factorization. The quartic
atom is the rational square (343/144)^2, although 343/144 is not in S.
Indeed its first canonical digit is 2, leaving 11/12 after division by
q; the next canonical digit is 3, which exceeds that positive residual.

These relations do not yield an infinite atom family or an infinite
factorization family. The P-unit atoms and the three endpoint branches
above leave the atomicity and IDF questions for this pair unresolved.
