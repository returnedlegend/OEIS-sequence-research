# Exact finite checks of the binary numerator valuation bound

**Status.** Exact exhaustive computation proves

    v_3(sum_(i=0)^n c_i*2^i*5^(n-i)) <= n

for every degree `1<=n<=100`, with `c_0=c_n=1` and all other digits in
`{0,1}`. This is a finite result. The assertion for all degrees, and hence
the proposed sufficient route to IDF, remain unproved. The equality case
`1+X+X^4` gives numerator `891=11*3^4` at degree 4.

The algorithms and reductions below were derived in this session. Novelty
has not been checked. They replace the earlier floating-point MILP reports
with exact exclusions; no solver infeasibility assertion is needed here.

## 1. The exact modular problem

Fix degree n and a valuation threshold e, normally e=n+1. Put

    T=3^e,
    N=5^n+2^n+sum_(i=1)^(n-1) c_i*2^i*5^(n-i).

A counterexample at this degree exists exactly when some binary choice of
the n-1 free digits makes N divisible by T. All computations below use
integer arithmetic. Every positive result is reconstructed as a complete
digit word and its integer numerator is checked independently.

## 2. Conventional meet-in-the-middle search

Split the free digits into two halves. Store all subset residues of one
half modulo T. Stream the other half and test for the complementary residue
to `-5^n-2^n`. This covers every binary word, regardless of collisions
between residues. The Python implementation uses a hash set; an independent
C++ implementation sorts two vectors and merges them.

Both enumerate subsets in Gray order: each step toggles exactly one digit,
so its residue changes by addition or subtraction of one fixed weight.
The usual complexity is exponential in roughly n/2, including a subset
table of that size.

The ordinary-mask test program independently checks the Gray recurrence,
both positive and negative threshold cases, and witness reconstruction.

## 3. A table-free search using exact digit decoding

The left subset table can be eliminated. Split after free digit m:

    sum_(i=1)^m c_i*2^i*5^(n-i) = C*A,
    C=2*5^(n-m),
    A=sum_(j=0)^(m-1) c_(j+1)*2^j*5^(m-1-j).

Every such m-digit block satisfies

    0 <= A <= A_m=(5^m-2^m)/3.

Choose the largest m<=n-1 such that A_m<T. Since C is invertible modulo T,
each choice of the remaining n-1-m right digits determines one residue

    A == -(5^n+2^n+right_sum)/C  (mod T).

Take its representative in `[0,T)`. Because A_m<T, this is the only possible
ordinary integer value of the left block. Reject it if it exceeds A_m.
Otherwise test its digit representation directly.

For a remaining block of length j+1, its first digit is `d=A mod 2`, because
the constant weight `5^j` is odd and all other weights are even. Subtract
`d*5^j`, reject a negative result, and divide by 2. Continue with length j,
checking its maximum possible value as well. The input is a valid block
exactly when this process reaches zero after all m digits. Thus every
right subset is tested against its unique possible left block, and no
solution is omitted. There is no stored subset table.

When e=n+1, the selected split has

    m = n*log(3)/log(5)+O(1),
    n-1-m = (1-log(3)/log(5))*n+O(1).

Consequently the number of streamed subsets grows like
`2^(0.317394...*n)`, up to a constant factor, rather than `2^(n/2)`.
Worst-case decoding adds a polynomial factor. Storage consists of O(n)
integers of O(n) bits.

At degree 100 the chosen left block has 69 digits and the right block has
30. Exhausting all 1,073,741,824 right subsets excludes every one of the
`2^99` full binary words. This is an exact exhaustive reduction, not random
sampling or a truncation of possible left blocks.

## 4. Reproduction and independently checked controls

Python requires only the standard library:

    python binary_valuation_mitm.py 1 40
    python binary_valuation_digit_search.py 1 100
    python check_binary_valuation_mitm.py

The faster independent table-free implementation uses GMP:

    g++ -O3 -std=c++17 binary_valuation_digit_search.cpp -lgmpxx -lgmp -o /tmp/binary_digit_search
    /tmp/binary_digit_search 1 100
    python check_binary_valuation_mitm.py --gmp-binary /tmp/binary_digit_search

The two command-line programs accept an offset from degree for the
valuation threshold. Offset 1 tests the conjecture; offset 0 at degree 4
is a positive control that finds 891 and explicitly reports that it does
not violate the degree bound. Explicit resource caps raise an inconclusive
exception or return a nonzero status, never a mathematical exclusion.

The check script passed 260 independent Gray-code comparisons, 123 exact
threshold comparisons through degree 18 for both Python algorithms and
the GMP implementation, and 64 reconstructed positive controls. It also
checks the equality case, maximal block selection, and resource limits.
The ordinary MITM C++ implementation independently agreed on degrees
31 through 57; the Python MITM implementation completed degrees 1 through
50. The table-free GMP implementation completed every degree 1 through
100 with no match at threshold n+1. Its complete run took about 282 seconds
and its recorded peak resident memory was 8,576 KiB in this environment.

## 5. Preserved exact outputs

All listed JSONL files contain a completed row for every degree in their
stated range. The search output is evidence from an audited exhaustive
algorithm, not a short independently checkable infeasibility certificate.
The code and positive-control tests make the computations reproducible.

| Artifact | Degrees | SHA-256 |
|---|---:|---|
| `binary_valuation_digit_search_cpp_1_100.jsonl` | 1--100 | `3af02d6766503397df103c81a8a1d46fe194a68a48c915f2e28623a965352a85` |
| `binary_valuation_mitm_cpp_31_57.jsonl` | 31--57 | `9b447d836ae21dfed9aa344a902d3b6f5c21c8ceaa2692cad67c1d72154d1643` |
| `binary_valuation_mitm_python_1_50.jsonl` | 1--50 | `b7b712090669e1f934eb2ff17c8b340bc70e36fcfd9f2a7bae0e99245ee07d59` |

The older C++ MITM log uses the key `counterexample`; every stored row
has threshold n+1, so its `false` value has exactly the same meaning as
`threshold_match:false` in the newer logs. Resource measurements for the
GMP run are preserved separately in
`binary_valuation_digit_search_cpp_1_100.resources.json`.

These finite exclusions do not provide a bound on the degree of a possible
first counterexample. A separate mathematical argument is still required
to establish the all-degree inequality or IDF.
