# Boolean forcing removes every denominator-block restriction

The results below are independently derived. Novelty relative to the full
online discussion and its unavailable attachments remains unverified.

## 1. A general coefficient-forcing theorem

Let

    q=a/b^m in(0,1),   r=A/b^k>1,
    a>=2, m,k>=1, gcd(a*A,b)=1, gcd(m,k)=1,
    P={p:p|b}, |P|>=2,
    R=Z[1/b], C=(a-1)/(1-q).

Assume r^m belongs N_0[q] and there is an identity

    2=r+K*q,   K in R, K>C.                               (1)

Then M=N_0[q,r] minus{0} is IDF and non-atomic. More precisely:

* every atom has a basis expression sum_(j=0)^(m-1) r^j*f_j(q) in which
  every coefficient of every f_j is0 or1;
* every atom has strictly negative valuation at every p in P;
* there are no integer atoms and no P-smooth atoms;
* every nonunit P-smooth element has no atom divisor;
* the only positive integer admitting an atomic factorization is1;
* all atom divisors and all atomic factorizations can be decided and listed
  by finite exact algorithms.

There is NO inequality comparing a with a denominator prime or prime-power
block. In particular every denominator prime may be smaller than a.

## 2. Conductor, units, and perturbation

The cyclic digit algorithm gives

    R intersect[C,infinity) subset N_0[q] subset N_0[q,r].  (2)

Every positive P-smooth element of N_0[q,r] is at least1. An element below1
has no q-degree-zero monomial, because r>1, and is therefore divisible by q.
Its valuation at every prime dividing a is positive, impossible for a
P-smooth element. A unit and its inverse must both be P-smooth, so the unit
group is{1}.

The dense congruence subgroup construction from the earlier proofs applies
without any block-size assumption. For a prescribed monomial q^i*r^j choose
near-one P-smooth h_L congruent to1 modulo A^j*a^L R, with

    1+C*q^L<h_L<1+(C+1)*q^L.

These h_L belong N_0[q] by (2). If x=F+c*q^i*r^j with F in the semiring,
c in R, and c>C, then

    z_L=(x/h_L-F)/(q^i*r^j)

belongs R for large L and tends to c>C. Hence z_L belongs the semiring,
and x=h_L*(F+z_L*q^i*r^j) is a nontrivial factorization after avoiding h_L=x.
Thus an atom cannot have an excessive coefficient c>C on any monomial.

## 3. Boolean basis coefficients and the leading numerator

A positive relation r^m=F(q) reduces every element to the finite basis

    x=sum_(j=0)^(m-1) r^j*f_j(q),   f_j in N_0[X].          (3)

If a coefficient of such a representation is at least2, replace one
2q^i*r^j using (1):

    2q^i*r^j=q^i*r^(j+1)+K*q^(i+1)*r^j.

The second term has coefficient K>C, so section2 makes x reducible.
Therefore every basis representation of an atom is Boolean.

The denominator weights mi+kj for 0<=j<m are pairwise distinct, by
coprimality of m,k. Let n be the largest weight in an atom expression and
write alpha=N/b^n without requiring prior reduction. The unique leading
term has coefficient1 and numerator a^i*A^j, coprime to b. Every other term
in N is divisible by b. Consequently

    gcd(N,b)=1.                                          (4)

If n=0, the expression can only be the constant1, which is a unit. Thus
n>0 for every atom, and

    v_p(alpha)=-n*v_p(b)<0 for all p in P.                 (5)

The element q is an atom: in q=yz a factor is below1 and hence is a multiple
of q, forcing the other factor to be a unit. Every atom other than q has a
positive q-degree-zero coefficient in some f_j, or else it factors out q.
That constant block contributes at least1, so

    alpha!=q implies N>=b^n and alpha>1.                  (6)

## 4. IDF, atomless elements, and explicit bounds

Fix x in M and let X be the part of its reduced numerator supported outside
P. For an atom divisor alpha=N/b^n other than q, (4) and outside-P valuation
nonnegativity on the cofactor give N|X. Equation(6) bounds n. Thus ALL atom
divisors occur in the finite list

    {q} union {N/b^n: N|X, 0<=n<=floor(log_b N)}.           (7)

This proves IDF. The list need not consist of atoms; a complete filter is
given below.

A P-smooth atom other than q would have N=1, contradicting (6) and n>0.
The atom q is not P-smooth, since a>1 is coprime to b. Hence there are no
P-smooth atoms. Any atom divisor of a P-smooth element would itself be
P-smooth (outside-P valuations cannot cancel), proving atomlessness of
every nonunit P-smooth element. In particular every prime p|b is atomless,
so the monoid is non-atomic. Equation(5) also shows that no positive integer
greater than1 can be a product of atoms.

## 5. Exact algorithms remain available

Use the general finite-basis membership graph: at states0<=x<C, each constant
basis coefficient is at most floor(C), so take all digits

    D={sum_(j=0)^(m-1) c_j*r^j: 0<=c_j<=floor(C)}.

Accept nonnegative integers and states at least C for membership. The depth
bound max(0,max(h,k(m-1))-m) makes unresolved states finite.

For the atom test explore ALL reachable states up to C, including integers,
and reject an atom claim if any reachable state exceeds C. A representation
with a coefficient2 can be changed by (1) into one with an excessive term,
so it necessarily yields an escaping path: strip its basis constant blocks
until the first tail>C. Before that tail every digit belongs D. Here the excessive term already has r-degree j<m. Expanding K in N_0[q]
leaves the q-tail at level i+1 at least K*r^j>C.

Thus every representation of an escape-free member has Boolean coefficients.
Boolean basis arrays are unique: subtract two arrays and use their largest
weight; its coefficient difference is+1 or-1, coprime to b, while lower terms
are divisible by b. A successful membership path recovers this unique array.

If its q-degree is h, every factor has a Boolean basis representation of
q-degree at most h. Indeed multiplying two positive basis expressions and
reducing r^m=F(q) cannot decrease a q-degree or remove a positive coefficient;
a factor coefficient at least2 would force one in the product. Enumerate
all Boolean arrays of q-degree at most h and use exact cofactor membership.
This decides irreducibility. Filtering (7) therefore gives all atom divisors.

Finally fix a prime ell|a. Copies of q in an atomic factorization of x are
bounded by floor(v_ell(x)/v_ell(a)); all other atoms in the finite divisor
list exceed1, so their multiplicities are bounded by the remaining real
product. This decides and enumerates all atomic factorizations.

The inequality C<a follows automatically from(1): C*q<K*q=2-r<1,
so a*q<1 and b^m>a^2. Consequently C does not belong R, by the same
coprime-denominator argument used in the earlier finite-basis theorem.
The algorithm may nevertheless use strict escape and continue any equality
state; its finite-state proof does not require special treatment of it.

## 6. Any prescribed numerator and denominator-prime support

Fix ANY integer a>=3 and ANY integer b>=2 coprime to a with at least two
prime divisors. Choose k>=1 such that b^k>a and set

    r=2-a/b^k in(1,2).

For every sufficiently large m coprime to k, put q=a/b^m. Then

    2=r+b^(m-k)*q.

As m grows, C=(a-1)/(1-q) tends to a-1, whereas b^(m-k) and r^m grow without
bound. Hence eventually K=b^(m-k)>C and r^m>=C, the latter implying
r^m in N_0[q] by the conductor. The theorem applies to EVERY such m.

The pair is multiplicatively independent: a denominator prime gives
mu+kv=0 in any relation q^u*r^v=1, and0<q^k/r^m<1 rules out a nonzero
solution. It is nonredundant: r has least residue2 modulo aR, exceeding
its real value, so it is not in N_0[q]; and q<1 excludes q in N_0[r].

Therefore for every prescribed numerator a>=3 and every prescribed finite
set of at least two denominator primes disjoint from the primes of a,
there are genuinely mixed, independent, nonredundant IDF/non-atomic examples
with exactly that denominator-prime support. All the denominator primes
may lie below a. These examples satisfy the effective-prime hypotheses in
the supplied Open Problem2.

## 7. A small example with both denominator blocks below the numerator

Take

    q=5/1296=5/6^4,   r=7/6,
    a=5, b=6, m=4, k=1.

The exact identities are

    r^4=1+221q,
    2=r+216q,
    C=5184/1291<5<216.

All hypotheses hold, although both blocks2 and3 are less than5. Its monoid
is IDF and non-atomic; both2 and3 have no atom divisor; no integer greater
than1 admits an atomic factorization. This is a different semiring from
N_0[5/6], whose atomicity remains unresolved in the supplied discussion.

## 8. A ternary family with a particularly short positive relation

For any b coprime to3 with at least two prime divisors, and any c satisfying

    1<=c<b/3, gcd(c,b)=1,

put

    q=3/b^2,   r=2-3c/b.

Then b>=10, 1<r<2, and

    2=r+bc*q,
    r^2=1+(b-c)*(b-3c)*q,
    C=2*b^2/(b^2-3)<3<bc.

Thus every such pair is IDF and non-atomic with no integer atoms and with
every denominator prime atomless. For b=10 the choices c=1 and c=3 give

    (3/100,17/10),   (3/100,11/10).

This family requires no denominator prime-power block to exceed3; the
2-block in these examples is only2.
