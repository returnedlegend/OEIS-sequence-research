# Density-one IDF for ternary mixed families over any prime p>3

This is an independently derived extension of the nearby family
N_0[3/(5n),7/5]. Novelty relative to the supplied discussion or the
literature is unverified. The density statement is not a claim that
every parameter has a finite carry tree or is IDF.

## Parameters and conclusion

Fix a prime p>3 and an integer A satisfying

    p<A<2p,  A=2p mod3.

For every integer n with

    n>=4, gcd(n,3A)=1, |P(pn)|>=2,

put q=3/(pn), r=A/p, R=Z[1/(pn)], S_n=N_0[q,r].

Every such monoid has trivial units and is non-atomic; no integer greater
than1 has an atomic factorization. Among these admissible parameters,
the set for which the finite carry certificate proves IDF has relative
natural density1. Consequently the IDF parameters themselves have relative
natural density1. The pair is multiplicatively independent and nonredundant.

Examples of fixed second generators include7/5,8/7, and11/7.

## 1. A uniform ternary digit system for every n>=4

The residues of D={0,1,r} modulo3R are0,1,2. The nonzero digit carries are

    (2-r)/q       = n*(2p-A)/3,
    (1+r)/q       = n*(p+A)/3,
    (2r-1)/q      = n*(2A-p)/3,
    (r^2-1)/q     = n*(A^2-p^2)/(3p).

The first three are nonnegative integers. The last belongs R and exceeds
8/3, since n>=4 and A^2-p^2>2p. The cyclic conductor is

    C_0=2/(1-q)<=40/17<8/3,

because q<=3/20. Thus every carry belongs N_0[q], and

    S_n=qS_n disjoint-union(1+qS_n) disjoint-union(r+qS_n).

Put C_n=r/(1-q). Since2p-A is a positive multiple of3,
n*(2p-A)>6, so C_n<2. Also

    3A/[p(A-p)] = 3/p+3/(A-p) <=3+3/p<4<=n,

which gives r^2>C_n. Canonical iteration subtracts the residue digit and
divides by q. Its minimal pn-denominator depth decreases until an integer
is reached. As in the nearby-family proof, C_n is a real conductor, the
critical elements are exactly finite D-words, and every atom is critical.

The conductor can be taken inclusive. If C_n belonged R, its maximal-digit
canonical orbit would be a nonintegral fixed point in(1,2), contradicting
the strict denominator-depth decrease.

The excessive-block perturbation uses the at least two denominator primes:
a q-block containing r^2 exceeds C_n, as does a block with two nonzero
monomials. Therefore every atom is a finite D-word; q is the only atom
below1. Units are trivial because an element below1 is a multiple of q
and has positive3-adic valuation, while every S_n-element has nonnegative
3-adic valuation.

## 2. Non-atomicity holds for every admissible parameter

Choose a prime l dividing n with l!=p, which exists because |P(pn)|>=2.
The hypothesis gcd(n,3A)=1 makes every nonzero digit an l-adic unit.
A finite word of highest q-degree N therefore has

    v_l(x)=-N*v_l(n).

Every atom has nonpositive l-adic valuation. An atomic factorization of
an integer could consequently use only degree-zero atoms. The only
nonunit degree-zero digit is r, but every positive power of r has negative
p-adic valuation. Therefore no integer greater than1 has an atomic
factorization, proving non-atomicity for every admissible n.

## 3. Finite p-integral closure is an all-height IDF certificate

If v_p(x)<0, then v_p(qx)<=-2, strictly below all digit valuations. Thus
v_p(d+qx)<0 for every d in D. Every suffix of a p-integral finite word
is therefore p-integral, and its top nonzero digit must be1.

Starting from1, repeatedly retain those prefix images d+qx with
nonnegative p-adic valuation. A finite closed reachable set F_n contains
all p-integral critical elements, at every word length.

Outside this finite exception set, an atom has negative p-adic valuation
and nonpositive valuation at every other denominator prime. Its reduced
numerator is consequently coprime to pn. For any fixed target, the
numerator of such an atom divisor divides the target's outside numerator;
the atom exceeds1 unless it is q, so its denominator is bounded by that
numerator. This gives finitely many atom divisors. Adjoining q and F_n
proves IDF whenever the closure is finite.

For n divisible by p, all three prefixes of1 have negative p-adic
valuation, so the closure is just{1}. For n coprime to p, a first retained
prefix must be r+q=(A*n+3)/(p*n); it can occur only when

    n=-3*A^(-1) mod p.                                (1)

Every other residue class has the same trivial closure.

## 4. Polynomial numerators and unique root classes

For n coprime to p, a word of length L built by prefixing digits to terminal1
has value H_w(n)/(pn)^L, where H_w is an integer polynomial. The first
retained digit is r, giving

    H_1(n)=A*n+3.

For every subsequent prefix, the numerator recursion is one of

    H_{L+1}=3H_L,
    H_{L+1}=3H_L+(pn)^(L+1),
    H_{L+1}=3H_L+A*p^L*n^(L+1).

It follows for every word of length L>=1 that

    H_w(n)=3^(L-1)*(A*n+3) mod p,
    H'_w(n)=A*3^(L-1) mod p !=0.                      (2)

There is exactly one root class modulo p, namely(1), and its derivative
is a unit. The elementary unique-lifting argument therefore gives exactly
one root class modulo p^L. Explicitly, replacing a root c modulo p^j by
c+t*p^j changes the polynomial modulo p^(j+1) by
t*p^j*H'_w(c), so exactly one t in{0,...,p-1} lifts it.

A retained length-L word must satisfy H_w(n)=0 mod p^L. There are at most
3^(L-1) such words after the forced first r. Consequently the parameters
admitting a retained word of length L lie in at most3^(L-1) residue classes
modulo p^L. Different words may give the same class, so this is an upper
bound, not an equality.

## 5. Density-one conclusion

An infinite reachable closure contains words of arbitrarily large length:
there are only finitely many words at each bounded length. Thus its
parameter set E is contained, for every L, in the preceding union of
residue classes. Hence

    upper_natural_density(E) <=3^(L-1)/p^L

for every L. Since p>3, the right side tends to0, proving that E has
upper natural density0. No exchange of limiting operations is required.

The admissible integers have positive natural density: gcd(n,3A)=1 has
density phi(3A)/(3A), and excluding parameters supported only on p removes
only a zero-density set. Therefore E also has relative density0 among
admissible parameters. All remaining admissible parameters have a finite
closed p-integral tree and hence are IDF by section3. This proves the
relative density-one theorem.

A quantitative finite-range version follows immediately. For N>=2 put
k=ceil(log_p N). Each residue class modulo p^k contains at most one integer
in[1,N], so all but at most

    3^(ceil(log_p N)-1) <= N^(log_p 3)

admissible parameters up to N have a finite tree of height below k and an
explicit IDF certificate. This bounds parameters not certified by that
particular finite-depth search, not parameters actually failing IDF.

This argument leaves open whether any admissible parameter has an infinite
closure, and whether such a parameter would actually fail IDF. It proves
neither universal termination nor universal IDF.

## 6. Independence and source attribution

The3-adic valuations of q and r are1 and0 respectively, so a multiplicative
relation forces the exponent of q to be0, then the exponent of r to be0.
The residue of r modulo3 is2>r, so r is outside N_0[q]; q<1 excludes q
from N_0[r].

The canonical-prefix and conductor methods build on the supplied discussion,
including ppdppd's October24 argument. The finite closed-graph method and
the unit-derivative density calculation are stated with complete proofs
here without asserting novelty against the unavailable source documents.
