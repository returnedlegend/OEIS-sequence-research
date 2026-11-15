# A complete mixed-sign-of-log family: prime-power numerator and denominator

All assertions below are elementary and proved here. No claim of novelty is made.

## Theorem

Let ell and p be distinct primes, let s,k be positive integers with
q=ell^s/p^k<1, and let r>1 be rational whose reduced denominator has no prime divisors outside {ell,p}. Then

    S = N_0[q,r] minus {0}

is atomic and IDF. In fact it has finitely many divisors modulo associates for each element.

Write r=c/(ell^t p^u) in lowest terms, with c a positive integer and t,u>=0. If t>0, put H=q^t r^s. More precisely:

* If t=0, or if t>0 and H>1, every element has finitely many actual divisors; the only unit is 1.
* If t>0 and H<1, S is the positive part of Z[1/(ell p)], so it is factorial modulo its units.
* If t>0 and H=1, S=N_0[v,v^(-1)] minus {0} for a rational v=ell^A/p^B<1 with A,B positive. Every element has finitely many divisors modulo units.

This includes every pair (2/3,c/(2^t 3^u)) with the second entry greater than 1 and written in lowest terms. The expanding generator may have arbitrary numerator prime factors.

## 1. A valuation lower-bound lemma

Let 0<q<1<r and fix a prime ell with v_ell(q)=s>0 and v_ell(r)=-t<0. Suppose H=q^t r^s>1. Put

    F(e)=max(q^(e/s), r^(-e/t)), e in R.

Every x in N_0[q,r] minus {0} satisfies x>=F(v_ell(x)).

For a monomial m=q^i r^j with e=v_ell(m)=si-tj,

    m=q^(e/s) H^(j/s)=r^(-e/t) H^(i/t),

so m>=F(e). Write x as a finite sum of monomials, repeating monomials to absorb their positive integer coefficients. If e_0 is the least ell-adic valuation among those monomials, then e_0<=v_ell(x). Since both functions defining F decrease, a summand with valuation e_0 is at least F(e_0)>=F(v_ell(x)). Positivity of all summands proves the assertion. This explicitly accommodates valuation cancellation.

For a fixed w and a divisor d with cofactor e, set E=v_ell(w), z=v_ell(d). Then

    w=d*e >= F(z) F(E-z).

The right hand side tends to infinity as z tends to either infinity or minus infinity. Indeed for z>=max(0,E) it equals H^(z/(st))*r^(-E/t), and for z<=min(0,E) it equals H^(-z/(st))*q^(E/s). Thus v_ell(d) ranges over a finite set. The same inequalities give positive lower bounds on d and its cofactor, so d also lies in a bounded positive real interval.

For w=1, F(z)F(-z)=H^(|z|/(st)) forces z=0. Then both d and its inverse are >=F(0)=1, so d=1. Thus the unit group is trivial.

## 2. The case H>1

The denominator primes of S are contained in {ell,p}. For any divisor d of a fixed w, every valuation at a prime outside {ell,p} is nonnegative and at most the corresponding valuation of w. Hence

    d = N * ell^z * p^j,

where N ranges over a finite set of positive integers coprime to ell*p. Section 1 bounds z and places d in a fixed compact subinterval of the positive reals. This bounds j. Thus w has finitely many actual divisors.

## 3. The case t=0

Now the only denominator prime is p, and v_ell(r)>=0. The same minimum-valuation argument gives

    x >= q^(v_ell(x)/s)

for every x in S: each monomial q^i r^j is at least q^((si+j*v_ell(r))/s), because r>1. If d divides w, then 0<=v_ell(d)<=v_ell(w), and the same holds for its cofactor. Thus both have positive lower bounds, and d has an upper bound. The outside-p numerator of d divides the fixed outside-p numerator of w, so finitely many possibilities for that numerator and the bounded size give finitely many possible p-exponents. Again there are finitely many actual divisors.

## 4. The case H<1

After canceling ell, H=c^s/p^(kt+us). Its reduced numerator is coprime to ell. Thus q and H are two rational numbers strictly between 0 and 1 with coprime reduced numerators, and both have denominator a power of p. By the elementary two-contracting-generator localization theorem in TWO_SMALL_GENERATORS.md, N_0[q,H] is the nonnegative part of Z[1/p]. In particular 1/p belongs to S.

Because r*p^u=c/ell^t belongs to S and gcd(c,ell)=1, choose n sufficiently large that

    p^n = a*c + b*ell^t

with a,b nonnegative integers; this is the standard numerical-semigroup consequence of gcd(c,ell^t)=1. Then

    1/ell^t = (a*c/ell^t+b)/p^n

belongs to S. Hence 1/ell belongs to S. It follows that S is exactly the positive part of Z[1/(ell*p)], a factorial monoid modulo its units.

## 5. The case H=1

The identity c^s=p^(kt+us), and reducedness of r, force u=0 and c=p^z for some z>0. Write s=g*A_0, k=g*B_0, with gcd(A_0,B_0)=1. The relation sz=kt implies t=h*A_0, z=h*B_0 for a positive integer h. With d=gcd(g,h), put

    v=ell^(d*A_0)/p^(d*B_0),
    i=g/d, j=h/d.

Then q=v^i, r=v^(-j), and gcd(i,j)=1. Every integer is a nonnegative integer combination of i and -j: start with Bezout coefficients and shift by a sufficiently large multiple of (j,i). Hence S=N_0[v,v^(-1)] minus {0}.

Write v=ell^A/p^B. Its integer powers are units. The minimum-valuation argument now gives

    x >= v^(v_ell(x)/A)

for every nonzero Laurent polynomial x in v with nonnegative integer coefficients.

Fix w. Each divisor class has a representative d for which 0<=v_ell(d)<A, obtained by multiplying by a power of v; its cofactor remains in S. The displayed inequality bounds d and its cofactor below by positive constants, hence bounds d above as well. The outside-{ell,p} numerator of d divides that of w. Writing d=N*ell^e*p^j, there are finitely many possibilities for N and for e in {0,...,A-1}; the size bound then bounds j. Thus there are finitely many divisors modulo associates.

In fact the unit group is exactly v^Z. To see this, the only nonnegative Laurent polynomial representing 1 is the constant 1. Any negative power is already greater than 1. If a polynomial with no negative powers and no constant term represented 1, its ell-adic valuation would be positive; and a positive constant term forces it to be precisely the constant 1. If two nonnegative Laurent polynomials multiply to 1, their formal product must therefore be 1, forcing both to be single monomials with coefficient 1.

## 6. Why divisor finiteness proves both properties

In a cancellative commutative monoid, a proper nonunit factor has a strictly smaller divisor class. Finitely many divisor classes of a fixed element therefore imply that repeatedly factoring nonatoms terminates in atoms. This proves atomicity. IDF is immediate because the atom-divisor classes are a subset of the finitely many divisor classes. With finitely many available atom classes and no nontrivial product of nonunits equal to a unit, Dickson's lemma also gives finitely many factorizations up to units and order.

## A broader sufficient criterion for finite actual divisors

Let q=a/b<1 be reduced with a>1, let r>1, and let P be the union of their denominator-prime sets. Let G be the set of those primes ell in P for which

    v_ell(q)=s_ell>0>v_ell(r)=-t_ell,
    q^(t_ell)*r^(s_ell)>1.

If |P minus G|<=1, then every element of N_0[q,r] minus {0} has finitely many actual divisors, and the monoid is atomic and IDF with trivial units.

When G is nonempty, Section 1 bounds each G-valuation of a fixed divisor and gives a bounded positive real interval. Its outside-P numerator divides that of the fixed element. At most one denominator-prime exponent remains, and the size interval bounds it. When G is empty, P has just one prime. Any prime ell dividing a lies outside P; the argument in Section 3, with s=v_ell(q), bounds sizes and gives the same conclusion.

This broader criterion permits a composite numerator a. For example, q=a/p^k<1 and r=c/a with c>p^k and gcd(a,c*p)=1 satisfy it: all primes of a are in G because qr=c/p^k>1, and the sole remaining denominator prime is p.
