# Stronger cyclic reductions; complete classification remains unresolved

Let t=a/b be reduced, 0<t<1, a>1. Let P be the prime divisors of b, and
assume |P|>=2. Write S=N_0[t], R=Z[1/b], and C=(a-1)b/(b-a).

The conductor and dense congruence-factor constructions in README.md apply:
R intersect [C,infinity) lies in S; S has trivial multiplicative units; and
there are P-smooth h_k in S with h_k>1, h_k tending to1, and
h_k-1 in a^k R.

## 1. Any coefficient greater than C forces reducibility

If x=f(t)+c*t^j with f in N_0[X] and integer c>C, let
z_k=(x/h_k-f(t))/t^j for k>=j. Then z_k belongs to R, and z_k tends to c>C.
For sufficiently large k, z_k belongs to S by the conductor. Consequently
x=h_k*(f(t)+t^j*z_k). Choose k so that h_k is not x. Both factors are nonunits.

This argument does not require C<a.

## 2. A stronger necessary condition for atomicity

If any prime p dividing b satisfies p>a, then S minus {0} is non-atomic.

Indeed, since b has another distinct prime divisor, b>=2p>2a. Therefore
C<b. Any polynomial coefficient at least a can be rewritten using

a*t^j=b*t^(j+1),

exposing a coefficient at least b>C. By section1 the element is reducible.
Thus every atom has a polynomial representation with coefficients below a.
If alpha=sum_(i=0)^n c_i*t^i is an atom and c_n>0, its numerator over b^n is

N=sum_(i=0)^n c_i*a^i*b^(n-i).

Because 1<=c_n<a<p, N is nonzero modulo p. Hence

v_p(alpha)=-n*v_p(b)<=0.

Every finite product of atoms has nonpositive p-adic valuation. The element
p belongs to S and has valuation1, so it cannot be a product of atoms.

Consequently, atomicity in this cyclic regime requires

a>max(P).

Equality is impossible because gcd(a,b)=1. This proves non-atomicity for
4/15, 3/10, and10/33, among many other parameters. It does NOT establish IDF
for these additional examples. A stronger proved IDF family now appears in PRIME_POWER_DENOMINATOR_FAMILIES.md:
it requires a<p^(v_p(b)) for every p in P.

## 2A. A stronger necessary condition using maximal prime powers

In fact S is non-atomic whenever p^(v_p(b))>a for at least one p in P.
Consequently atomicity requires

    a > max{p^(v_p(b)): p in P}.

Proof: write e=v_p(b). The presence of another denominator prime gives
b>=2*p^e>2a, so the coefficient-carry argument above applies. Every atom has
coefficients below a. If such an atom is nonconstant, with degree n>=1,
its numerator N over b^n satisfies

    v_p(N)=v_p(c_n)<e,
    v_p(N/b^n)<0,

because all terms except the leading term are divisible by p^e and
0<c_n<a<p^e.

Choose another prime s in P. For each k the ratios
p^(phi(a^k)*m)/s^(phi(a^k)*n), with positive integers m,n, are dense in the
positive reals. This is the usual irrational-rotation density argument;
approximating log(target) by m*log(p)-n*log(s) can use arbitrarily large
positive m,n. We may therefore select h_k in

    (1+C*t^k, 1+(C+1)*t^k)

with v_p(h_k)>0 and h_k-1 in a^k R. The conductor gives h_k in S exactly as
in README.md. For large k, 1<h_k<2.

Suppose such an h_k factors into atoms. All factors are P-smooth and hence
strictly greater than 1. Each must also be below 2, so no factor can be a
constant integer. Every factor thus has negative p-adic valuation by the
preceding calculation. Their product cannot have v_p(h_k)>0. This proves
non-atomicity.

For example this settles non-atomicity of N_0[7/18] minus {0}, since 9>7,
even though neither denominator prime exceeds 7. It does not by itself
settle IDF for that example. The older necessary condition a>max(P) is not sufficient:
5/72 has 5>max{2,3} but is IDF and non-atomic by the stronger family; the
new maximal-prime-power condition excludes it because 5<8,9. No sufficient
criterion for atomicity in the remaining multi-prime cyclic regime is
claimed.

## 3. Unique polynomial representations and an exact atom criterion

For any reduced 0<a/b<1 with a>1, a polynomial f with all coefficients below a
is the unique polynomial in N_0[X] representing f(t).

Suppose g(t)=f(t) with g in N_0[X]. The primitive polynomial bX-a divides g-f
over Z[X] by Gauss's lemma, so g-f=(bX-a)h for h in Z[X].

If h has a positive coefficient, choose its first positive coefficient h_j.
Taking h_(-1)=0 gives h_(j-1)<=0, so

g_j-f_j=b*h_(j-1)-a*h_j<=-a.

This contradicts g_j>=0 and f_j<a. Thus all coefficients of h are nonpositive.
If h is nonzero, take its highest nonzero coefficient h_j<0. Then

g_(j+1)-f_(j+1)=b*h_j<=-b,

again impossible because g_(j+1)>=0 and f_(j+1)<a<b. Thus h=0 and g=f.
Conversely, a coefficient at least a permits aX^j to be replaced by bX^(j+1),
so the polynomial representation is not unique.

For such a bounded-coefficient polynomial f with f(t) nonunit,

f(t) is an atom of S minus {0}
iff f is an atom of the multiplicative monoid N_0[X] minus {0}.

Any factorization of f(t) evaluates two nonnegative polynomials; uniqueness
forces their formal product to be f. Conversely formal factors give factors
of f(t), and only the polynomial1 evaluates to the unit1.

In particular every ordinary prime less than a is an atom. Primitive linear
polynomials d+cX with 1<=d,c<a give atoms. For t=5/6 this proves that2,3,
1+2t=8/3, and2+3t=9/2 are atoms. For t=7/18, 1+2t=16/9 is an atom below2.
These facts do not establish atomicity of the entire monoid.

## 4. Complete atom description when b>=2a, but not a classification of pairs

When b>=2a, C<b. Section1 and the relation a*t^j=b*t^(j+1) show that every
atom has coefficients below a. Thus section3 describes all atoms exactly
as evaluations of formally irreducible bounded-coefficient polynomials.

This does not settle whether every element factors into such atoms, or
whether a fixed rational has finitely many such atomic divisors. The degree
of a bounded-coefficient polynomial is not bounded merely by its coefficients.

For a<b<2a, a coefficient>=a need not carry to a coefficient>C. The terminal
integer coefficient under canonical carrying follows

T(c)=b*floor(c/a).

Nonzero fixed points are c=bk with 1<=k<a/(b-a). For t=5/6, C=24 and
T(5)=6, T(6)=6; tails6,12,18,24 are fixed. Thus a proof that all coefficients
>=a imply reducibility for arbitrary t would have a gap.

## Remaining obstruction

The methods here do not decide atomicity or IDF of N_0[5/6] minus {0}.
If it is atomic, it must be non-IDF by README.md; proving atomicity would
require infinitely many denominator-smooth atoms tending to1. The known
atoms2,3,8/3,9/2 do not suffice. No necessity-and-sufficiency classification
for the original rational-pair problem is claimed.
