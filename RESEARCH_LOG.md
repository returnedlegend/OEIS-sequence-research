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

- 2026-11-15T18:01:20+00:00 | 20261115T175120-seed20261116 | progress | device=cpu | generated=43314, unique screened=36235, exact=36195, unknown=0 | 60.39 unique graphs/s | best exact gap=0.

- 2026-11-15T18:05:16+00:00 | 20261115T175120-seed20261116 | scheduled sync | device=cpu | generated=59800, unique screened=50063, exact=50014, unknown=0 | 59.89 unique graphs/s | best exact gap=0.

- 2026-11-15T18:11:20+00:00 | 20261115T175120-seed20261116 | progress | device=cpu | generated=84877, unique screened=71050, exact=70991, unknown=0 | 59.21 unique graphs/s | best exact gap=0.

- 2026-11-15T18:19:40+00:00 | 20261115T175120-seed20261116 | scheduled sync | device=cpu | generated=119653, unique screened=100063, exact=99994, unknown=0 | 58.87 unique graphs/s | best exact gap=0.

- 2026-11-15T18:21:20+00:00 | 20261115T175120-seed20261116 | progress | device=cpu | generated=126412, unique screened=105696, exact=105625, unknown=0 | 58.72 unique graphs/s | best exact gap=0.

- 2026-11-15T18:31:20+00:00 | 20261115T175120-seed20261116 | progress | device=cpu | generated=168484, unique screened=140652, exact=140569, unknown=0 | 58.60 unique graphs/s | best exact gap=0.

- 2026-11-15T18:34:04+00:00 | 20261115T175120-seed20261116 | scheduled sync | device=cpu | generated=179828, unique screened=150063, exact=149973, unknown=0 | 58.52 unique graphs/s | best exact gap=0.

- 2026-11-15T18:44:03Z | Local Windows CUDA setup verified | Python 3.13.17
  in .venv; locked dependencies; PyTorch 2.14.1+cu126 with CUDA 12.6 on NVIDIA
  GeForce RTX 2070 with Max-Q Design (8 GB, sm_75; driver 610.91). A real 32x32
  float32 CUDA matrix product agrees with the CPU reference (checksum
  8575959040). The portable installer completed end to end: pip check clean,
  75 tests passed, none skipped, including CUDA triangle-free swaps. Replaced
  Linux-only fcntl locking with filelock and added cross-process CLI exclusion
  and release coverage. Test deadlines no longer depend on Git startup speed.
  Evidence: runs/windows-cuda-setup-20261115/validation.json. Continue with a new
  one-hour triangle-free search, seed=20261117, n<=50, --device cuda --sync;
  prior run artifacts are retained. No counterexample has been found.

- 2026-11-15T18:45:26+00:00 | 20261115T184525-seed20261117 | seed evaluation | device=cuda | generated=63, unique screened=63, exact=53, unknown=0 | 72.93 unique graphs/s | best exact gap=0.

- 2026-11-15T18:46:25+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=2192, unique screened=1784, exact=1773, unknown=0 | 29.73 unique graphs/s | best exact gap=0.

- 2026-11-15T18:47:25+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=4520, unique screened=3748, exact=3735, unknown=0 | 31.23 unique graphs/s | best exact gap=0.

- 2026-11-15T18:48:26+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=6784, unique screened=5629, exact=5616, unknown=0 | 31.20 unique graphs/s | best exact gap=0.

- 2026-11-15T18:49:26+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=9067, unique screened=7520, exact=7506, unknown=0 | 31.27 unique graphs/s | best exact gap=0.

- 2026-11-15T18:50:26+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=11088, unique screened=9220, exact=9204, unknown=0 | 30.68 unique graphs/s | best exact gap=0.

- 2026-11-15T18:51:26+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=13104, unique screened=10911, exact=10893, unknown=0 | 30.27 unique graphs/s | best exact gap=0.

- 2026-11-15T18:52:26+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=15263, unique screened=12713, exact=12693, unknown=0 | 30.23 unique graphs/s | best exact gap=0.

- 2026-11-15T18:53:26+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=17342, unique screened=14451, exact=14430, unknown=0 | 30.07 unique graphs/s | best exact gap=0.

- 2026-11-15T18:54:26+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=19600, unique screened=16328, exact=16305, unknown=0 | 30.21 unique graphs/s | best exact gap=0.

- 2026-11-15T18:55:26+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=21952, unique screened=18282, exact=18258, unknown=0 | 30.44 unique graphs/s | best exact gap=0.

- 2026-11-15T18:56:26+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=23881, unique screened=19892, exact=19868, unknown=0 | 30.11 unique graphs/s | best exact gap=0.

- 2026-11-15T18:57:26+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=25812, unique screened=21510, exact=21485, unknown=0 | 29.85 unique graphs/s | best exact gap=0.

- 2026-11-15T18:58:26+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=27585, unique screened=23008, exact=22983, unknown=0 | 29.47 unique graphs/s | best exact gap=0.

- 2026-11-15T18:59:26+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=29372, unique screened=24505, exact=24480, unknown=0 | 29.15 unique graphs/s | best exact gap=0.

- 2026-11-15T19:00:26+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=31303, unique screened=26123, exact=26097, unknown=0 | 29.00 unique graphs/s | best exact gap=0.

- 2026-11-15T19:00:29+00:00 | 20261115T184525-seed20261117 | scheduled sync | device=cuda | generated=31419, unique screened=26215, exact=26189, unknown=0 | 29.01 unique graphs/s | best exact gap=0.

- 2026-11-15T19:01:26+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=33156, unique screened=27697, exact=27671, unknown=0 | 28.83 unique graphs/s | best exact gap=0.

- 2026-11-15T19:02:26+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=35212, unique screened=29394, exact=29368, unknown=0 | 28.80 unique graphs/s | best exact gap=0.

- 2026-11-15T19:03:26+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=37275, unique screened=31140, exact=31114, unknown=0 | 28.81 unique graphs/s | best exact gap=0.

- 2026-11-15T19:04:26+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=39296, unique screened=32824, exact=32798, unknown=0 | 28.77 unique graphs/s | best exact gap=0.

- 2026-11-15T19:05:27+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=41344, unique screened=34554, exact=34527, unknown=0 | 28.76 unique graphs/s | best exact gap=0.

- 2026-11-15T19:06:27+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=43397, unique screened=36259, exact=36231, unknown=0 | 28.75 unique graphs/s | best exact gap=0.

- 2026-11-15T19:07:27+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=45241, unique screened=37813, exact=37785, unknown=0 | 28.62 unique graphs/s | best exact gap=0.

- 2026-11-15T19:08:27+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=47064, unique screened=39342, exact=39313, unknown=0 | 28.48 unique graphs/s | best exact gap=0.

- 2026-11-15T19:09:27+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=48985, unique screened=40909, exact=40880, unknown=0 | 28.38 unique graphs/s | best exact gap=0.

- 2026-11-15T19:10:27+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=50816, unique screened=42480, exact=42451, unknown=0 | 28.29 unique graphs/s | best exact gap=0.

- 2026-11-15T19:11:27+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=52800, unique screened=44128, exact=44097, unknown=0 | 28.26 unique graphs/s | best exact gap=0.

- 2026-11-15T19:12:27+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=54737, unique screened=45735, exact=45703, unknown=0 | 28.20 unique graphs/s | best exact gap=0.

- 2026-11-15T19:13:27+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=56960, unique screened=47563, exact=47528, unknown=0 | 28.28 unique graphs/s | best exact gap=0.

- 2026-11-15T19:14:27+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=59354, unique screened=49551, exact=49515, unknown=0 | 28.45 unique graphs/s | best exact gap=0.

- 2026-11-15T19:15:27+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=61312, unique screened=51169, exact=51131, unknown=0 | 28.39 unique graphs/s | best exact gap=0.

- 2026-11-15T19:15:33+00:00 | 20261115T184525-seed20261117 | scheduled sync | device=cuda | generated=61492, unique screened=51315, exact=51277, unknown=0 | 28.39 unique graphs/s | best exact gap=0.

- 2026-11-15T19:16:28+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=62848, unique screened=52447, exact=52409, unknown=0 | 28.16 unique graphs/s | best exact gap=0.

- 2026-11-15T19:17:28+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=64384, unique screened=53736, exact=53696, unknown=0 | 27.95 unique graphs/s | best exact gap=0.

- 2026-11-15T19:18:28+00:00 | 20261115T184525-seed20261117 | progress | device=cuda | generated=66100, unique screened=55154, exact=55113, unknown=0 | 27.82 unique graphs/s | best exact gap=0.

- 2026-11-15T19:19:38+00:00 | CUDA baseline interrupted for GPU pipeline upgrade. Windows console stop ended the process before its final checkpoint; retained 55804 complete verification records. The last periodic summary remains labeled as progress. No positive exact gap. See runs/20261115T184525-seed20261117/interruption.json. Future runs use a portable stop file.

- 2026-11-15T19:29:08+00:00 | GPU pipeline deployed | Resident batches of 8192; four DSATUR coloring trials and edgewise certificate checks on CUDA; four parallel CPU exact workers. Every unresolved positive upper bound is checked or retained pending. Up to 8 safe tight/near candidates sampled per batch. 45-second benchmark: 4,898,816 GPU-screened instances (possibly repeated), 3,898 distinct exact verifications versus 1,144 baseline; GPU mean 51.24%, peak 77%. No counterexample; best exact gap 0. Full suite: 110 passed, no skips. Every 50,000 generated instances checkpoints locally; network-only background pushes overlap GPU work. Benchmark and validation: runs/gpu-pipeline-benchmark-20261115/. Starting one-hour CUDA run seed20261119, n<=50, --gpu-pipeline --sync with portable stop file.

- 2026-11-15T19:29:38+00:00 | 20261115T192936-gpu-seed20261119 | seed evaluation | device=cuda, GPU pipeline | generated draws=63, GPU certified nonviolations=0, unique transferred candidates=53, exact=53, unknown=0, pending=0 | 0.00 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:29:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=57407, GPU certified nonviolations=57344, unique transferred candidates=80, exact=73, unknown=0, pending=0 | 21592.66 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:29:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=114751, GPU certified nonviolations=114688, unique transferred candidates=128, exact=119, unknown=0, pending=0 | 33632.98 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:29:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=172095, GPU certified nonviolations=172032, unique transferred candidates=168, exact=156, unknown=0, pending=0 | 40822.14 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:29:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=229439, GPU certified nonviolations=229376, unique transferred candidates=201, exact=185, unknown=0, pending=0 | 43080.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:29:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=286783, GPU certified nonviolations=286720, unique transferred candidates=245, exact=238, unknown=0, pending=0 | 47640.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:29:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=344127, GPU certified nonviolations=344064, unique transferred candidates=293, exact=281, unknown=0, pending=0 | 51152.26 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:29:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=401471, GPU certified nonviolations=401408, unique transferred candidates=333, exact=318, unknown=0, pending=0 | 51909.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:29:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=458815, GPU certified nonviolations=458752, unique transferred candidates=370, exact=366, unknown=0, pending=0 | 53640.74 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:29:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=516159, GPU certified nonviolations=516096, unique transferred candidates=424, exact=412, unknown=0, pending=0 | 55818.76 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:29:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=573503, GPU certified nonviolations=573440, unique transferred candidates=464, exact=452, unknown=0, pending=0 | 57576.26 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:29:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=630847, GPU certified nonviolations=630784, unique transferred candidates=503, exact=488, unknown=0, pending=0 | 57797.71 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:29:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=688191, GPU certified nonviolations=688128, unique transferred candidates=548, exact=540, unknown=0, pending=0 | 59589.22 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:29:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=745535, GPU certified nonviolations=745472, unique transferred candidates=596, exact=587, unknown=0, pending=0 | 60563.93 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:29:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=802879, GPU certified nonviolations=802816, unique transferred candidates=643, exact=627, unknown=0, pending=0 | 60492.71 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:29:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=860223, GPU certified nonviolations=860160, unique transferred candidates=677, exact=672, unknown=0, pending=0 | 59898.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:29:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=917567, GPU certified nonviolations=917504, unique transferred candidates=727, exact=716, unknown=0, pending=0 | 61503.57 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:29:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=974911, GPU certified nonviolations=974848, unique transferred candidates=767, exact=755, unknown=0, pending=0 | 62170.61 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:29:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=1032255, GPU certified nonviolations=1032192, unique transferred candidates=807, exact=799, unknown=0, pending=0 | 61797.66 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:29:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=1089599, GPU certified nonviolations=1089536, unique transferred candidates=860, exact=852, unknown=0, pending=0 | 62746.44 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:29:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=1146943, GPU certified nonviolations=1146880, unique transferred candidates=908, exact=895, unknown=0, pending=0 | 63214.75 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:29:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=1204287, GPU certified nonviolations=1204224, unique transferred candidates=954, exact=938, unknown=0, pending=0 | 63146.66 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:29:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=1261631, GPU certified nonviolations=1261568, unique transferred candidates=993, exact=988, unknown=0, pending=0 | 62708.24 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:29:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=1318975, GPU certified nonviolations=1318912, unique transferred candidates=1044, exact=1033, unknown=0, pending=0 | 63496.95 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:29:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=1376319, GPU certified nonviolations=1376256, unique transferred candidates=1084, exact=1071, unknown=0, pending=0 | 63533.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:29:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=1433663, GPU certified nonviolations=1433600, unique transferred candidates=1132, exact=1120, unknown=0, pending=0 | 62853.53 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:29:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=1491007, GPU certified nonviolations=1490944, unique transferred candidates=1172, exact=1168, unknown=0, pending=0 | 63812.14 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=1548351, GPU certified nonviolations=1548288, unique transferred candidates=1228, exact=1216, unknown=0, pending=0 | 64337.66 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=1605695, GPU certified nonviolations=1605632, unique transferred candidates=1268, exact=1256, unknown=0, pending=0 | 64554.16 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=1663039, GPU certified nonviolations=1662976, unique transferred candidates=1301, exact=1285, unknown=0, pending=0 | 64353.61 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=1720383, GPU certified nonviolations=1720319, unique transferred candidates=1359, exact=1350, unknown=0, pending=0 | 65139.55 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=1777727, GPU certified nonviolations=1777663, unique transferred candidates=1407, exact=1394, unknown=0, pending=0 | 65579.24 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=1835071, GPU certified nonviolations=1835007, unique transferred candidates=1447, exact=1431, unknown=0, pending=0 | 64882.52 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=1892415, GPU certified nonviolations=1892351, unique transferred candidates=1491, exact=1483, unknown=0, pending=0 | 64256.03 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=1949759, GPU certified nonviolations=1949695, unique transferred candidates=1547, exact=1533, unknown=0, pending=0 | 64272.76 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=2007103, GPU certified nonviolations=2007039, unique transferred candidates=1587, exact=1575, unknown=0, pending=0 | 64167.66 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=2064447, GPU certified nonviolations=2064383, unique transferred candidates=1627, exact=1611, unknown=0, pending=0 | 64010.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=2121791, GPU certified nonviolations=2121727, unique transferred candidates=1678, exact=1670, unknown=0, pending=0 | 64258.16 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=2179135, GPU certified nonviolations=2179071, unique transferred candidates=1726, exact=1718, unknown=0, pending=0 | 64618.76 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=2236479, GPU certified nonviolations=2236415, unique transferred candidates=1771, exact=1755, unknown=0, pending=0 | 64596.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=2293823, GPU certified nonviolations=2293759, unique transferred candidates=1814, exact=1806, unknown=0, pending=0 | 64486.62 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=2351167, GPU certified nonviolations=2351103, unique transferred candidates=1867, exact=1856, unknown=0, pending=0 | 64880.05 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=2408511, GPU certified nonviolations=2408447, unique transferred candidates=1907, exact=1898, unknown=0, pending=0 | 65023.62 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=2465855, GPU certified nonviolations=2465791, unique transferred candidates=1947, exact=1931, unknown=0, pending=0 | 64409.70 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=2523199, GPU certified nonviolations=2523135, unique transferred candidates=1999, exact=1991, unknown=0, pending=0 | 64496.98 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=2580543, GPU certified nonviolations=2580479, unique transferred candidates=2047, exact=2034, unknown=0, pending=0 | 64671.02 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=2637887, GPU certified nonviolations=2637823, unique transferred candidates=2095, exact=2080, unknown=0, pending=0 | 64514.78 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=2695231, GPU certified nonviolations=2695167, unique transferred candidates=2135, exact=2126, unknown=0, pending=0 | 64057.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=2752575, GPU certified nonviolations=2752511, unique transferred candidates=2190, exact=2181, unknown=0, pending=0 | 64211.66 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=2809919, GPU certified nonviolations=2809855, unique transferred candidates=2230, exact=2218, unknown=0, pending=0 | 64246.44 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=2867263, GPU certified nonviolations=2867199, unique transferred candidates=2278, exact=2269, unknown=0, pending=0 | 63530.48 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=2924607, GPU certified nonviolations=2924543, unique transferred candidates=2322, exact=2316, unknown=0, pending=0 | 63613.39 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=2981951, GPU certified nonviolations=2981887, unique transferred candidates=2378, exact=2366, unknown=0, pending=0 | 63776.72 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=3039295, GPU certified nonviolations=3039231, unique transferred candidates=2418, exact=2402, unknown=0, pending=0 | 63762.77 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=3096639, GPU certified nonviolations=3096575, unique transferred candidates=2451, exact=2435, unknown=0, pending=0 | 63508.98 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=3153983, GPU certified nonviolations=3153919, unique transferred candidates=2510, exact=2500, unknown=0, pending=0 | 63781.02 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=3211327, GPU certified nonviolations=3211263, unique transferred candidates=2558, exact=2545, unknown=0, pending=0 | 63940.45 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=3268671, GPU certified nonviolations=3268607, unique transferred candidates=2598, exact=2582, unknown=0, pending=0 | 63546.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=3326015, GPU certified nonviolations=3325951, unique transferred candidates=2643, exact=2635, unknown=0, pending=0 | 63300.55 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=3383359, GPU certified nonviolations=3383295, unique transferred candidates=2699, exact=2689, unknown=0, pending=0 | 63603.49 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=3440703, GPU certified nonviolations=3440639, unique transferred candidates=2739, exact=2725, unknown=0, pending=0 | 63599.08 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=3498047, GPU certified nonviolations=3497983, unique transferred candidates=2779, exact=2763, unknown=0, pending=0 | 63354.33 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=3555391, GPU certified nonviolations=3555327, unique transferred candidates=2829, exact=2820, unknown=0, pending=0 | 63282.26 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=3612735, GPU certified nonviolations=3612671, unique transferred candidates=2877, exact=2869, unknown=0, pending=0 | 63355.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=3670079, GPU certified nonviolations=3670015, unique transferred candidates=2922, exact=2906, unknown=0, pending=0 | 63233.40 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=3727423, GPU certified nonviolations=3727359, unique transferred candidates=2962, exact=2954, unknown=0, pending=0 | 62802.64 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:36+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=3760191, GPU certified nonviolations=3760127, unique transferred candidates=2992, exact=2984, unknown=0, pending=0 | 62667.34 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=3784767, GPU certified nonviolations=3784703, unique transferred candidates=3016, exact=3006, unknown=0, pending=0 | 62890.08 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=3842111, GPU certified nonviolations=3842047, unique transferred candidates=3056, exact=3044, unknown=0, pending=0 | 62871.93 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=3899455, GPU certified nonviolations=3899391, unique transferred candidates=3096, exact=3088, unknown=0, pending=0 | 62722.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=3956799, GPU certified nonviolations=3956735, unique transferred candidates=3149, exact=3141, unknown=0, pending=0 | 62797.76 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=4014143, GPU certified nonviolations=4014079, unique transferred candidates=3197, exact=3185, unknown=0, pending=0 | 62875.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=4071487, GPU certified nonviolations=4071423, unique transferred candidates=3245, exact=3229, unknown=0, pending=0 | 62888.28 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=4128831, GPU certified nonviolations=4128767, unique transferred candidates=3285, exact=3276, unknown=0, pending=0 | 62638.35 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=4186175, GPU certified nonviolations=4186111, unique transferred candidates=3339, exact=3330, unknown=0, pending=0 | 62741.99 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=4243519, GPU certified nonviolations=4243455, unique transferred candidates=3379, exact=3367, unknown=0, pending=0 | 62758.76 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=4300863, GPU certified nonviolations=4300799, unique transferred candidates=3427, exact=3411, unknown=0, pending=0 | 62407.97 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=4358207, GPU certified nonviolations=4358143, unique transferred candidates=3469, exact=3464, unknown=0, pending=0 | 62443.36 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=4415551, GPU certified nonviolations=4415487, unique transferred candidates=3525, exact=3513, unknown=0, pending=0 | 62333.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=4472895, GPU certified nonviolations=4472831, unique transferred candidates=3563, exact=3547, unknown=0, pending=0 | 62243.78 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=4530239, GPU certified nonviolations=4530175, unique transferred candidates=3598, exact=3582, unknown=0, pending=0 | 62014.64 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=4587583, GPU certified nonviolations=4587519, unique transferred candidates=3657, exact=3649, unknown=0, pending=0 | 61917.85 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=4644927, GPU certified nonviolations=4644863, unique transferred candidates=3705, exact=3693, unknown=0, pending=0 | 61831.76 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=4702271, GPU certified nonviolations=4702207, unique transferred candidates=3745, exact=3729, unknown=0, pending=0 | 61352.55 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=4759615, GPU certified nonviolations=4759550, unique transferred candidates=3792, exact=3784, unknown=0, pending=0 | 61295.97 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=4816959, GPU certified nonviolations=4816894, unique transferred candidates=3847, exact=3835, unknown=0, pending=0 | 61443.65 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=4874303, GPU certified nonviolations=4874238, unique transferred candidates=3887, exact=3873, unknown=0, pending=0 | 61416.39 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=4931647, GPU certified nonviolations=4931582, unique transferred candidates=3927, exact=3911, unknown=0, pending=0 | 61220.45 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=4988991, GPU certified nonviolations=4988926, unique transferred candidates=3977, exact=3969, unknown=0, pending=0 | 61286.97 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=5046335, GPU certified nonviolations=5046270, unique transferred candidates=4025, exact=4017, unknown=0, pending=0 | 61333.86 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:30:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=5103679, GPU certified nonviolations=5103614, unique transferred candidates=4073, exact=4058, unknown=0, pending=0 | 61211.99 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=5161023, GPU certified nonviolations=5160958, unique transferred candidates=4111, exact=4103, unknown=0, pending=0 | 61015.04 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=5218367, GPU certified nonviolations=5218302, unique transferred candidates=4165, exact=4154, unknown=0, pending=0 | 61075.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=5275711, GPU certified nonviolations=5275646, unique transferred candidates=4205, exact=4195, unknown=0, pending=0 | 61026.42 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=5333055, GPU certified nonviolations=5332990, unique transferred candidates=4245, exact=4236, unknown=0, pending=0 | 60862.40 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=5390399, GPU certified nonviolations=5390334, unique transferred candidates=4299, exact=4291, unknown=0, pending=0 | 60904.62 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=5447743, GPU certified nonviolations=5447678, unique transferred candidates=4347, exact=4334, unknown=0, pending=0 | 60929.91 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=5505087, GPU certified nonviolations=5505022, unique transferred candidates=4395, exact=4379, unknown=0, pending=0 | 60887.00 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=5562431, GPU certified nonviolations=5562366, unique transferred candidates=4435, exact=4427, unknown=0, pending=0 | 60570.06 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=5619775, GPU certified nonviolations=5619710, unique transferred candidates=4491, exact=4481, unknown=0, pending=0 | 60696.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=5677119, GPU certified nonviolations=5677054, unique transferred candidates=4531, exact=4518, unknown=0, pending=0 | 60708.40 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=5734463, GPU certified nonviolations=5734398, unique transferred candidates=4579, exact=4569, unknown=0, pending=0 | 60564.03 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=5791807, GPU certified nonviolations=5791742, unique transferred candidates=4626, exact=4618, unknown=0, pending=0 | 60581.77 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=5849151, GPU certified nonviolations=5849086, unique transferred candidates=4682, exact=4670, unknown=0, pending=0 | 60698.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=5906495, GPU certified nonviolations=5906430, unique transferred candidates=4722, exact=4706, unknown=0, pending=0 | 60655.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=5963839, GPU certified nonviolations=5963774, unique transferred candidates=4755, exact=4739, unknown=0, pending=0 | 60544.99 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=6021183, GPU certified nonviolations=6021118, unique transferred candidates=4815, exact=4807, unknown=0, pending=0 | 60567.17 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=6078527, GPU certified nonviolations=6078462, unique transferred candidates=4863, exact=4850, unknown=0, pending=0 | 60515.85 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=6135871, GPU certified nonviolations=6135806, unique transferred candidates=4903, exact=4887, unknown=0, pending=0 | 60134.13 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=6193215, GPU certified nonviolations=6193150, unique transferred candidates=4948, exact=4940, unknown=0, pending=0 | 59559.35 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=6250559, GPU certified nonviolations=6250494, unique transferred candidates=5001, exact=4990, unknown=0, pending=0 | 59560.33 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=6307903, GPU certified nonviolations=6307838, unique transferred candidates=5041, exact=5027, unknown=0, pending=0 | 59567.23 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=6365247, GPU certified nonviolations=6365182, unique transferred candidates=5081, exact=5065, unknown=0, pending=0 | 59406.76 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=6422591, GPU certified nonviolations=6422526, unique transferred candidates=5134, exact=5126, unknown=0, pending=0 | 59421.94 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=6479935, GPU certified nonviolations=6479870, unique transferred candidates=5182, exact=5174, unknown=0, pending=0 | 59509.52 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=6537279, GPU certified nonviolations=6537214, unique transferred candidates=5229, exact=5213, unknown=0, pending=0 | 59523.02 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=6594623, GPU certified nonviolations=6594558, unique transferred candidates=5268, exact=5260, unknown=0, pending=0 | 59426.91 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=6651967, GPU certified nonviolations=6651902, unique transferred candidates=5323, exact=5313, unknown=0, pending=0 | 59457.73 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=6709311, GPU certified nonviolations=6709246, unique transferred candidates=5363, exact=5353, unknown=0, pending=0 | 59520.84 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=6766655, GPU certified nonviolations=6766590, unique transferred candidates=5403, exact=5393, unknown=0, pending=0 | 59401.56 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=6823999, GPU certified nonviolations=6823934, unique transferred candidates=5455, exact=5447, unknown=0, pending=0 | 59492.74 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=6881343, GPU certified nonviolations=6881278, unique transferred candidates=5503, exact=5491, unknown=0, pending=0 | 59567.37 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=6938687, GPU certified nonviolations=6938622, unique transferred candidates=5551, exact=5535, unknown=0, pending=0 | 59617.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=6996031, GPU certified nonviolations=6995966, unique transferred candidates=5588, exact=5580, unknown=0, pending=0 | 59453.71 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=7053375, GPU certified nonviolations=7053310, unique transferred candidates=5643, exact=5634, unknown=0, pending=0 | 59550.44 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=7110719, GPU certified nonviolations=7110654, unique transferred candidates=5683, exact=5671, unknown=0, pending=0 | 59594.94 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:36+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=7143487, GPU certified nonviolations=7143422, unique transferred candidates=5715, exact=5699, unknown=0, pending=0 | 59481.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=7168063, GPU certified nonviolations=7167998, unique transferred candidates=5731, exact=5722, unknown=0, pending=0 | 59467.62 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=7225407, GPU certified nonviolations=7225342, unique transferred candidates=5778, exact=5771, unknown=0, pending=0 | 59588.49 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=7282751, GPU certified nonviolations=7282686, unique transferred candidates=5834, exact=5821, unknown=0, pending=0 | 59684.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=7340095, GPU certified nonviolations=7340030, unique transferred candidates=5874, exact=5858, unknown=0, pending=0 | 59737.80 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=7397439, GPU certified nonviolations=7397374, unique transferred candidates=5907, exact=5891, unknown=0, pending=0 | 59594.83 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=7454783, GPU certified nonviolations=7454718, unique transferred candidates=5968, exact=5960, unknown=0, pending=0 | 59582.59 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=7512127, GPU certified nonviolations=7512062, unique transferred candidates=6016, exact=6004, unknown=0, pending=0 | 59594.86 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=7569471, GPU certified nonviolations=7569406, unique transferred candidates=6056, exact=6040, unknown=0, pending=0 | 59481.35 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=7626815, GPU certified nonviolations=7626750, unique transferred candidates=6104, exact=6096, unknown=0, pending=0 | 59436.13 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=7684159, GPU certified nonviolations=7684094, unique transferred candidates=6159, exact=6150, unknown=0, pending=0 | 59561.35 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=7741503, GPU certified nonviolations=7741438, unique transferred candidates=6199, exact=6186, unknown=0, pending=0 | 59605.97 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=7798847, GPU certified nonviolations=7798782, unique transferred candidates=6238, exact=6223, unknown=0, pending=0 | 59514.11 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=7856191, GPU certified nonviolations=7856126, unique transferred candidates=6293, exact=6285, unknown=0, pending=0 | 59575.56 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=7913535, GPU certified nonviolations=7913470, unique transferred candidates=6341, exact=6333, unknown=0, pending=0 | 59637.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=7970879, GPU certified nonviolations=7970814, unique transferred candidates=6386, exact=6370, unknown=0, pending=0 | 59459.11 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=8028223, GPU certified nonviolations=8028158, unique transferred candidates=6428, exact=6420, unknown=0, pending=0 | 59157.64 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=8085567, GPU certified nonviolations=8085502, unique transferred candidates=6483, exact=6472, unknown=0, pending=0 | 59234.10 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=8142911, GPU certified nonviolations=8142846, unique transferred candidates=6523, exact=6515, unknown=0, pending=0 | 59196.96 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=8200255, GPU certified nonviolations=8200190, unique transferred candidates=6563, exact=6549, unknown=0, pending=0 | 59087.16 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=8257599, GPU certified nonviolations=8257534, unique transferred candidates=6617, exact=6609, unknown=0, pending=0 | 59182.27 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=8314943, GPU certified nonviolations=8314878, unique transferred candidates=6665, exact=6653, unknown=0, pending=0 | 59274.77 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=8372287, GPU certified nonviolations=8372222, unique transferred candidates=6713, exact=6697, unknown=0, pending=0 | 59295.13 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=8429631, GPU certified nonviolations=8429566, unique transferred candidates=6752, exact=6744, unknown=0, pending=0 | 59096.04 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:31:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=8486975, GPU certified nonviolations=8486909, unique transferred candidates=6806, exact=6796, unknown=0, pending=0 | 59235.40 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=8544319, GPU certified nonviolations=8544253, unique transferred candidates=6846, exact=6833, unknown=0, pending=0 | 59320.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=8601663, GPU certified nonviolations=8601597, unique transferred candidates=6894, exact=6882, unknown=0, pending=0 | 59213.71 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=8659007, GPU certified nonviolations=8658941, unique transferred candidates=6942, exact=6934, unknown=0, pending=0 | 59263.10 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=8716351, GPU certified nonviolations=8716285, unique transferred candidates=6998, exact=6986, unknown=0, pending=0 | 59349.89 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=8773695, GPU certified nonviolations=8773629, unique transferred candidates=7038, exact=7028, unknown=0, pending=0 | 59309.67 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=8831039, GPU certified nonviolations=8830973, unique transferred candidates=7071, exact=7055, unknown=0, pending=0 | 59226.22 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=8888383, GPU certified nonviolations=8888317, unique transferred candidates=7132, exact=7124, unknown=0, pending=0 | 59261.70 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=8945727, GPU certified nonviolations=8945661, unique transferred candidates=7180, exact=7168, unknown=0, pending=0 | 59308.55 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=9003071, GPU certified nonviolations=9003005, unique transferred candidates=7220, exact=7204, unknown=0, pending=0 | 59238.17 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=9060415, GPU certified nonviolations=9060348, unique transferred candidates=7267, exact=7259, unknown=0, pending=0 | 59166.44 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=9117759, GPU certified nonviolations=9117692, unique transferred candidates=7323, exact=7313, unknown=0, pending=0 | 59251.89 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=9175103, GPU certified nonviolations=9175036, unique transferred candidates=7363, exact=7348, unknown=0, pending=0 | 59279.03 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=9232447, GPU certified nonviolations=9232380, unique transferred candidates=7401, exact=7387, unknown=0, pending=0 | 59167.69 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=9289791, GPU certified nonviolations=9289724, unique transferred candidates=7457, exact=7449, unknown=0, pending=0 | 59206.74 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=9347135, GPU certified nonviolations=9347068, unique transferred candidates=7505, exact=7495, unknown=0, pending=0 | 59281.04 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=9404479, GPU certified nonviolations=9404412, unique transferred candidates=7553, exact=7537, unknown=0, pending=0 | 59265.04 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=9461823, GPU certified nonviolations=9461756, unique transferred candidates=7592, exact=7584, unknown=0, pending=0 | 59117.55 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=9519167, GPU certified nonviolations=9519100, unique transferred candidates=7648, exact=7636, unknown=0, pending=0 | 59181.14 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=9576511, GPU certified nonviolations=9576444, unique transferred candidates=7688, exact=7680, unknown=0, pending=0 | 59105.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=9633855, GPU certified nonviolations=9633788, unique transferred candidates=7728, exact=7719, unknown=0, pending=0 | 58981.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=9691199, GPU certified nonviolations=9691132, unique transferred candidates=7781, exact=7773, unknown=0, pending=0 | 59028.32 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=9748543, GPU certified nonviolations=9748476, unique transferred candidates=7829, exact=7820, unknown=0, pending=0 | 59113.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=9805887, GPU certified nonviolations=9805820, unique transferred candidates=7877, exact=7861, unknown=0, pending=0 | 59103.06 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=9863231, GPU certified nonviolations=9863164, unique transferred candidates=7916, exact=7908, unknown=0, pending=0 | 58939.91 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=9920575, GPU certified nonviolations=9920508, unique transferred candidates=7971, exact=7962, unknown=0, pending=0 | 59047.64 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=9977919, GPU certified nonviolations=9977852, unique transferred candidates=8011, exact=7999, unknown=0, pending=0 | 59113.64 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=10035263, GPU certified nonviolations=10035196, unique transferred candidates=8059, exact=8051, unknown=0, pending=0 | 59000.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=10092607, GPU certified nonviolations=10092540, unique transferred candidates=8107, exact=8098, unknown=0, pending=0 | 59061.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=10149951, GPU certified nonviolations=10149884, unique transferred candidates=8163, exact=8151, unknown=0, pending=0 | 59108.12 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=10207295, GPU certified nonviolations=10207228, unique transferred candidates=8203, exact=8191, unknown=0, pending=0 | 59095.59 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=10264639, GPU certified nonviolations=10264572, unique transferred candidates=8236, exact=8220, unknown=0, pending=0 | 59026.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=10321983, GPU certified nonviolations=10321916, unique transferred candidates=8297, exact=8288, unknown=0, pending=0 | 59119.19 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=10379327, GPU certified nonviolations=10379260, unique transferred candidates=8345, exact=8333, unknown=0, pending=0 | 59172.78 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=10436671, GPU certified nonviolations=10436604, unique transferred candidates=8385, exact=8372, unknown=0, pending=0 | 59099.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=10494015, GPU certified nonviolations=10493948, unique transferred candidates=8431, exact=8423, unknown=0, pending=0 | 59073.14 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=10551359, GPU certified nonviolations=10551292, unique transferred candidates=8487, exact=8476, unknown=0, pending=0 | 59146.84 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=10608703, GPU certified nonviolations=10608636, unique transferred candidates=8527, exact=8513, unknown=0, pending=0 | 59170.73 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:36+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=10633279, GPU certified nonviolations=10633212, unique transferred candidates=8551, exact=8537, unknown=0, pending=0 | 59029.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=10666047, GPU certified nonviolations=10665980, unique transferred candidates=8567, exact=8551, unknown=0, pending=0 | 59059.37 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=10723391, GPU certified nonviolations=10723324, unique transferred candidates=8623, exact=8615, unknown=0, pending=0 | 58919.07 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=10780735, GPU certified nonviolations=10780668, unique transferred candidates=8671, exact=8662, unknown=0, pending=0 | 58941.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=10838079, GPU certified nonviolations=10838012, unique transferred candidates=8719, exact=8703, unknown=0, pending=0 | 58910.28 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=10895423, GPU certified nonviolations=10895355, unique transferred candidates=8759, exact=8750, unknown=0, pending=0 | 58814.62 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=10952767, GPU certified nonviolations=10952699, unique transferred candidates=8815, exact=8803, unknown=0, pending=0 | 58864.94 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=11010111, GPU certified nonviolations=11010043, unique transferred candidates=8855, exact=8843, unknown=0, pending=0 | 58901.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=11067455, GPU certified nonviolations=11067387, unique transferred candidates=8895, exact=8882, unknown=0, pending=0 | 58793.80 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=11124799, GPU certified nonviolations=11124731, unique transferred candidates=8949, exact=8941, unknown=0, pending=0 | 58765.95 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=11182143, GPU certified nonviolations=11182075, unique transferred candidates=8997, exact=8985, unknown=0, pending=0 | 58757.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=11239487, GPU certified nonviolations=11239419, unique transferred candidates=9045, exact=9032, unknown=0, pending=0 | 58732.69 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=11296831, GPU certified nonviolations=11296763, unique transferred candidates=9083, exact=9072, unknown=0, pending=0 | 58591.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=11354175, GPU certified nonviolations=11354107, unique transferred candidates=9138, exact=9129, unknown=0, pending=0 | 58676.92 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=11411519, GPU certified nonviolations=11411451, unique transferred candidates=9178, exact=9166, unknown=0, pending=0 | 58738.00 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=11468863, GPU certified nonviolations=11468795, unique transferred candidates=9226, exact=9218, unknown=0, pending=0 | 58647.16 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=11526207, GPU certified nonviolations=11526138, unique transferred candidates=9274, exact=9266, unknown=0, pending=0 | 58710.10 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=11583551, GPU certified nonviolations=11583482, unique transferred candidates=9330, exact=9318, unknown=0, pending=0 | 58778.70 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=11640895, GPU certified nonviolations=11640826, unique transferred candidates=9370, exact=9354, unknown=0, pending=0 | 58778.15 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=11698239, GPU certified nonviolations=11698170, unique transferred candidates=9403, exact=9387, unknown=0, pending=0 | 58664.36 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=11755583, GPU certified nonviolations=11755514, unique transferred candidates=9466, exact=9458, unknown=0, pending=0 | 58678.39 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=11812927, GPU certified nonviolations=11812858, unique transferred candidates=9514, exact=9502, unknown=0, pending=0 | 58696.59 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:32:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=11870271, GPU certified nonviolations=11870202, unique transferred candidates=9554, exact=9538, unknown=0, pending=0 | 58645.37 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=11927615, GPU certified nonviolations=11927546, unique transferred candidates=9599, exact=9591, unknown=0, pending=0 | 58556.75 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=11984959, GPU certified nonviolations=11984890, unique transferred candidates=9655, exact=9645, unknown=0, pending=0 | 58611.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=12042303, GPU certified nonviolations=12042234, unique transferred candidates=9695, exact=9682, unknown=0, pending=0 | 58602.57 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=12099647, GPU certified nonviolations=12099578, unique transferred candidates=9734, exact=9719, unknown=0, pending=0 | 58518.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=12156991, GPU certified nonviolations=12156922, unique transferred candidates=9790, exact=9781, unknown=0, pending=0 | 58534.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=12214335, GPU certified nonviolations=12214266, unique transferred candidates=9838, exact=9830, unknown=0, pending=0 | 58573.81 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=12271679, GPU certified nonviolations=12271610, unique transferred candidates=9886, exact=9871, unknown=0, pending=0 | 58550.14 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=12329023, GPU certified nonviolations=12328953, unique transferred candidates=9927, exact=9918, unknown=0, pending=0 | 58468.18 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=12386367, GPU certified nonviolations=12386297, unique transferred candidates=9982, exact=9973, unknown=0, pending=0 | 58530.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=12443711, GPU certified nonviolations=12443641, unique transferred candidates=10022, exact=10014, unknown=0, pending=0 | 58568.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=12501055, GPU certified nonviolations=12500985, unique transferred candidates=10062, exact=10054, unknown=0, pending=0 | 58475.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=12558399, GPU certified nonviolations=12558329, unique transferred candidates=10114, exact=10106, unknown=0, pending=0 | 58513.71 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=12615743, GPU certified nonviolations=12615673, unique transferred candidates=10162, exact=10150, unknown=0, pending=0 | 58525.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=12673087, GPU certified nonviolations=12673017, unique transferred candidates=10210, exact=10194, unknown=0, pending=0 | 58519.42 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=12730431, GPU certified nonviolations=12730361, unique transferred candidates=10239, exact=10222, unknown=0, pending=0 | 58475.37 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=12787775, GPU certified nonviolations=12787704, unique transferred candidates=10302, exact=10293, unknown=0, pending=0 | 58535.42 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=12845119, GPU certified nonviolations=12845048, unique transferred candidates=10342, exact=10330, unknown=0, pending=0 | 58479.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=12902463, GPU certified nonviolations=12902392, unique transferred candidates=10390, exact=10376, unknown=0, pending=0 | 58349.49 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=12959807, GPU certified nonviolations=12959736, unique transferred candidates=10436, exact=10428, unknown=0, pending=0 | 58268.38 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=13017151, GPU certified nonviolations=13017080, unique transferred candidates=10492, exact=10478, unknown=0, pending=0 | 58293.86 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=13074495, GPU certified nonviolations=13074424, unique transferred candidates=10530, exact=10514, unknown=0, pending=0 | 58219.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=13131839, GPU certified nonviolations=13131768, unique transferred candidates=10565, exact=10548, unknown=0, pending=0 | 58092.61 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=13189183, GPU certified nonviolations=13189112, unique transferred candidates=10625, exact=10617, unknown=0, pending=0 | 58122.60 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=13246527, GPU certified nonviolations=13246456, unique transferred candidates=10673, exact=10661, unknown=0, pending=0 | 58133.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=13303871, GPU certified nonviolations=13303800, unique transferred candidates=10713, exact=10697, unknown=0, pending=0 | 58033.26 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=13361215, GPU certified nonviolations=13361144, unique transferred candidates=10760, exact=10752, unknown=0, pending=0 | 57930.52 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=13418559, GPU certified nonviolations=13418488, unique transferred candidates=10815, exact=10803, unknown=0, pending=0 | 57889.10 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=13475903, GPU certified nonviolations=13475832, unique transferred candidates=10855, exact=10840, unknown=0, pending=0 | 57897.04 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=13533247, GPU certified nonviolations=13533176, unique transferred candidates=10893, exact=10879, unknown=0, pending=0 | 57842.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=13590591, GPU certified nonviolations=13590520, unique transferred candidates=10948, exact=10940, unknown=0, pending=0 | 57805.36 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=13647935, GPU certified nonviolations=13647864, unique transferred candidates=10996, exact=10988, unknown=0, pending=0 | 57758.27 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=13705279, GPU certified nonviolations=13705208, unique transferred candidates=11044, exact=11028, unknown=0, pending=0 | 57722.79 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=13762623, GPU certified nonviolations=13762552, unique transferred candidates=11084, exact=11076, unknown=0, pending=0 | 57646.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=13819967, GPU certified nonviolations=13819896, unique transferred candidates=11140, exact=11128, unknown=0, pending=0 | 57673.92 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:36+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=13844543, GPU certified nonviolations=13844472, unique transferred candidates=11156, exact=11144, unknown=0, pending=0 | 57643.44 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=13877311, GPU certified nonviolations=13877240, unique transferred candidates=11180, exact=11172, unknown=0, pending=0 | 57707.42 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=13934655, GPU certified nonviolations=13934584, unique transferred candidates=11220, exact=11207, unknown=0, pending=0 | 57642.42 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=13991999, GPU certified nonviolations=13991928, unique transferred candidates=11274, exact=11266, unknown=0, pending=0 | 57684.60 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=14049343, GPU certified nonviolations=14049272, unique transferred candidates=11322, exact=11310, unknown=0, pending=0 | 57721.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=14106687, GPU certified nonviolations=14106616, unique transferred candidates=11370, exact=11354, unknown=0, pending=0 | 57734.86 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=14164031, GPU certified nonviolations=14163960, unique transferred candidates=11409, exact=11400, unknown=0, pending=0 | 57663.93 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=14221375, GPU certified nonviolations=14221304, unique transferred candidates=11465, exact=11456, unknown=0, pending=0 | 57741.85 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=14278719, GPU certified nonviolations=14278648, unique transferred candidates=11505, exact=11493, unknown=0, pending=0 | 57765.90 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=14336063, GPU certified nonviolations=14335992, unique transferred candidates=11553, exact=11545, unknown=0, pending=0 | 57709.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=14393407, GPU certified nonviolations=14393336, unique transferred candidates=11599, exact=11592, unknown=0, pending=0 | 57748.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=14450751, GPU certified nonviolations=14450680, unique transferred candidates=11655, exact=11642, unknown=0, pending=0 | 57809.03 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=14508095, GPU certified nonviolations=14508024, unique transferred candidates=11695, exact=11682, unknown=0, pending=0 | 57803.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=14565439, GPU certified nonviolations=14565368, unique transferred candidates=11728, exact=11711, unknown=0, pending=0 | 57737.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=14622783, GPU certified nonviolations=14622712, unique transferred candidates=11788, exact=11779, unknown=0, pending=0 | 57773.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=14680127, GPU certified nonviolations=14680056, unique transferred candidates=11836, exact=11824, unknown=0, pending=0 | 57797.03 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=14737471, GPU certified nonviolations=14737400, unique transferred candidates=11876, exact=11860, unknown=0, pending=0 | 57744.14 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=14794815, GPU certified nonviolations=14794744, unique transferred candidates=11923, exact=11915, unknown=0, pending=0 | 57700.65 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=14852159, GPU certified nonviolations=14852088, unique transferred candidates=11979, exact=11971, unknown=0, pending=0 | 57693.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=14909503, GPU certified nonviolations=14909432, unique transferred candidates=12019, exact=12007, unknown=0, pending=0 | 57721.59 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=14966847, GPU certified nonviolations=14966776, unique transferred candidates=12058, exact=12043, unknown=0, pending=0 | 57675.94 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=15024191, GPU certified nonviolations=15024120, unique transferred candidates=12113, exact=12105, unknown=0, pending=0 | 57721.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=15081535, GPU certified nonviolations=15081464, unique transferred candidates=12161, exact=12153, unknown=0, pending=0 | 57764.74 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=15138879, GPU certified nonviolations=15138808, unique transferred candidates=12206, exact=12190, unknown=0, pending=0 | 57741.77 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:33:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=15196223, GPU certified nonviolations=15196152, unique transferred candidates=12248, exact=12240, unknown=0, pending=0 | 57668.62 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=15253567, GPU certified nonviolations=15253496, unique transferred candidates=12304, exact=12295, unknown=0, pending=0 | 57739.66 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=15310911, GPU certified nonviolations=15310840, unique transferred candidates=12344, exact=12336, unknown=0, pending=0 | 57734.78 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=15368255, GPU certified nonviolations=15368184, unique transferred candidates=12384, exact=12373, unknown=0, pending=0 | 57613.91 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=15425599, GPU certified nonviolations=15425528, unique transferred candidates=12438, exact=12430, unknown=0, pending=0 | 57585.00 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=15482943, GPU certified nonviolations=15482872, unique transferred candidates=12486, exact=12474, unknown=0, pending=0 | 57597.73 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=15540287, GPU certified nonviolations=15540216, unique transferred candidates=12534, exact=12518, unknown=0, pending=0 | 57584.18 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=15597631, GPU certified nonviolations=15597560, unique transferred candidates=12573, exact=12564, unknown=0, pending=0 | 57513.91 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=15654975, GPU certified nonviolations=15654903, unique transferred candidates=12629, exact=12621, unknown=0, pending=0 | 57557.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=15712319, GPU certified nonviolations=15712247, unique transferred candidates=12669, exact=12657, unknown=0, pending=0 | 57558.51 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=15769663, GPU certified nonviolations=15769591, unique transferred candidates=12717, exact=12709, unknown=0, pending=0 | 57515.81 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=15827007, GPU certified nonviolations=15826935, unique transferred candidates=12765, exact=12757, unknown=0, pending=0 | 57571.83 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=15884351, GPU certified nonviolations=15884279, unique transferred candidates=12821, exact=12806, unknown=0, pending=0 | 57599.12 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=15941695, GPU certified nonviolations=15941623, unique transferred candidates=12861, exact=12850, unknown=0, pending=0 | 57598.24 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=15999039, GPU certified nonviolations=15998967, unique transferred candidates=12894, exact=12877, unknown=0, pending=0 | 57563.70 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=16056383, GPU certified nonviolations=16056311, unique transferred candidates=12956, exact=12948, unknown=0, pending=0 | 57606.24 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=16113727, GPU certified nonviolations=16113655, unique transferred candidates=13004, exact=12991, unknown=0, pending=0 | 57594.85 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=16171071, GPU certified nonviolations=16170999, unique transferred candidates=13044, exact=13032, unknown=0, pending=0 | 57571.24 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=16228415, GPU certified nonviolations=16228343, unique transferred candidates=13090, exact=13082, unknown=0, pending=0 | 57549.46 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=16285759, GPU certified nonviolations=16285687, unique transferred candidates=13146, exact=13138, unknown=0, pending=0 | 57587.89 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=16343103, GPU certified nonviolations=16343031, unique transferred candidates=13186, exact=13172, unknown=0, pending=0 | 57567.24 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=16400447, GPU certified nonviolations=16400375, unique transferred candidates=13224, exact=13210, unknown=0, pending=0 | 57494.35 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=16457791, GPU certified nonviolations=16457719, unique transferred candidates=13278, exact=13269, unknown=0, pending=0 | 57527.52 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=16515135, GPU certified nonviolations=16515063, unique transferred candidates=13326, exact=13318, unknown=0, pending=0 | 57543.46 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=16572479, GPU certified nonviolations=16572407, unique transferred candidates=13374, exact=13358, unknown=0, pending=0 | 57523.63 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=16629823, GPU certified nonviolations=16629750, unique transferred candidates=13414, exact=13405, unknown=0, pending=0 | 57387.51 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=16687167, GPU certified nonviolations=16687094, unique transferred candidates=13470, exact=13460, unknown=0, pending=0 | 57430.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=16744511, GPU certified nonviolations=16744438, unique transferred candidates=13510, exact=13502, unknown=0, pending=0 | 57429.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=16801855, GPU certified nonviolations=16801782, unique transferred candidates=13550, exact=13539, unknown=0, pending=0 | 57367.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=16859199, GPU certified nonviolations=16859126, unique transferred candidates=13605, exact=13597, unknown=0, pending=0 | 57379.18 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=16916543, GPU certified nonviolations=16916470, unique transferred candidates=13653, exact=13641, unknown=0, pending=0 | 57393.78 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=16973887, GPU certified nonviolations=16973814, unique transferred candidates=13701, exact=13687, unknown=0, pending=0 | 57376.44 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=17031231, GPU certified nonviolations=17031158, unique transferred candidates=13740, exact=13731, unknown=0, pending=0 | 57273.42 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=17088575, GPU certified nonviolations=17088502, unique transferred candidates=13796, exact=13787, unknown=0, pending=0 | 57336.37 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=17145919, GPU certified nonviolations=17145846, unique transferred candidates=13836, exact=13824, unknown=0, pending=0 | 57374.93 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=17203263, GPU certified nonviolations=17203190, unique transferred candidates=13884, exact=13872, unknown=0, pending=0 | 57326.83 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:37+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=17211455, GPU certified nonviolations=17211382, unique transferred candidates=13884, exact=13880, unknown=0, pending=0 | 57254.00 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=17260607, GPU certified nonviolations=17260534, unique transferred candidates=13931, exact=13923, unknown=0, pending=0 | 57362.76 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=17317951, GPU certified nonviolations=17317878, unique transferred candidates=13987, exact=13975, unknown=0, pending=0 | 57400.78 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=17375295, GPU certified nonviolations=17375222, unique transferred candidates=14027, exact=14015, unknown=0, pending=0 | 57413.95 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=17432639, GPU certified nonviolations=17432566, unique transferred candidates=14060, exact=14044, unknown=0, pending=0 | 57379.96 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=17489983, GPU certified nonviolations=17489909, unique transferred candidates=14120, exact=14110, unknown=0, pending=0 | 57425.66 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=17547327, GPU certified nonviolations=17547253, unique transferred candidates=14168, exact=14156, unknown=0, pending=0 | 57443.28 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=17604671, GPU certified nonviolations=17604597, unique transferred candidates=14208, exact=14192, unknown=0, pending=0 | 57388.26 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=17662015, GPU certified nonviolations=17661941, unique transferred candidates=14255, exact=14247, unknown=0, pending=0 | 57384.16 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=17719359, GPU certified nonviolations=17719285, unique transferred candidates=14310, exact=14299, unknown=0, pending=0 | 57430.15 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=17776703, GPU certified nonviolations=17776629, unique transferred candidates=14350, exact=14337, unknown=0, pending=0 | 57438.06 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=17834047, GPU certified nonviolations=17833973, unique transferred candidates=14386, exact=14374, unknown=0, pending=0 | 57393.81 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=17891391, GPU certified nonviolations=17891317, unique transferred candidates=14441, exact=14433, unknown=0, pending=0 | 57449.84 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=17948735, GPU certified nonviolations=17948661, unique transferred candidates=14489, exact=14481, unknown=0, pending=0 | 57485.97 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=18006079, GPU certified nonviolations=18006005, unique transferred candidates=14537, exact=14524, unknown=0, pending=0 | 57470.64 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=18063423, GPU certified nonviolations=18063348, unique transferred candidates=14577, exact=14568, unknown=0, pending=0 | 57439.14 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=18120767, GPU certified nonviolations=18120692, unique transferred candidates=14632, exact=14620, unknown=0, pending=0 | 57486.20 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=18178111, GPU certified nonviolations=18178036, unique transferred candidates=14672, exact=14664, unknown=0, pending=0 | 57508.36 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=18235455, GPU certified nonviolations=18235380, unique transferred candidates=14712, exact=14704, unknown=0, pending=0 | 57467.64 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=18292799, GPU certified nonviolations=18292724, unique transferred candidates=14767, exact=14759, unknown=0, pending=0 | 57491.49 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=18350143, GPU certified nonviolations=18350068, unique transferred candidates=14815, exact=14803, unknown=0, pending=0 | 57529.60 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=18407487, GPU certified nonviolations=18407412, unique transferred candidates=14863, exact=14851, unknown=0, pending=0 | 57526.38 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=18464831, GPU certified nonviolations=18464756, unique transferred candidates=14902, exact=14893, unknown=0, pending=0 | 57472.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=18522175, GPU certified nonviolations=18522100, unique transferred candidates=14958, exact=14950, unknown=0, pending=0 | 57508.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:34:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=18579519, GPU certified nonviolations=18579444, unique transferred candidates=14998, exact=14986, unknown=0, pending=0 | 57511.99 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=18636863, GPU certified nonviolations=18636788, unique transferred candidates=15046, exact=15038, unknown=0, pending=0 | 57460.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=18694207, GPU certified nonviolations=18694132, unique transferred candidates=15092, exact=15085, unknown=0, pending=0 | 57487.89 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=18751551, GPU certified nonviolations=18751476, unique transferred candidates=15148, exact=15136, unknown=0, pending=0 | 57513.69 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=18808895, GPU certified nonviolations=18808820, unique transferred candidates=15188, exact=15180, unknown=0, pending=0 | 57516.00 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=18866239, GPU certified nonviolations=18866164, unique transferred candidates=15221, exact=15205, unknown=0, pending=0 | 57495.55 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=18923583, GPU certified nonviolations=18923507, unique transferred candidates=15281, exact=15273, unknown=0, pending=0 | 57532.63 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=18980927, GPU certified nonviolations=18980851, unique transferred candidates=15329, exact=15316, unknown=0, pending=0 | 57561.70 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=19038271, GPU certified nonviolations=19038195, unique transferred candidates=15369, exact=15355, unknown=0, pending=0 | 57521.87 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=19095615, GPU certified nonviolations=19095539, unique transferred candidates=15416, exact=15408, unknown=0, pending=0 | 57506.72 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=19152959, GPU certified nonviolations=19152883, unique transferred candidates=15472, exact=15463, unknown=0, pending=0 | 57540.99 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=19210303, GPU certified nonviolations=19210227, unique transferred candidates=15512, exact=15500, unknown=0, pending=0 | 57560.98 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=19267647, GPU certified nonviolations=19267571, unique transferred candidates=15552, exact=15536, unknown=0, pending=0 | 57530.16 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=19324991, GPU certified nonviolations=19324914, unique transferred candidates=15609, exact=15601, unknown=0, pending=0 | 57567.45 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=19382335, GPU certified nonviolations=19382258, unique transferred candidates=15657, exact=15649, unknown=0, pending=0 | 57587.17 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=19439679, GPU certified nonviolations=19439602, unique transferred candidates=15705, exact=15691, unknown=0, pending=0 | 57576.74 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=19497023, GPU certified nonviolations=19496946, unique transferred candidates=15743, exact=15735, unknown=0, pending=0 | 57521.46 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=19554367, GPU certified nonviolations=19554290, unique transferred candidates=15798, exact=15786, unknown=0, pending=0 | 57572.60 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=19611711, GPU certified nonviolations=19611634, unique transferred candidates=15838, exact=15830, unknown=0, pending=0 | 57598.20 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=19669055, GPU certified nonviolations=19668978, unique transferred candidates=15878, exact=15865, unknown=0, pending=0 | 57545.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=19726399, GPU certified nonviolations=19726322, unique transferred candidates=15931, exact=15923, unknown=0, pending=0 | 57585.64 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=19783743, GPU certified nonviolations=19783666, unique transferred candidates=15979, exact=15967, unknown=0, pending=0 | 57630.74 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=19841087, GPU certified nonviolations=19841010, unique transferred candidates=16027, exact=16012, unknown=0, pending=0 | 57628.80 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=19898431, GPU certified nonviolations=19898354, unique transferred candidates=16066, exact=16057, unknown=0, pending=0 | 57563.71 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=19955775, GPU certified nonviolations=19955698, unique transferred candidates=16122, exact=16114, unknown=0, pending=0 | 57616.28 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=20013119, GPU certified nonviolations=20013042, unique transferred candidates=16162, exact=16149, unknown=0, pending=0 | 57629.48 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=20070463, GPU certified nonviolations=20070386, unique transferred candidates=16210, exact=16202, unknown=0, pending=0 | 57565.27 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=20127807, GPU certified nonviolations=20127730, unique transferred candidates=16253, exact=16246, unknown=0, pending=0 | 57596.84 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=20185151, GPU certified nonviolations=20185074, unique transferred candidates=16309, exact=16297, unknown=0, pending=0 | 57641.52 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=20242495, GPU certified nonviolations=20242418, unique transferred candidates=16349, exact=16336, unknown=0, pending=0 | 57640.83 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=20299839, GPU certified nonviolations=20299762, unique transferred candidates=16382, exact=16366, unknown=0, pending=0 | 57611.11 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=20357183, GPU certified nonviolations=20357106, unique transferred candidates=16443, exact=16435, unknown=0, pending=0 | 57640.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=20414527, GPU certified nonviolations=20414450, unique transferred candidates=16491, exact=16479, unknown=0, pending=0 | 57667.72 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=20471871, GPU certified nonviolations=20471794, unique transferred candidates=16531, exact=16515, unknown=0, pending=0 | 57621.17 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=20529215, GPU certified nonviolations=20529137, unique transferred candidates=16578, exact=16570, unknown=0, pending=0 | 57621.93 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=20586559, GPU certified nonviolations=20586481, unique transferred candidates=16634, exact=16622, unknown=0, pending=0 | 57661.42 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=20643903, GPU certified nonviolations=20643825, unique transferred candidates=16674, exact=16661, unknown=0, pending=0 | 57663.17 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=20701247, GPU certified nonviolations=20701169, unique transferred candidates=16714, exact=16698, unknown=0, pending=0 | 57624.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=20758591, GPU certified nonviolations=20758513, unique transferred candidates=16770, exact=16762, unknown=0, pending=0 | 57667.23 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:37+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=20799551, GPU certified nonviolations=20799473, unique transferred candidates=16810, exact=16798, unknown=0, pending=0 | 57677.87 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=20815935, GPU certified nonviolations=20815857, unique transferred candidates=16818, exact=16810, unknown=0, pending=0 | 57696.88 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=20873279, GPU certified nonviolations=20873201, unique transferred candidates=16866, exact=16854, unknown=0, pending=0 | 57671.15 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=20930623, GPU certified nonviolations=20930545, unique transferred candidates=16904, exact=16896, unknown=0, pending=0 | 57645.55 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=20987967, GPU certified nonviolations=20987889, unique transferred candidates=16960, exact=16947, unknown=0, pending=0 | 57693.86 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=21045311, GPU certified nonviolations=21045233, unique transferred candidates=17000, exact=16991, unknown=0, pending=0 | 57707.92 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=21102655, GPU certified nonviolations=21102577, unique transferred candidates=17040, exact=17032, unknown=0, pending=0 | 57667.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=21159999, GPU certified nonviolations=21159921, unique transferred candidates=17091, exact=17083, unknown=0, pending=0 | 57687.33 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=21217343, GPU certified nonviolations=21217265, unique transferred candidates=17139, exact=17127, unknown=0, pending=0 | 57722.20 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=21274687, GPU certified nonviolations=21274609, unique transferred candidates=17187, exact=17174, unknown=0, pending=0 | 57716.65 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=21332031, GPU certified nonviolations=21331953, unique transferred candidates=17226, exact=17218, unknown=0, pending=0 | 57667.14 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=21389375, GPU certified nonviolations=21389297, unique transferred candidates=17280, exact=17271, unknown=0, pending=0 | 57712.91 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=21446719, GPU certified nonviolations=21446641, unique transferred candidates=17320, exact=17308, unknown=0, pending=0 | 57721.20 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=21504063, GPU certified nonviolations=21503985, unique transferred candidates=17368, exact=17360, unknown=0, pending=0 | 57671.66 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=21561407, GPU certified nonviolations=21561328, unique transferred candidates=17416, exact=17408, unknown=0, pending=0 | 57688.39 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=21618751, GPU certified nonviolations=21618672, unique transferred candidates=17472, exact=17460, unknown=0, pending=0 | 57719.67 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=21676095, GPU certified nonviolations=21676016, unique transferred candidates=17512, exact=17502, unknown=0, pending=0 | 57722.45 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=21733439, GPU certified nonviolations=21733360, unique transferred candidates=17545, exact=17529, unknown=0, pending=0 | 57706.64 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=21790783, GPU certified nonviolations=21790704, unique transferred candidates=17607, exact=17599, unknown=0, pending=0 | 57741.28 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=21848127, GPU certified nonviolations=21848048, unique transferred candidates=17655, exact=17643, unknown=0, pending=0 | 57737.02 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=21905471, GPU certified nonviolations=21905392, unique transferred candidates=17695, exact=17681, unknown=0, pending=0 | 57707.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=21962815, GPU certified nonviolations=21962736, unique transferred candidates=17741, exact=17733, unknown=0, pending=0 | 57700.59 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=22020159, GPU certified nonviolations=22020080, unique transferred candidates=17797, exact=17786, unknown=0, pending=0 | 57735.14 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=22077503, GPU certified nonviolations=22077424, unique transferred candidates=17837, exact=17825, unknown=0, pending=0 | 57742.71 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:35:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=22134847, GPU certified nonviolations=22134768, unique transferred candidates=17874, exact=17861, unknown=0, pending=0 | 57713.63 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=22192191, GPU certified nonviolations=22192112, unique transferred candidates=17930, exact=17922, unknown=0, pending=0 | 57734.36 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=22249535, GPU certified nonviolations=22249456, unique transferred candidates=17978, exact=17969, unknown=0, pending=0 | 57749.83 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=22306879, GPU certified nonviolations=22306800, unique transferred candidates=18026, exact=18014, unknown=0, pending=0 | 57727.92 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=22364223, GPU certified nonviolations=22364144, unique transferred candidates=18063, exact=18055, unknown=0, pending=0 | 57685.11 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=22421567, GPU certified nonviolations=22421488, unique transferred candidates=18119, exact=18108, unknown=0, pending=0 | 57703.48 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=22478911, GPU certified nonviolations=22478832, unique transferred candidates=18159, exact=18149, unknown=0, pending=0 | 57696.69 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=22536255, GPU certified nonviolations=22536176, unique transferred candidates=18199, exact=18191, unknown=0, pending=0 | 57633.60 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=22593599, GPU certified nonviolations=22593520, unique transferred candidates=18254, exact=18246, unknown=0, pending=0 | 57617.38 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=22650943, GPU certified nonviolations=22650864, unique transferred candidates=18302, exact=18290, unknown=0, pending=0 | 57656.57 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=22708287, GPU certified nonviolations=22708208, unique transferred candidates=18350, exact=18334, unknown=0, pending=0 | 57654.35 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=22765631, GPU certified nonviolations=22765552, unique transferred candidates=18388, exact=18378, unknown=0, pending=0 | 57607.70 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=22822975, GPU certified nonviolations=22822896, unique transferred candidates=18444, exact=18435, unknown=0, pending=0 | 57656.28 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=22880319, GPU certified nonviolations=22880240, unique transferred candidates=18484, exact=18472, unknown=0, pending=0 | 57660.49 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=22937663, GPU certified nonviolations=22937584, unique transferred candidates=18532, exact=18520, unknown=0, pending=0 | 57595.53 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=22995007, GPU certified nonviolations=22994928, unique transferred candidates=18575, exact=18568, unknown=0, pending=0 | 57613.62 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=23052351, GPU certified nonviolations=23052272, unique transferred candidates=18631, exact=18619, unknown=0, pending=0 | 57649.14 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=23109695, GPU certified nonviolations=23109616, unique transferred candidates=18671, exact=18659, unknown=0, pending=0 | 57638.36 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=23167039, GPU certified nonviolations=23166960, unique transferred candidates=18704, exact=18688, unknown=0, pending=0 | 57580.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=23224383, GPU certified nonviolations=23224304, unique transferred candidates=18764, exact=18756, unknown=0, pending=0 | 57606.95 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=23281727, GPU certified nonviolations=23281648, unique transferred candidates=18812, exact=18798, unknown=0, pending=0 | 57590.99 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=23339071, GPU certified nonviolations=23338992, unique transferred candidates=18852, exact=18836, unknown=0, pending=0 | 57522.26 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=23396415, GPU certified nonviolations=23396336, unique transferred candidates=18899, exact=18891, unknown=0, pending=0 | 57518.81 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=23453759, GPU certified nonviolations=23453680, unique transferred candidates=18955, exact=18944, unknown=0, pending=0 | 57546.47 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=23511103, GPU certified nonviolations=23511024, unique transferred candidates=18995, exact=18983, unknown=0, pending=0 | 57556.85 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=23568447, GPU certified nonviolations=23568368, unique transferred candidates=19034, exact=19019, unknown=0, pending=0 | 57532.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=23625791, GPU certified nonviolations=23625712, unique transferred candidates=19089, exact=19081, unknown=0, pending=0 | 57569.73 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=23683135, GPU certified nonviolations=23683056, unique transferred candidates=19137, exact=19129, unknown=0, pending=0 | 57590.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=23740479, GPU certified nonviolations=23740400, unique transferred candidates=19185, exact=19173, unknown=0, pending=0 | 57577.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=23797823, GPU certified nonviolations=23797744, unique transferred candidates=19224, exact=19216, unknown=0, pending=0 | 57548.02 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=23855167, GPU certified nonviolations=23855088, unique transferred candidates=19280, exact=19268, unknown=0, pending=0 | 57588.46 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=23912511, GPU certified nonviolations=23912432, unique transferred candidates=19320, exact=19311, unknown=0, pending=0 | 57608.17 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=23969855, GPU certified nonviolations=23969776, unique transferred candidates=19360, exact=19352, unknown=0, pending=0 | 57568.45 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=24027199, GPU certified nonviolations=24027120, unique transferred candidates=19413, exact=19405, unknown=0, pending=0 | 57588.52 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=24084543, GPU certified nonviolations=24084464, unique transferred candidates=19461, exact=19449, unknown=0, pending=0 | 57628.03 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=24141887, GPU certified nonviolations=24141808, unique transferred candidates=19509, exact=19493, unknown=0, pending=0 | 57629.80 GPU screened draws/s | best exact gap=0.
