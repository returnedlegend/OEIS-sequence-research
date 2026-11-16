# A finite carry automaton for ratios of endpoint atoms

Source status: the canonical digits and conductor were reported by ppdppd
on October 16, and non-atomicity and the integer factorization result on
October 24, in the discussion excerpt supplied by the user. See
[SOURCE_STATUS.md](SOURCE_STATUS.md). The inaccessible draft PDFs have not
been checked; no novelty claim is made for the additional reductions or
algorithms here. IDF for this pair remains unresolved.

Put q=3/10 and r=7/5. Every value

  x=sum_{i=0}^{n-1} d_i*q^i+2*q^n,
  d_i in {0,1,r}, d_0 in {1,r},

is an atom, with the possible repetitions of the value2 coming from
all-r prefixes. This follows from the endpoint theorem in
PAIR_3_10_CRITICAL_REDUCTION.md. Here we give an exact finite algorithm
for deciding whether two **nonconstant endpoints**, meaning endpoints
strictly below2, can have a prescribed ratio A/B with A,B positive
integers coprime to3.

This yields certified exclusions at all word depths for each fixed
ratio. It does not prove the full IDF finiteness statement.

## 1. Equalizing depths

The identity2=r+2q permits an endpoint representation to be extended
by arbitrarily many trailing r digits. Thus any two endpoint values
can be expressed at a common depth N with both terminal tails equal2.
Let x_i,y_i be their successive tails. If x=(A/B)*y, put

  k_i=A*y_i-B*x_i.

Then k_0=0, while k_N=2(A-B). Write the digit values as D_i/10,E_i/10,
where D_i,E_i belong{0,10,14}. From x_i=D_i/10+q*x_{i+1} and the
corresponding equation for y_i, obtain

  k_{i+1}=(10*k_i+B*D_i-A*E_i)/3.                  (1)

Every tail is in[0,2], so

  -2B <= k_i <= 2A.                               (2)

Every k_i is an integer. Initially k_0=0. If k_i is an integer, (1)
places k_{i+1} in (1/3)Z. On the other hand, the actual tails belong
R=Z[1/10], so k_{i+1} belongs R. Since (1/3)Z intersect R=Z, the next
carry is an integer as well.

Thus every actual pair gives a path through finitely many integer
states in[-2B,2A], using only transitions for which the numerator in
(1) is divisible by3.

## 2. A finite acceptance test

Start with carry0. For the first transition require D,E in{10,14},
so both initial endpoint values are at least1. Later transitions allow
all D,E in{0,10,14}. Track two Boolean flags: whether a digit other
than14 has occurred on the x side and on the y side. An endpoint is
strictly below2 exactly when its flag is true, because the all-r word
has value2 and replacing any digit by0 or1 strictly lowers the value.

Accept exactly when the carry is2(A-B) and both flags are true.

Conversely, any accepted path of length N reconstructs endpoint values
by starting with x_N=y_N=2 and applying the selected digit maps in
reverse order. These values lie in[1,2), and recurrence(1) with its
starting and ending carries proves A*y=B*x. Thus acceptance is
**equivalent** to the existence of the desired pair.

There are at most4*(2A+2B+1) carry-and-flag states. Breadth-first search
therefore terminates, and exhaustion without acceptance certifies that
there is no such pair at any word depth. The implementation records
predecessors, so an accepted path would also return exact rational
endpoint witnesses.

## 3. Endpoint collisions with fixed outside numerator

If two distinct nonconstant endpoints have the same outside-{2,5}
reduced numerator M, let their denominator depths be n>m. Their ratio
is

  x/y=2^u/5^v,  v=n-m>=1.

Because both endpoints lie in[1,2), the ratio lies strictly between
1/2 and2, so u is positive. For B=5^v, the only possible powers A=2^u
are obtained with

  u in {B.bit_length()-1, B.bit_length()}.

This is exact and uses no floating-point logarithms. Reordering the
two endpoints if necessary places the deeper endpoint in the numerator,
so testing these ratios covers every possible positive depth gap v.

The constant endpoint2 is deliberately excluded by the two flags:
2 and8/5 already share M=1 and have depth gap1.

## 4. Exact finite computation

The scripts

  endpoint_ratio_automaton.py
  endpoint_ratio_gap_scan.py

implement the automaton and the gap scan using Python integers and
Fractions. The completed run

  python endpoint_ratio_gap_scan.py 10000

tested all20000 possible ratios for1<=v<=10000. Every search exhausted
its reachable graph without acceptance. No state cap was reached.
The largest reachable graph had1027 carry-and-flag states, at
(u,v)=(2779,1197). The complete summary is in

  endpoint_ratio_gap_scan10000.log.

Consequently, subject to the exact finite computation just described,
any two distinct nonconstant endpoint atoms with the same outside
numerator M have denominator-depth difference greater than10000.
This exclusion holds at **arbitrary individual word depths**, not
merely for words of length at most10000.

An infinite fixed-M family could still have unbounded gaps. Therefore
this certified finite-gap exclusion is not a proof of IDF. A universal
no-acceptance theorem for all ratios2^u/5^v would be much stronger and
would settle the endpoint finiteness question, but no such theorem is
claimed here.
