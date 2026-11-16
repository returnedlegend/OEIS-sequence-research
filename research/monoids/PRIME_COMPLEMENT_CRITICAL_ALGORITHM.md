# Critical divisors for a prime complementary endpoint

The broader theorem for every integer C>=3 is now in
[COMPLEMENTARY_CRITICAL_FACTORIZATIONS.md](COMPLEMENTARY_CRITICAL_FACTORIZATIONS.md).
The prime-C endpoint atom theorem and shorter divisor lists below remain
useful specializations; the implementation shares the general core.

The following is an independently derived extension of the endpoint
argument for N_0[3/10,7/5]. No novelty relative to the supplied discussion
or the inaccessible PDFs is asserted. The user's source credits ppdppd
with the canonical digits and conductor for that pair on October16, and
with its nonatomicity on October24. Mardcelo's October20 result already
studies q=a/b, r=(a-1)(1-q), with b>=a^2-1 and every maximal denominator
prime-power block at least a, proving IDF and nonatomicity. See
[SOURCE_STATUS.md](SOURCE_STATUS.md) for the source limitations.

Let C>=3 be a prime, put a=C+1, and suppose

    b>a*C, gcd(a,b)=1,
    q=a/b, r=C*(1-q), R=Z[1/b], S=N_0[q,r].

The restriction C>=3 is used to rule out r^2 in a critical q-free block.
The condition gives

    0<q<1/C, C-1<r<C, 1+r>C, 2r>C, r^2>C.

The critical-divisor statements below do not require multiple denominator
primes. The assertions about all noncritical elements being reducible and
having infinite divisor sets additionally assume that b has at least two
distinct prime divisors.

## Canonical digits and membership

Use the digit set D={0,1,...,C-1,r}. Its residues modulo aR are exactly
0,1,...,C, because r=C mod aR. For x in R, choose its unique residue digit
d and set

    tau(x)=(x-d)/q.

For a nonintegral state of b-depth h>=1, the next state has depth at most
max(h,1)-1. Thus iteration until the first integer terminates. An element
belongs to S exactly when its canonical iteration stays nonnegative and
ends at a nonnegative integer.

For completeness of this membership claim, every nonnegative polynomial
representation can be separated as x=P(r)+q*y. If x<C, its q-free block
P(r) is either an integer in{0,...,C-1} or r, so the canonical step leaves
an S-element. If x>=C, membership follows from the conductor argument
below. The finite nonnegative canonical expansion proves soundness.

For x>=C, every canonical step obeys

    tau(x)>=(x-r)/q>=C.

The terminating integer is nonnegative, so R intersect[C,infinity) lies
in S. Conversely, a tail at most C has every predecessor at most C,
because d+q*C<=r+q*C=C. Therefore a member is critical exactly when its
first integral canonical terminal belongs to{0,...,C}.

Every positive element below1 lies in qS, because it has no q-free
monomial. Valuations at primes dividing a show that no element below1 is
a unit. Thus S has unit group{1}, and the same cancellation argument
shows that q is an atom.

There are no prime elements in this family. To see this, first note that
q*S=S intersect a*R by the zero canonical digit. Since C is an odd prime,
a=C+1 is composite: choose proper integer factors u,v>1 with u*v=a.
Then q divides u*v because a=q*b, but q divides neither u nor v because
a does not divide either integer in R. Thus q is not prime.

For every alpha>1 in S, put h_0=1/b and
h_n=C-(C-h_0)*q^n. The first canonical digit of h_0 is nonzero and
exceeds h_0, so h_0 is outside S. The identity h_n=r+q*h_(n-1) shows
that all h_n are outside S, while h_n approaches C from below. Choose n
with h_n>1 and alpha*h_n>=C. Then z=alpha*h_n and z^2/alpha are in S
by the conductor, but z/alpha is not. Hence alpha divides a square
without dividing its base and is not prime. Every other element below1
is reducible by q, so none can be prime either. This corollary does not
require multiple denominator primes.

## All polynomial representations of a critical element

At a critical tail x<=C, a q-free block P(r) can only be an ordinary
integer in{0,...,C} or the single monomial r: r^2, 2r, and1+r all exceed C.
The residue modulo aR forces the block, except when x=C. At that endpoint
the only choices are the constant C or r followed by the same tail C,
using

    C=r+Cq.

Consequently, if the canonical terminal is below C, there is a unique
nonnegative polynomial representation F(X,Y), evaluated at (q,r).
Its Y-degree is at most1, ordinary coefficients are below C, and any
Y-coefficient equals1 and occurs at a q-degree with no ordinary term.

If the canonical terminal is C at depth n, with canonical prefix P(X,Y),
all representations are exactly

    P(X,Y)+X^n*(C*X^m+Y*(1+X+...+X^(m-1))),  m>=0.

The prefix has q-degrees below n. The parenthesized expression for m=0
means just C. These statements follow recursively from the complete list
of q-free blocks and therefore include arbitrary polynomial expressions,
not only a preferred normal form.

## Every normalized endpoint is an atom

Call an endpoint normalized if its representation has nonzero X-constant
part, equivalently its canonical word has no initial zero digit. This
includes the constant C itself.

Each polynomial representing such an endpoint has highest X-coefficient
equal to the constant prime C. All lower ordinary coefficients are below
C, and all Y-coefficients are at most1. Suppose F=U*V in N_0[X,Y]. The
highest X-coefficients of U,V multiply to C, so one is1 and the other C.
Both X-constant parts are nonzero because F has nonzero X-constant part.

If the factor whose highest coefficient is1 had positive X-degree, its
nonzero X-constant part times the other factor's highest coefficient C
would produce a lower monomial coefficient at least C. This contradicts
the bounds just given, whether that monomial contains Y or not. Hence
that factor has X-degree0 and highest coefficient1, so it is the unit1.
Every representing polynomial is irreducible, proving that the endpoint
value is an atom in S. Primality of C is the only primality used here;
a=C+1 may be composite.

## Exact finite divisor sets

If a critical x has terminal below C, its unique polynomial F bounds every
possible divisor representation. In a factorization x=y*z, choose
nonnegative polynomial representations U,V. Uniqueness forces U*V=F.
Thus their X- and Y-degrees do not exceed those of F, and every coefficient
is at most H, the largest coefficient of F. Enumerating all such finite
arrays and testing membership of x/U(q,r) lists every actual divisor.

If x is an endpoint, remove its e initial zero digits and write

    x=q^e*y,

where y is a normalized endpoint atom. Every representing polynomial is
X^e*F_m with F_m irreducible and with nonzero X-constant part. In any
formal factorization, the orders of vanishing in X add to e; after
removing them, one factor must be1 and the other F_m. Hence the actual
divisor set is exactly

    {q^i:0<=i<=e} union {q^i*y:0<=i<=e}.

In particular every critical element has finitely many actual divisors and
is atomic. The endpoint has the unique atomic factorization consisting
of e copies of q and one copy of y.

For a unique-polynomial critical element, nonconstant formal factors
number at most the total degree of F. Constant nonunit factors number at
most floor(log_2(content(F))), where content is the gcd of its nonzero
coefficients. Thus

    total_degree(F)+floor(log_2(content(F)))

is an explicit bound on nonunit factorization length. Alternatively, the
finite divisor set itself gives a length bound: partial products in a
nonunit factorization are distinct divisors because the unit group is
trivial.

## Finite exact algorithms

1. Check the input belongs to R and run the terminating canonical digit
   procedure. Negative tails reject membership.
2. A nonnegative terminal at most C certifies criticality.
3. For a critical endpoint, use the explicit divisor list above. For a
   critical nonendpoint, enumerate bounded coefficient arrays from its
   unique polynomial and test the cofactor by canonical membership.
4. An element in this finite divisor set is an atom exactly when it has
   no proper nonunit divisor in the same set. Any divisor of a divisor
   is a divisor of the original target, so this test is complete.
5. Enumerate finite multisets of the resulting atoms, using the proved
   length bound and exact products, to list all atomic factorizations of
   the critical target.

No general IDF conclusion is implied by these fixed-target algorithms.
Atom divisors of noncritical targets can still require an independent
height bound or infinite-divisor analysis.

## Multiple denominator primes

Assume b has at least two distinct prime divisors. The usual dense smooth
congruence subgroup provides elements h>1 in S approaching1 and congruent
to1 modulo arbitrarily high powers of a. If a canonical tail c exceeds C,
write x=F+q^n*c. For sufficiently close such h,

    x/h=F+q^n*c_h, c_h in R, c_h>C.

The conductor puts c_h in S. Thus x has infinitely many distinct actual
divisors h, and the same construction can be repeated on the remaining
factor while retaining a tail above C. It has nonunit factorizations of
arbitrarily large length and is reducible.

Combining with the critical case gives exact equivalence of criticality,
finitely many actual divisors, and bounded nonunit factorization length.
It also extends the finite atom test to every S-element: a noncritical
member is reducible, and a critical member has the finite divisor test.
This does not decide whether every noncritical element has an atomic
factorization, nor whether fixed noncritical targets have finitely many
atom divisors.

The implementation [prime_complementary.py](prime_complementary.py)
provides the canonical, critical-divisor, and atom algorithms. Under one
large denominator prime-power block it also enumerates every complete
atomic factorization, as proved in
[PRIME_COMPLEMENT_GLOBAL_FACTORIZATIONS.md](PRIME_COMPLEMENT_GLOBAL_FACTORIZATIONS.md).
The exact checks are in
[check_prime_complementary.py](check_prime_complementary.py); run
`python research/monoids/check_prime_complementary.py` from the repository
root, or `python -m research.monoids.check_prime_complementary`.
