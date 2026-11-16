# IDF as finiteness of critical S-unit classes

The supplied discussion reports reductions of IDF to critical classes in
Hyunjun Yi's November 2 write-up and Mardcelo's Section 5.2. Those complete
documents have not been inspected. This note is a self-contained recovery
and formulation of a reduction of that kind; **no novelty claim is made**.
See [SOURCE_STATUS.md](SOURCE_STATUS.md) for the source limitations.

Let `1<a<b` be coprime, put `t=a/b`, `S=N_0[t]`, and let `P` be the set
of prime divisors of `b`. Assume `|P|>=2`. Write

    C=(a-1)*b/(b-a),
    K=floor((a-1)/(b-a)),
    M=a*(K+1)-1.

For a nonzero rational in `Z[1/b]`, its **outside numerator** is the part
of its reduced numerator supported on primes outside `P`. For a positive
integer `N` coprime to `b`, define

    K_N = {x in S : x is critical and its outside numerator is N}.

Here criticality means that the entire canonical digit orbit remains at
most `C`. It is equivalent to the first integral canonical terminal being
at most `M`; merely testing that terminal against `C` is insufficient in
general. Every critical element is at most `C`.

## The equivalence

**Theorem.** The multiplicative monoid `S minus {0}` is IDF if and only
if `K_N` is finite for every positive integer `N` coprime to `b`.

This equivalence does not require a finite carry-prefix certificate.

**Proof.** We use two consequences of
[CRITICAL_BOUNDED_FACTORIZATIONS.md](CRITICAL_BOUNDED_FACTORIZATIONS.md):

1. Every noncritical element is reducible, so every atom is critical.
2. A critical element with outside numerator `N` has an atomic
   factorization, and every factorization into nonunits has length at most
   `Omega(N)+floor(log_(p_min) M)`, where `p_min=min P`.

First suppose every `K_N` is finite, and fix a nonzero `x` in `S` with
outside numerator `N`. All valuations outside `P` are nonnegative on `S`.
Thus any atom dividing `x` has outside numerator dividing `N`. Since it is
critical, it belongs to the finite union of `K_D` over positive divisors
`D` of `N`. Hence `x` has finitely many atom divisors.

Conversely suppose the monoid is IDF, and fix `N`. Choose a positive
integer `L` divisible by `N` and satisfying `L>=C^2`. Every critical atom
whose outside numerator divides `N` divides `L` in `S`: its value
`alpha` satisfies `alpha<=C`, the quotient `L/alpha` belongs to `Z[1/b]`,
and `L/alpha>=C`. The real conductor therefore puts this quotient in `S`.
IDF gives only finitely many such atoms. Every element of `K_N` is a
product of at most `Omega(N)+floor(log_(p_min) M)` atoms from this one finite
set. There are finitely many such products, proving the assertion. QED.

Equivalently, IDF asks whether the critical condition bounds the usual
rational height in each class

    N * product_(p in P) p^(z_p),     z_p in Z.

This is a finiteness problem for S-units with a fixed outside numerator.
The theorem supplies no bound on the exponents `z_p`. In particular,
finitely many actual divisors of each *fixed critical target* does not
prove that a whole `K_N` is finite.

## Removing powers of the generator

It suffices to test integers `N` that are not divisible by `a`. Indeed,
the canonical constant digit is zero exactly when `x` belongs to `aR`,
where `R=Z[1/b]`. In that case `x=t*y` with `y` in `S`, and the orbit of
`y` is the orbit of `x` with its initial zero digit removed. Conversely,
the orbit of `t*y` begins with a zero digit and then follows that of `y`.
Since `t<1`, criticality is preserved in both directions.

If `N=a^k*N_0`, with `k` maximal and `a` not dividing `N_0`, division by
`t^k` therefore gives a bijection

    K_N  <->  K_(N_0).

This is also why `t` is the only atom whose outside numerator is divisible
by `a`. When `a` is prime, all other atoms have valuation zero at `a`.

## A necessary condition for atomicity

Every nonunit element with outside numerator `1` is strictly greater
than `1`. Its canonical constant digit cannot be zero, since that would
make its outside numerator divisible by `a`. Thus a nonunit has either
constant term at least `2`, or a positive constant term and another
positive term.

The smooth elements in `S` approach `1` from above. For completeness,
choose `j` and choose a positive `P`-unit `h` such that

    1+C*t^j < h < 1+2*C*t^j,    h=1 (mod a^j R).

Such choices exist: the subgroup of positive `P`-units congruent to `1`
modulo `a^j R` contains a positive power of every denominator prime; two
distinct primes have logarithms of irrational ratio, so this subgroup is
dense in the positive reals. The element `(h-1)/t^j` belongs to `R` and
exceeds `C`, so the conductor gives `h` in `S`. Letting `j` increase gives
smooth nonunits approaching `1`.

Consequently, if `S minus {0}` is atomic, its smooth atoms must approach
`1`. Indeed, every factor of a smooth element is smooth and at least `1`,
so an atomic factorization of `1<h<1+epsilon` contains an atom in that
same interval. All these atoms are critical. In particular, finiteness of
`K_1` alone suffices to prove non-atomicity; global IDF is a stronger
condition.

## Specialization to 5/6

Here `C=M=24`, and the reduced canonical terminal test is `terminal<=24`.
The exact IDF question is whether, for every `N` coprime to `30`, only
finitely many pairs of integers `(u,v)` give

    x=N*2^u*3^v in S with canonical terminal at most 24.

The finite-prefix theorem in
[CRITICAL_FINITE_DIVISORS.md](CRITICAL_FINITE_DIVISORS.md) proves finite
actual divisors for each such *fixed* `x`, and a terminating atom test.
It does not bound the heights of all these `x` as `(u,v)` varies. Neither
the equivalence above nor a finite numerical scan settles this remaining
height question or the global atomicity of `5/6`.
