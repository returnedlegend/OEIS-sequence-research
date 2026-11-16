# Canonical factorization for complementary generators

This note removes the prime-conductor restriction from
[PRIME_COMPLEMENT_CRITICAL_ALGORITHM.md](PRIME_COMPLEMENT_CRITICAL_ALGORITHM.md).
It makes no novelty claim relative
to the supplied discussion or the inaccessible PDFs. The supplied source
credits ppdppd with the canonical digits and conductor for(3/10,7/5), and
Mardcelo's October20 theorem already treats q=a/b, r=(a-1)(1-q),
b>=a^2-1, with all maximal denominator prime-power blocks at least a,
proving IDF and nonatomicity. The theorem below proves a canonical
factorization rule and effective individual-element results under the
stated hypotheses; it does not settle global IDF when a denominator block
is smaller. See [SOURCE_STATUS.md](SOURCE_STATUS.md) for the source limitations.

Let

    C>=3 be an integer, a=C+1, b>a*C, gcd(a,b)=1,
    q=a/b, r=C*(1-q), R=Z[1/b], S=N_0[q,r].

Then C-1<r<C, r^2>C, 2r>C, and1+r>C. The canonical digit set is

    {0,1,...,C-1,r},

representing the distinct residues modulo aR. Starting from x in R,
subtract its residue digit and divide by q, stopping at the first integer.
The minimal b-denominator depth drops at each step, so this terminates.
Membership holds exactly when the process ends at a nonnegative integer
without a negative tail. For x>=C, every successive tail is at least C;
thus R intersect[C,infinity) lies in S. For x<C, a q-free polynomial
block can only be an integer0,...,C-1 or r, proving completeness of the
canonical membership test.

Call a member critical when its terminal is at most C. This is equivalent
to all canonical tails being in[0,C], since d+qC<=r+qC=C for every digit d.
The only unit is1, and q is the only atom below1.

## 1. All representations of a critical value

If the canonical terminal is below C, the canonical polynomial F(X,Y)
is the unique nonnegative polynomial representing x at(q,r). Its Y-degree
is at most1. Ordinary coefficients are below C, Y-coefficients are0 or1,
and both types never occur at the same X-degree.

If the terminal is C at depth n, write its prefix P(X,Y). All
representations are exactly

    F_m=P+X^n*(C*X^m+Y*(1+X+...+X^(m-1))), m>=0.     (1)

Here F_0=P+C*X^n is the canonical polynomial. The proof is recursive:
a critical q-free block can only be an ordinary integer0,...,C or r.
The residue forces the block except at tail C, where the only choices
are C itself or r+qC. Removing initial zero digits factors out a common
power X^e from every representation. The remaining endpoint is called
normalized; its X-constant part is nonzero.

## 2. Every noncanonical endpoint representation is irreducible

**Lemma.** For a normalized endpoint, every F_m with m>=1 is formally
irreducible in N_0[X,Y], for arbitrary integer C>=3.

Its top X-coefficient is the constant C. Its Y-degree is1, and its highest
Y-coefficient, viewed as a coefficient of the polynomial in X multiplying
Y, is1. Suppose F_m=G*H. One factor, say G, is an ordinary polynomial in
X because Y-degrees add. The highest Y-coefficient of the product is
lc(G)*lc(H_Y)=1, so lc(G)=1. Its ordinary constant coefficient G(0) is
positive, since the product has nonzero X-constant part. The highest
X-coefficient of H must then be the constant C.

If deg(G)>0, multiplying G(0) by that top coefficient produces an
ordinary coefficient at least C at X-degree deg(H)<deg(F_m). Every lower
ordinary coefficient of F_m is below C, a contradiction. Thus G has
degree0 and leading coefficient1, so it is the unit1. This proves the
lemma without assuming C prime.

The same argument proves that the canonical endpoint F_0 is irreducible
whenever it contains Y. If F_0 is ordinary, it may be reducible. For
example, at C=6,

    1+5X+6X^2=(1+2X)*(1+3X).                        (2)

When C is prime, even an ordinary F_0 is irreducible: its top coefficient
factors as1*C, and the same lower-coefficient argument forces the factor
with leading coefficient1 to be the unit. This recovers the prime-C
endpoint theorem as a special case.

## 3. Actual divisors are exactly canonical formal divisors

**Theorem.** For every nonzero critical x, its actual multiplicative
divisors in S are exactly the evaluations at(q,r) of the nonnegative
polynomial divisors of its canonical polynomial F_0.

For a nonendpoint, uniqueness of its polynomial representation makes
this immediate. For a normalized endpoint, choose polynomial
representations for a divisor and its cofactor. Their product is some
F_m. If both factors are nonunits, the lemma excludes m>=1, so their
product must be F_0. The unit and whole-element divisors also occur in
F_0. If x has initial X-order e, write x=q^e*y with y normalized. In a
product representation, the X-orders of the factors add to e. After
removing those powers, either the product is the canonical F_0 for y, or
it is an irreducible noncanonical F_m. In the latter case one normalized
factor is1 and the other is F_m; the numerical divisors q^i orq^i*y are
already evaluations of divisors of X^e*F_0. This proves the theorem.

Every critical element therefore has finitely many actual divisors and
is atomic. An explicit nonunit-factorization length bound is

    total_degree(F_0)+floor(log_2(content(F_0))).     (3)

Indeed any factorization can be represented using factors of F_0, as in
the preceding proof. Nonconstant factors consume total degree, while
integer factors multiply into the content, the gcd of all coefficients.

There is a finite exact divisor algorithm: enumerate polynomial factors
with X- and Y-degrees bounded by those of F_0 and coefficients bounded by
its largest coefficient, and retain exact formal divisors. Since the
Y-degree is at most1, it is enough to enumerate ordinary factors G(X),
divide both the ordinary and Y parts of F_0 by G, and include both G and
its quotient. Restore all possible powers of X from the initial zero
digits. This gives a finite atom test and all complete atomic
factorizations of every critical target.

## 4. Classification of individual elements with two denominator primes

Now assume b has at least two distinct prime divisors. Dense b-smooth
congruence subgroups give h>1 approaching1 with h-1 in a^L*R for
arbitrarily large L, and with h in S. To see the latter explicitly, choose
h>1+Cq^L; then h=1+q^L*c with c>C in R, hence c in S.

If a canonical tail c of x exceeds C, write x=P(q,r)+q^n*c. Choose L>=n
and h close enough to1. Then

    x/h=P(q,r)+q^n*c_h,  c_h in R, c_h>C,

because the congruence preserves membership in R and c_h tends to c.
The conductor puts c_h in S. Such h are infinitely many distinct actual
divisors of x, and the construction can be repeated on the cofactor
while preserving a tail above C. Consequently, for each individual
nonzero element, the following are equivalent:

* it is critical;
* it has finitely many actual divisors;
* its factorizations into arbitrary nonunits have bounded lengths;
* no infinite proper divisor chain starts at it.

Every noncritical member is reducible. Thus the canonical formal-factor
test extends to a terminating atom decision procedure on all of S.
This does not assert global atomicity or global IDF.

## 5. One large denominator block gives a global complete-factorization algorithm

Suppose some p^e exactly dividing b satisfies p^e>C. Every noninteger
atom other than q has negative p-adic valuation. Let n>=1 be its minimal
b-depth and k in{0,...,C} its terminal. If k>0 and the preceding digit is
ordinary, the cleared leading coefficient has valuation v_p(k)<e. If
that digit is r, the top two terms reduce modulo p^e to a^n*(k-C), giving
v_p(C-k)<e. Here k<C, since r+qC=C would have ended the word sooner. If
k=0, the last digit is r and the valuation is v_p(C)<e. Thus in every case

    d=-v_p(alpha)>0,
    n<=floor((d+floor(log_p C))/e).                  (4)

The integer atoms are precisely the ordinary primes at most C.

For a fixed x, define

    A=min_{ell|a} floor(v_ell(x)/v_ell(a)),
    B=x*q^(-A),
    J=floor(log_p B) if p<=C, otherwise J=0,
    D=J-v_p(x).

Any atomic factorization uses at most A copies of q. The product of all
other atoms is at most B, so at most floor(log_2 B) integer atoms occur.
If j is the number of q factors, taking p-adic valuations gives

    sum_{noninteger atoms !=q} -v_p(alpha)
       =multiplicity(integer atom p)-e*j-v_p(x)<=D. (5)

If D<0, no atomic factorization exists. Otherwise at most D noninteger
atoms occur, all with b-depth at most
K=floor((D+floor(log_p C))/e). Their outside-b numerators divide the
outside-b numerator X of x. For each N|X and each l^f exactly dividing b,
enumerate valuations in

    -K*f<=v_l(alpha)<=floor(log_l(C*(b/l^f)^K)).      (6)

This is a finite list containing every possible noninteger atom factor;
the canonical atom oracle filters it. Include the finitely many integer
primes at most C, enumerate the bounded multisets from(5), and test exact
products. This terminates and lists every complete atomic factorization
of x, possibly none. It does not bound atom divisors whose cofactors are
nonatomic, and therefore does not prove IDF.

The same one-block hypothesis proves nonatomicity. Choose another prime
s|b and a b-smooth h=p^u/s^v in(1,2), with v_p(h)>0 and h-1 in a^L*R,
large enough that h>1+Cq^L. Then h is in S. Its valuations at all primes
of a are zero, so no q factor can occur. Every remaining atom is greater
than1; integer atoms are at least2 and cannot occur in a factorization of
h. All other atoms have negative p-adic valuation, contradicting
v_p(h)>0. Thus h is nonatomic.

A composite-C example is C=4,b=36, so q=5/36,r=31/9. The block3^2>4
is large while the block2^2=4 is smaller than a=5. Here

    243/128=1+q+q^3+2034q^4

is a nonatomic member in(1,2). Every element nevertheless has finitely
many complete atomic factorizations, with the exact algorithm above.

**Integer corollary (an immediate consequence, not a novelty claim).**
If some prime divisor p of b itself satisfies p>C, the positive integers
admitting atomic factorizations are exactly those whose prime factors
are at most C. Each has exactly its ordinary prime factorization. Indeed,
every noninteger atom, including q, has negative p-adic valuation, whereas
every integer atom is a prime at most C and has p-adic valuation zero.
An integer has nonnegative p-adic valuation, so an atomic factorization
can contain only the integer atoms. This applies in particular to b=C*P
with primes C>=3 and P>C+1; these parameters are coprime to a=C+1.

For example, at C=4,b=21, integer18 has just2*3*3, while integer5 has
no atomic factorization. The stronger condition p>C matters: at C=6,b=45
the large block is3^2>6, and the integer7 has factorization q*3*3*5.

## 6. Prime elements and conditional IDF witnesses

The zero digit gives qS=S intersect aR. If a is prime, this makes q
prime. If a is composite, write a=u*v with1<u,v<a. Then q divides u*v
but neither factor, so q is not prime.

Every alpha>1 in S is nonprime. Indeed, h_0=1/b is outside S, and the
holes h_n=C-(C-h_0)q^n remain outside S while tending to C from below.
Choose h_n>1 with alpha*h_n>=C. The conductor puts z=alpha*h_n and
z^2/alpha in S, while z/alpha=h_n is outside S. Thus alpha divides a
square without dividing its base. As q is the only atom below1, q is the
unique prime when a is prime, and there are no prime elements when a is
composite.

If IDF fails, infinitely many atom divisors of a single target share one
outside-b numerator. Choose one such atom alpha_0. Every other atom alpha
in that family lies in(1,C], has ratio with alpha_0 in R, and divides
C^2*alpha_0 by the conductor. The latter element is atomic: factor the
integer C into its ordinary prime atoms and use alpha_0. This gives an
explicit atomic witness of length2*Omega(C)+1 for any possible IDF failure.
Under the one-large-block hypothesis, all but finitely many corresponding
cofactors must be nonatomic, because complete atomic-factorization sets
are finite. No IDF failure is asserted to exist.

## 7. Reproducible exact implementation

[complementary_family.py](complementary_family.py) implements terminating
canonical membership, critical divisors, the global atom oracle when b
has two prime divisors, and complete atomic-factorization enumeration
when one prime-power block exceeds C. The `Complementary` class permits
all integer C>=3; `PrimeComplement` additionally checks that C is prime.
[prime_complementary.py](prime_complementary.py) remains a compatibility
entry point for the prime subfamily.

The meaningful checks are
[check_complementary_family.py](check_complementary_family.py) and
[check_prime_complementary.py](check_prime_complementary.py). From the
repository root, run:

    python -m research.monoids.check_complementary_family
    python -m research.monoids.check_prime_complementary

The general checks include composite endpoint(2), its exact four-divisor
list, the nonatomic243/128 witness, and a critical example with only one
denominator prime. The prime-subfamily checks include the variable-q
factorizations8=2^3=(8/63)*3^2*7 and the preceding-r valuation exception.
