# Atomic positive integers up to 10^14 in the binary pair

Let `S=N_0[2/5,2/3]`, put `q=2/5`, `h=5/3`, and set

    alpha=(1+X+X^4)(q)=891/625.

**Computer-assisted finite theorem.** A positive integer `I<=10^14`
admits a factorization into atoms of S if and only if

    I=11^k,  0<=k<=13.

Its atomic factorization is unique up to order and is exactly

    I=h^(4k)*alpha^k.

For k=0 this is the empty factorization of the unit 1. This is a finite
classification, not a statement about all positive integers or a solution
of IDF. Its novelty has not been checked. The proof combines the exact
atom classification with two exhaustive finite checks, described below.

## 1. The two finite inputs

For a binary polynomial `f(X)=sum c_i X^i` of degree n, with both endpoint
digits 1, write

    f(q)=N/5^n,  N=sum_(i=0)^n c_i*2^i*5^(n-i).

The following assertions have been checked exhaustively with integer
arithmetic:

1. For every `1<=n<=100`, one has `v_3(N)<=n`.
2. For every `1<=n<=63`, the only word with `v_3(N)>=n` is
   `f=1+X+X^4`, of degree 4, with `N=891=11*3^4`.

The first input is documented in BINARY_VALUATION_SEARCH.md. The second
uses the same complete modular block reduction, but enumerates **all**
matches at threshold n instead of stopping at the first match.
The standalone `binary_equality_catalog.py` uses ordinary subset masks
and direct right-block sums, independently of the Gray-code implementations.
It examined 2,363,423 right subsets through degree 63 and found only the
displayed word. Ordinary exhaustive full-word checks through degree 18
agree with its complete match lists.

As an additional independent check, the GMP implementation excludes every
degree from 1 through 63 other than 4 at threshold n. Degree 4 has only
eight complete words and is directly exhausted.

The polynomial `1+X+X^4` is formally irreducible in N_0[X]: its constant
coefficient is 1 and its coefficient sum is 3, whereas two nonunit
positive-constant factors would have coefficient sums at least 2 each.
The bounded-series uniqueness theorem therefore makes alpha an S-atom.
Also h is an atom, and exact multiplication gives `h^4*alpha=11`.

## 2. First bound every atom degree by 100

Assume that `1<=I<=10^14` admits an atomic factorization. The exact atom
classification says that every factor is one of:

- q;
- h;
- a finite binary atom of degree n>=1, with `v_5=-n` and `v_3=k>=0`;
- another endpoint atom of index i>=1, with `v_5=-i` and `v_3=-1`.

All atoms except q have 2-adic valuation zero and real value greater than 1.
Thus the number of q factors is exactly `E=v_2(I)`. Write J for the number
of h factors. Since `10^14<2^47`, one has `E<=46`. Removing the q factors
and using the real sizes of all remaining atoms gives

    h^J <= I/q^E,
    h^(J-E) <= I*(3/2)^E <= 10^14*(3/2)^46 < h^101.

The final strict inequality is the exact integer comparison

    3^147 < 2^32*5^87.

Consequently `J-E<=100`. The 5-adic valuation equation is

    sum_(finite factors) n + sum_(other endpoints) i
        = J-E-v_5(I) <= 100.

Here `v_5(I)>=0` because I is an integer. Every finite atom occurring in
the factorization therefore has degree at most 100, so finite input 1
applies to every one of them.

## 3. Force coprimality and equality of valuations

Adding the 2-, 3-, and 5-adic valuation equations yields

    v_2(I)+v_3(I)+v_5(I)
        = sum_(finite factors) (k-n)
          -sum_(other endpoints) (i+1).

The left side is nonnegative. Finite input 1 makes every term `k-n`
nonpositive, and every other-endpoint contribution is strictly negative.
Equality therefore forces all of the following:

- I is coprime to 30, in particular E=0;
- no endpoint atom other than h occurs;
- each finite binary atom has `k=n`.

Now the real bound improves to

    h^J <= I <= 10^14 < h^64,

where the last inequality is exactly `2^14*3^64<5^50`. Thus `J<=63`.
The 5-adic equation, now with E=0 and `v_5(I)=0`, says that the sum of
finite atom degrees is J. Every such degree is at most 63.

Finite input 2 consequently forces every finite atom in the factorization
to be alpha. If it occurs k times, the 5-adic equation gives `J=4k`, and

    I=h^(4k)*alpha^k=11^k.

Conversely this displayed product is an atomic factorization for every k.
The exact comparison `11^13<=10^14<11^14` gives the stated range. The same
argument applies to every possible atomic factorization of I, so its
multiset of atoms is forced, proving uniqueness.

## 4. A sharper certified interval from the same finite inputs

The same classification and uniqueness statement hold for every positive
integer `I<2^47`, that is, `I<=140737488355327`. The powers in this larger
interval are still exactly `11^k` for `0<=k<=13`.

To sharpen the first degree bound, write `I=2^E*t`, with t odd, and put
`r=46-E>=0`. From `I<2^47` one obtains

    t <= 2^(r+1)-1 <= 3^r,
    I*(3/2)^E = 3^E*t <= 3^46 < h^101.

The middle inequality follows by induction on r. The last is the exact
integer comparison `3^147<5^101`. Thus the argument in Section 2 still
bounds every finite atom degree by 100. After coprimality has been forced,
the exact inequality `2^47*3^64<5^64` gives `I<h^64`, so the equality
catalog through degree 63 still suffices.

This particular uniform size estimate first exceeds the checked degree
range at `I=2^47`, since then `I*(3/2)^E=3^47>h^101`, equivalently
`3^148>5^101`. This observation does not preclude extending the theorem
with additional arguments or finite checks.

## 5. Reproduction and preserved catalogs

Run from this directory:

    python binary_equality_catalog.py 1 63
    python check_binary_atomic_integers.py

The independent GMP exclusions at threshold n can be reproduced with:

    /tmp/binary_digit_search 1 3 0
    /tmp/binary_digit_search 5 63 0

Here `/tmp/binary_digit_search` is compiled from
`binary_valuation_digit_search.cpp` as documented in
BINARY_VALUATION_SEARCH.md. Both commands must finish with no threshold
match. Degree 4 is checked separately so that its equality word does not
prematurely stop a command-line scan.

| Artifact | SHA-256 |
|---|---|
| `binary_equality_catalog_1_63.jsonl` | `dd875f7086046f2a6bb1e5685fad625993dc51ff7e51039b1de247aaf3f073ee` |
| `binary_equality_gmp_negative_degrees_1_63.jsonl` | `58336ccfe8c4662efb2366e7471c58b1620075d61d9f4c12bf2ed3c1ab481043` |

The check script verifies the complete catalog, independent small-degree
enumerations, exact inequalities used above, and the displayed atomic
factorizations. It does not loop over all 10^14 integers: the valuation
argument is what transfers the finite word checks to that entire range.
