# An obstruction to recurrent-degree constructions

This is a restriction on particular proposed infinite families, not an IDF
proof. Novelty has not been checked.

## 1. A discrete-ratio lemma

Fix positive real numbers M,B,r with B>1 and r>1, and a finite set
E of positive real numbers. Suppose

    x_j = M*eta_j*r^k_j/B^n_j,
    eta_j in E, k_j,n_j in Z,

and x_j converges to a positive limit xi.

If fixed integers c_0,...,c_d, not all zero, and c satisfy

    sum_(i=0)^d c_i*n_(j+i) = c

for every sufficiently large j, then y_j=log(x_j)-log(xi) satisfies

    sum_(i=0)^d c_i*y_(j+i) = 0

for every sufficiently large j.

Indeed, put S=sum c_i. The product

    R_j = product_(i=0)^d x_(j+i)^c_i

belongs to

    M^S*B^(-c)*E'*r^Z,

where E' is the finite set of possible products of the eta factors.
This set meets every compact subinterval of (0,infinity) in finitely many
points. Since R_j converges to xi^S, it is eventually exactly xi^S.
Taking logarithms proves the assertion.

Only one unbounded exponent k_j occurs here. The analogous union of
powers of two multiplicatively independent numbers is generally dense,
so the discreteness argument would fail in that setting.

## 2. Affine degree recurrences

Under the preceding hypotheses, suppose

    n_(j+1)=d*n_j+c

with fixed integers d>=1 and c. Then x_j is eventually constant.

The lemma gives y_(j+1)=d*y_j eventually. Because y_j tends to zero, this
forces y_j=0 for every sufficiently large j. Thus a nonconstant family
with these exact degree recurrences cannot both converge and retain the
specified one-dimensional unit form.

This covers arithmetic degree progressions (d=1) and geometric/affine
progressions such as n_j=2^j-1. No rate of convergence is required here.

## 3. General recurrences with fast prefix convergence

For a general recurrence as in Section 1, assume in addition that
x_j-xi decays faster than every exponential in j:

    R^j*abs(x_j-xi) -> 0 for every R>1.

Then x_j is again eventually constant.

By Section 1, y_j satisfies a fixed homogeneous linear recurrence. Its
logarithmic errors have the same superexponential decay because xi>0.
A nonzero sequence satisfying such a recurrence cannot decay this fast.
For an elementary proof, discard initial zero coefficients of the
recurrence and arrange that c_0!=0. If its order is positive, let
A=sum_(i=1)^d abs(c_i/c_0) and C=max(1,A). Then

    abs(y_j) <= C*max_(1<=i<=d) abs(y_(j+i)).

Starting at any nonzero y_j, repeatedly choose a later term attaining
this lower bound. This gives an unbounded subsequence whose absolute
values are bounded below exponentially in their indices, contradicting
the assumed decay. An order-zero recurrence forces y_j=0 directly.

For bounded-coefficient polynomial prefixes, the rate condition is easy
to verify. Suppose F_j and a fixed infinite digit word agree through
position L_j-1, all digits lie in {0,...,a-1}, and q in (0,1). Then

    abs(F_j(q)-xi) <= (a-1)*q^L_j/(1-q).

Consequently L_j/j -> infinity suffices. In particular, when actual
polynomial degrees obey a fixed linear recurrence and the common prefix
length grows exponentially, a fixed-outside-part family cannot persist
at every iteration. Fibonacci- or Pell-degree prefix constructions fall
under this statement whenever their stated degree and prefix conditions
are verified.

## 4. Application to the two pairs under investigation

For q=2/5, finite binary polynomials with positive constant coefficient
and fixed outside-{3,5} numerator part M have

    F_j(q)=M*3^k_j/5^n_j,

where n_j is the actual degree. Thus Sections 1-3 apply with E={1}, r=3,
and B=5.

For q=4/9, finite polynomials with coefficients in {0,1,2,3}, positive
constant coefficient, and fixed outside-{3,5} numerator part M have

    F_j(q)=M*3^s_j*5^k_j/9^n_j,  s_j in {0,1}.

The bounded exponent s_j follows from the leading digit: the numerator
over 9^n_j is congruent to d_n*4^n_j modulo 9, with 1<=d_n<=3.
Here E={1,3}, r=5, and B=9.

In either pair, eventual equality of evaluated values forces eventual
equality of the finite digit polynomials by uniqueness of bounded-digit
representations. Hence the hypotheses exclude an infinite family of
distinct such polynomials.

## Scope limitations

- The numerator part M must be fixed (or range over a fixed finite set,
  which can be absorbed into E). Arbitrarily varying M is not covered.
- The recurrence concerns actual polynomial degrees, not an unverified
  nominal block length before trailing zero coefficients are removed.
- The entire proposed sequence, or a subsequence that itself satisfies
  the stated degree recurrence, must consist of successful values.
  Infinitely many successful iterates at irregular indices are not ruled out.
- A general linear recurrence alone is insufficient for Section 3: the
  superexponential prefix-convergence hypothesis is essential to the proof.
- A normalized multiplicative rotation need not converge. The attempted
  (4/9,4/5) orbit 2*(5/3)^n/(9/5)^m therefore is not excluded merely by
  this lemma.

These results eliminate several natural exact substitution or recurrent-
degree constructions. They do not prove finiteness of all solutions to
the remaining restricted-digit equations.

## 5. Bounded recurrence residuals also suffice

The exact constant c in Section 1 can be replaced by a bounded integer
sequence c_j:

    sum_(i=0)^d c_i*n_(j+i)=c_j,  sup_j abs(c_j)<infinity.

Indeed B^(-c_j) then ranges over a finite set and can be absorbed into E'.
The same discrete-ratio proof gives the same eventual homogeneous
recurrence for the logarithmic errors. Therefore all conclusions above
remain valid with bounded integer recurrence residuals.

For example, if integers u>=v>=1 satisfy

    v*n_(j+1)-u*n_j = O(1),

convergence of x_j alone forces eventual constancy: the logarithmic error
eventually satisfies y_(j+1)=(u/v)*y_j. More general bounded-residual
recurrences still require the superexponential convergence condition used
in Section 3. This covers bounded integer perturbations of many standard
block-length or Pell-type degree sequences, when the stated hypotheses
are verified.

## 6. Logarithmic separation forces very large degree gaps

This section uses the standard effective lower-bound theorem for a
nonzero linear form in logarithms of fixed positive algebraic numbers
(Baker's theorem, or its explicit refinements). Only the following
two-logarithm consequence is needed: for fixed multiplicatively
independent positive rationals r,B>1, there are constants c,C>0 such that

    0 < abs(K*log(r)-L*log(B))
        >= c*max(2,abs(K),abs(L))^(-C)

for all integers K,L. No numerical value of these constants is claimed
or needed here.

Consider two distinct finite binary polynomials F,G with constant
coefficient 1 and fixed outside-{3,5} numerator part M. Write

    F(2/5)=M*3^k/5^n,  G(2/5)=M*3^k'/5^n',
    K=k-k',  L=n-n'.

Their values belong to [1,5/3), so

    abs(K)*log(3) <= abs(L)*log(5)+log(5/3).

The logarithmic linear form is nonzero by uniqueness of the digit
representation. If their digit words, extended by trailing zeros, agree
in positions 0 through m-1, then

    abs(log(F(2/5)/G(2/5)))
      <= abs(F(2/5)-G(2/5)) <= (5/3)*(2/5)^m.

Combining the lower and upper bounds gives constants c_0,c_1>0,
depending only on the two primes, such that

    max(2,abs(n-n')) >= c_0*exp(c_1*m).

In particular, an infinite nested-prefix fixed-M family must have at
least exponentially large degree gaps in the common prefix length.
Any proposed sequence with unbounded common-prefix lengths m_j and
log(2+abs(n_(j+1)-n_j))=o(m_j) is impossible. This applies without any
recurrence assumption on the degrees. It does not imply that only
finitely many fixed-M words exist: extremely sparse families are not
excluded.

The same conclusion holds for the (4/9,4/5) bounded-digit family.
Here values with positive constant coefficient lie in [1,27/5), and

    F(4/9)/G(4/9)=3^(s-s'-2L)*5^K,  s,s' in {0,1}.

The exponent of 3 is bounded by 2*abs(L)+1, while the real bound gives
abs(K)=O(abs(L)+1). Apply the same two-logarithm lower bound to log(3)
and log(5). Prefix agreement gives the upper bound
(27/5)*(4/9)^m. Thus the same exponential degree-gap conclusion follows,
with different positive constants. As in the binary case, the common
outside numerator part M cancels exactly in the ratio.

## 7. Stronger two-prime recurrence obstruction via Gelfond--Schneider

For the actual two-prime families, the superexponential convergence
condition in Section 3 can be removed by using a standard transcendence
theorem. This strengthening does not assert the same conclusion for the
arbitrary finite set of real factors E in Section 1.

**Theorem.** Let r,B>1 be multiplicatively independent positive
algebraic numbers, let M>0 be fixed, and let k_j,n_j be integer sequences.
Suppose

    x_j=M*r^k_j/B^n_j -> xi>0,

and some nonzero polynomial P in Z[T] has bounded degree-sequence
residuals P(T)n_j, where T is the forward shift. Then both k_j and n_j
are eventually constant. In particular x_j is eventually constant.

**Proof.** Write P(T)=sum c_i T^i and C=sum c_i. Taking logarithms of
the convergent products gives

    log(prod_i x_(j+i)^c_i)
       = C*log(M)+(P(T)k_j)*log(r)-(P(T)n_j)*log(B)
       -> C*log(xi).

The integer P(T)n_j is bounded by hypothesis, so the displayed relation
also bounds the integer P(T)k_j. Consequently these products range over
a finite set and hence are eventually equal. Multiplicative independence
of r and B then forces P(T)k_j and P(T)n_j to be individually constant
for all sufficiently large j. Both exponent sequences therefore satisfy
the same homogeneous recurrence

    (T-1)*P(T)u_j=0

eventually.

An integer sequence satisfying a homogeneous recurrence with integer
coefficients is, after discarding any finite initial contribution from
the root zero, an exponential polynomial

    u_j=sum_lambda p_lambda(j)*lambda^j,

where each lambda is algebraic and every polynomial p_lambda has
algebraic coefficients. This follows either from the companion matrix
over the algebraic numbers or from solving the confluent Vandermonde
system for the finitely many integer initial values. Apply this to k_j
and n_j using their common characteristic polynomial.

The real sequence

    k_j*log(r)-n_j*log(B) -> log(xi/M)

is also an exponential polynomial. In a convergent exponential
polynomial, every mode with abs(lambda)>1 vanishes, as do all positive-
degree polynomial modes with abs(lambda)=1 and all constant modes with
abs(lambda)=1, lambda!=1. For completeness, choose the largest modulus R
and then the largest polynomial degree d among offending modes. Divide
by R^j*j^d. If R>1 or d>0, convergence makes this quotient tend to zero,
while its leading part is a finite sum sum a_lambda*(lambda/R)^j of
distinct unit-circle exponentials. The Cesaro mean of the squared
absolute value of that sum tends to sum abs(a_lambda)^2, because every
cross geometric average tends to zero. Thus all leading coefficients
vanish. Descending through the finitely many modes removes them all.
For the remaining constant unit-circle modes, subtract the limiting
constant and use the same squared-mean argument.

Each coefficient required to vanish has the form

    A*log(r)-D*log(B)=0,  A,D algebraic.

Gelfond--Schneider implies that log(B)/log(r) is transcendental: it
cannot be rational by multiplicative independence, and if it were
algebraic irrational, r^(log(B)/log(r))=B would be transcendental.
Therefore the displayed cancellation forces A=D=0. It follows that the
individual exponent sequences k_j and n_j have only a constant mode and
modes with abs(lambda)<1. They each converge. A convergent integer
sequence is eventually constant, proving the theorem.

For binary fixed-M values, use r=3,B=5 and the actual degree n_j.
For the (4/9,4/5) fixed-M family, absorb the bounded extra power of 3:

    x_j=M*5^k_j/3^m_j,  m_j=2*n_j-s_j,  s_j in {0,1}.

If P(T)n_j is bounded, then P(T)m_j is bounded as well. The theorem with
r=5,B=3 makes k_j and m_j eventually constant. Since s_j is uniquely
determined by the parity of m_j, both s_j and n_j are eventually
constant. Hence a convergent sequence of distinct bounded-digit
polynomials with fixed outside part cannot have degrees satisfying any
fixed nonzero integer linear recurrence with bounded residuals.

This is a restriction on a proposed infinite family, not a proof of IDF.
An irregular subsequence of successful degrees need not retain a fixed
bounded-residual recurrence, and the fixed-M hypothesis remains essential.
