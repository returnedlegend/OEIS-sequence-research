# Endpoint height reduction when b=C*P

This note supplements
[PRIME_COMPLEMENT_CRITICAL_ALGORITHM.md](PRIME_COMPLEMENT_CRITICAL_ALGORITHM.md).
The ppdppd and Mardcelo source attributions and comparison limitations
stated there apply here too. This note makes no novelty claim and does
not prove the finiteness condition stated below.

Let C>=3 be prime, let P>C+1 be another prime, and put

    a=C+1, b=C*P, q=a/b, r=C*(1-q)=(b-a)/P.

The critical representation theorem applies. Every normalized critical
endpoint terminating at C is an atom. Every other normalized critical
value has a unique finite polynomial representation. Here normalized
means that its canonical first digit is nonzero, so its value is greater
than1 except for the unit1 itself.

For a rational in Z[1/(CP)], its outside numerator means the part of the
reduced numerator coprime to CP.

## Nonendpoint values have bounded degree at fixed outside numerator

Fix an outside numerator M. If the highest nonzero canonical digit is an
ordinary k in{1,...,C-1} at q-degree n, write x=N/b^n. Modulo C, its
leading term k*a^n is nonzero and every lower term vanishes. Modulo P,
the only possible tie is a preceding r digit at degree n-1. Without
that digit the leading term is again nonzero. With it, the two terms sum to

    a^(n-1)*(k*a+C*(b-a)) = a^n*(k-C) mod P,

which is nonzero because1<=k<C<P. (When n=0 there is no preceding digit.)
Thus N is coprime to CP and N=M. Since a normalized value is at least1,
b^n<=M.

If the highest nonzero digit is r at q-degree n, write x=N/b^(n+1).
The leading numerator is

    C*(b-a)*a^n.

All lower terms are divisible by C^2 and by P. Therefore v_C(N)=1 and
v_P(N)=0, so N=C*M and b^(n+1)<=C*M. Thus there are only finitely many
normalized nonendpoint critical values with any fixed M.

## Endpoint numerators and the exceptional preceding digit

Take a nonconstant normalized endpoint whose first integral terminal is
C at depth n>=1. Its preceding digit must be ordinary k in{0,...,C-1}:
a preceding r would give r+qC=C and would have ended the canonical word
one step earlier.

Clearing b^n gives an integer N with v_P(N)=0. Its last two terms give

    N = C*a^(n-1)*(a+P*k)  mod C^2.                    (1)

Every earlier ordinary term is divisible by C^2. Every earlier r-term
also has that divisibility because r's denominator is P, while its
numerator after clearing one b contributes an additional factor C.

Since a=1 mod C, equation(1) implies v_C(N)=1 unless

    k=k_0=-P^(-1) mod C, 1<=k_0<=C-1.                 (2)

In the nonexceptional case N=C*M and n<=floor(log_b(C*M)). Consequently
any unbounded fixed-M endpoint sequence must eventually use the single
exceptional preceding ordinary digit k_0.

Write N=C^E*M. Every endpoint has the form

    x=M*C^(E-n)/P^n in(1,C].                           (3)

The actual P-denominator exponent is exactly n, since v_P(N)=0.

## Exact IDF reduction

The monoid N_0[q,r] minus{0} is IDF if and only if, for each M coprime
to CP, there are finitely many normalized critical endpoints of the
form(3).

Indeed all atoms except q are normalized critical values. The nonendpoint
ones with fixed outside numerator have just been bounded. Any atom divisor
of a fixed target has outside numerator dividing that target's outside
numerator, giving only finitely many M to consider.

Conversely, if infinitely many endpoints share one M, all are atoms in
(1,C]. Choose an integer L divisible by M and satisfying L>=C^2. For every
such atom alpha, L/alpha belongs Z[1/(CP)] and is at least C, so it belongs
the semiring by the conductor. Thus one fixed L has infinitely many atom
divisors. This proves the stated equivalence without an irreducibility
test on endpoint candidates.

## Integral reverse orbit for sufficiently deep candidates

Construct an endpoint from its terminal C by repeatedly prefixing digits.
Let N_k be its numerator when written over b^k after k prefix steps.
For an ordinary digit j, put delta=j*P; for the digit r, put delta=b-a.
Then

    N_0=C,
    N_k=a*N_(k-1)+C*delta_k*b^(k-1),
    delta_k in {0,P,2P,...,(C-1)P,b-a}.                 (4)

Suppose the final N_n=C^E*M has E>n. Then every prefix numerator N_k is
divisible by C^(k+1). To see this, subsequent terms in(4) are divisible by
C^(k+1), so

    N_n=a^(n-k)*N_k mod C^(k+1),

and a is a C-adic unit. Put U_k=N_k/C^(k+1). Equation(4) becomes

    U_0=1,
    U_k=(a*U_(k-1)+delta_k*P^(k-1))/C.                (5)

Every U_k must be an integer. For fixed M and sufficiently large n,
the condition E>n is automatic from x>=1 and
M*C^(E-n)>=P^n. At the endpoint,

    x=C*U_n/P^n,
    P^n/C<=U_n<=P^n,
    U_n=M*C^h for some h>=0.                          (6)

The last equality expresses that the outside numerator is M; P never
divides U_n. To use minimal endpoint words, the first reverse digit cannot
be r, since that merely repeats C. Integrality then forces the first
ordinary digit to be k_0 from(2).

For example C=3,P=5 gives k_0=1 and U_1=(4+5)/3=3, producing the endpoint
atom9/5. This shares outside numerator1 with the constant endpoint3.

The reverse orbit is an exact reduction, not a height bound. No assertion
that a fixed M is visited finitely often, or that different nonconstant
endpoints always have distinct outside numerators, is proved here.
