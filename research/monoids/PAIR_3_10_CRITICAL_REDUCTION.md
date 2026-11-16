# An exact critical-value reduction for IDF at (3/10,7/5)

Source status: the canonical digits and conductor were reported by ppdppd
on October 16, and non-atomicity and the integer factorization result on
October 24, in the discussion excerpt supplied by the user. See
[SOURCE_STATUS.md](SOURCE_STATUS.md). The inaccessible draft PDFs have not
been checked; no novelty claim is made for the additional reductions or
algorithms here. IDF for this pair remains unresolved.

This is a partial arithmetic reduction, not a proof or disproof of IDF.
The known non-atomicity result for this pair is credited in
PAIR_3_10_7_5.md. No novelty claim is made for the reduction below.

Put q=3/10, r=7/5=2(1-q), S=N_0[q,r], R=Z[1/10]. The elementary facts
used here are: S has only the unit 1; R intersect [2,infinity) lies in S;
and any expression x=f+q^i*c with f in S, c in R, c>2 forces x to be
multiplicatively reducible. The last assertion uses 2,5-smooth h_L in S
with h_L tending to 1 and h_L-1 in 3^L R, and applies the conductor to
(x/h_L-f)/q^i, which tends to c>2. These facts are proved in the pair note.

## 1. Exact canonical membership and criticality

For x=N/10^n in R choose its digit d from {0,1,r} according to its residue
modulo 3R: the three digits have residues 0,1,2, respectively. Put

  x'=(x-d)/q.

If n>=1, x' has denominator dividing 10^(n-1). Repeat until the first integer is reached; the denominator reduction
ensures that this happens after finitely many steps.

For x in S, every canonical tail x' remains in S. If x>=2, then
x'>=(2-r)/q=2 and the conductor proves this. If 0<=x<2, split an arbitrary
polynomial expression into its q-degree-zero part G(r) and q*H(q,r).
The only possibilities for G are 0,1,Y,Y^2. The first three give the
selected canonical digit. If G=Y^2, its residue is 1 and

  (r^2-1)/q=16/5>=2,

so replacing Y^2 by 1 plus q times an S-element also yields the selected
digit. Hence membership in S is decided exactly by this finite canonical
procedure: all tails must stay nonnegative, and the terminal integer
must be nonnegative. The returned expression certifies membership.

Call x in R intersect [0,2] critical if all of its canonical tails stay
in [0,2]. A critical value belongs S, since the terminal integer is
0,1, or 2 and all digits are nonnegative S-elements.

Every atom except q lies in the critical set intersect [1,2]. Indeed,
any element less than 1 has every polynomial monomial divisible by q,
so an atom less than 1 can only be q. An atom is at most 2 by the
large-block reducibility lemma. A canonical tail exceeding 2 would
apply that same lemma to the finite prefix and make the atom reducible.

Every critical x in [1,2] has v_3(x)=0. A zero first digit would give
x=q*x'<=2q<1, so its first digit is 1 or r (except the integer endpoint
2), and all these values have nonzero residue modulo 3.

## 2. All polynomial representations of a critical value

For a noninteger critical x<2, the q-degree-zero polynomial G(Y) in any
expression must be exactly its canonical digit 0,1, or Y. The only
additional possibility Y^2 would force the next canonical tail to be
at least16/5>2, a contradiction. Thus the choice is forced, and the
argument repeats on the next tail.

The value 0 has only the zero expression, and 1 only the constant
expression. All polynomial expressions for 2 are

  F_m(X,Y)=2X^m+Y*(1+X+...+X^(m-1)),  m>=0,

where F_0=2. To prove this, its q-degree-zero part must be either the
constant2, which ends the expression, or Y, which leaves q times another
expression for2. Iteration terminates because the original polynomial
is finite.

Consequently a critical value whose canonical terminal integer is0 or1
has exactly one polynomial expression. If its canonical expansion ends
in2 at depth n, and P(X,Y) is its prefix, then all its expressions are

  P(X,Y)+X^n*F_m(X,Y),  m>=0.

Every such expression has Y-degree at most1. Its coefficients of Y are
0 or1, its coefficients independent of Y are0 or1 except for a possible
terminal coefficient2, and at each q-degree at most one of the ordinary
and Y coefficients is nonzero. A coefficient2, if present, is at the
highest q-degree. Every q-tail of every such expression has value at
most2.

## 2A. Every normalized endpoint is an atom

Every critical value in [1,2] whose canonical expansion ends in the
integer2 is an atom. This includes2 itself.

For a nonconstant polynomial representation F of such a value, section2
shows that its highest X-degree coefficient is the constant2, every
lower formal coefficient is0 or1, and its X-degree-zero part is nonzero.
Suppose F=G*H in N_0[X,Y]. The leading X-coefficients of G,H multiply to
the constant2, so they are the constants1 and2. Both factors have
nonzero X-degree-zero parts. If both have positive X-degree, multiply
the leading coefficient2 of one factor by the X-degree-zero part of
the other. This creates a formal coefficient at least2 at an X-degree
strictly below deg_X(F), a contradiction. If one factor has X-degree
zero, its multiplication with the other leading coefficient to give2
forces it to be the ordinary integer1 or2. The integer2 cannot divide
F because F has a lower coefficient1. Thus one factor is1. The constant
representation F=2 is formally irreducible as well.

All polynomial representations of the endpoint are therefore formally
irreducible, so it is a numerical atom of S. In particular there is no
irreducibility qualification on the endpoint values in the eventual
IDF criterion below.

## 3. Every critical value in [1,2] is atomic

For a positive rational x in S, let M(x) be the part of its reduced
numerator supported outside {2,5}. For critical x in [1,2], M(x) is
coprime to30 by the v_3 observation above.

First, a nonconstant ordinary binary polynomial G(X), with G(0)=1,
has a unique expression in q,r: all its canonical digits are0 or1 and
its terminal digit is1. Any formal factorization of G into nonnegative
ordinary polynomials consequently transfers exactly to S. The formal
monoid on such polynomials is atomic by induction on degree. Thus G(q)
has an atomic factorization. Its reduced numerator is

  N=sum_i G_i*3^i*10^(d-i),  d=deg(G),

which is odd, is not divisible by5, and exceeds1.

Now suppose a critical nonunit x has a proper factorization x=u*v.
Both factors have v_3=0, hence are at least1: any S-element less than1
has positive v_3. Choose polynomial expressions U,V. Their product is
one of the representations in section2. Its Y-degree is at most1, so
at least one factor is an ordinary polynomial G(X) with positive
constant coefficient. For x<2, that constant is1. If G is binary, keep
it. Otherwise G has a coefficient2. The other factor cannot have any Y
term (the product would contain a coefficient2 on a Y term) and cannot
have any coefficient2 (the product would contain a coefficient4).
Hence the other factor is an ordinary binary polynomial with constant1.
In either case a proper factorization supplies a nonconstant ordinary
binary factor G(q).

The quotient h=x/G(q) is critical. If it had a canonical tail greater
than2, multiply that canonical expression by G(X). Because G(0)=1, the
corresponding q-tail of the product has value at least that of the tail
of h, contrary to section2. The quotient is at least1 and at most2,
as above. Its outside-{2,5} numerator is M(x)/N, where N>1 is the
numerator of G(q), so its number of prime factors with multiplicity
strictly decreases.

Induction on Omega(M(x)) now proves that x is atomic: if x is not
already an atom, extract such a binary factor, factor that binary
polynomial formally, and apply induction to the critical quotient.
When M(x)=1, no proper factorization can supply N>1 dividing M(x), so
every nonunit critical value with M=1 is itself an atom. The endpoint2
is also an atom directly from the F_m representations: a factor
independent of Y would divide both2X^m and1+...+X^(m-1), forcing it to
be1. This handles x=2 in the preceding argument.

## 4. A uniform length bound

Every atomic factorization of a critical x in [1,2] has length at most

  Omega(M(x))+1.

An endpoint has factorization length1 by section2A. More generally,
in a product of polynomial representations, at most one factor can
involve Y or have a coefficient2. Two such exceptional factors would
produce either a Y^2 term, a coefficient2 on a Y term, or a coefficient4,
all impossible by section2. Every other factor is an ordinary binary
polynomial with constant1 and has reduced numerator greater than1,
coprime to10. Those numerators multiply into M(x). There are therefore
at most Omega(M(x)) binary atom factors and at most one other factor.

## 5. Removing all nonendpoint obstructions to IDF

Normalize a critical expression by deleting trailing zeros and collapsing

  r*q^(n-1)+2*q^n=2*q^(n-1)

whenever possible. Write its highest nonzero q-degree as n.

* If the highest digit is1, its numerator over10^n is odd and not
  divisible by5. Thus it equals M(x), and x>=1 bounds 10^n<=M(x).
* If the highest digit is r, its numerator over10^(n+1) has 2-adic
  valuation exactly1 and5-adic valuation0. Thus it equals2M(x), and
  x>=1 bounds 10^(n+1)<=2M(x).
* If the highest digit is2 and the preceding digit is0 (or is absent),
  its numerator over10^n has 2-adic valuation1 and5-adic valuation0.
  Again n is bounded by 10^n<=2M(x).
* A preceding digit r has already been collapsed. The only remaining
  unbounded case is a terminal2 immediately preceded by1.

The valuation assertions follow because the highest term has the unique
least2-adic valuation in the first three cases. At5, a possible tie
between a highest digit1 and preceding r contributes coefficient3+14=17,
which does not cancel; terminal2 cannot have a preceding r after
normalization.

There is in fact at most one nonunit critical value with fixed M among
the first three bounded-valuation cases. Such a value is either M/10^n
or2M/10^n and lies in [1,2]. Two distinct choices have ratio2 times an
integral power of10, or an integral power of10; none can lie strictly
between1/2 and2. The only boundary coincidence is the unit1 versus the
atom2 for M=1. In particular each M gives at most one nonendpoint
critical value, and at most one nonendpoint atom.

Thus only endpoint expressions ending in the two-digit block1,2 can
produce infinitely many critical values with fixed M. Equivalently,
these end in the q-scaled block1+2q=8/5.

## 6. Exact arithmetic criterion for IDF

For a positive M coprime to30, let C_M be the set of critical values in
[1,2] with M(x)=M. Then

  S minus {0} is IDF  iff  C_M is finite for every M coprime to30.

For the reverse implication, an atom divisor of fixed w, other than the
single possible atom q, is a critical value whose outside numerator
M divides M(w). There are finitely many such divisors M, and the assumed
finiteness of each C_M proves IDF.

Conversely every x in C_M divides the fixed integer4M: 4M/x belongs R
and is at least2, so it belongs S by the conductor. Every x in C_M is
atomic by section3 and all its atom factors divide4M. If S were IDF,
only finitely many atom values could occur. The uniform length bound
Omega(M)+1 would then leave only finitely many products, proving C_M
finite.

By sections2A and5, all possibly unbounded candidates are themselves
atoms. Thus this is equivalently the question whether for every M
coprime to30 there are only finitely many terminal2 endpoint values

  x=M*2^u/5^n in [1,2],  n>=1,

whose canonical expansion stays in [0,2] and, after terminal collapses,
ends in the block1,2. Here u may be an integer. At any such endpoint,
writing x=N/10^n gives N=M*2^E with E=u+n>=0. This criterion involves
all critical endpoint values; no separate irreducibility test is needed.

If IDF fails, it already fails at an element with an explicit atomic
factorization of length3. Indeed, choose one endpoint alpha_0 in an
infinite fixed-M family. Every other endpoint alpha in that family
divides4*alpha_0: the quotient belongs R and is greater than2, hence
belongs S. The target has factorization2*2*alpha_0. The finite complete
atomic-factorization theorem in PAIR_3_10_FACTORIZATION_ALGORITHM.md
then implies that all but finitely many of these cofactors are
nonatomic. This is a conditional witness reduction, not an IDF answer.

## 7. Reverse critical orbits for the unresolved endpoint problem

Fix an endpoint with terminal2 and build its digits in reverse. Let N_k
be the numerator of its last k+1 digits over10^k. Then

  N_0=2,
  N_k=3*N_(k-1)+2*delta_k*10^(k-1),
  delta_k in {0,5,7},

where delta=0,5,7 corresponds to preceding digit0,1,r, respectively.
If the final numerator is M*2^E and E>n, all intermediate N_k for k<n
must be divisible by2^(k+1), since all later contributions have at
least that valuation. Hence setting U_k=N_k/2^(k+1) gives

  U_0=1,
  U_k=(3*U_(k-1)+delta_k*5^(k-1))/2.

Integrality at the next stage forces delta=0 when U_(k-1) is even,
and permits delta=5 or7 when it is odd. The initial noncollapsible
choice is delta_1=5, giving U_1=4. The alternative delta_1=7 merely
represents the collapsed endpoint2.

At depth n,

  x=2*U_n/5^n,
  M=odd_part(U_n).

Here 5 does not divide U_n: U_1=4 and, for k>=2,
U_k is congruent to (3/2)*U_(k-1) modulo5.

For x in [1,2], U_n lies in [5^n/2,5^n]. For fixed M and sufficiently
large n, E>n automatically, since M*2^E>=10^n. Thus this integral
branching recurrence captures every sufficiently deep possible
obstruction to IDF. A proof that fixed odd parts occur only finitely
often would settle IDF; no such proof is supplied here.

## 8. Limited computations, not a height bound

The exact necessary criticality test was applied to M*2^E/10^n in[1,2)
for every odd M<=1000 coprime to5 and n<=1000, taking the unique E>=0
that places the value in that interval when one exists. It found38
critical values, all at depths n<=5. A second search with M<=100000
and n<=300 found344 values, all at depths n<=7. A third search with
M<=1000000 and n<=80 found1041 values, all at depths n<=12;555 of these
were nonconstant endpoint values, with no repeated M in that finite
endpoint sample. The boundary endpoint2 is not included in [1,2). For M=1, the only nonunit found
was8/5, at n=1. The separate boundary value2 is critical and atomic.
These finite searches neither prove IDF nor give an eventual degree
bound. The remaining problem is explicitly the arithmetic finiteness
of the reverse orbits in section7.

## 9. The unique prime element

The element q is prime, and every other atom is nonprime. This is a
minor structural consequence of the canonical digits and conductor,
not a resolution of IDF.

Canonical subtraction of the zero digit gives

  q*S = S intersect 3*R.

Every nonzero element of S has nonnegative 3-adic valuation. Thus q
divides a product exactly when at least one factor has positive
3-adic valuation, proving primality. Iterating the identity also gives
the unique decomposition x=q^e*y with e=v_3(x) and v_3(y)=0.

For the other direction, put

  h_n=2-(3/2)*q^n,  n>=0.

These elements of R are outside S: h_0=1/2 has canonical digit r
followed by the negative integer tail -3, and h_n=r+q*h_(n-1).
Consequently h_n approaches2 from below through nonmembers.

Fix any alpha in S with alpha>1. Choose n large enough that h_n>1
and alpha*h_n>=2. The conductor shows that b=alpha*h_n belongs S,
and also that b^2/alpha=alpha*h_n^2 belongs S. But b/alpha=h_n does
not belong S. Thus alpha divides a square without dividing its base,
and cannot be prime. Since q is the only atom below1, it follows that
q is the unique prime element of the multiplicative monoid S\{0}.
