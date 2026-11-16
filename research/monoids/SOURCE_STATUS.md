# Source and novelty status — 2026-11-16

The requested live source is
https://artofproblemsolving.com/polymath/mitprimes2026/f .

## Access and evidence

The enforced network policy currently permits package-manager and GitHub
hosts but not AoPS or research-index hosts. Requests to AoPS and Crossref
failed with proxy tunnel HTTP 403. A draft adding research hosts was saved,
but the active runtime still reports revision 1 with no custom allowed
hosts. No live-page or current-literature verification has been completed.
The runtime configuration and AoPS request were checked again at about
00:25 UTC on November 16: revision 1 remained active, and the request
again failed with proxy tunnel HTTP 403.
The direct AoPS request was retried at 01:22 UTC on November 16 and still
failed with proxy tunnel HTTP 403. No later live progress was verified.

The work used discussion excerpts uploaded or pasted by the user. During
this session the user supplied a much more detailed progress excerpt,
including posts dated October 16–November 9, 2026. The following account is
based on that excerpt, not on independently retrieved live pages or PDFs.
The attachments Notes 1.5.pdf and Hyunjun_Yi_Open_Problem_2.pdf were named
but their contents were not provided in that message.

## Reported progress and attribution

- ppdppd, October 16: exact digits {0,1,7/5} for (3/10,7/5), a terminating
  membership procedure, and sharp conductor 2.
- Mardcelo, October 20: complementary digit family q=a/b,
  r=(a-1)(1-q), b>=a^2-1; a proposed IDF/non-atomic theorem under the condition
  p^(v_p(b))>=a at all denominator primes. This already uses the same kind
  of denominator-block bound appearing in our cyclic argument.
- ppdppd, October 24: non-atomicity for (3/10,7/5), with exactly the powers
  of 2 among positive integers admitting atomic factorizations. IDF remains
  unresolved. The post also corrects the scope of an earlier assertion at
  b=8; we do not treat the entire quoted general classification as verified.
- Hyunjun Yi (hjyi09), November 2 write-up, discussed November 9: analysis
  of (6/35,19/3) using N_0[6/35,38/35], conductors 175/29 and 105/29,
  finite digit/graph computations, and valuation arguments. The supplied
  discussion records corrections to a count and depth inequalities. We
  have not read the complete revised PDF and do not independently certify
  its detailed conclusion or computation.
- Mardcelo, draft discussed November 9: atomicity classification for finitely
  many generators 2/d with odd denominators; credits earlier work by
  BakedPotatoz on (2/5,2/3). Also reports a quadratic-character proof of
  non-atomicity for 7/15 and a larger monogenic family.
- The November 9 summary explicitly says IDF for (2/5,2/3) and (3/10,7/5),
  and atomicity for 5/6, remain unresolved in that draft.

The supplied Open Problem 2 uses effective denominator primes: p is
 effective when some q^i r^j<1 has negative p-adic valuation. In the mixed
case it assumes multiplicative independence, at least two effective primes,
and a numerator prime of q that is not effective. ACCP failure for this
family was already established in the discussion. The monogenic part asks
whether any reduced a/b in (0,1), with a>1 and at least two denominator
primes, gives an atomic multiplicative monoid.

## What we may and may not claim

Atomic plus IDF implies finitely many divisor classes and therefore ACCP.
Thus failure of ACCP implies failure of at least one of those properties;
it does not determine which one fails. Our conditional statements of the
form 'atomic implies non-IDF' overlap the established ACCP results.

Our direct non-atomicity proofs for (3/10,7/5) and (2/5,2/3) recover
reported results; they must not be presented as new solutions. The canonical
and conductor tools overlap credited discussion contributions.

The remaining theorems in this directory have self-contained proofs, but
their novelty relative to the complete discussion, attached drafts, or
literature is unverified. The general reciprocal transfer theorem, Boolean
mixed families, critical divisor certificates, and contracting Mobius
factorization algorithms are not explicitly stated in the supplied excerpt;
that is not enough to establish novelty. None of these notes completes the original rational-
pair classification. No atomic, non-IDF example in the requested two-generator
semiring family has been proved here.
