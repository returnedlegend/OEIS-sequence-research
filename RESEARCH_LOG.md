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

- 2026-11-15T19:36:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=24199231, GPU certified nonviolations=24199152, unique transferred candidates=19547, exact=19539, unknown=0, pending=0 | 57586.49 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:37+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=24207423, GPU certified nonviolations=24207344, unique transferred candidates=19555, exact=19547, unknown=0, pending=0 | 57545.94 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=24256575, GPU certified nonviolations=24256496, unique transferred candidates=19603, exact=19594, unknown=0, pending=0 | 57609.62 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=24313919, GPU certified nonviolations=24313840, unique transferred candidates=19643, exact=19631, unknown=0, pending=0 | 57628.96 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=24371263, GPU certified nonviolations=24371184, unique transferred candidates=19691, exact=19683, unknown=0, pending=0 | 57591.07 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=24428607, GPU certified nonviolations=24428528, unique transferred candidates=19736, exact=19728, unknown=0, pending=0 | 57587.88 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=24485951, GPU certified nonviolations=24485872, unique transferred candidates=19792, exact=19779, unknown=0, pending=0 | 57621.27 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=24543295, GPU certified nonviolations=24543216, unique transferred candidates=19832, exact=19816, unknown=0, pending=0 | 57627.14 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=24600639, GPU certified nonviolations=24600560, unique transferred candidates=19865, exact=19848, unknown=0, pending=0 | 57580.89 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=24657983, GPU certified nonviolations=24657903, unique transferred candidates=19927, exact=19919, unknown=0, pending=0 | 57608.14 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=24715327, GPU certified nonviolations=24715247, unique transferred candidates=19975, exact=19962, unknown=0, pending=0 | 57638.53 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=24772671, GPU certified nonviolations=24772591, unique transferred candidates=20015, exact=20003, unknown=0, pending=0 | 57598.77 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=24830015, GPU certified nonviolations=24829935, unique transferred candidates=20059, exact=20051, unknown=0, pending=0 | 57563.27 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=24887359, GPU certified nonviolations=24887279, unique transferred candidates=20115, exact=20103, unknown=0, pending=0 | 57565.45 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=24944703, GPU certified nonviolations=24944623, unique transferred candidates=20155, exact=20143, unknown=0, pending=0 | 57570.08 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=25002047, GPU certified nonviolations=25001967, unique transferred candidates=20194, exact=20179, unknown=0, pending=0 | 57544.62 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=25059391, GPU certified nonviolations=25059311, unique transferred candidates=20250, exact=20240, unknown=0, pending=0 | 57588.83 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=25116735, GPU certified nonviolations=25116655, unique transferred candidates=20298, exact=20290, unknown=0, pending=0 | 57614.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=25174079, GPU certified nonviolations=25173999, unique transferred candidates=20346, exact=20330, unknown=0, pending=0 | 57594.71 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=25231423, GPU certified nonviolations=25231343, unique transferred candidates=20383, exact=20375, unknown=0, pending=0 | 57548.35 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=25288767, GPU certified nonviolations=25288687, unique transferred candidates=20439, exact=20430, unknown=0, pending=0 | 57590.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=25346111, GPU certified nonviolations=25346031, unique transferred candidates=20479, exact=20471, unknown=0, pending=0 | 57599.77 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=25403455, GPU certified nonviolations=25403375, unique transferred candidates=20519, exact=20511, unknown=0, pending=0 | 57563.69 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=25460799, GPU certified nonviolations=25460719, unique transferred candidates=20572, exact=20564, unknown=0, pending=0 | 57595.99 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:36:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=25518143, GPU certified nonviolations=25518063, unique transferred candidates=20620, exact=20605, unknown=0, pending=0 | 57612.90 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=25575487, GPU certified nonviolations=25575407, unique transferred candidates=20668, exact=20654, unknown=0, pending=0 | 57603.76 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=25632831, GPU certified nonviolations=25632751, unique transferred candidates=20708, exact=20700, unknown=0, pending=0 | 57563.84 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=25690175, GPU certified nonviolations=25690095, unique transferred candidates=20764, exact=20756, unknown=0, pending=0 | 57603.79 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=25747519, GPU certified nonviolations=25747439, unique transferred candidates=20804, exact=20791, unknown=0, pending=0 | 57603.49 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=25804863, GPU certified nonviolations=25804783, unique transferred candidates=20852, exact=20844, unknown=0, pending=0 | 57568.49 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=25862207, GPU certified nonviolations=25862127, unique transferred candidates=20900, exact=20892, unknown=0, pending=0 | 57604.39 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=25919551, GPU certified nonviolations=25919471, unique transferred candidates=20956, exact=20943, unknown=0, pending=0 | 57628.01 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=25976895, GPU certified nonviolations=25976815, unique transferred candidates=20996, exact=20983, unknown=0, pending=0 | 57627.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=26034239, GPU certified nonviolations=26034159, unique transferred candidates=21029, exact=21013, unknown=0, pending=0 | 57603.37 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=26091583, GPU certified nonviolations=26091502, unique transferred candidates=21089, exact=21081, unknown=0, pending=0 | 57624.39 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=26148927, GPU certified nonviolations=26148846, unique transferred candidates=21137, exact=21124, unknown=0, pending=0 | 57632.49 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=26206271, GPU certified nonviolations=26206190, unique transferred candidates=21177, exact=21161, unknown=0, pending=0 | 57605.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=26263615, GPU certified nonviolations=26263534, unique transferred candidates=21224, exact=21216, unknown=0, pending=0 | 57594.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=26320959, GPU certified nonviolations=26320878, unique transferred candidates=21279, exact=21269, unknown=0, pending=0 | 57626.47 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=26378303, GPU certified nonviolations=26378222, unique transferred candidates=21319, exact=21307, unknown=0, pending=0 | 57624.57 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=26435647, GPU certified nonviolations=26435566, unique transferred candidates=21358, exact=21343, unknown=0, pending=0 | 57600.65 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=26492991, GPU certified nonviolations=26492910, unique transferred candidates=21414, exact=21406, unknown=0, pending=0 | 57631.26 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=26550335, GPU certified nonviolations=26550254, unique transferred candidates=21462, exact=21454, unknown=0, pending=0 | 57644.34 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=26607679, GPU certified nonviolations=26607598, unique transferred candidates=21510, exact=21498, unknown=0, pending=0 | 57628.07 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=26665023, GPU certified nonviolations=26664942, unique transferred candidates=21550, exact=21542, unknown=0, pending=0 | 57588.60 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=26722367, GPU certified nonviolations=26722286, unique transferred candidates=21606, exact=21594, unknown=0, pending=0 | 57609.00 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=26779711, GPU certified nonviolations=26779630, unique transferred candidates=21646, exact=21638, unknown=0, pending=0 | 57622.19 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=26837055, GPU certified nonviolations=26836974, unique transferred candidates=21686, exact=21678, unknown=0, pending=0 | 57594.88 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=26894399, GPU certified nonviolations=26894318, unique transferred candidates=21739, exact=21731, unknown=0, pending=0 | 57619.60 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=26951743, GPU certified nonviolations=26951662, unique transferred candidates=21787, exact=21775, unknown=0, pending=0 | 57637.45 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=27009087, GPU certified nonviolations=27009006, unique transferred candidates=21835, exact=21824, unknown=0, pending=0 | 57619.75 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=27066431, GPU certified nonviolations=27066350, unique transferred candidates=21872, exact=21856, unknown=0, pending=0 | 57589.13 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=27123775, GPU certified nonviolations=27123694, unique transferred candidates=21929, exact=21919, unknown=0, pending=0 | 57609.47 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=27181119, GPU certified nonviolations=27181038, unique transferred candidates=21969, exact=21957, unknown=0, pending=0 | 57618.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=27238463, GPU certified nonviolations=27238382, unique transferred candidates=22017, exact=22009, unknown=0, pending=0 | 57576.56 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=27295807, GPU certified nonviolations=27295726, unique transferred candidates=22062, exact=22054, unknown=0, pending=0 | 57602.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=27353151, GPU certified nonviolations=27353070, unique transferred candidates=22118, exact=22106, unknown=0, pending=0 | 57623.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=27410495, GPU certified nonviolations=27410414, unique transferred candidates=22157, exact=22141, unknown=0, pending=0 | 57593.04 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=27467839, GPU certified nonviolations=27467758, unique transferred candidates=22191, exact=22175, unknown=0, pending=0 | 57536.92 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=27525183, GPU certified nonviolations=27525102, unique transferred candidates=22251, exact=22243, unknown=0, pending=0 | 57550.24 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=27582527, GPU certified nonviolations=27582446, unique transferred candidates=22299, exact=22286, unknown=0, pending=0 | 57520.59 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:37+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=27631679, GPU certified nonviolations=27631598, unique transferred candidates=22337, exact=22321, unknown=0, pending=0 | 57484.11 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=27639871, GPU certified nonviolations=27639790, unique transferred candidates=22339, exact=22323, unknown=0, pending=0 | 57477.17 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=27697215, GPU certified nonviolations=27697134, unique transferred candidates=22385, exact=22377, unknown=0, pending=0 | 57445.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=27754559, GPU certified nonviolations=27754478, unique transferred candidates=22441, exact=22432, unknown=0, pending=0 | 57468.51 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=27811903, GPU certified nonviolations=27811822, unique transferred candidates=22481, exact=22469, unknown=0, pending=0 | 57469.70 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=27869247, GPU certified nonviolations=27869166, unique transferred candidates=22519, exact=22505, unknown=0, pending=0 | 57431.47 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=27926591, GPU certified nonviolations=27926510, unique transferred candidates=22575, exact=22567, unknown=0, pending=0 | 57436.90 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=27983935, GPU certified nonviolations=27983854, unique transferred candidates=22623, exact=22613, unknown=0, pending=0 | 57449.10 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=28041279, GPU certified nonviolations=28041198, unique transferred candidates=22671, exact=22656, unknown=0, pending=0 | 57432.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=28098623, GPU certified nonviolations=28098542, unique transferred candidates=22709, exact=22701, unknown=0, pending=0 | 57383.97 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=28155967, GPU certified nonviolations=28155886, unique transferred candidates=22765, exact=22754, unknown=0, pending=0 | 57410.90 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=28213311, GPU certified nonviolations=28213230, unique transferred candidates=22805, exact=22795, unknown=0, pending=0 | 57414.78 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=28270655, GPU certified nonviolations=28270574, unique transferred candidates=22845, exact=22836, unknown=0, pending=0 | 57380.23 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=28327999, GPU certified nonviolations=28327918, unique transferred candidates=22900, exact=22892, unknown=0, pending=0 | 57373.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=28385343, GPU certified nonviolations=28385262, unique transferred candidates=22948, exact=22936, unknown=0, pending=0 | 57395.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=28442687, GPU certified nonviolations=28442606, unique transferred candidates=22996, exact=22980, unknown=0, pending=0 | 57382.49 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=28500031, GPU certified nonviolations=28499950, unique transferred candidates=23025, exact=23008, unknown=0, pending=0 | 57321.59 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=28557375, GPU certified nonviolations=28557294, unique transferred candidates=23088, exact=23080, unknown=0, pending=0 | 57337.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=28614719, GPU certified nonviolations=28614638, unique transferred candidates=23128, exact=23116, unknown=0, pending=0 | 57351.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=28672063, GPU certified nonviolations=28671982, unique transferred candidates=23176, exact=23163, unknown=0, pending=0 | 57307.83 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=28729407, GPU certified nonviolations=28729326, unique transferred candidates=23221, exact=23213, unknown=0, pending=0 | 57324.38 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=28786751, GPU certified nonviolations=28786670, unique transferred candidates=23277, exact=23265, unknown=0, pending=0 | 57340.85 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:37:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=28844095, GPU certified nonviolations=28844014, unique transferred candidates=23317, exact=23301, unknown=0, pending=0 | 57341.42 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=28901439, GPU certified nonviolations=28901358, unique transferred candidates=23350, exact=23334, unknown=0, pending=0 | 57308.91 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=28958783, GPU certified nonviolations=28958702, unique transferred candidates=23411, exact=23403, unknown=0, pending=0 | 57320.07 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=29016127, GPU certified nonviolations=29016046, unique transferred candidates=23459, exact=23446, unknown=0, pending=0 | 57329.05 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=29073471, GPU certified nonviolations=29073390, unique transferred candidates=23499, exact=23483, unknown=0, pending=0 | 57299.56 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=29130815, GPU certified nonviolations=29130734, unique transferred candidates=23545, exact=23537, unknown=0, pending=0 | 57262.26 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=29188159, GPU certified nonviolations=29188078, unique transferred candidates=23601, exact=23592, unknown=0, pending=0 | 57262.11 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=29245503, GPU certified nonviolations=29245422, unique transferred candidates=23641, exact=23628, unknown=0, pending=0 | 57255.71 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=29302847, GPU certified nonviolations=29302766, unique transferred candidates=23680, exact=23665, unknown=0, pending=0 | 57216.81 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=29360191, GPU certified nonviolations=29360110, unique transferred candidates=23735, exact=23727, unknown=0, pending=0 | 57208.23 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=29417535, GPU certified nonviolations=29417454, unique transferred candidates=23783, exact=23774, unknown=0, pending=0 | 57222.46 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=29474879, GPU certified nonviolations=29474798, unique transferred candidates=23830, exact=23814, unknown=0, pending=0 | 57194.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=29532223, GPU certified nonviolations=29532142, unique transferred candidates=23871, exact=23863, unknown=0, pending=0 | 57152.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=29589567, GPU certified nonviolations=29589486, unique transferred candidates=23927, exact=23915, unknown=0, pending=0 | 57165.73 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=29646911, GPU certified nonviolations=29646830, unique transferred candidates=23967, exact=23959, unknown=0, pending=0 | 57163.07 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=29704255, GPU certified nonviolations=29704174, unique transferred candidates=24007, exact=23996, unknown=0, pending=0 | 57116.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=29761599, GPU certified nonviolations=29761518, unique transferred candidates=24062, exact=24054, unknown=0, pending=0 | 57124.94 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=29818943, GPU certified nonviolations=29818862, unique transferred candidates=24109, exact=24097, unknown=0, pending=0 | 57111.95 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=29876287, GPU certified nonviolations=29876206, unique transferred candidates=24157, exact=24142, unknown=0, pending=0 | 57096.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=29933631, GPU certified nonviolations=29933550, unique transferred candidates=24194, exact=24181, unknown=0, pending=0 | 57052.89 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=29990975, GPU certified nonviolations=29990894, unique transferred candidates=24250, exact=24238, unknown=0, pending=0 | 57054.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=30048319, GPU certified nonviolations=30048238, unique transferred candidates=24290, exact=24278, unknown=0, pending=0 | 57051.59 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=30105663, GPU certified nonviolations=30105582, unique transferred candidates=24338, exact=24329, unknown=0, pending=0 | 56998.85 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=30163007, GPU certified nonviolations=30162926, unique transferred candidates=24382, exact=24375, unknown=0, pending=0 | 56991.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=30220351, GPU certified nonviolations=30220270, unique transferred candidates=24438, exact=24425, unknown=0, pending=0 | 56976.19 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=30277695, GPU certified nonviolations=30277614, unique transferred candidates=24478, exact=24462, unknown=0, pending=0 | 56940.64 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=30335039, GPU certified nonviolations=30334958, unique transferred candidates=24511, exact=24494, unknown=0, pending=0 | 56879.46 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=30392383, GPU certified nonviolations=30392302, unique transferred candidates=24570, exact=24561, unknown=0, pending=0 | 56866.13 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=30449727, GPU certified nonviolations=30449646, unique transferred candidates=24618, exact=24606, unknown=0, pending=0 | 56851.14 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=30507071, GPU certified nonviolations=30506990, unique transferred candidates=24658, exact=24642, unknown=0, pending=0 | 56791.13 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=30564415, GPU certified nonviolations=30564334, unique transferred candidates=24704, exact=24696, unknown=0, pending=0 | 56763.23 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=30621759, GPU certified nonviolations=30621678, unique transferred candidates=24759, exact=24747, unknown=0, pending=0 | 56768.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=30679103, GPU certified nonviolations=30679022, unique transferred candidates=24799, exact=24787, unknown=0, pending=0 | 56770.02 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:37+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=30687295, GPU certified nonviolations=30687214, unique transferred candidates=24807, exact=24799, unknown=0, pending=0 | 56735.59 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=30736447, GPU certified nonviolations=30736366, unique transferred candidates=24836, exact=24822, unknown=0, pending=0 | 56745.49 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=30793791, GPU certified nonviolations=30793710, unique transferred candidates=24891, exact=24883, unknown=0, pending=0 | 56763.11 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=30851135, GPU certified nonviolations=30851054, unique transferred candidates=24939, exact=24930, unknown=0, pending=0 | 56764.76 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=30908479, GPU certified nonviolations=30908398, unique transferred candidates=24987, exact=24971, unknown=0, pending=0 | 56755.84 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=30965823, GPU certified nonviolations=30965742, unique transferred candidates=25026, exact=25018, unknown=0, pending=0 | 56724.79 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=31023167, GPU certified nonviolations=31023086, unique transferred candidates=25082, exact=25070, unknown=0, pending=0 | 56748.01 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=31080511, GPU certified nonviolations=31080430, unique transferred candidates=25122, exact=25113, unknown=0, pending=0 | 56748.04 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=31137855, GPU certified nonviolations=31137774, unique transferred candidates=25162, exact=25150, unknown=0, pending=0 | 56710.83 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=31195199, GPU certified nonviolations=31195118, unique transferred candidates=25217, exact=25209, unknown=0, pending=0 | 56738.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=31252543, GPU certified nonviolations=31252462, unique transferred candidates=25265, exact=25253, unknown=0, pending=0 | 56759.63 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=31309887, GPU certified nonviolations=31309806, unique transferred candidates=25313, exact=25297, unknown=0, pending=0 | 56745.57 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=31367231, GPU certified nonviolations=31367150, unique transferred candidates=25351, exact=25342, unknown=0, pending=0 | 56700.17 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=31424575, GPU certified nonviolations=31424494, unique transferred candidates=25407, exact=25398, unknown=0, pending=0 | 56713.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=31481919, GPU certified nonviolations=31481838, unique transferred candidates=25447, exact=25434, unknown=0, pending=0 | 56719.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=31539263, GPU certified nonviolations=31539182, unique transferred candidates=25495, exact=25487, unknown=0, pending=0 | 56679.02 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=31596607, GPU certified nonviolations=31596526, unique transferred candidates=25539, exact=25531, unknown=0, pending=0 | 56707.46 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=31653951, GPU certified nonviolations=31653870, unique transferred candidates=25595, exact=25582, unknown=0, pending=0 | 56716.62 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=31711295, GPU certified nonviolations=31711214, unique transferred candidates=25635, exact=25621, unknown=0, pending=0 | 56708.34 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=31768639, GPU certified nonviolations=31768558, unique transferred candidates=25668, exact=25652, unknown=0, pending=0 | 56687.33 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=31825983, GPU certified nonviolations=31825902, unique transferred candidates=25730, exact=25722, unknown=0, pending=0 | 56696.76 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=31883327, GPU certified nonviolations=31883246, unique transferred candidates=25778, exact=25766, unknown=0, pending=0 | 56702.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:38:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=31940671, GPU certified nonviolations=31940590, unique transferred candidates=25818, exact=25802, unknown=0, pending=0 | 56675.81 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=31998015, GPU certified nonviolations=31997934, unique transferred candidates=25862, exact=25854, unknown=0, pending=0 | 56659.83 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=32055359, GPU certified nonviolations=32055278, unique transferred candidates=25918, exact=25910, unknown=0, pending=0 | 56662.42 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=32112703, GPU certified nonviolations=32112622, unique transferred candidates=25958, exact=25946, unknown=0, pending=0 | 56655.92 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=32170047, GPU certified nonviolations=32169966, unique transferred candidates=25993, exact=25982, unknown=0, pending=0 | 56622.19 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=32227391, GPU certified nonviolations=32227309, unique transferred candidates=26050, exact=26041, unknown=0, pending=0 | 56605.12 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=32284735, GPU certified nonviolations=32284653, unique transferred candidates=26098, exact=26090, unknown=0, pending=0 | 56615.04 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=32342079, GPU certified nonviolations=32341997, unique transferred candidates=26146, exact=26134, unknown=0, pending=0 | 56594.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=32399423, GPU certified nonviolations=32399340, unique transferred candidates=26184, exact=26175, unknown=0, pending=0 | 56566.95 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=32456767, GPU certified nonviolations=32456684, unique transferred candidates=26240, exact=26229, unknown=0, pending=0 | 56587.20 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=32514111, GPU certified nonviolations=32514028, unique transferred candidates=26280, exact=26268, unknown=0, pending=0 | 56580.85 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=32571455, GPU certified nonviolations=32571372, unique transferred candidates=26320, exact=26310, unknown=0, pending=0 | 56557.66 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=32628799, GPU certified nonviolations=32628716, unique transferred candidates=26373, exact=26365, unknown=0, pending=0 | 56577.75 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=32686143, GPU certified nonviolations=32686060, unique transferred candidates=26421, exact=26409, unknown=0, pending=0 | 56589.98 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=32743487, GPU certified nonviolations=32743404, unique transferred candidates=26469, exact=26453, unknown=0, pending=0 | 56592.80 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=32800831, GPU certified nonviolations=32800748, unique transferred candidates=26498, exact=26481, unknown=0, pending=0 | 56559.98 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=32858175, GPU certified nonviolations=32858092, unique transferred candidates=26561, exact=26551, unknown=0, pending=0 | 56578.38 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=32915519, GPU certified nonviolations=32915436, unique transferred candidates=26601, exact=26589, unknown=0, pending=0 | 56586.27 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=32972863, GPU certified nonviolations=32972780, unique transferred candidates=26649, exact=26639, unknown=0, pending=0 | 56563.01 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=33030207, GPU certified nonviolations=33030124, unique transferred candidates=26695, exact=26687, unknown=0, pending=0 | 56586.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=33087551, GPU certified nonviolations=33087468, unique transferred candidates=26751, exact=26737, unknown=0, pending=0 | 56595.92 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=33144895, GPU certified nonviolations=33144812, unique transferred candidates=26790, exact=26774, unknown=0, pending=0 | 56581.51 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=33202239, GPU certified nonviolations=33202156, unique transferred candidates=26824, exact=26808, unknown=0, pending=0 | 56561.69 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=33259583, GPU certified nonviolations=33259500, unique transferred candidates=26883, exact=26875, unknown=0, pending=0 | 56575.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=33316927, GPU certified nonviolations=33316844, unique transferred candidates=26931, exact=26919, unknown=0, pending=0 | 56571.76 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=33374271, GPU certified nonviolations=33374188, unique transferred candidates=26971, exact=26955, unknown=0, pending=0 | 56551.06 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=33431615, GPU certified nonviolations=33431532, unique transferred candidates=27017, exact=27009, unknown=0, pending=0 | 56543.06 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=33488959, GPU certified nonviolations=33488876, unique transferred candidates=27073, exact=27063, unknown=0, pending=0 | 56550.16 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=33546303, GPU certified nonviolations=33546220, unique transferred candidates=27113, exact=27101, unknown=0, pending=0 | 56555.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=33603647, GPU certified nonviolations=33603564, unique transferred candidates=27147, exact=27137, unknown=0, pending=0 | 56537.33 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=33660991, GPU certified nonviolations=33660908, unique transferred candidates=27203, exact=27195, unknown=0, pending=0 | 56553.92 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=33718335, GPU certified nonviolations=33718252, unique transferred candidates=27251, exact=27243, unknown=0, pending=0 | 56559.90 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=33775679, GPU certified nonviolations=33775596, unique transferred candidates=27299, exact=27284, unknown=0, pending=0 | 56541.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=33833023, GPU certified nonviolations=33832940, unique transferred candidates=27334, exact=27326, unknown=0, pending=0 | 56528.20 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=33890367, GPU certified nonviolations=33890284, unique transferred candidates=27390, exact=27381, unknown=0, pending=0 | 56547.75 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=33947711, GPU certified nonviolations=33947628, unique transferred candidates=27430, exact=27420, unknown=0, pending=0 | 56546.08 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:37+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=33955903, GPU certified nonviolations=33955820, unique transferred candidates=27438, exact=27430, unknown=0, pending=0 | 56503.00 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=34005055, GPU certified nonviolations=34004972, unique transferred candidates=27470, exact=27462, unknown=0, pending=0 | 56513.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=34062399, GPU certified nonviolations=34062316, unique transferred candidates=27522, exact=27514, unknown=0, pending=0 | 56517.46 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=34119743, GPU certified nonviolations=34119660, unique transferred candidates=27570, exact=27558, unknown=0, pending=0 | 56533.55 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=34177087, GPU certified nonviolations=34177004, unique transferred candidates=27618, exact=27604, unknown=0, pending=0 | 56525.64 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=34234431, GPU certified nonviolations=34234348, unique transferred candidates=27646, exact=27630, unknown=0, pending=0 | 56503.13 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=34291775, GPU certified nonviolations=34291692, unique transferred candidates=27708, exact=27698, unknown=0, pending=0 | 56510.06 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=34349119, GPU certified nonviolations=34349036, unique transferred candidates=27748, exact=27735, unknown=0, pending=0 | 56521.08 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=34406463, GPU certified nonviolations=34406380, unique transferred candidates=27796, exact=27788, unknown=0, pending=0 | 56492.77 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=34463807, GPU certified nonviolations=34463724, unique transferred candidates=27842, exact=27834, unknown=0, pending=0 | 56513.05 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=34521151, GPU certified nonviolations=34521068, unique transferred candidates=27898, exact=27886, unknown=0, pending=0 | 56521.74 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=34578495, GPU certified nonviolations=34578412, unique transferred candidates=27938, exact=27925, unknown=0, pending=0 | 56516.20 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=34635839, GPU certified nonviolations=34635756, unique transferred candidates=27971, exact=27955, unknown=0, pending=0 | 56504.52 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=34693183, GPU certified nonviolations=34693100, unique transferred candidates=28032, exact=28024, unknown=0, pending=0 | 56518.79 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=34750527, GPU certified nonviolations=34750444, unique transferred candidates=28080, exact=28068, unknown=0, pending=0 | 56524.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=34807871, GPU certified nonviolations=34807788, unique transferred candidates=28120, exact=28104, unknown=0, pending=0 | 56507.92 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=34865215, GPU certified nonviolations=34865131, unique transferred candidates=28168, exact=28160, unknown=0, pending=0 | 56502.11 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=34922559, GPU certified nonviolations=34922475, unique transferred candidates=28224, exact=28212, unknown=0, pending=0 | 56506.37 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=34979903, GPU certified nonviolations=34979819, unique transferred candidates=28264, exact=28252, unknown=0, pending=0 | 56505.47 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=35037247, GPU certified nonviolations=35037163, unique transferred candidates=28301, exact=28288, unknown=0, pending=0 | 56483.32 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=35094591, GPU certified nonviolations=35094507, unique transferred candidates=28357, exact=28348, unknown=0, pending=0 | 56500.24 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=35151935, GPU certified nonviolations=35151851, unique transferred candidates=28405, exact=28394, unknown=0, pending=0 | 56507.61 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:39:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=35209279, GPU certified nonviolations=35209195, unique transferred candidates=28453, exact=28437, unknown=0, pending=0 | 56485.40 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=35266623, GPU certified nonviolations=35266539, unique transferred candidates=28491, exact=28483, unknown=0, pending=0 | 56461.02 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=35323967, GPU certified nonviolations=35323883, unique transferred candidates=28547, exact=28538, unknown=0, pending=0 | 56482.85 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=35381311, GPU certified nonviolations=35381227, unique transferred candidates=28587, exact=28579, unknown=0, pending=0 | 56491.13 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=35438655, GPU certified nonviolations=35438571, unique transferred candidates=28627, exact=28613, unknown=0, pending=0 | 56456.76 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=35495999, GPU certified nonviolations=35495915, unique transferred candidates=28680, exact=28672, unknown=0, pending=0 | 56476.67 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=35553343, GPU certified nonviolations=35553259, unique transferred candidates=28728, exact=28716, unknown=0, pending=0 | 56490.79 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=35610687, GPU certified nonviolations=35610603, unique transferred candidates=28776, exact=28760, unknown=0, pending=0 | 56484.51 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=35668031, GPU certified nonviolations=35667947, unique transferred candidates=28816, exact=28808, unknown=0, pending=0 | 56438.53 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=35725375, GPU certified nonviolations=35725291, unique transferred candidates=28872, exact=28860, unknown=0, pending=0 | 56455.18 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=35782719, GPU certified nonviolations=35782635, unique transferred candidates=28912, exact=28900, unknown=0, pending=0 | 56463.33 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=35840063, GPU certified nonviolations=35839979, unique transferred candidates=28960, exact=28947, unknown=0, pending=0 | 56427.67 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=35897407, GPU certified nonviolations=35897323, unique transferred candidates=29005, exact=28997, unknown=0, pending=0 | 56437.57 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=35954751, GPU certified nonviolations=35954667, unique transferred candidates=29061, exact=29048, unknown=0, pending=0 | 56449.47 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=36012095, GPU certified nonviolations=36012011, unique transferred candidates=29101, exact=29086, unknown=0, pending=0 | 56450.77 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=36069439, GPU certified nonviolations=36069355, unique transferred candidates=29134, exact=29118, unknown=0, pending=0 | 56427.22 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=36126783, GPU certified nonviolations=36126699, unique transferred candidates=29194, exact=29186, unknown=0, pending=0 | 56437.94 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=36184127, GPU certified nonviolations=36184043, unique transferred candidates=29242, exact=29230, unknown=0, pending=0 | 56441.06 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=36241471, GPU certified nonviolations=36241387, unique transferred candidates=29282, exact=29266, unknown=0, pending=0 | 56430.16 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=36298815, GPU certified nonviolations=36298730, unique transferred candidates=29329, exact=29321, unknown=0, pending=0 | 56411.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=36356159, GPU certified nonviolations=36356074, unique transferred candidates=29385, exact=29375, unknown=0, pending=0 | 56420.44 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=36413503, GPU certified nonviolations=36413418, unique transferred candidates=29425, exact=29411, unknown=0, pending=0 | 56421.36 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=36470847, GPU certified nonviolations=36470762, unique transferred candidates=29462, exact=29449, unknown=0, pending=0 | 56402.51 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=36528191, GPU certified nonviolations=36528106, unique transferred candidates=29518, exact=29506, unknown=0, pending=0 | 56400.39 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=36585535, GPU certified nonviolations=36585450, unique transferred candidates=29566, exact=29558, unknown=0, pending=0 | 56403.65 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=36642879, GPU certified nonviolations=36642794, unique transferred candidates=29614, exact=29599, unknown=0, pending=0 | 56381.34 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=36700223, GPU certified nonviolations=36700138, unique transferred candidates=29652, exact=29644, unknown=0, pending=0 | 56358.74 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=36757567, GPU certified nonviolations=36757482, unique transferred candidates=29707, exact=29697, unknown=0, pending=0 | 56370.85 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=36814911, GPU certified nonviolations=36814826, unique transferred candidates=29747, exact=29738, unknown=0, pending=0 | 56367.46 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=36872255, GPU certified nonviolations=36872170, unique transferred candidates=29787, exact=29779, unknown=0, pending=0 | 56333.69 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=36929599, GPU certified nonviolations=36929514, unique transferred candidates=29840, exact=29832, unknown=0, pending=0 | 56354.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=36986943, GPU certified nonviolations=36986858, unique transferred candidates=29888, exact=29876, unknown=0, pending=0 | 56364.95 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=37044287, GPU certified nonviolations=37044202, unique transferred candidates=29933, exact=29917, unknown=0, pending=0 | 56350.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=37101631, GPU certified nonviolations=37101546, unique transferred candidates=29973, exact=29961, unknown=0, pending=0 | 56320.40 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=37158975, GPU certified nonviolations=37158890, unique transferred candidates=30029, exact=30020, unknown=0, pending=0 | 56329.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=37216319, GPU certified nonviolations=37216234, unique transferred candidates=30069, exact=30057, unknown=0, pending=0 | 56336.79 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:37+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=37224511, GPU certified nonviolations=37224426, unique transferred candidates=30077, exact=30069, unknown=0, pending=0 | 56309.81 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=37273663, GPU certified nonviolations=37273578, unique transferred candidates=30117, exact=30109, unknown=0, pending=0 | 56316.73 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=37331007, GPU certified nonviolations=37330922, unique transferred candidates=30161, exact=30153, unknown=0, pending=0 | 56335.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=37388351, GPU certified nonviolations=37388266, unique transferred candidates=30217, exact=30205, unknown=0, pending=0 | 56365.37 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=37445695, GPU certified nonviolations=37445610, unique transferred candidates=30257, exact=30242, unknown=0, pending=0 | 56371.89 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=37503039, GPU certified nonviolations=37502954, unique transferred candidates=30290, exact=30274, unknown=0, pending=0 | 56347.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=37560383, GPU certified nonviolations=37560298, unique transferred candidates=30348, exact=30340, unknown=0, pending=0 | 56364.13 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=37617727, GPU certified nonviolations=37617642, unique transferred candidates=30396, exact=30382, unknown=0, pending=0 | 56385.94 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=37675071, GPU certified nonviolations=37674986, unique transferred candidates=30436, exact=30420, unknown=0, pending=0 | 56366.42 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=37732415, GPU certified nonviolations=37732330, unique transferred candidates=30482, exact=30474, unknown=0, pending=0 | 56354.26 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=37789759, GPU certified nonviolations=37789674, unique transferred candidates=30538, exact=30529, unknown=0, pending=0 | 56373.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=37847103, GPU certified nonviolations=37847018, unique transferred candidates=30578, exact=30564, unknown=0, pending=0 | 56385.62 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=37904447, GPU certified nonviolations=37904362, unique transferred candidates=30615, exact=30602, unknown=0, pending=0 | 56370.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=37961791, GPU certified nonviolations=37961706, unique transferred candidates=30671, exact=30663, unknown=0, pending=0 | 56394.27 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=38019135, GPU certified nonviolations=38019050, unique transferred candidates=30718, exact=30710, unknown=0, pending=0 | 56417.03 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=38076479, GPU certified nonviolations=38076394, unique transferred candidates=30766, exact=30750, unknown=0, pending=0 | 56414.24 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=38133823, GPU certified nonviolations=38133738, unique transferred candidates=30802, exact=30794, unknown=0, pending=0 | 56392.38 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=38191167, GPU certified nonviolations=38191082, unique transferred candidates=30858, exact=30850, unknown=0, pending=0 | 56419.88 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=38248511, GPU certified nonviolations=38248426, unique transferred candidates=30898, exact=30890, unknown=0, pending=0 | 56435.18 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=38305855, GPU certified nonviolations=38305770, unique transferred candidates=30938, exact=30930, unknown=0, pending=0 | 56420.77 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=38363199, GPU certified nonviolations=38363113, unique transferred candidates=30992, exact=30984, unknown=0, pending=0 | 56444.04 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=38420543, GPU certified nonviolations=38420457, unique transferred candidates=31040, exact=31028, unknown=0, pending=0 | 56461.45 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=38477887, GPU certified nonviolations=38477801, unique transferred candidates=31088, exact=31073, unknown=0, pending=0 | 56459.04 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=38535231, GPU certified nonviolations=38535145, unique transferred candidates=31117, exact=31100, unknown=0, pending=0 | 56440.05 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:40:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=38592575, GPU certified nonviolations=38592489, unique transferred candidates=31180, exact=31172, unknown=0, pending=0 | 56469.26 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=38649919, GPU certified nonviolations=38649833, unique transferred candidates=31220, exact=31208, unknown=0, pending=0 | 56475.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=38707263, GPU certified nonviolations=38707177, unique transferred candidates=31268, exact=31260, unknown=0, pending=0 | 56451.10 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=38764607, GPU certified nonviolations=38764521, unique transferred candidates=31314, exact=31306, unknown=0, pending=0 | 56469.65 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=38821951, GPU certified nonviolations=38821865, unique transferred candidates=31370, exact=31359, unknown=0, pending=0 | 56490.27 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=38879295, GPU certified nonviolations=38879209, unique transferred candidates=31410, exact=31397, unknown=0, pending=0 | 56492.93 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=38936639, GPU certified nonviolations=38936553, unique transferred candidates=31443, exact=31427, unknown=0, pending=0 | 56480.93 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=38993983, GPU certified nonviolations=38993897, unique transferred candidates=31503, exact=31495, unknown=0, pending=0 | 56502.98 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=39051327, GPU certified nonviolations=39051241, unique transferred candidates=31551, exact=31539, unknown=0, pending=0 | 56510.52 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=39108671, GPU certified nonviolations=39108585, unique transferred candidates=31591, exact=31579, unknown=0, pending=0 | 56498.27 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=39166015, GPU certified nonviolations=39165929, unique transferred candidates=31638, exact=31630, unknown=0, pending=0 | 56503.01 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=39223359, GPU certified nonviolations=39223273, unique transferred candidates=31694, exact=31683, unknown=0, pending=0 | 56524.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=39280703, GPU certified nonviolations=39280617, unique transferred candidates=31734, exact=31722, unknown=0, pending=0 | 56533.81 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=39338047, GPU certified nonviolations=39337961, unique transferred candidates=31770, exact=31758, unknown=0, pending=0 | 56524.56 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=39395391, GPU certified nonviolations=39395305, unique transferred candidates=31826, exact=31818, unknown=0, pending=0 | 56539.13 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=39452735, GPU certified nonviolations=39452649, unique transferred candidates=31874, exact=31866, unknown=0, pending=0 | 56555.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=39510079, GPU certified nonviolations=39509993, unique transferred candidates=31922, exact=31907, unknown=0, pending=0 | 56550.14 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=39567423, GPU certified nonviolations=39567337, unique transferred candidates=31959, exact=31951, unknown=0, pending=0 | 56536.53 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=39624767, GPU certified nonviolations=39624681, unique transferred candidates=32015, exact=32006, unknown=0, pending=0 | 56554.11 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=39682111, GPU certified nonviolations=39682025, unique transferred candidates=32055, exact=32047, unknown=0, pending=0 | 56564.66 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=39739455, GPU certified nonviolations=39739369, unique transferred candidates=32095, exact=32087, unknown=0, pending=0 | 56549.11 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=39796799, GPU certified nonviolations=39796713, unique transferred candidates=32149, exact=32141, unknown=0, pending=0 | 56561.26 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=39854143, GPU certified nonviolations=39854057, unique transferred candidates=32197, exact=32185, unknown=0, pending=0 | 56586.94 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=39911487, GPU certified nonviolations=39911401, unique transferred candidates=32245, exact=32231, unknown=0, pending=0 | 56590.53 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=39968831, GPU certified nonviolations=39968745, unique transferred candidates=32283, exact=32275, unknown=0, pending=0 | 56565.57 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=40026175, GPU certified nonviolations=40026089, unique transferred candidates=32339, exact=32331, unknown=0, pending=0 | 56583.36 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=40083519, GPU certified nonviolations=40083433, unique transferred candidates=32379, exact=32367, unknown=0, pending=0 | 56601.46 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=40140863, GPU certified nonviolations=40140777, unique transferred candidates=32427, exact=32416, unknown=0, pending=0 | 56581.61 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=40198207, GPU certified nonviolations=40198121, unique transferred candidates=32471, exact=32463, unknown=0, pending=0 | 56602.91 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=40255551, GPU certified nonviolations=40255465, unique transferred candidates=32527, exact=32515, unknown=0, pending=0 | 56626.17 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=40312895, GPU certified nonviolations=40312809, unique transferred candidates=32567, exact=32551, unknown=0, pending=0 | 56631.73 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=40370239, GPU certified nonviolations=40370153, unique transferred candidates=32600, exact=32584, unknown=0, pending=0 | 56614.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=40427583, GPU certified nonviolations=40427497, unique transferred candidates=32659, exact=32651, unknown=0, pending=0 | 56630.93 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=40484927, GPU certified nonviolations=40484841, unique transferred candidates=32707, exact=32695, unknown=0, pending=0 | 56647.97 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=40542271, GPU certified nonviolations=40542185, unique transferred candidates=32747, exact=32731, unknown=0, pending=0 | 56638.15 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=40599615, GPU certified nonviolations=40599529, unique transferred candidates=32791, exact=32783, unknown=0, pending=0 | 56629.86 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=40656959, GPU certified nonviolations=40656873, unique transferred candidates=32847, exact=32837, unknown=0, pending=0 | 56644.57 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=40714303, GPU certified nonviolations=40714217, unique transferred candidates=32887, exact=32871, unknown=0, pending=0 | 56651.46 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=40771647, GPU certified nonviolations=40771561, unique transferred candidates=32926, exact=32911, unknown=0, pending=0 | 56641.00 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=40828991, GPU certified nonviolations=40828905, unique transferred candidates=32981, exact=32973, unknown=0, pending=0 | 56651.94 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:37+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=40837183, GPU certified nonviolations=40837097, unique transferred candidates=32989, exact=32981, unknown=0, pending=0 | 56633.37 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=40886335, GPU certified nonviolations=40886249, unique transferred candidates=33029, exact=33021, unknown=0, pending=0 | 56667.93 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=40943679, GPU certified nonviolations=40943593, unique transferred candidates=33077, exact=33061, unknown=0, pending=0 | 56665.37 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=41001023, GPU certified nonviolations=41000937, unique transferred candidates=33114, exact=33106, unknown=0, pending=0 | 56647.87 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=41058367, GPU certified nonviolations=41058281, unique transferred candidates=33170, exact=33158, unknown=0, pending=0 | 56663.00 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=41115711, GPU certified nonviolations=41115625, unique transferred candidates=33210, exact=33201, unknown=0, pending=0 | 56674.56 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=41173055, GPU certified nonviolations=41172969, unique transferred candidates=33250, exact=33242, unknown=0, pending=0 | 56656.97 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=41230399, GPU certified nonviolations=41230313, unique transferred candidates=33305, exact=33297, unknown=0, pending=0 | 56668.51 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=41287743, GPU certified nonviolations=41287657, unique transferred candidates=33353, exact=33337, unknown=0, pending=0 | 56680.45 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=41345087, GPU certified nonviolations=41345001, unique transferred candidates=33401, exact=33389, unknown=0, pending=0 | 56681.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=41402431, GPU certified nonviolations=41402345, unique transferred candidates=33438, exact=33431, unknown=0, pending=0 | 56655.22 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=41459775, GPU certified nonviolations=41459689, unique transferred candidates=33494, exact=33483, unknown=0, pending=0 | 56683.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:41:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=41517119, GPU certified nonviolations=41517033, unique transferred candidates=33534, exact=33522, unknown=0, pending=0 | 56700.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=41574463, GPU certified nonviolations=41574377, unique transferred candidates=33582, exact=33571, unknown=0, pending=0 | 55776.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=41631807, GPU certified nonviolations=41631721, unique transferred candidates=33626, exact=33618, unknown=0, pending=0 | 55798.44 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=41689151, GPU certified nonviolations=41689065, unique transferred candidates=33682, exact=33669, unknown=0, pending=0 | 55811.65 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=41746495, GPU certified nonviolations=41746409, unique transferred candidates=33722, exact=33706, unknown=0, pending=0 | 55798.23 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=41803839, GPU certified nonviolations=41803753, unique transferred candidates=33755, exact=33738, unknown=0, pending=0 | 55771.19 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=41861183, GPU certified nonviolations=41861097, unique transferred candidates=33816, exact=33808, unknown=0, pending=0 | 55788.95 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=41918527, GPU certified nonviolations=41918441, unique transferred candidates=33864, exact=33851, unknown=0, pending=0 | 55802.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=41975871, GPU certified nonviolations=41975785, unique transferred candidates=33904, exact=33888, unknown=0, pending=0 | 55792.37 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=42033215, GPU certified nonviolations=42033129, unique transferred candidates=33947, exact=33939, unknown=0, pending=0 | 55790.35 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=42090559, GPU certified nonviolations=42090473, unique transferred candidates=34003, exact=33991, unknown=0, pending=0 | 55809.33 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=42147903, GPU certified nonviolations=42147817, unique transferred candidates=34043, exact=34031, unknown=0, pending=0 | 55816.51 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=42205247, GPU certified nonviolations=42205161, unique transferred candidates=34083, exact=34067, unknown=0, pending=0 | 55804.38 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=42262591, GPU certified nonviolations=42262505, unique transferred candidates=34139, exact=34131, unknown=0, pending=0 | 55826.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=42319935, GPU certified nonviolations=42319849, unique transferred candidates=34187, exact=34177, unknown=0, pending=0 | 55837.72 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=42377279, GPU certified nonviolations=42377193, unique transferred candidates=34235, exact=34219, unknown=0, pending=0 | 55836.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=42434623, GPU certified nonviolations=42434537, unique transferred candidates=34272, exact=34264, unknown=0, pending=0 | 55823.11 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=42491967, GPU certified nonviolations=42491881, unique transferred candidates=34327, exact=34317, unknown=0, pending=0 | 55836.72 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=42549311, GPU certified nonviolations=42549225, unique transferred candidates=34367, exact=34359, unknown=0, pending=0 | 55835.66 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=42606655, GPU certified nonviolations=42606569, unique transferred candidates=34407, exact=34399, unknown=0, pending=0 | 55823.36 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=42663999, GPU certified nonviolations=42663912, unique transferred candidates=34463, exact=34455, unknown=0, pending=0 | 55843.16 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=42721343, GPU certified nonviolations=42721256, unique transferred candidates=34511, exact=34498, unknown=0, pending=0 | 55855.12 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=42778687, GPU certified nonviolations=42778600, unique transferred candidates=34559, exact=34546, unknown=0, pending=0 | 55847.33 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=42836031, GPU certified nonviolations=42835944, unique transferred candidates=34588, exact=34571, unknown=0, pending=0 | 55837.73 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=42893375, GPU certified nonviolations=42893288, unique transferred candidates=34651, exact=34643, unknown=0, pending=0 | 55854.37 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=42950719, GPU certified nonviolations=42950632, unique transferred candidates=34691, exact=34680, unknown=0, pending=0 | 55862.37 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=43008063, GPU certified nonviolations=43007976, unique transferred candidates=34739, exact=34730, unknown=0, pending=0 | 55845.37 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=43065407, GPU certified nonviolations=43065320, unique transferred candidates=34782, exact=34774, unknown=0, pending=0 | 55864.40 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=43122751, GPU certified nonviolations=43122664, unique transferred candidates=34838, exact=34826, unknown=0, pending=0 | 55880.15 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=43180095, GPU certified nonviolations=43180008, unique transferred candidates=34878, exact=34864, unknown=0, pending=0 | 55888.48 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=43237439, GPU certified nonviolations=43237352, unique transferred candidates=34911, exact=34895, unknown=0, pending=0 | 55876.26 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=43294783, GPU certified nonviolations=43294696, unique transferred candidates=34972, exact=34964, unknown=0, pending=0 | 55899.69 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=43352127, GPU certified nonviolations=43352040, unique transferred candidates=35020, exact=35008, unknown=0, pending=0 | 55912.67 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=43409471, GPU certified nonviolations=43409384, unique transferred candidates=35060, exact=35047, unknown=0, pending=0 | 55897.28 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=43466815, GPU certified nonviolations=43466728, unique transferred candidates=35105, exact=35097, unknown=0, pending=0 | 55896.02 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=43524159, GPU certified nonviolations=43524072, unique transferred candidates=35161, exact=35150, unknown=0, pending=0 | 55917.27 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=43581503, GPU certified nonviolations=43581416, unique transferred candidates=35201, exact=35189, unknown=0, pending=0 | 55923.40 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=43638847, GPU certified nonviolations=43638760, unique transferred candidates=35236, exact=35225, unknown=0, pending=0 | 55907.14 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:37+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=43647039, GPU certified nonviolations=43646952, unique transferred candidates=35244, exact=35236, unknown=0, pending=0 | 55874.37 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=43696191, GPU certified nonviolations=43696104, unique transferred candidates=35290, exact=35282, unknown=0, pending=0 | 55914.26 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=43753535, GPU certified nonviolations=43753448, unique transferred candidates=35338, exact=35330, unknown=0, pending=0 | 55919.57 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=43810879, GPU certified nonviolations=43810792, unique transferred candidates=35386, exact=35374, unknown=0, pending=0 | 55912.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=43868223, GPU certified nonviolations=43868136, unique transferred candidates=35423, exact=35415, unknown=0, pending=0 | 55900.95 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=43925567, GPU certified nonviolations=43925479, unique transferred candidates=35480, exact=35468, unknown=0, pending=0 | 55918.65 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=43982911, GPU certified nonviolations=43982823, unique transferred candidates=35520, exact=35512, unknown=0, pending=0 | 55921.74 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=44040255, GPU certified nonviolations=44040167, unique transferred candidates=35560, exact=35549, unknown=0, pending=0 | 55908.75 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=44097599, GPU certified nonviolations=44097511, unique transferred candidates=35613, exact=35605, unknown=0, pending=0 | 55924.34 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=44154943, GPU certified nonviolations=44154855, unique transferred candidates=35661, exact=35648, unknown=0, pending=0 | 55940.23 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=44212287, GPU certified nonviolations=44212199, unique transferred candidates=35709, exact=35696, unknown=0, pending=0 | 55936.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=44269631, GPU certified nonviolations=44269543, unique transferred candidates=35746, exact=35738, unknown=0, pending=0 | 55907.65 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=44326975, GPU certified nonviolations=44326887, unique transferred candidates=35802, exact=35794, unknown=0, pending=0 | 55930.94 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=44384319, GPU certified nonviolations=44384231, unique transferred candidates=35842, exact=35830, unknown=0, pending=0 | 55945.11 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=44441663, GPU certified nonviolations=44441575, unique transferred candidates=35890, exact=35878, unknown=0, pending=0 | 55922.62 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=44499007, GPU certified nonviolations=44498919, unique transferred candidates=35936, exact=35927, unknown=0, pending=0 | 55944.59 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=44556351, GPU certified nonviolations=44556263, unique transferred candidates=35992, exact=35980, unknown=0, pending=0 | 55960.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=44613695, GPU certified nonviolations=44613607, unique transferred candidates=36032, exact=36020, unknown=0, pending=0 | 55956.02 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=44671039, GPU certified nonviolations=44670951, unique transferred candidates=36065, exact=36049, unknown=0, pending=0 | 55940.19 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=44728383, GPU certified nonviolations=44728295, unique transferred candidates=36123, exact=36115, unknown=0, pending=0 | 55955.72 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=44785727, GPU certified nonviolations=44785639, unique transferred candidates=36171, exact=36159, unknown=0, pending=0 | 55957.57 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=44843071, GPU certified nonviolations=44842983, unique transferred candidates=36211, exact=36198, unknown=0, pending=0 | 55943.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=44900415, GPU certified nonviolations=44900327, unique transferred candidates=36255, exact=36247, unknown=0, pending=0 | 55933.06 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:42:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=44957759, GPU certified nonviolations=44957671, unique transferred candidates=36311, exact=36300, unknown=0, pending=0 | 55951.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=45015103, GPU certified nonviolations=45015015, unique transferred candidates=36351, exact=36338, unknown=0, pending=0 | 55956.52 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=45072447, GPU certified nonviolations=45072359, unique transferred candidates=36390, exact=36375, unknown=0, pending=0 | 55943.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=45129791, GPU certified nonviolations=45129703, unique transferred candidates=36446, exact=36438, unknown=0, pending=0 | 55958.11 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=45187135, GPU certified nonviolations=45187047, unique transferred candidates=36494, exact=36486, unknown=0, pending=0 | 55966.74 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=45244479, GPU certified nonviolations=45244391, unique transferred candidates=36542, exact=36530, unknown=0, pending=0 | 55957.70 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=45301823, GPU certified nonviolations=45301734, unique transferred candidates=36579, exact=36569, unknown=0, pending=0 | 55950.17 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=45359167, GPU certified nonviolations=45359078, unique transferred candidates=36635, exact=36624, unknown=0, pending=0 | 55970.34 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=45416511, GPU certified nonviolations=45416422, unique transferred candidates=36675, exact=36666, unknown=0, pending=0 | 55980.06 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=45473855, GPU certified nonviolations=45473766, unique transferred candidates=36715, exact=36707, unknown=0, pending=0 | 55967.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=45531199, GPU certified nonviolations=45531110, unique transferred candidates=36767, exact=36759, unknown=0, pending=0 | 55978.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=45588543, GPU certified nonviolations=45588454, unique transferred candidates=36815, exact=36803, unknown=0, pending=0 | 55992.56 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=45645887, GPU certified nonviolations=45645798, unique transferred candidates=36863, exact=36848, unknown=0, pending=0 | 55989.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=45703231, GPU certified nonviolations=45703142, unique transferred candidates=36892, exact=36875, unknown=0, pending=0 | 55974.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=45760575, GPU certified nonviolations=45760486, unique transferred candidates=36954, exact=36946, unknown=0, pending=0 | 55991.88 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=45817919, GPU certified nonviolations=45817830, unique transferred candidates=36994, exact=36982, unknown=0, pending=0 | 55994.05 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=45875263, GPU certified nonviolations=45875174, unique transferred candidates=37042, exact=37034, unknown=0, pending=0 | 55971.05 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=45932607, GPU certified nonviolations=45932518, unique transferred candidates=37088, exact=37081, unknown=0, pending=0 | 55980.47 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=45989951, GPU certified nonviolations=45989862, unique transferred candidates=37144, exact=37131, unknown=0, pending=0 | 55997.70 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=46047295, GPU certified nonviolations=46047206, unique transferred candidates=37184, exact=37172, unknown=0, pending=0 | 55995.35 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=46104639, GPU certified nonviolations=46104550, unique transferred candidates=37217, exact=37201, unknown=0, pending=0 | 55975.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=46161983, GPU certified nonviolations=46161893, unique transferred candidates=37279, exact=37271, unknown=0, pending=0 | 55991.12 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=46219327, GPU certified nonviolations=46219237, unique transferred candidates=37327, exact=37315, unknown=0, pending=0 | 56003.69 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=46276671, GPU certified nonviolations=46276581, unique transferred candidates=37367, exact=37354, unknown=0, pending=0 | 55987.72 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=46334015, GPU certified nonviolations=46333924, unique transferred candidates=37411, exact=37403, unknown=0, pending=0 | 55989.75 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=46391359, GPU certified nonviolations=46391268, unique transferred candidates=37467, exact=37456, unknown=0, pending=0 | 56008.78 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=46448703, GPU certified nonviolations=46448612, unique transferred candidates=37507, exact=37495, unknown=0, pending=0 | 56009.12 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=46506047, GPU certified nonviolations=46505956, unique transferred candidates=37544, exact=37531, unknown=0, pending=0 | 55995.89 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=46563391, GPU certified nonviolations=46563300, unique transferred candidates=37600, exact=37592, unknown=0, pending=0 | 56010.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=46620735, GPU certified nonviolations=46620644, unique transferred candidates=37648, exact=37638, unknown=0, pending=0 | 56017.32 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=46678079, GPU certified nonviolations=46677988, unique transferred candidates=37696, exact=37684, unknown=0, pending=0 | 56011.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=46735423, GPU certified nonviolations=46735332, unique transferred candidates=37730, exact=37722, unknown=0, pending=0 | 55986.89 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=46792767, GPU certified nonviolations=46792676, unique transferred candidates=37786, exact=37777, unknown=0, pending=0 | 56001.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=46850111, GPU certified nonviolations=46850020, unique transferred candidates=37826, exact=37818, unknown=0, pending=0 | 56010.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=46907455, GPU certified nonviolations=46907364, unique transferred candidates=37866, exact=37858, unknown=0, pending=0 | 55999.00 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=46964799, GPU certified nonviolations=46964708, unique transferred candidates=37918, exact=37910, unknown=0, pending=0 | 56018.00 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=47022143, GPU certified nonviolations=47022052, unique transferred candidates=37966, exact=37954, unknown=0, pending=0 | 56025.42 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=47079487, GPU certified nonviolations=47079396, unique transferred candidates=38014, exact=38002, unknown=0, pending=0 | 56017.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:37+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=47095871, GPU certified nonviolations=47095780, unique transferred candidates=38022, exact=38014, unknown=0, pending=0 | 55988.77 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=47136831, GPU certified nonviolations=47136740, unique transferred candidates=38043, exact=38026, unknown=0, pending=0 | 55996.88 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=47194175, GPU certified nonviolations=47194084, unique transferred candidates=38105, exact=38097, unknown=0, pending=0 | 56010.87 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=47251519, GPU certified nonviolations=47251428, unique transferred candidates=38145, exact=38133, unknown=0, pending=0 | 56015.38 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=47308863, GPU certified nonviolations=47308772, unique transferred candidates=38193, exact=38185, unknown=0, pending=0 | 55999.89 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=47366207, GPU certified nonviolations=47366116, unique transferred candidates=38238, exact=38231, unknown=0, pending=0 | 56016.52 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=47423551, GPU certified nonviolations=47423460, unique transferred candidates=38294, exact=38282, unknown=0, pending=0 | 56027.62 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=47480895, GPU certified nonviolations=47480804, unique transferred candidates=38334, exact=38321, unknown=0, pending=0 | 56025.80 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=47538239, GPU certified nonviolations=47538148, unique transferred candidates=38367, exact=38351, unknown=0, pending=0 | 56006.51 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=47595583, GPU certified nonviolations=47595492, unique transferred candidates=38426, exact=38417, unknown=0, pending=0 | 56019.42 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=47652927, GPU certified nonviolations=47652836, unique transferred candidates=38474, exact=38462, unknown=0, pending=0 | 56027.15 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=47710271, GPU certified nonviolations=47710180, unique transferred candidates=38514, exact=38498, unknown=0, pending=0 | 56007.70 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=47767615, GPU certified nonviolations=47767524, unique transferred candidates=38555, exact=38547, unknown=0, pending=0 | 55996.39 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=47824959, GPU certified nonviolations=47824868, unique transferred candidates=38611, exact=38603, unknown=0, pending=0 | 56016.62 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=47882303, GPU certified nonviolations=47882212, unique transferred candidates=38651, exact=38639, unknown=0, pending=0 | 56024.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=47939647, GPU certified nonviolations=47939556, unique transferred candidates=38689, exact=38673, unknown=0, pending=0 | 56007.40 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=47996991, GPU certified nonviolations=47996900, unique transferred candidates=38746, exact=38738, unknown=0, pending=0 | 56022.06 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=48054335, GPU certified nonviolations=48054244, unique transferred candidates=38794, exact=38786, unknown=0, pending=0 | 56038.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=48111679, GPU certified nonviolations=48111588, unique transferred candidates=38842, exact=38826, unknown=0, pending=0 | 56033.78 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=48169023, GPU certified nonviolations=48168932, unique transferred candidates=38880, exact=38872, unknown=0, pending=0 | 56012.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=48226367, GPU certified nonviolations=48226276, unique transferred candidates=38936, exact=38925, unknown=0, pending=0 | 56033.80 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=48283711, GPU certified nonviolations=48283620, unique transferred candidates=38976, exact=38967, unknown=0, pending=0 | 56036.59 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:43:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=48341055, GPU certified nonviolations=48340964, unique transferred candidates=39016, exact=39004, unknown=0, pending=0 | 56019.01 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=48398399, GPU certified nonviolations=48398308, unique transferred candidates=39068, exact=39060, unknown=0, pending=0 | 56028.36 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=48455743, GPU certified nonviolations=48455652, unique transferred candidates=39116, exact=39102, unknown=0, pending=0 | 56032.93 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=48513087, GPU certified nonviolations=48512996, unique transferred candidates=39164, exact=39151, unknown=0, pending=0 | 56031.77 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=48570431, GPU certified nonviolations=48570340, unique transferred candidates=39193, exact=39176, unknown=0, pending=0 | 56017.63 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=48627775, GPU certified nonviolations=48627683, unique transferred candidates=39257, exact=39248, unknown=0, pending=0 | 56035.92 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=48685119, GPU certified nonviolations=48685027, unique transferred candidates=39297, exact=39284, unknown=0, pending=0 | 56037.51 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=48742463, GPU certified nonviolations=48742371, unique transferred candidates=39345, exact=39333, unknown=0, pending=0 | 56022.00 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=48799807, GPU certified nonviolations=48799715, unique transferred candidates=39391, exact=39383, unknown=0, pending=0 | 56037.99 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=48857151, GPU certified nonviolations=48857059, unique transferred candidates=39447, exact=39432, unknown=0, pending=0 | 56038.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=48914495, GPU certified nonviolations=48914403, unique transferred candidates=39487, exact=39478, unknown=0, pending=0 | 56036.98 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=48971839, GPU certified nonviolations=48971747, unique transferred candidates=39520, exact=39504, unknown=0, pending=0 | 56027.38 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=49029183, GPU certified nonviolations=49029091, unique transferred candidates=39581, exact=39571, unknown=0, pending=0 | 56040.28 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=49086527, GPU certified nonviolations=49086435, unique transferred candidates=39629, exact=39617, unknown=0, pending=0 | 56050.46 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=49143871, GPU certified nonviolations=49143779, unique transferred candidates=39669, exact=39654, unknown=0, pending=0 | 56036.94 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=49201215, GPU certified nonviolations=49201123, unique transferred candidates=39714, exact=39706, unknown=0, pending=0 | 56028.44 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=49258559, GPU certified nonviolations=49258467, unique transferred candidates=39770, exact=39761, unknown=0, pending=0 | 56048.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=49315903, GPU certified nonviolations=49315811, unique transferred candidates=39810, exact=39798, unknown=0, pending=0 | 56052.34 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=49373247, GPU certified nonviolations=49373155, unique transferred candidates=39845, exact=39834, unknown=0, pending=0 | 56036.84 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=49430591, GPU certified nonviolations=49430499, unique transferred candidates=39901, exact=39893, unknown=0, pending=0 | 56048.76 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=49487935, GPU certified nonviolations=49487843, unique transferred candidates=39949, exact=39938, unknown=0, pending=0 | 56055.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=49545279, GPU certified nonviolations=49545187, unique transferred candidates=39997, exact=39981, unknown=0, pending=0 | 56046.88 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=49602623, GPU certified nonviolations=49602531, unique transferred candidates=40033, exact=40025, unknown=0, pending=0 | 56035.78 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=49659967, GPU certified nonviolations=49659875, unique transferred candidates=40089, exact=40078, unknown=0, pending=0 | 56044.61 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=49717311, GPU certified nonviolations=49717219, unique transferred candidates=40129, exact=40121, unknown=0, pending=0 | 56048.86 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=49774655, GPU certified nonviolations=49774563, unique transferred candidates=40169, exact=40161, unknown=0, pending=0 | 56027.33 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=49831999, GPU certified nonviolations=49831907, unique transferred candidates=40222, exact=40214, unknown=0, pending=0 | 56044.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=49889343, GPU certified nonviolations=49889251, unique transferred candidates=40270, exact=40258, unknown=0, pending=0 | 56056.49 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=49946687, GPU certified nonviolations=49946595, unique transferred candidates=40318, exact=40305, unknown=0, pending=0 | 56053.37 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=50004031, GPU certified nonviolations=50003939, unique transferred candidates=40347, exact=40330, unknown=0, pending=0 | 56038.63 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=50061375, GPU certified nonviolations=50061283, unique transferred candidates=40410, exact=40399, unknown=0, pending=0 | 56048.75 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=50118719, GPU certified nonviolations=50118627, unique transferred candidates=40450, exact=40438, unknown=0, pending=0 | 56054.79 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=50176063, GPU certified nonviolations=50175971, unique transferred candidates=40498, exact=40490, unknown=0, pending=0 | 56034.98 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=50233407, GPU certified nonviolations=50233315, unique transferred candidates=40544, exact=40536, unknown=0, pending=0 | 56054.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=50290751, GPU certified nonviolations=50290659, unique transferred candidates=40600, exact=40585, unknown=0, pending=0 | 56060.05 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=50348095, GPU certified nonviolations=50348003, unique transferred candidates=40640, exact=40627, unknown=0, pending=0 | 56055.10 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=50405439, GPU certified nonviolations=50405347, unique transferred candidates=40673, exact=40657, unknown=0, pending=0 | 56043.65 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=50462783, GPU certified nonviolations=50462691, unique transferred candidates=40734, exact=40726, unknown=0, pending=0 | 56054.03 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:37+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=50520127, GPU certified nonviolations=50520035, unique transferred candidates=40782, exact=40770, unknown=0, pending=0 | 56057.47 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=50520127, GPU certified nonviolations=50520035, unique transferred candidates=40782, exact=40770, unknown=0, pending=0 | 56057.04 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=50577471, GPU certified nonviolations=50577379, unique transferred candidates=40822, exact=40806, unknown=0, pending=0 | 56046.61 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=50634815, GPU certified nonviolations=50634723, unique transferred candidates=40868, exact=40860, unknown=0, pending=0 | 56028.38 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=50692159, GPU certified nonviolations=50692067, unique transferred candidates=40924, exact=40915, unknown=0, pending=0 | 56043.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=50749503, GPU certified nonviolations=50749411, unique transferred candidates=40964, exact=40952, unknown=0, pending=0 | 56050.93 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=50806847, GPU certified nonviolations=50806755, unique transferred candidates=40998, exact=40988, unknown=0, pending=0 | 56035.45 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=50864191, GPU certified nonviolations=50864099, unique transferred candidates=41054, exact=41046, unknown=0, pending=0 | 56050.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=50921535, GPU certified nonviolations=50921443, unique transferred candidates=41102, exact=41094, unknown=0, pending=0 | 56066.79 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=50978879, GPU certified nonviolations=50978787, unique transferred candidates=41148, exact=41132, unknown=0, pending=0 | 56058.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=51036223, GPU certified nonviolations=51036131, unique transferred candidates=41185, exact=41174, unknown=0, pending=0 | 56043.15 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=51093567, GPU certified nonviolations=51093475, unique transferred candidates=41241, exact=41229, unknown=0, pending=0 | 56057.20 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=51150911, GPU certified nonviolations=51150819, unique transferred candidates=41281, exact=41273, unknown=0, pending=0 | 56066.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=51208255, GPU certified nonviolations=51208163, unique transferred candidates=41321, exact=41313, unknown=0, pending=0 | 56043.86 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=51265599, GPU certified nonviolations=51265507, unique transferred candidates=41373, exact=41365, unknown=0, pending=0 | 56049.45 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=51322943, GPU certified nonviolations=51322851, unique transferred candidates=41421, exact=41409, unknown=0, pending=0 | 56064.15 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=51380287, GPU certified nonviolations=51380195, unique transferred candidates=41469, exact=41453, unknown=0, pending=0 | 56064.42 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=51437631, GPU certified nonviolations=51437539, unique transferred candidates=41498, exact=41481, unknown=0, pending=0 | 56039.53 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=51494975, GPU certified nonviolations=51494883, unique transferred candidates=41560, exact=41551, unknown=0, pending=0 | 56034.75 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=51552319, GPU certified nonviolations=51552227, unique transferred candidates=41600, exact=41588, unknown=0, pending=0 | 56027.84 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=51609663, GPU certified nonviolations=51609571, unique transferred candidates=41648, exact=41640, unknown=0, pending=0 | 55990.06 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:44:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=51667007, GPU certified nonviolations=51666915, unique transferred candidates=41689, exact=41681, unknown=0, pending=0 | 55980.88 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=51724351, GPU certified nonviolations=51724259, unique transferred candidates=41745, exact=41733, unknown=0, pending=0 | 55982.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=51781695, GPU certified nonviolations=51781603, unique transferred candidates=41785, exact=41773, unknown=0, pending=0 | 55971.63 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=51839039, GPU certified nonviolations=51838947, unique transferred candidates=41818, exact=41801, unknown=0, pending=0 | 55945.48 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=51896383, GPU certified nonviolations=51896291, unique transferred candidates=41878, exact=41870, unknown=0, pending=0 | 55942.12 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=51953727, GPU certified nonviolations=51953635, unique transferred candidates=41926, exact=41914, unknown=0, pending=0 | 55942.85 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=52011071, GPU certified nonviolations=52010979, unique transferred candidates=41966, exact=41950, unknown=0, pending=0 | 55905.98 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=52068415, GPU certified nonviolations=52068323, unique transferred candidates=42011, exact=42003, unknown=0, pending=0 | 55870.73 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=52125759, GPU certified nonviolations=52125667, unique transferred candidates=42067, exact=42057, unknown=0, pending=0 | 55881.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=52183103, GPU certified nonviolations=52183011, unique transferred candidates=42107, exact=42095, unknown=0, pending=0 | 55872.86 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=52240447, GPU certified nonviolations=52240355, unique transferred candidates=42143, exact=42131, unknown=0, pending=0 | 55839.97 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=52297791, GPU certified nonviolations=52297699, unique transferred candidates=42198, exact=42190, unknown=0, pending=0 | 55839.89 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=52355135, GPU certified nonviolations=52355043, unique transferred candidates=42246, exact=42238, unknown=0, pending=0 | 55841.19 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=52412479, GPU certified nonviolations=52412387, unique transferred candidates=42294, exact=42278, unknown=0, pending=0 | 55825.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=52469823, GPU certified nonviolations=52469731, unique transferred candidates=42334, exact=42325, unknown=0, pending=0 | 55799.88 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=52527167, GPU certified nonviolations=52527075, unique transferred candidates=42390, exact=42378, unknown=0, pending=0 | 55802.05 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=52584511, GPU certified nonviolations=52584419, unique transferred candidates=42430, exact=42422, unknown=0, pending=0 | 55801.16 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=52641855, GPU certified nonviolations=52641763, unique transferred candidates=42470, exact=42459, unknown=0, pending=0 | 55781.32 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=52699199, GPU certified nonviolations=52699107, unique transferred candidates=42520, exact=42512, unknown=0, pending=0 | 55783.01 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=52756543, GPU certified nonviolations=52756451, unique transferred candidates=42568, exact=42556, unknown=0, pending=0 | 55784.56 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=52813887, GPU certified nonviolations=52813795, unique transferred candidates=42616, exact=42600, unknown=0, pending=0 | 55776.01 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=52871231, GPU certified nonviolations=52871139, unique transferred candidates=42645, exact=42628, unknown=0, pending=0 | 55760.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=52928575, GPU certified nonviolations=52928483, unique transferred candidates=42707, exact=42698, unknown=0, pending=0 | 55761.63 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=52985919, GPU certified nonviolations=52985827, unique transferred candidates=42747, exact=42735, unknown=0, pending=0 | 55771.55 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=53043263, GPU certified nonviolations=53043171, unique transferred candidates=42795, exact=42784, unknown=0, pending=0 | 55758.15 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=53100607, GPU certified nonviolations=53100515, unique transferred candidates=42840, exact=42832, unknown=0, pending=0 | 55770.34 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=53157951, GPU certified nonviolations=53157859, unique transferred candidates=42896, exact=42884, unknown=0, pending=0 | 55785.24 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=53215295, GPU certified nonviolations=53215203, unique transferred candidates=42936, exact=42924, unknown=0, pending=0 | 55791.05 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=53272639, GPU certified nonviolations=53272547, unique transferred candidates=42969, exact=42953, unknown=0, pending=0 | 55782.77 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=53329983, GPU certified nonviolations=53329891, unique transferred candidates=43028, exact=43020, unknown=0, pending=0 | 55799.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=53387327, GPU certified nonviolations=53387235, unique transferred candidates=43076, exact=43063, unknown=0, pending=0 | 55809.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=53444671, GPU certified nonviolations=53444579, unique transferred candidates=43116, exact=43104, unknown=0, pending=0 | 55802.78 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=53502015, GPU certified nonviolations=53501923, unique transferred candidates=43159, exact=43151, unknown=0, pending=0 | 55802.57 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=53559359, GPU certified nonviolations=53559267, unique transferred candidates=43215, exact=43205, unknown=0, pending=0 | 55816.14 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=53616703, GPU certified nonviolations=53616611, unique transferred candidates=43255, exact=43243, unknown=0, pending=0 | 55822.64 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:37+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=53649471, GPU certified nonviolations=53649379, unique transferred candidates=43279, exact=43267, unknown=0, pending=0 | 55808.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=53674047, GPU certified nonviolations=53673955, unique transferred candidates=43292, exact=43279, unknown=0, pending=0 | 55817.05 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=53731391, GPU certified nonviolations=53731299, unique transferred candidates=43348, exact=43339, unknown=0, pending=0 | 55828.91 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=53788735, GPU certified nonviolations=53788643, unique transferred candidates=43396, exact=43388, unknown=0, pending=0 | 55842.04 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=53846079, GPU certified nonviolations=53845987, unique transferred candidates=43443, exact=43427, unknown=0, pending=0 | 55835.36 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=53903423, GPU certified nonviolations=53903331, unique transferred candidates=43482, exact=43472, unknown=0, pending=0 | 55825.56 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=53960767, GPU certified nonviolations=53960675, unique transferred candidates=43538, exact=43526, unknown=0, pending=0 | 55838.24 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=54018111, GPU certified nonviolations=54018019, unique transferred candidates=43578, exact=43570, unknown=0, pending=0 | 55843.74 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=54075455, GPU certified nonviolations=54075363, unique transferred candidates=43618, exact=43610, unknown=0, pending=0 | 55834.69 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=54132799, GPU certified nonviolations=54132707, unique transferred candidates=43671, exact=43663, unknown=0, pending=0 | 55851.76 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=54190143, GPU certified nonviolations=54190051, unique transferred candidates=43719, exact=43706, unknown=0, pending=0 | 55861.59 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=54247487, GPU certified nonviolations=54247395, unique transferred candidates=43767, exact=43755, unknown=0, pending=0 | 55860.34 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=54304831, GPU certified nonviolations=54304739, unique transferred candidates=43796, exact=43779, unknown=0, pending=0 | 55854.10 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=54362175, GPU certified nonviolations=54362083, unique transferred candidates=43858, exact=43850, unknown=0, pending=0 | 55868.33 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=54419519, GPU certified nonviolations=54419427, unique transferred candidates=43898, exact=43886, unknown=0, pending=0 | 55876.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=54476863, GPU certified nonviolations=54476771, unique transferred candidates=43946, exact=43938, unknown=0, pending=0 | 55861.98 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=54534207, GPU certified nonviolations=54534115, unique transferred candidates=43989, exact=43981, unknown=0, pending=0 | 55874.49 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=54591551, GPU certified nonviolations=54591459, unique transferred candidates=44045, exact=44033, unknown=0, pending=0 | 55890.19 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=54648895, GPU certified nonviolations=54648803, unique transferred candidates=44085, exact=44069, unknown=0, pending=0 | 55893.45 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=54706239, GPU certified nonviolations=54706147, unique transferred candidates=44118, exact=44102, unknown=0, pending=0 | 55883.75 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=54763583, GPU certified nonviolations=54763491, unique transferred candidates=44180, exact=44172, unknown=0, pending=0 | 55898.84 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=54820927, GPU certified nonviolations=54820835, unique transferred candidates=44228, exact=44216, unknown=0, pending=0 | 55905.06 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=54878271, GPU certified nonviolations=54878179, unique transferred candidates=44268, exact=44253, unknown=0, pending=0 | 55893.78 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:45:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=54935615, GPU certified nonviolations=54935523, unique transferred candidates=44312, exact=44304, unknown=0, pending=0 | 55887.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=54992959, GPU certified nonviolations=54992867, unique transferred candidates=44368, exact=44358, unknown=0, pending=0 | 55901.53 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=55050303, GPU certified nonviolations=55050211, unique transferred candidates=44408, exact=44396, unknown=0, pending=0 | 55907.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=55107647, GPU certified nonviolations=55107555, unique transferred candidates=44443, exact=44432, unknown=0, pending=0 | 55901.19 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=55164991, GPU certified nonviolations=55164899, unique transferred candidates=44498, exact=44490, unknown=0, pending=0 | 55911.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=55222335, GPU certified nonviolations=55222243, unique transferred candidates=44546, exact=44538, unknown=0, pending=0 | 55924.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=55279679, GPU certified nonviolations=55279587, unique transferred candidates=44594, exact=44578, unknown=0, pending=0 | 55920.74 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=55337023, GPU certified nonviolations=55336931, unique transferred candidates=44629, exact=44619, unknown=0, pending=0 | 55908.11 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=55394367, GPU certified nonviolations=55394275, unique transferred candidates=44685, exact=44674, unknown=0, pending=0 | 55924.27 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=55451711, GPU certified nonviolations=55451619, unique transferred candidates=44725, exact=44716, unknown=0, pending=0 | 55933.23 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=55509055, GPU certified nonviolations=55508963, unique transferred candidates=44765, exact=44755, unknown=0, pending=0 | 55923.53 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=55566399, GPU certified nonviolations=55566307, unique transferred candidates=44819, exact=44811, unknown=0, pending=0 | 55937.75 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=55623743, GPU certified nonviolations=55623651, unique transferred candidates=44867, exact=44855, unknown=0, pending=0 | 55948.83 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=55681087, GPU certified nonviolations=55680995, unique transferred candidates=44915, exact=44902, unknown=0, pending=0 | 55949.93 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=55738431, GPU certified nonviolations=55738339, unique transferred candidates=44943, exact=44927, unknown=0, pending=0 | 55944.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=55795775, GPU certified nonviolations=55795683, unique transferred candidates=45003, exact=44992, unknown=0, pending=0 | 55955.86 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=55853119, GPU certified nonviolations=55853027, unique transferred candidates=45043, exact=45028, unknown=0, pending=0 | 55964.60 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=55910463, GPU certified nonviolations=55910371, unique transferred candidates=45091, exact=45081, unknown=0, pending=0 | 55948.02 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=55967807, GPU certified nonviolations=55967715, unique transferred candidates=45136, exact=45128, unknown=0, pending=0 | 55960.44 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=56025151, GPU certified nonviolations=56025059, unique transferred candidates=45192, exact=45181, unknown=0, pending=0 | 55974.87 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=56082495, GPU certified nonviolations=56082403, unique transferred candidates=45232, exact=45216, unknown=0, pending=0 | 55977.51 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=56139839, GPU certified nonviolations=56139747, unique transferred candidates=45265, exact=45248, unknown=0, pending=0 | 55963.08 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=56197183, GPU certified nonviolations=56197091, unique transferred candidates=45325, exact=45317, unknown=0, pending=0 | 55975.46 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=56254527, GPU certified nonviolations=56254435, unique transferred candidates=45373, exact=45360, unknown=0, pending=0 | 55978.87 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=56311871, GPU certified nonviolations=56311779, unique transferred candidates=45413, exact=45398, unknown=0, pending=0 | 55969.55 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=56369215, GPU certified nonviolations=56369123, unique transferred candidates=45458, exact=45449, unknown=0, pending=0 | 55965.71 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=56426559, GPU certified nonviolations=56426467, unique transferred candidates=45514, exact=45505, unknown=0, pending=0 | 55979.87 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=56483903, GPU certified nonviolations=56483811, unique transferred candidates=45554, exact=45542, unknown=0, pending=0 | 55984.42 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=56541247, GPU certified nonviolations=56541155, unique transferred candidates=45587, exact=45578, unknown=0, pending=0 | 55978.05 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=56598591, GPU certified nonviolations=56598499, unique transferred candidates=45643, exact=45635, unknown=0, pending=0 | 55984.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=56655935, GPU certified nonviolations=56655843, unique transferred candidates=45691, exact=45683, unknown=0, pending=0 | 55997.84 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=56713279, GPU certified nonviolations=56713187, unique transferred candidates=45739, exact=45723, unknown=0, pending=0 | 55996.52 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=56770623, GPU certified nonviolations=56770530, unique transferred candidates=45775, exact=45766, unknown=0, pending=0 | 55981.76 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=56827967, GPU certified nonviolations=56827874, unique transferred candidates=45831, exact=45820, unknown=0, pending=0 | 55998.10 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=56885311, GPU certified nonviolations=56885218, unique transferred candidates=45871, exact=45863, unknown=0, pending=0 | 56005.20 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=56942655, GPU certified nonviolations=56942562, unique transferred candidates=45911, exact=45901, unknown=0, pending=0 | 55995.98 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=56999999, GPU certified nonviolations=56999906, unique transferred candidates=45964, exact=45956, unknown=0, pending=0 | 56011.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=57057343, GPU certified nonviolations=57057250, unique transferred candidates=46012, exact=46000, unknown=0, pending=0 | 56026.33 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=57114687, GPU certified nonviolations=57114594, unique transferred candidates=46060, exact=46046, unknown=0, pending=0 | 56026.73 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=57172031, GPU certified nonviolations=57171938, unique transferred candidates=46089, exact=46072, unknown=0, pending=0 | 56013.61 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:37+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=57229375, GPU certified nonviolations=57229282, unique transferred candidates=46151, exact=46142, unknown=0, pending=0 | 56033.13 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=57229375, GPU certified nonviolations=57229282, unique transferred candidates=46151, exact=46142, unknown=0, pending=0 | 56032.79 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=57286719, GPU certified nonviolations=57286626, unique transferred candidates=46191, exact=46179, unknown=0, pending=0 | 56045.46 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=57344063, GPU certified nonviolations=57343970, unique transferred candidates=46239, exact=46231, unknown=0, pending=0 | 56031.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=57401407, GPU certified nonviolations=57401314, unique transferred candidates=46282, exact=46274, unknown=0, pending=0 | 56042.56 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=57458751, GPU certified nonviolations=57458658, unique transferred candidates=46338, exact=46326, unknown=0, pending=0 | 56057.97 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=57516095, GPU certified nonviolations=57516002, unique transferred candidates=46378, exact=46363, unknown=0, pending=0 | 56061.99 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=57573439, GPU certified nonviolations=57573346, unique transferred candidates=46411, exact=46395, unknown=0, pending=0 | 56051.48 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=57630783, GPU certified nonviolations=57630690, unique transferred candidates=46471, exact=46463, unknown=0, pending=0 | 56066.97 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=57688127, GPU certified nonviolations=57688034, unique transferred candidates=46519, exact=46506, unknown=0, pending=0 | 56079.78 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=57745471, GPU certified nonviolations=57745378, unique transferred candidates=46559, exact=46543, unknown=0, pending=0 | 56066.38 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=57802815, GPU certified nonviolations=57802721, unique transferred candidates=46603, exact=46595, unknown=0, pending=0 | 56059.72 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=57860159, GPU certified nonviolations=57860065, unique transferred candidates=46657, exact=46647, unknown=0, pending=0 | 56074.75 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=57917503, GPU certified nonviolations=57917409, unique transferred candidates=46697, exact=46684, unknown=0, pending=0 | 56073.79 GPU screened draws/s | best exact gap=0.
