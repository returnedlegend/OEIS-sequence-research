# Reed conjecture research log

All timestamps below are UTC. A gap is reported only after exact clique and
chromatic numbers have been established. No counterexample has been found.

## Initial environment and strategy

- Repository initially contained only a README; local HEAD matched remote main.
- Five CPU cores are available. No NVIDIA device, driver, or CUDA runtime is
  exposed. This instance uses CPU PyTorch; CUDA execution remains untested.
- Search structured seed families and degree-preserving double-edge swaps.
  Swaps control maximum degree but do not guarantee preservation of clique
  number or an increase in chromatic number; recompute both before accepting.
- Screen using a coloring upper bound and a clique lower bound. This gives an
  optimistic upper bound on the true gap, never a proof of a violation.
- CP-SAT proves clique and chromatic optimality; timeouts remain unknown.
  A separate standard-library verifier must agree before any counterexample
  is reported. Known tight graphs are regression controls, not discoveries.

- 2026-11-15T17:39:13Z | Pre-publication smoke run (15 seconds, max n=24,
  seed=20261115, CPU) | 2,842 generated; 2,628 unique screened; 2,534 exact;
  1 unknown; 175.20 unique graphs/s. Best exact gap 0; no counterexample.
  All 91 saved parameter representatives agreed with the independent verifier.
  Smoke artifacts are in /tmp/oeis-smoke; the summary is retained here.
- Initial validation: 33 tests passed, including brute-force reference checks,
  exact known families, timeouts and tensor swap invariants. CUDA untested.

- 2026-11-15T17:40:11+00:00 | 20261115T174010-seed20261115 | seed evaluation | device=cpu | generated=83, unique screened=83, exact=73, unknown=0 | 148.38 unique graphs/s | best exact gap=0.

- 2026-11-15T17:41:10+00:00 | 20261115T174010-seed20261115 | progress | device=cpu | generated=6553, unique screened=6134, exact=5860, unknown=0 | 102.23 unique graphs/s | best exact gap=0.

- 2026-11-15T17:42:10+00:00 | 20261115T174010-seed20261115 | progress | device=cpu | generated=13797, unique screened=12867, exact=12272, unknown=0 | 107.22 unique graphs/s | best exact gap=0.

- 2026-11-15T17:43:10+00:00 | 20261115T174010-seed20261115 | progress | device=cpu | generated=21106, unique screened=19670, exact=18754, unknown=0 | 109.27 unique graphs/s | best exact gap=0.

- 2026-11-15T17:43:04Z | Reliability update | 64 tests passed. Added independent
  verifier and controller regressions; isolated output-directory locks; finite
  budget validation; safe commit-failure unstaging; rotated event logs for future
  runs. Repeated pinned installation succeeded; pip check reports no conflicts.
  Saved reusable install_script and start_skill in the environment draft;
  publication remains a user action in environment settings.

- 2026-11-15T17:44:10+00:00 | 20261115T174010-seed20261115 | progress | device=cpu | generated=28497, unique screened=26500, exact=25236, unknown=0 | 110.41 unique graphs/s | best exact gap=0.

- 2026-11-15T17:45:10+00:00 | 20261115T174010-seed20261115 | progress | device=cpu | generated=35369, unique screened=32852, exact=31309, unknown=0 | 109.50 unique graphs/s | best exact gap=0.

- 2026-11-15T17:46:10+00:00 | 20261115T174010-seed20261115 | progress | device=cpu | generated=42915, unique screened=39831, exact=37955, unknown=0 | 110.63 unique graphs/s | best exact gap=0.

- 2026-11-15T17:45:51Z | Triangle-free mutation experiment | Baseline swaps
  often destroy the requested graph class. Added optional --triangle-free mode,
  with exact common-neighbor rejection of each proposed added edge. This
  preserves all vertex degrees and forbids new triangles; it does not guarantee
  increased chromatic number. Every accepted research candidate still goes
  through exact CP-SAT verification.
- Fixed-seed benchmark, 256 children / 8 attempts: Chvatal retained triangle-free
  children 10 -> 256 and unique labeled triangle-free children 8 -> 36;
  Mycielski(C5) retained 18 -> 256 and unique children 11 -> 45.
  Full measured outputs: runs/mutation-benchmark.json; reproduce with
  `python scripts/benchmark_mutations.py`. These are mutation microbenchmarks,
  not end-to-end search rates or evidence of better Reed gaps.
- Validation after adding the focused mode: 73 passed, 1 skipped. The skip is
  the CUDA hardware test. A 120-second focused pilot runs alongside the original
  600-second baseline in a separate output directory, so timings are under
  concurrent CPU load.

- 2026-11-15T17:47:10+00:00 | 20261115T174010-seed20261115 | progress | device=cpu | generated=50324, unique screened=46676, exact=44475, unknown=0 | 111.12 unique graphs/s | best exact gap=0.

- 2026-11-15T17:47:41+00:00 | 20261115T174010-seed20261115 | scheduled sync | device=cpu | generated=54026, unique screened=50083, exact=47731, unknown=0 | 111.14 unique graphs/s | best exact gap=0.

- 2026-11-15T17:48:10+00:00 | 20261115T174010-seed20261115 | progress | device=cpu | generated=57204, unique screened=53016, exact=50541, unknown=0 | 110.44 unique graphs/s | best exact gap=0.

- 2026-11-15T17:47:24Z | Focused pilot complete | 120 seconds, n<=40,
  seed=20261115, CPU triangle-free swaps. 8,778 generated; 7,473 distinct labeled
  graphs screened; 7,451 exact; 1 unknown at deadline; 62.27 screened graphs/s.
  Best gap 0, no counterexample. All 50 saved parameter representatives agreed
  independently. Full pilot logs and candidates are archived under
  runs/20261115T174524-seed20261115/; implementation corresponds to fc6b183.
  Initial smoke artifacts are also retained under their timestamped run folder.
- 2026-11-15T17:47:41Z | Automatic threshold sync succeeded at 50,083 uniquely
  screened baseline graphs (50,000 since the seed checkpoint); 47,731 exact,
  best gap 0. Future runs record source SHA-256 hashes as well as the Git HEAD
  so local code changes are visible in provenance.

- 2026-11-15T17:49:10+00:00 | 20261115T174010-seed20261115 | progress | device=cpu | generated=64812, unique screened=60036, exact=57245, unknown=0 | 111.16 unique graphs/s | best exact gap=0.

- 2026-11-15T17:50:10+00:00 | 20261115T174010-seed20261115 | runtime limit | device=cpu | generated=72454, unique screened=67086, exact=63938, unknown=1 | 111.81 unique graphs/s | best exact gap=0.

- 2026-11-15T17:50:10Z | Baseline finished | 600 seconds; 72,454 generated;
  67,086 uniquely screened; 63,938 exact; 1 unknown at deadline; 111.81 screened
  graphs/s. Best exact gap 0; no counterexample. All 136 saved parameter
  representatives agreed with independent verification. Final auto-push
  succeeded. JSONL counts for all three completed runs match their summaries;
  both standalone CLIs independently reverified the saved Chvatal control.
- Next bounded experiment: one hour, seed=20261116, maximum 50 vertices,
  triangle-free mutation, CPU, 3-second exact-solver budget, automatic sync.
  No persistent execution is assumed after this cloud machine stops.

- 2026-11-15T17:51:20+00:00 | 20261115T175120-seed20261116 | seed evaluation | device=cpu | generated=63, unique screened=63, exact=53, unknown=0 | 127.67 unique graphs/s | best exact gap=0.
