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
