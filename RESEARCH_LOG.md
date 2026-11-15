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

- 2026-11-15T19:46:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=57974847, GPU certified nonviolations=57974753, unique transferred candidates=46736, exact=46721, unknown=0, pending=0 | 56065.26 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=58032191, GPU certified nonviolations=58032097, unique transferred candidates=46791, exact=46783, unknown=0, pending=0 | 56082.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=58089535, GPU certified nonviolations=58089441, unique transferred candidates=46839, exact=46830, unknown=0, pending=0 | 56094.81 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=58146879, GPU certified nonviolations=58146785, unique transferred candidates=46883, exact=46867, unknown=0, pending=0 | 56087.81 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=58204223, GPU certified nonviolations=58204126, unique transferred candidates=46925, exact=46913, unknown=0, pending=0 | 56068.45 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=58261567, GPU certified nonviolations=58261470, unique transferred candidates=46981, exact=46972, unknown=0, pending=0 | 56084.40 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=58318911, GPU certified nonviolations=58318813, unique transferred candidates=47022, exact=47010, unknown=0, pending=0 | 56085.35 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=58376255, GPU certified nonviolations=58376157, unique transferred candidates=47062, exact=47048, unknown=0, pending=0 | 56061.63 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=58433599, GPU certified nonviolations=58433501, unique transferred candidates=47115, exact=47107, unknown=0, pending=0 | 56064.81 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:46:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=58490943, GPU certified nonviolations=58490845, unique transferred candidates=47163, exact=47151, unknown=0, pending=0 | 56077.33 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=58548287, GPU certified nonviolations=58548189, unique transferred candidates=47211, exact=47196, unknown=0, pending=0 | 56077.91 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=58605631, GPU certified nonviolations=58605533, unique transferred candidates=47248, exact=47239, unknown=0, pending=0 | 56060.49 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=58662975, GPU certified nonviolations=58662877, unique transferred candidates=47304, exact=47296, unknown=0, pending=0 | 56075.18 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=58720319, GPU certified nonviolations=58720221, unique transferred candidates=47344, exact=47332, unknown=0, pending=0 | 56079.19 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=58777663, GPU certified nonviolations=58777565, unique transferred candidates=47392, exact=47383, unknown=0, pending=0 | 56064.49 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=58835007, GPU certified nonviolations=58834909, unique transferred candidates=47438, exact=47430, unknown=0, pending=0 | 56074.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=58892351, GPU certified nonviolations=58892253, unique transferred candidates=47494, exact=47484, unknown=0, pending=0 | 56091.48 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=58949695, GPU certified nonviolations=58949597, unique transferred candidates=47534, exact=47519, unknown=0, pending=0 | 56095.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=59007039, GPU certified nonviolations=59006941, unique transferred candidates=47567, exact=47551, unknown=0, pending=0 | 56084.45 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=59064383, GPU certified nonviolations=59064285, unique transferred candidates=47627, exact=47619, unknown=0, pending=0 | 56099.37 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=59121727, GPU certified nonviolations=59121629, unique transferred candidates=47675, exact=47663, unknown=0, pending=0 | 56114.20 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=59179071, GPU certified nonviolations=59178973, unique transferred candidates=47715, exact=47699, unknown=0, pending=0 | 56106.06 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=59236415, GPU certified nonviolations=59236317, unique transferred candidates=47760, exact=47752, unknown=0, pending=0 | 56101.77 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=59293759, GPU certified nonviolations=59293661, unique transferred candidates=47816, exact=47807, unknown=0, pending=0 | 56118.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=59351103, GPU certified nonviolations=59351005, unique transferred candidates=47856, exact=47842, unknown=0, pending=0 | 56114.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=59408447, GPU certified nonviolations=59408349, unique transferred candidates=47892, exact=47880, unknown=0, pending=0 | 56103.16 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=59465791, GPU certified nonviolations=59465693, unique transferred candidates=47948, exact=47940, unknown=0, pending=0 | 56115.13 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=59523135, GPU certified nonviolations=59523037, unique transferred candidates=47996, exact=47988, unknown=0, pending=0 | 56129.83 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=59580479, GPU certified nonviolations=59580381, unique transferred candidates=48044, exact=48028, unknown=0, pending=0 | 56125.88 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=59637823, GPU certified nonviolations=59637725, unique transferred candidates=48081, exact=48073, unknown=0, pending=0 | 56104.91 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=59695167, GPU certified nonviolations=59695069, unique transferred candidates=48137, exact=48126, unknown=0, pending=0 | 56124.22 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=59752511, GPU certified nonviolations=59752413, unique transferred candidates=48177, exact=48167, unknown=0, pending=0 | 56129.80 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=59809855, GPU certified nonviolations=59809757, unique transferred candidates=48217, exact=48206, unknown=0, pending=0 | 56119.46 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=59867199, GPU certified nonviolations=59867101, unique transferred candidates=48268, exact=48260, unknown=0, pending=0 | 56133.24 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=59924543, GPU certified nonviolations=59924445, unique transferred candidates=48316, exact=48304, unknown=0, pending=0 | 56146.28 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=59981887, GPU certified nonviolations=59981789, unique transferred candidates=48364, exact=48350, unknown=0, pending=0 | 56142.40 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=60039231, GPU certified nonviolations=60039133, unique transferred candidates=48393, exact=48376, unknown=0, pending=0 | 56132.71 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=60096575, GPU certified nonviolations=60096477, unique transferred candidates=48456, exact=48447, unknown=0, pending=0 | 56149.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=60153919, GPU certified nonviolations=60153821, unique transferred candidates=48496, exact=48483, unknown=0, pending=0 | 56157.67 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=60211263, GPU certified nonviolations=60211165, unique transferred candidates=48544, exact=48536, unknown=0, pending=0 | 56146.70 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=60268607, GPU certified nonviolations=60268509, unique transferred candidates=48587, exact=48579, unknown=0, pending=0 | 56154.83 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=60325951, GPU certified nonviolations=60325853, unique transferred candidates=48643, exact=48631, unknown=0, pending=0 | 56170.38 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=60383295, GPU certified nonviolations=60383197, unique transferred candidates=48683, exact=48670, unknown=0, pending=0 | 56173.17 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=60440639, GPU certified nonviolations=60440541, unique transferred candidates=48716, exact=48700, unknown=0, pending=0 | 56165.83 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=60497983, GPU certified nonviolations=60497885, unique transferred candidates=48773, exact=48765, unknown=0, pending=0 | 56176.23 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=60555327, GPU certified nonviolations=60555229, unique transferred candidates=48821, exact=48806, unknown=0, pending=0 | 56185.05 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=60612671, GPU certified nonviolations=60612573, unique transferred candidates=48861, exact=48845, unknown=0, pending=0 | 56170.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=60670015, GPU certified nonviolations=60669917, unique transferred candidates=48907, exact=48899, unknown=0, pending=0 | 56162.61 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=60727359, GPU certified nonviolations=60727261, unique transferred candidates=48963, exact=48953, unknown=0, pending=0 | 56172.67 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:37+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=60735551, GPU certified nonviolations=60735453, unique transferred candidates=48971, exact=48963, unknown=0, pending=0 | 56156.93 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=60784703, GPU certified nonviolations=60784605, unique transferred candidates=49003, exact=48991, unknown=0, pending=0 | 56179.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=60842047, GPU certified nonviolations=60841949, unique transferred candidates=49040, exact=49027, unknown=0, pending=0 | 56172.81 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=60899391, GPU certified nonviolations=60899293, unique transferred candidates=49096, exact=49088, unknown=0, pending=0 | 56181.45 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=60956735, GPU certified nonviolations=60956637, unique transferred candidates=49144, exact=49136, unknown=0, pending=0 | 56188.83 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=61014079, GPU certified nonviolations=61013981, unique transferred candidates=49192, exact=49179, unknown=0, pending=0 | 56190.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=61071423, GPU certified nonviolations=61071325, unique transferred candidates=49229, exact=49221, unknown=0, pending=0 | 56180.44 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=61128767, GPU certified nonviolations=61128669, unique transferred candidates=49285, exact=49275, unknown=0, pending=0 | 56194.26 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=61186111, GPU certified nonviolations=61186013, unique transferred candidates=49325, exact=49317, unknown=0, pending=0 | 56202.69 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=61243455, GPU certified nonviolations=61243357, unique transferred candidates=49365, exact=49354, unknown=0, pending=0 | 56190.08 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=61300799, GPU certified nonviolations=61300701, unique transferred candidates=49415, exact=49407, unknown=0, pending=0 | 56201.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=61358143, GPU certified nonviolations=61358045, unique transferred candidates=49463, exact=49448, unknown=0, pending=0 | 56216.16 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=61415487, GPU certified nonviolations=61415389, unique transferred candidates=49511, exact=49495, unknown=0, pending=0 | 56217.03 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=61472831, GPU certified nonviolations=61472733, unique transferred candidates=49540, exact=49523, unknown=0, pending=0 | 56204.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=61530175, GPU certified nonviolations=61530077, unique transferred candidates=49602, exact=49594, unknown=0, pending=0 | 56220.35 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=61587519, GPU certified nonviolations=61587421, unique transferred candidates=49642, exact=49630, unknown=0, pending=0 | 56225.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=61644863, GPU certified nonviolations=61644765, unique transferred candidates=49690, exact=49679, unknown=0, pending=0 | 56212.63 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=61702207, GPU certified nonviolations=61702108, unique transferred candidates=49733, exact=49725, unknown=0, pending=0 | 56225.56 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=61759551, GPU certified nonviolations=61759452, unique transferred candidates=49789, exact=49777, unknown=0, pending=0 | 56240.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=61816895, GPU certified nonviolations=61816796, unique transferred candidates=49829, exact=49817, unknown=0, pending=0 | 56242.96 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=61874239, GPU certified nonviolations=61874140, unique transferred candidates=49862, exact=49846, unknown=0, pending=0 | 56231.36 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=61931583, GPU certified nonviolations=61931484, unique transferred candidates=49921, exact=49913, unknown=0, pending=0 | 56244.53 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=61988927, GPU certified nonviolations=61988828, unique transferred candidates=49969, exact=49957, unknown=0, pending=0 | 56248.35 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:47:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=62046271, GPU certified nonviolations=62046172, unique transferred candidates=50009, exact=49993, unknown=0, pending=0 | 56241.70 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=62103615, GPU certified nonviolations=62103516, unique transferred candidates=50054, exact=50046, unknown=0, pending=0 | 56240.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=62160959, GPU certified nonviolations=62160860, unique transferred candidates=50110, exact=50098, unknown=0, pending=0 | 56243.22 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=62218303, GPU certified nonviolations=62218204, unique transferred candidates=50150, exact=50138, unknown=0, pending=0 | 56245.91 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=62275647, GPU certified nonviolations=62275548, unique transferred candidates=50185, exact=50174, unknown=0, pending=0 | 56240.10 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=62332991, GPU certified nonviolations=62332892, unique transferred candidates=50241, exact=50233, unknown=0, pending=0 | 56254.66 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=62390335, GPU certified nonviolations=62390236, unique transferred candidates=50289, exact=50281, unknown=0, pending=0 | 56263.75 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=62447679, GPU certified nonviolations=62447580, unique transferred candidates=50336, exact=50320, unknown=0, pending=0 | 56258.53 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=62505023, GPU certified nonviolations=62504924, unique transferred candidates=50375, exact=50367, unknown=0, pending=0 | 56247.48 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=62562367, GPU certified nonviolations=62562268, unique transferred candidates=50431, exact=50422, unknown=0, pending=0 | 56260.84 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=62619711, GPU certified nonviolations=62619612, unique transferred candidates=50471, exact=50463, unknown=0, pending=0 | 56262.88 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=62677055, GPU certified nonviolations=62676956, unique transferred candidates=50511, exact=50502, unknown=0, pending=0 | 56254.20 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=62734399, GPU certified nonviolations=62734299, unique transferred candidates=50563, exact=50555, unknown=0, pending=0 | 56269.27 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=62791743, GPU certified nonviolations=62791643, unique transferred candidates=50611, exact=50598, unknown=0, pending=0 | 56278.77 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=62849087, GPU certified nonviolations=62848987, unique transferred candidates=50659, exact=50645, unknown=0, pending=0 | 56278.00 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=62906431, GPU certified nonviolations=62906331, unique transferred candidates=50688, exact=50672, unknown=0, pending=0 | 56268.18 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=62963775, GPU certified nonviolations=62963675, unique transferred candidates=50751, exact=50743, unknown=0, pending=0 | 56284.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=63021119, GPU certified nonviolations=63021019, unique transferred candidates=50791, exact=50778, unknown=0, pending=0 | 56292.38 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=63078463, GPU certified nonviolations=63078363, unique transferred candidates=50839, exact=50831, unknown=0, pending=0 | 56280.77 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=63135807, GPU certified nonviolations=63135707, unique transferred candidates=50882, exact=50874, unknown=0, pending=0 | 56288.99 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=63193151, GPU certified nonviolations=63193051, unique transferred candidates=50938, exact=50926, unknown=0, pending=0 | 56301.08 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=63250495, GPU certified nonviolations=63250395, unique transferred candidates=50978, exact=50966, unknown=0, pending=0 | 56304.83 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=63307839, GPU certified nonviolations=63307739, unique transferred candidates=51011, exact=50995, unknown=0, pending=0 | 56300.96 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=63365183, GPU certified nonviolations=63365083, unique transferred candidates=51070, exact=51061, unknown=0, pending=0 | 56312.63 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=63422527, GPU certified nonviolations=63422427, unique transferred candidates=51118, exact=51106, unknown=0, pending=0 | 56315.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=63479871, GPU certified nonviolations=63479771, unique transferred candidates=51158, exact=51142, unknown=0, pending=0 | 56307.99 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=63537215, GPU certified nonviolations=63537115, unique transferred candidates=51203, exact=51195, unknown=0, pending=0 | 56298.07 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=63594559, GPU certified nonviolations=63594459, unique transferred candidates=51259, exact=51248, unknown=0, pending=0 | 56308.98 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=63651903, GPU certified nonviolations=63651803, unique transferred candidates=51299, exact=51287, unknown=0, pending=0 | 56313.71 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=63709247, GPU certified nonviolations=63709147, unique transferred candidates=51336, exact=51322, unknown=0, pending=0 | 56304.56 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=63766591, GPU certified nonviolations=63766490, unique transferred candidates=51393, exact=51385, unknown=0, pending=0 | 56312.22 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=63823935, GPU certified nonviolations=63823834, unique transferred candidates=51441, exact=51433, unknown=0, pending=0 | 56322.70 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=63881279, GPU certified nonviolations=63881178, unique transferred candidates=51489, exact=51473, unknown=0, pending=0 | 56316.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=63938623, GPU certified nonviolations=63938522, unique transferred candidates=51528, exact=51520, unknown=0, pending=0 | 56302.89 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=63995967, GPU certified nonviolations=63995866, unique transferred candidates=51584, exact=51573, unknown=0, pending=0 | 56320.24 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=64053311, GPU certified nonviolations=64053210, unique transferred candidates=51624, exact=51616, unknown=0, pending=0 | 56326.42 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=64110655, GPU certified nonviolations=64110554, unique transferred candidates=51664, exact=51656, unknown=0, pending=0 | 56316.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=64167999, GPU certified nonviolations=64167898, unique transferred candidates=51714, exact=51706, unknown=0, pending=0 | 56327.94 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=64225343, GPU certified nonviolations=64225242, unique transferred candidates=51762, exact=51750, unknown=0, pending=0 | 56340.65 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=64282687, GPU certified nonviolations=64282586, unique transferred candidates=51810, exact=51794, unknown=0, pending=0 | 56343.07 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:37+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=64290879, GPU certified nonviolations=64290778, unique transferred candidates=51818, exact=51810, unknown=0, pending=0 | 56319.76 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=64340031, GPU certified nonviolations=64339930, unique transferred candidates=51839, exact=51822, unknown=0, pending=0 | 56329.17 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=64397375, GPU certified nonviolations=64397274, unique transferred candidates=51900, exact=51892, unknown=0, pending=0 | 56344.65 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=64454719, GPU certified nonviolations=64454618, unique transferred candidates=51940, exact=51928, unknown=0, pending=0 | 56355.77 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=64512063, GPU certified nonviolations=64511962, unique transferred candidates=51988, exact=51980, unknown=0, pending=0 | 56339.35 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=64569407, GPU certified nonviolations=64569306, unique transferred candidates=52032, exact=52024, unknown=0, pending=0 | 56350.61 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=64626751, GPU certified nonviolations=64626650, unique transferred candidates=52088, exact=52076, unknown=0, pending=0 | 56365.62 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=64684095, GPU certified nonviolations=64683994, unique transferred candidates=52128, exact=52113, unknown=0, pending=0 | 56367.47 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=64741439, GPU certified nonviolations=64741338, unique transferred candidates=52161, exact=52144, unknown=0, pending=0 | 56360.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=64798783, GPU certified nonviolations=64798681, unique transferred candidates=52222, exact=52214, unknown=0, pending=0 | 56371.10 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=64856127, GPU certified nonviolations=64856025, unique transferred candidates=52270, exact=52257, unknown=0, pending=0 | 56381.56 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=64913471, GPU certified nonviolations=64913369, unique transferred candidates=52310, exact=52295, unknown=0, pending=0 | 56375.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=64970815, GPU certified nonviolations=64970713, unique transferred candidates=52354, exact=52346, unknown=0, pending=0 | 56374.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=65028159, GPU certified nonviolations=65028057, unique transferred candidates=52410, exact=52399, unknown=0, pending=0 | 56388.32 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=65085503, GPU certified nonviolations=65085401, unique transferred candidates=52450, exact=52438, unknown=0, pending=0 | 56391.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=65142847, GPU certified nonviolations=65142745, unique transferred candidates=52489, exact=52474, unknown=0, pending=0 | 56385.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=65200191, GPU certified nonviolations=65200088, unique transferred candidates=52546, exact=52538, unknown=0, pending=0 | 56398.37 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=65257535, GPU certified nonviolations=65257432, unique transferred candidates=52594, exact=52586, unknown=0, pending=0 | 56408.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=65314879, GPU certified nonviolations=65314776, unique transferred candidates=52642, exact=52627, unknown=0, pending=0 | 56401.80 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=65372223, GPU certified nonviolations=65372120, unique transferred candidates=52678, exact=52669, unknown=0, pending=0 | 56395.10 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=65429567, GPU certified nonviolations=65429464, unique transferred candidates=52734, exact=52724, unknown=0, pending=0 | 56409.35 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=65486911, GPU certified nonviolations=65486808, unique transferred candidates=52774, exact=52765, unknown=0, pending=0 | 56412.89 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=65544255, GPU certified nonviolations=65544152, unique transferred candidates=52814, exact=52806, unknown=0, pending=0 | 56402.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:48:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=65601599, GPU certified nonviolations=65601496, unique transferred candidates=52864, exact=52856, unknown=0, pending=0 | 56408.18 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=65658943, GPU certified nonviolations=65658840, unique transferred candidates=52912, exact=52901, unknown=0, pending=0 | 56421.20 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=65716287, GPU certified nonviolations=65716184, unique transferred candidates=52960, exact=52944, unknown=0, pending=0 | 56424.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=65773631, GPU certified nonviolations=65773528, unique transferred candidates=52989, exact=52972, unknown=0, pending=0 | 56415.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=65830975, GPU certified nonviolations=65830872, unique transferred candidates=53052, exact=53042, unknown=0, pending=0 | 56427.47 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=65888319, GPU certified nonviolations=65888216, unique transferred candidates=53092, exact=53080, unknown=0, pending=0 | 56438.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=65945663, GPU certified nonviolations=65945560, unique transferred candidates=53140, exact=53129, unknown=0, pending=0 | 56422.46 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=66003007, GPU certified nonviolations=66002904, unique transferred candidates=53183, exact=53175, unknown=0, pending=0 | 56429.80 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=66060351, GPU certified nonviolations=66060248, unique transferred candidates=53239, exact=53227, unknown=0, pending=0 | 56444.49 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=66117695, GPU certified nonviolations=66117592, unique transferred candidates=53279, exact=53265, unknown=0, pending=0 | 56449.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=66175039, GPU certified nonviolations=66174936, unique transferred candidates=53312, exact=53296, unknown=0, pending=0 | 56440.14 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=66232383, GPU certified nonviolations=66232280, unique transferred candidates=53368, exact=53360, unknown=0, pending=0 | 56454.15 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=66289727, GPU certified nonviolations=66289624, unique transferred candidates=53416, exact=53403, unknown=0, pending=0 | 56463.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=66347071, GPU certified nonviolations=66346968, unique transferred candidates=53456, exact=53440, unknown=0, pending=0 | 56454.55 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=66404415, GPU certified nonviolations=66404311, unique transferred candidates=53501, exact=53493, unknown=0, pending=0 | 56453.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=66461759, GPU certified nonviolations=66461655, unique transferred candidates=53557, exact=53545, unknown=0, pending=0 | 56458.28 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=66519103, GPU certified nonviolations=66518999, unique transferred candidates=53597, exact=53585, unknown=0, pending=0 | 56459.90 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=66576447, GPU certified nonviolations=66576343, unique transferred candidates=53630, exact=53621, unknown=0, pending=0 | 56453.75 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=66633791, GPU certified nonviolations=66633687, unique transferred candidates=53686, exact=53678, unknown=0, pending=0 | 56467.22 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=66691135, GPU certified nonviolations=66691031, unique transferred candidates=53734, exact=53725, unknown=0, pending=0 | 56473.03 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=66748479, GPU certified nonviolations=66748375, unique transferred candidates=53782, exact=53768, unknown=0, pending=0 | 56471.64 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=66805823, GPU certified nonviolations=66805719, unique transferred candidates=53816, exact=53808, unknown=0, pending=0 | 56462.39 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=66863167, GPU certified nonviolations=66863063, unique transferred candidates=53872, exact=53862, unknown=0, pending=0 | 56471.53 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=66920511, GPU certified nonviolations=66920407, unique transferred candidates=53912, exact=53903, unknown=0, pending=0 | 56477.17 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=66977855, GPU certified nonviolations=66977751, unique transferred candidates=53952, exact=53943, unknown=0, pending=0 | 56468.73 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=67035199, GPU certified nonviolations=67035095, unique transferred candidates=54003, exact=53995, unknown=0, pending=0 | 56480.39 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=67092543, GPU certified nonviolations=67092439, unique transferred candidates=54051, exact=54039, unknown=0, pending=0 | 56490.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=67149887, GPU certified nonviolations=67149783, unique transferred candidates=54099, exact=54084, unknown=0, pending=0 | 56491.02 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=67207231, GPU certified nonviolations=67207127, unique transferred candidates=54137, exact=54128, unknown=0, pending=0 | 56471.86 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=67264575, GPU certified nonviolations=67264471, unique transferred candidates=54193, exact=54184, unknown=0, pending=0 | 56488.33 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=67321919, GPU certified nonviolations=67321815, unique transferred candidates=54233, exact=54221, unknown=0, pending=0 | 56496.61 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=67379263, GPU certified nonviolations=67379159, unique transferred candidates=54281, exact=54267, unknown=0, pending=0 | 56485.06 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=67436607, GPU certified nonviolations=67436503, unique transferred candidates=54322, exact=54314, unknown=0, pending=0 | 56492.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=67493951, GPU certified nonviolations=67493847, unique transferred candidates=54378, exact=54366, unknown=0, pending=0 | 56498.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=67551295, GPU certified nonviolations=67551191, unique transferred candidates=54418, exact=54405, unknown=0, pending=0 | 56496.60 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=67608639, GPU certified nonviolations=67608535, unique transferred candidates=54452, exact=54436, unknown=0, pending=0 | 56491.27 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=67665983, GPU certified nonviolations=67665879, unique transferred candidates=54512, exact=54504, unknown=0, pending=0 | 56504.42 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=67723327, GPU certified nonviolations=67723223, unique transferred candidates=54560, exact=54548, unknown=0, pending=0 | 56508.52 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=67780671, GPU certified nonviolations=67780567, unique transferred candidates=54600, exact=54587, unknown=0, pending=0 | 56504.67 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=67838015, GPU certified nonviolations=67837911, unique transferred candidates=54641, exact=54633, unknown=0, pending=0 | 56504.94 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=67895359, GPU certified nonviolations=67895255, unique transferred candidates=54697, exact=54686, unknown=0, pending=0 | 56517.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:38+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=67903551, GPU certified nonviolations=67903447, unique transferred candidates=54705, exact=54697, unknown=0, pending=0 | 56503.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=67952703, GPU certified nonviolations=67952599, unique transferred candidates=54737, exact=54725, unknown=0, pending=0 | 56521.79 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=68010047, GPU certified nonviolations=68009943, unique transferred candidates=54773, exact=54761, unknown=0, pending=0 | 56514.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=68067391, GPU certified nonviolations=68067287, unique transferred candidates=54829, exact=54821, unknown=0, pending=0 | 56530.03 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=68124735, GPU certified nonviolations=68124631, unique transferred candidates=54877, exact=54867, unknown=0, pending=0 | 56539.27 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=68182079, GPU certified nonviolations=68181975, unique transferred candidates=54925, exact=54909, unknown=0, pending=0 | 56532.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=68239423, GPU certified nonviolations=68239319, unique transferred candidates=54962, exact=54955, unknown=0, pending=0 | 56525.93 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=68296767, GPU certified nonviolations=68296663, unique transferred candidates=55018, exact=55008, unknown=0, pending=0 | 56540.22 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=68354111, GPU certified nonviolations=68354007, unique transferred candidates=55058, exact=55048, unknown=0, pending=0 | 56546.24 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=68411455, GPU certified nonviolations=68411351, unique transferred candidates=55098, exact=55090, unknown=0, pending=0 | 56531.52 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=68468799, GPU certified nonviolations=68468695, unique transferred candidates=55147, exact=55139, unknown=0, pending=0 | 56537.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=68526143, GPU certified nonviolations=68526039, unique transferred candidates=55195, exact=55183, unknown=0, pending=0 | 56546.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=68583487, GPU certified nonviolations=68583383, unique transferred candidates=55243, exact=55231, unknown=0, pending=0 | 56547.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=68640831, GPU certified nonviolations=68640727, unique transferred candidates=55272, exact=55255, unknown=0, pending=0 | 56541.64 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=68698175, GPU certified nonviolations=68698071, unique transferred candidates=55331, exact=55322, unknown=0, pending=0 | 56555.04 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=68755519, GPU certified nonviolations=68755415, unique transferred candidates=55371, exact=55359, unknown=0, pending=0 | 56562.52 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=68812863, GPU certified nonviolations=68812759, unique transferred candidates=55419, exact=55411, unknown=0, pending=0 | 56549.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=68870207, GPU certified nonviolations=68870103, unique transferred candidates=55461, exact=55454, unknown=0, pending=0 | 56558.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=68927551, GPU certified nonviolations=68927447, unique transferred candidates=55517, exact=55505, unknown=0, pending=0 | 56571.26 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=68984895, GPU certified nonviolations=68984791, unique transferred candidates=55557, exact=55545, unknown=0, pending=0 | 56573.81 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=69042239, GPU certified nonviolations=69042135, unique transferred candidates=55590, exact=55574, unknown=0, pending=0 | 56569.69 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=69099583, GPU certified nonviolations=69099479, unique transferred candidates=55650, exact=55642, unknown=0, pending=0 | 56578.57 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=69156927, GPU certified nonviolations=69156823, unique transferred candidates=55698, exact=55685, unknown=0, pending=0 | 56584.02 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:49:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=69214271, GPU certified nonviolations=69214167, unique transferred candidates=55738, exact=55725, unknown=0, pending=0 | 56577.91 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=69271615, GPU certified nonviolations=69271510, unique transferred candidates=55782, exact=55774, unknown=0, pending=0 | 56576.37 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=69328959, GPU certified nonviolations=69328854, unique transferred candidates=55838, exact=55826, unknown=0, pending=0 | 56587.96 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=69386303, GPU certified nonviolations=69386198, unique transferred candidates=55878, exact=55866, unknown=0, pending=0 | 56590.35 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=69443647, GPU certified nonviolations=69443542, unique transferred candidates=55912, exact=55902, unknown=0, pending=0 | 56583.14 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=69500991, GPU certified nonviolations=69500886, unique transferred candidates=55968, exact=55960, unknown=0, pending=0 | 56595.07 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=69558335, GPU certified nonviolations=69558230, unique transferred candidates=56016, exact=56006, unknown=0, pending=0 | 56600.63 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=69615679, GPU certified nonviolations=69615574, unique transferred candidates=56064, exact=56049, unknown=0, pending=0 | 56598.80 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=69673023, GPU certified nonviolations=69672918, unique transferred candidates=56100, exact=56092, unknown=0, pending=0 | 56593.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=69730367, GPU certified nonviolations=69730262, unique transferred candidates=56156, exact=56143, unknown=0, pending=0 | 56604.84 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=69787711, GPU certified nonviolations=69787606, unique transferred candidates=56196, exact=56188, unknown=0, pending=0 | 56608.86 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=69845055, GPU certified nonviolations=69844950, unique transferred candidates=56236, exact=56226, unknown=0, pending=0 | 56598.92 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=69902399, GPU certified nonviolations=69902294, unique transferred candidates=56287, exact=56279, unknown=0, pending=0 | 56612.88 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=69959743, GPU certified nonviolations=69959638, unique transferred candidates=56335, exact=56323, unknown=0, pending=0 | 56623.38 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=70017087, GPU certified nonviolations=70016982, unique transferred candidates=56383, exact=56370, unknown=0, pending=0 | 56619.24 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=70074431, GPU certified nonviolations=70074326, unique transferred candidates=56412, exact=56395, unknown=0, pending=0 | 56611.53 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=70131775, GPU certified nonviolations=70131670, unique transferred candidates=56472, exact=56462, unknown=0, pending=0 | 56625.52 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=70189119, GPU certified nonviolations=70189014, unique transferred candidates=56512, exact=56500, unknown=0, pending=0 | 56632.19 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=70246463, GPU certified nonviolations=70246358, unique transferred candidates=56560, exact=56552, unknown=0, pending=0 | 56621.99 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=70303807, GPU certified nonviolations=70303702, unique transferred candidates=56605, exact=56597, unknown=0, pending=0 | 56633.10 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=70361151, GPU certified nonviolations=70361046, unique transferred candidates=56661, exact=56648, unknown=0, pending=0 | 56640.91 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=70418495, GPU certified nonviolations=70418390, unique transferred candidates=56701, exact=56689, unknown=0, pending=0 | 56637.91 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=70475839, GPU certified nonviolations=70475734, unique transferred candidates=56734, exact=56718, unknown=0, pending=0 | 56632.52 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=70533183, GPU certified nonviolations=70533078, unique transferred candidates=56793, exact=56785, unknown=0, pending=0 | 56642.13 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=70590527, GPU certified nonviolations=70590422, unique transferred candidates=56841, exact=56828, unknown=0, pending=0 | 56650.87 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=70647871, GPU certified nonviolations=70647766, unique transferred candidates=56881, exact=56868, unknown=0, pending=0 | 56644.12 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=70705215, GPU certified nonviolations=70705110, unique transferred candidates=56926, exact=56918, unknown=0, pending=0 | 56642.96 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=70762559, GPU certified nonviolations=70762454, unique transferred candidates=56982, exact=56970, unknown=0, pending=0 | 56653.02 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=70819903, GPU certified nonviolations=70819798, unique transferred candidates=57022, exact=57010, unknown=0, pending=0 | 56658.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=70877247, GPU certified nonviolations=70877142, unique transferred candidates=57060, exact=57046, unknown=0, pending=0 | 56653.49 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=70934591, GPU certified nonviolations=70934486, unique transferred candidates=57116, exact=57107, unknown=0, pending=0 | 56661.02 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=70991935, GPU certified nonviolations=70991830, unique transferred candidates=57164, exact=57156, unknown=0, pending=0 | 56666.72 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=71049279, GPU certified nonviolations=71049174, unique transferred candidates=57212, exact=57199, unknown=0, pending=0 | 56664.01 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=71106623, GPU certified nonviolations=71106517, unique transferred candidates=57248, exact=57238, unknown=0, pending=0 | 56655.48 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=71163967, GPU certified nonviolations=71163861, unique transferred candidates=57304, exact=57292, unknown=0, pending=0 | 56669.78 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=71221311, GPU certified nonviolations=71221205, unique transferred candidates=57344, exact=57336, unknown=0, pending=0 | 56675.63 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=71278655, GPU certified nonviolations=71278549, unique transferred candidates=57384, exact=57372, unknown=0, pending=0 | 56665.04 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=71335999, GPU certified nonviolations=71335892, unique transferred candidates=57436, exact=57428, unknown=0, pending=0 | 56671.73 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=71393343, GPU certified nonviolations=71393236, unique transferred candidates=57484, exact=57472, unknown=0, pending=0 | 56680.78 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=71450687, GPU certified nonviolations=71450580, unique transferred candidates=57532, exact=57516, unknown=0, pending=0 | 56680.86 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:38+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=71508031, GPU certified nonviolations=71507924, unique transferred candidates=57561, exact=57544, unknown=0, pending=0 | 56669.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=71508031, GPU certified nonviolations=71507924, unique transferred candidates=57561, exact=57544, unknown=0, pending=0 | 56668.94 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=71565375, GPU certified nonviolations=71565267, unique transferred candidates=57624, exact=57614, unknown=0, pending=0 | 56684.84 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=71622719, GPU certified nonviolations=71622611, unique transferred candidates=57664, exact=57651, unknown=0, pending=0 | 56691.53 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=71680063, GPU certified nonviolations=71679955, unique transferred candidates=57712, exact=57702, unknown=0, pending=0 | 56680.36 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=71737407, GPU certified nonviolations=71737299, unique transferred candidates=57756, exact=57748, unknown=0, pending=0 | 56690.66 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=71794751, GPU certified nonviolations=71794643, unique transferred candidates=57812, exact=57800, unknown=0, pending=0 | 56702.17 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=71852095, GPU certified nonviolations=71851987, unique transferred candidates=57852, exact=57836, unknown=0, pending=0 | 56702.22 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=71909439, GPU certified nonviolations=71909331, unique transferred candidates=57885, exact=57868, unknown=0, pending=0 | 56690.86 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=71966783, GPU certified nonviolations=71966675, unique transferred candidates=57943, exact=57935, unknown=0, pending=0 | 56699.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=72024127, GPU certified nonviolations=72024019, unique transferred candidates=57991, exact=57977, unknown=0, pending=0 | 56709.38 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=72081471, GPU certified nonviolations=72081363, unique transferred candidates=58031, exact=58015, unknown=0, pending=0 | 56703.87 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=72138815, GPU certified nonviolations=72138707, unique transferred candidates=58075, exact=58067, unknown=0, pending=0 | 56701.12 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=72196159, GPU certified nonviolations=72196051, unique transferred candidates=58131, exact=58123, unknown=0, pending=0 | 56714.77 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=72253503, GPU certified nonviolations=72253395, unique transferred candidates=58171, exact=58159, unknown=0, pending=0 | 56717.91 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=72310847, GPU certified nonviolations=72310739, unique transferred candidates=58206, exact=58195, unknown=0, pending=0 | 56706.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=72368191, GPU certified nonviolations=72368083, unique transferred candidates=58262, exact=58254, unknown=0, pending=0 | 56715.15 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=72425535, GPU certified nonviolations=72425427, unique transferred candidates=58310, exact=58302, unknown=0, pending=0 | 56724.14 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=72482879, GPU certified nonviolations=72482771, unique transferred candidates=58358, exact=58343, unknown=0, pending=0 | 56719.81 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=72540223, GPU certified nonviolations=72540115, unique transferred candidates=58392, exact=58384, unknown=0, pending=0 | 56710.91 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=72597567, GPU certified nonviolations=72597459, unique transferred candidates=58448, exact=58440, unknown=0, pending=0 | 56724.06 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=72654911, GPU certified nonviolations=72654803, unique transferred candidates=58488, exact=58480, unknown=0, pending=0 | 56730.44 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=72712255, GPU certified nonviolations=72712147, unique transferred candidates=58528, exact=58515, unknown=0, pending=0 | 56719.03 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=72769599, GPU certified nonviolations=72769491, unique transferred candidates=58579, exact=58571, unknown=0, pending=0 | 56727.96 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:50:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=72826943, GPU certified nonviolations=72826835, unique transferred candidates=58627, exact=58615, unknown=0, pending=0 | 56737.85 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=72884287, GPU certified nonviolations=72884179, unique transferred candidates=58675, exact=58659, unknown=0, pending=0 | 56736.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=72941631, GPU certified nonviolations=72941523, unique transferred candidates=58704, exact=58687, unknown=0, pending=0 | 56723.65 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=72998975, GPU certified nonviolations=72998867, unique transferred candidates=58765, exact=58754, unknown=0, pending=0 | 56736.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=73056319, GPU certified nonviolations=73056211, unique transferred candidates=58805, exact=58793, unknown=0, pending=0 | 56744.19 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=73113663, GPU certified nonviolations=73113555, unique transferred candidates=58853, exact=58842, unknown=0, pending=0 | 56732.42 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=73171007, GPU certified nonviolations=73170898, unique transferred candidates=58896, exact=58888, unknown=0, pending=0 | 56743.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=73228351, GPU certified nonviolations=73228242, unique transferred candidates=58952, exact=58942, unknown=0, pending=0 | 56753.79 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=73285695, GPU certified nonviolations=73285586, unique transferred candidates=58992, exact=58976, unknown=0, pending=0 | 56755.83 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=73343039, GPU certified nonviolations=73342930, unique transferred candidates=59025, exact=59009, unknown=0, pending=0 | 56745.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=73400383, GPU certified nonviolations=73400274, unique transferred candidates=59082, exact=59074, unknown=0, pending=0 | 56757.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=73457727, GPU certified nonviolations=73457618, unique transferred candidates=59130, exact=59116, unknown=0, pending=0 | 56759.77 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=73515071, GPU certified nonviolations=73514962, unique transferred candidates=59170, exact=59154, unknown=0, pending=0 | 56754.67 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=73572415, GPU certified nonviolations=73572306, unique transferred candidates=59216, exact=59208, unknown=0, pending=0 | 56746.53 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=73629759, GPU certified nonviolations=73629650, unique transferred candidates=59272, exact=59261, unknown=0, pending=0 | 56757.88 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=73687103, GPU certified nonviolations=73686994, unique transferred candidates=59312, exact=59300, unknown=0, pending=0 | 56760.08 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=73744447, GPU certified nonviolations=73744338, unique transferred candidates=59348, exact=59336, unknown=0, pending=0 | 56753.57 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=73801791, GPU certified nonviolations=73801682, unique transferred candidates=59404, exact=59396, unknown=0, pending=0 | 56765.80 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=73859135, GPU certified nonviolations=73859026, unique transferred candidates=59452, exact=59442, unknown=0, pending=0 | 56775.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=73916479, GPU certified nonviolations=73916370, unique transferred candidates=59500, exact=59484, unknown=0, pending=0 | 56771.92 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=73973823, GPU certified nonviolations=73973713, unique transferred candidates=59535, exact=59526, unknown=0, pending=0 | 56764.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=74031167, GPU certified nonviolations=74031057, unique transferred candidates=59591, exact=59579, unknown=0, pending=0 | 56777.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=74088511, GPU certified nonviolations=74088401, unique transferred candidates=59631, exact=59623, unknown=0, pending=0 | 56784.59 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=74145855, GPU certified nonviolations=74145745, unique transferred candidates=59671, exact=59663, unknown=0, pending=0 | 56759.49 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=74203199, GPU certified nonviolations=74203089, unique transferred candidates=59723, exact=59715, unknown=0, pending=0 | 56768.34 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=74260543, GPU certified nonviolations=74260433, unique transferred candidates=59771, exact=59759, unknown=0, pending=0 | 56771.64 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=74317887, GPU certified nonviolations=74317777, unique transferred candidates=59819, exact=59803, unknown=0, pending=0 | 56768.01 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=74375231, GPU certified nonviolations=74375121, unique transferred candidates=59848, exact=59831, unknown=0, pending=0 | 56759.11 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=74432575, GPU certified nonviolations=74432465, unique transferred candidates=59910, exact=59902, unknown=0, pending=0 | 56770.67 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=74489919, GPU certified nonviolations=74489809, unique transferred candidates=59950, exact=59938, unknown=0, pending=0 | 56770.07 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=74547263, GPU certified nonviolations=74547153, unique transferred candidates=59998, exact=59985, unknown=0, pending=0 | 56752.16 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=74604607, GPU certified nonviolations=74604497, unique transferred candidates=60043, exact=60035, unknown=0, pending=0 | 56757.10 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=74661951, GPU certified nonviolations=74661841, unique transferred candidates=60099, exact=60086, unknown=0, pending=0 | 56753.66 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=74719295, GPU certified nonviolations=74719185, unique transferred candidates=60139, exact=60126, unknown=0, pending=0 | 56751.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=74776639, GPU certified nonviolations=74776529, unique transferred candidates=60172, exact=60156, unknown=0, pending=0 | 56738.24 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=74833983, GPU certified nonviolations=74833873, unique transferred candidates=60232, exact=60222, unknown=0, pending=0 | 56746.89 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=74891327, GPU certified nonviolations=74891217, unique transferred candidates=60280, exact=60268, unknown=0, pending=0 | 56752.45 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=74948671, GPU certified nonviolations=74948561, unique transferred candidates=60320, exact=60304, unknown=0, pending=0 | 56747.11 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=75006015, GPU certified nonviolations=75005905, unique transferred candidates=60364, exact=60356, unknown=0, pending=0 | 56748.12 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:38+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=75014207, GPU certified nonviolations=75014097, unique transferred candidates=60372, exact=60364, unknown=0, pending=0 | 56734.28 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=75063359, GPU certified nonviolations=75063249, unique transferred candidates=60420, exact=60409, unknown=0, pending=0 | 56751.45 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=75120703, GPU certified nonviolations=75120593, unique transferred candidates=60460, exact=60448, unknown=0, pending=0 | 56755.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=75178047, GPU certified nonviolations=75177937, unique transferred candidates=60496, exact=60483, unknown=0, pending=0 | 56746.94 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=75235391, GPU certified nonviolations=75235280, unique transferred candidates=60553, exact=60544, unknown=0, pending=0 | 56752.14 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=75292735, GPU certified nonviolations=75292624, unique transferred candidates=60601, exact=60593, unknown=0, pending=0 | 56753.90 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=75350079, GPU certified nonviolations=75349968, unique transferred candidates=60649, exact=60637, unknown=0, pending=0 | 56747.59 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=75407423, GPU certified nonviolations=75407312, unique transferred candidates=60684, exact=60676, unknown=0, pending=0 | 56734.18 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=75464767, GPU certified nonviolations=75464656, unique transferred candidates=60740, exact=60729, unknown=0, pending=0 | 56736.88 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=75522111, GPU certified nonviolations=75522000, unique transferred candidates=60780, exact=60772, unknown=0, pending=0 | 56739.23 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=75579455, GPU certified nonviolations=75579344, unique transferred candidates=60820, exact=60808, unknown=0, pending=0 | 56724.60 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=75636799, GPU certified nonviolations=75636688, unique transferred candidates=60870, exact=60862, unknown=0, pending=0 | 56730.14 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=75694143, GPU certified nonviolations=75694032, unique transferred candidates=60918, exact=60906, unknown=0, pending=0 | 56735.47 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=75751487, GPU certified nonviolations=75751376, unique transferred candidates=60966, exact=60952, unknown=0, pending=0 | 56734.00 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=75808831, GPU certified nonviolations=75808720, unique transferred candidates=60995, exact=60978, unknown=0, pending=0 | 56711.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=75866175, GPU certified nonviolations=75866064, unique transferred candidates=61057, exact=61048, unknown=0, pending=0 | 56711.55 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=75923519, GPU certified nonviolations=75923408, unique transferred candidates=61097, exact=61085, unknown=0, pending=0 | 56711.17 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=75980863, GPU certified nonviolations=75980752, unique transferred candidates=61145, exact=61133, unknown=0, pending=0 | 56694.28 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=76038207, GPU certified nonviolations=76038096, unique transferred candidates=61186, exact=61178, unknown=0, pending=0 | 56704.23 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=76095551, GPU certified nonviolations=76095440, unique transferred candidates=61242, exact=61230, unknown=0, pending=0 | 56705.28 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:51:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=76152895, GPU certified nonviolations=76152784, unique transferred candidates=61282, exact=61269, unknown=0, pending=0 | 56700.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=76210239, GPU certified nonviolations=76210128, unique transferred candidates=61315, exact=61299, unknown=0, pending=0 | 56688.93 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=76267583, GPU certified nonviolations=76267472, unique transferred candidates=61372, exact=61364, unknown=0, pending=0 | 56700.46 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=76324927, GPU certified nonviolations=76324816, unique transferred candidates=61420, exact=61408, unknown=0, pending=0 | 56704.42 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=76382271, GPU certified nonviolations=76382160, unique transferred candidates=61460, exact=61444, unknown=0, pending=0 | 56696.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=76439615, GPU certified nonviolations=76439504, unique transferred candidates=61503, exact=61495, unknown=0, pending=0 | 56696.24 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=76496959, GPU certified nonviolations=76496848, unique transferred candidates=61559, exact=61549, unknown=0, pending=0 | 56697.37 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=76554303, GPU certified nonviolations=76554192, unique transferred candidates=61599, exact=61587, unknown=0, pending=0 | 56704.06 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=76611647, GPU certified nonviolations=76611536, unique transferred candidates=61634, exact=61623, unknown=0, pending=0 | 56697.72 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=76668991, GPU certified nonviolations=76668880, unique transferred candidates=61690, exact=61682, unknown=0, pending=0 | 56707.69 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=76726335, GPU certified nonviolations=76726224, unique transferred candidates=61738, exact=61729, unknown=0, pending=0 | 56713.03 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=76783679, GPU certified nonviolations=76783568, unique transferred candidates=61786, exact=61770, unknown=0, pending=0 | 56708.20 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=76841023, GPU certified nonviolations=76840912, unique transferred candidates=61820, exact=61806, unknown=0, pending=0 | 56696.59 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=76898367, GPU certified nonviolations=76898256, unique transferred candidates=61876, exact=61865, unknown=0, pending=0 | 56707.59 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=76955711, GPU certified nonviolations=76955600, unique transferred candidates=61916, exact=61907, unknown=0, pending=0 | 56709.18 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=77013055, GPU certified nonviolations=77012944, unique transferred candidates=61956, exact=61940, unknown=0, pending=0 | 56693.06 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=77070399, GPU certified nonviolations=77070288, unique transferred candidates=62009, exact=62001, unknown=0, pending=0 | 56692.07 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=77127743, GPU certified nonviolations=77127632, unique transferred candidates=62057, exact=62045, unknown=0, pending=0 | 56692.53 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=77185087, GPU certified nonviolations=77184976, unique transferred candidates=62105, exact=62091, unknown=0, pending=0 | 56685.53 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=77242431, GPU certified nonviolations=77242320, unique transferred candidates=62134, exact=62117, unknown=0, pending=0 | 56672.17 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=77299775, GPU certified nonviolations=77299664, unique transferred candidates=62195, exact=62185, unknown=0, pending=0 | 56680.64 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=77357119, GPU certified nonviolations=77357008, unique transferred candidates=62235, exact=62222, unknown=0, pending=0 | 56679.13 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=77414463, GPU certified nonviolations=77414352, unique transferred candidates=62283, exact=62273, unknown=0, pending=0 | 56666.74 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=77471807, GPU certified nonviolations=77471695, unique transferred candidates=62325, exact=62318, unknown=0, pending=0 | 56678.19 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=77529151, GPU certified nonviolations=77529039, unique transferred candidates=62381, exact=62369, unknown=0, pending=0 | 56683.40 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=77586495, GPU certified nonviolations=77586383, unique transferred candidates=62421, exact=62409, unknown=0, pending=0 | 56680.51 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=77643839, GPU certified nonviolations=77643727, unique transferred candidates=62454, exact=62438, unknown=0, pending=0 | 56673.71 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=77701183, GPU certified nonviolations=77701071, unique transferred candidates=62514, exact=62506, unknown=0, pending=0 | 56683.17 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=77758527, GPU certified nonviolations=77758415, unique transferred candidates=62562, exact=62548, unknown=0, pending=0 | 56686.02 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=77815871, GPU certified nonviolations=77815759, unique transferred candidates=62602, exact=62590, unknown=0, pending=0 | 56677.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=77873215, GPU certified nonviolations=77873103, unique transferred candidates=62645, exact=62637, unknown=0, pending=0 | 56674.92 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=77930559, GPU certified nonviolations=77930447, unique transferred candidates=62701, exact=62689, unknown=0, pending=0 | 56680.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=77987903, GPU certified nonviolations=77987791, unique transferred candidates=62741, exact=62729, unknown=0, pending=0 | 56675.77 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=78045247, GPU certified nonviolations=78045135, unique transferred candidates=62776, exact=62765, unknown=0, pending=0 | 56667.76 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=78102591, GPU certified nonviolations=78102479, unique transferred candidates=62832, exact=62824, unknown=0, pending=0 | 56678.00 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=78159935, GPU certified nonviolations=78159823, unique transferred candidates=62880, exact=62871, unknown=0, pending=0 | 56683.39 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=78217279, GPU certified nonviolations=78217167, unique transferred candidates=62928, exact=62916, unknown=0, pending=0 | 56676.11 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=78274623, GPU certified nonviolations=78274511, unique transferred candidates=62967, exact=62959, unknown=0, pending=0 | 56664.66 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=78331967, GPU certified nonviolations=78331855, unique transferred candidates=63023, exact=63011, unknown=0, pending=0 | 56674.49 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:38+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=78340159, GPU certified nonviolations=78340047, unique transferred candidates=63031, exact=63023, unknown=0, pending=0 | 56661.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=78389311, GPU certified nonviolations=78389199, unique transferred candidates=63063, exact=63055, unknown=0, pending=0 | 56678.07 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=78446655, GPU certified nonviolations=78446543, unique transferred candidates=63103, exact=63092, unknown=0, pending=0 | 56667.32 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=78503999, GPU certified nonviolations=78503887, unique transferred candidates=63155, exact=63147, unknown=0, pending=0 | 56673.44 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=78561343, GPU certified nonviolations=78561231, unique transferred candidates=63203, exact=63189, unknown=0, pending=0 | 56678.20 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=78618687, GPU certified nonviolations=78618575, unique transferred candidates=63251, exact=63236, unknown=0, pending=0 | 56675.22 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=78676031, GPU certified nonviolations=78675919, unique transferred candidates=63279, exact=63263, unknown=0, pending=0 | 56655.61 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=78733375, GPU certified nonviolations=78733261, unique transferred candidates=63343, exact=63335, unknown=0, pending=0 | 56661.85 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=78790719, GPU certified nonviolations=78790605, unique transferred candidates=63383, exact=63371, unknown=0, pending=0 | 56669.15 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=78848063, GPU certified nonviolations=78847949, unique transferred candidates=63431, exact=63418, unknown=0, pending=0 | 56651.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=78905407, GPU certified nonviolations=78905293, unique transferred candidates=63473, exact=63465, unknown=0, pending=0 | 56659.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=78962751, GPU certified nonviolations=78962637, unique transferred candidates=63529, exact=63515, unknown=0, pending=0 | 56665.67 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=79020095, GPU certified nonviolations=79019981, unique transferred candidates=63569, exact=63557, unknown=0, pending=0 | 56666.20 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=79077439, GPU certified nonviolations=79077325, unique transferred candidates=63602, exact=63586, unknown=0, pending=0 | 56661.37 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=79134783, GPU certified nonviolations=79134669, unique transferred candidates=63658, exact=63650, unknown=0, pending=0 | 56670.55 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=79192127, GPU certified nonviolations=79192013, unique transferred candidates=63706, exact=63692, unknown=0, pending=0 | 56669.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=79249471, GPU certified nonviolations=79249357, unique transferred candidates=63746, exact=63732, unknown=0, pending=0 | 56664.75 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=79306815, GPU certified nonviolations=79306701, unique transferred candidates=63789, exact=63781, unknown=0, pending=0 | 56662.76 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=79364159, GPU certified nonviolations=79364045, unique transferred candidates=63845, exact=63834, unknown=0, pending=0 | 56672.73 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=79421503, GPU certified nonviolations=79421389, unique transferred candidates=63885, exact=63873, unknown=0, pending=0 | 56674.59 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=79478847, GPU certified nonviolations=79478733, unique transferred candidates=63919, exact=63909, unknown=0, pending=0 | 56668.20 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:52:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=79536191, GPU certified nonviolations=79536077, unique transferred candidates=63975, exact=63967, unknown=0, pending=0 | 56674.46 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=79593535, GPU certified nonviolations=79593421, unique transferred candidates=64023, exact=64015, unknown=0, pending=0 | 56680.02 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=79650879, GPU certified nonviolations=79650765, unique transferred candidates=64071, exact=64056, unknown=0, pending=0 | 56678.37 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=79708223, GPU certified nonviolations=79708109, unique transferred candidates=64108, exact=64100, unknown=0, pending=0 | 56670.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=79765567, GPU certified nonviolations=79765453, unique transferred candidates=64164, exact=64152, unknown=0, pending=0 | 56680.80 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=79822911, GPU certified nonviolations=79822797, unique transferred candidates=64204, exact=64194, unknown=0, pending=0 | 56683.46 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=79880255, GPU certified nonviolations=79880141, unique transferred candidates=64244, exact=64231, unknown=0, pending=0 | 56673.08 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=79937599, GPU certified nonviolations=79937485, unique transferred candidates=64292, exact=64284, unknown=0, pending=0 | 56680.74 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=79994943, GPU certified nonviolations=79994829, unique transferred candidates=64340, exact=64325, unknown=0, pending=0 | 56690.59 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=80052287, GPU certified nonviolations=80052173, unique transferred candidates=64388, exact=64372, unknown=0, pending=0 | 56690.86 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=80109631, GPU certified nonviolations=80109517, unique transferred candidates=64417, exact=64400, unknown=0, pending=0 | 56679.34 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=80166975, GPU certified nonviolations=80166861, unique transferred candidates=64480, exact=64472, unknown=0, pending=0 | 56691.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=80224319, GPU certified nonviolations=80224205, unique transferred candidates=64520, exact=64508, unknown=0, pending=0 | 56698.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=80281663, GPU certified nonviolations=80281549, unique transferred candidates=64568, exact=64557, unknown=0, pending=0 | 56688.53 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=80339007, GPU certified nonviolations=80338893, unique transferred candidates=64609, exact=64601, unknown=0, pending=0 | 56699.23 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=80396351, GPU certified nonviolations=80396237, unique transferred candidates=64665, exact=64652, unknown=0, pending=0 | 56706.87 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=80453695, GPU certified nonviolations=80453581, unique transferred candidates=64705, exact=64691, unknown=0, pending=0 | 56705.20 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=80511039, GPU certified nonviolations=80510925, unique transferred candidates=64738, exact=64722, unknown=0, pending=0 | 56696.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=80568383, GPU certified nonviolations=80568269, unique transferred candidates=64795, exact=64787, unknown=0, pending=0 | 56708.45 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=80625727, GPU certified nonviolations=80625613, unique transferred candidates=64843, exact=64831, unknown=0, pending=0 | 56715.61 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=80683071, GPU certified nonviolations=80682957, unique transferred candidates=64883, exact=64867, unknown=0, pending=0 | 56708.38 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=80740415, GPU certified nonviolations=80740301, unique transferred candidates=64926, exact=64918, unknown=0, pending=0 | 56700.10 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=80797759, GPU certified nonviolations=80797645, unique transferred candidates=64982, exact=64971, unknown=0, pending=0 | 56710.75 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=80855103, GPU certified nonviolations=80854989, unique transferred candidates=65022, exact=65006, unknown=0, pending=0 | 56708.47 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=80912447, GPU certified nonviolations=80912333, unique transferred candidates=65057, exact=65046, unknown=0, pending=0 | 56700.65 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=80969791, GPU certified nonviolations=80969677, unique transferred candidates=65113, exact=65105, unknown=0, pending=0 | 56711.85 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=81027135, GPU certified nonviolations=81027021, unique transferred candidates=65161, exact=65153, unknown=0, pending=0 | 56718.19 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=81084479, GPU certified nonviolations=81084365, unique transferred candidates=65209, exact=65194, unknown=0, pending=0 | 56715.23 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=81141823, GPU certified nonviolations=81141709, unique transferred candidates=65246, exact=65238, unknown=0, pending=0 | 56706.38 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=81199167, GPU certified nonviolations=81199053, unique transferred candidates=65302, exact=65292, unknown=0, pending=0 | 56717.55 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=81256511, GPU certified nonviolations=81256397, unique transferred candidates=65342, exact=65334, unknown=0, pending=0 | 56721.95 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=81313855, GPU certified nonviolations=81313741, unique transferred candidates=65382, exact=65371, unknown=0, pending=0 | 56713.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=81371199, GPU certified nonviolations=81371085, unique transferred candidates=65431, exact=65423, unknown=0, pending=0 | 56722.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=81428543, GPU certified nonviolations=81428429, unique transferred candidates=65479, exact=65467, unknown=0, pending=0 | 56730.01 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=81485887, GPU certified nonviolations=81485773, unique transferred candidates=65527, exact=65515, unknown=0, pending=0 | 56728.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=81543231, GPU certified nonviolations=81543117, unique transferred candidates=65556, exact=65539, unknown=0, pending=0 | 56723.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=81600575, GPU certified nonviolations=81600461, unique transferred candidates=65617, exact=65609, unknown=0, pending=0 | 56730.48 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=81657919, GPU certified nonviolations=81657805, unique transferred candidates=65657, exact=65645, unknown=0, pending=0 | 56728.20 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=81715263, GPU certified nonviolations=81715149, unique transferred candidates=65705, exact=65697, unknown=0, pending=0 | 56717.52 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=81772607, GPU certified nonviolations=81772493, unique transferred candidates=65747, exact=65739, unknown=0, pending=0 | 56715.49 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:39+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=81813567, GPU certified nonviolations=81813453, unique transferred candidates=65787, exact=65771, unknown=0, pending=0 | 56709.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=81829951, GPU certified nonviolations=81829837, unique transferred candidates=65803, exact=65787, unknown=0, pending=0 | 56712.39 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=81887295, GPU certified nonviolations=81887181, unique transferred candidates=65843, exact=65828, unknown=0, pending=0 | 56708.75 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=81944639, GPU certified nonviolations=81944525, unique transferred candidates=65876, exact=65859, unknown=0, pending=0 | 56698.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=82001983, GPU certified nonviolations=82001869, unique transferred candidates=65934, exact=65926, unknown=0, pending=0 | 56706.93 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=82059327, GPU certified nonviolations=82059213, unique transferred candidates=65982, exact=65970, unknown=0, pending=0 | 56708.69 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=82116671, GPU certified nonviolations=82116557, unique transferred candidates=66022, exact=66009, unknown=0, pending=0 | 56703.23 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=82174015, GPU certified nonviolations=82173901, unique transferred candidates=66064, exact=66056, unknown=0, pending=0 | 56698.84 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=82231359, GPU certified nonviolations=82231245, unique transferred candidates=66120, exact=66109, unknown=0, pending=0 | 56706.03 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=82288703, GPU certified nonviolations=82288589, unique transferred candidates=66160, exact=66148, unknown=0, pending=0 | 56706.12 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=82346047, GPU certified nonviolations=82345933, unique transferred candidates=66196, exact=66184, unknown=0, pending=0 | 56699.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=82403391, GPU certified nonviolations=82403277, unique transferred candidates=66252, exact=66244, unknown=0, pending=0 | 56701.51 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=82460735, GPU certified nonviolations=82460621, unique transferred candidates=66300, exact=66291, unknown=0, pending=0 | 56699.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=82518079, GPU certified nonviolations=82517965, unique transferred candidates=66348, exact=66332, unknown=0, pending=0 | 56690.33 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=82575423, GPU certified nonviolations=82575309, unique transferred candidates=66385, exact=66377, unknown=0, pending=0 | 56675.11 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=82632767, GPU certified nonviolations=82632653, unique transferred candidates=66441, exact=66429, unknown=0, pending=0 | 56685.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=82690111, GPU certified nonviolations=82689997, unique transferred candidates=66481, exact=66472, unknown=0, pending=0 | 56689.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=82747455, GPU certified nonviolations=82747341, unique transferred candidates=66521, exact=66507, unknown=0, pending=0 | 56673.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=82804799, GPU certified nonviolations=82804685, unique transferred candidates=66573, exact=66565, unknown=0, pending=0 | 56679.17 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=82862143, GPU certified nonviolations=82862029, unique transferred candidates=66621, exact=66609, unknown=0, pending=0 | 56687.15 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:53:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=82919487, GPU certified nonviolations=82919373, unique transferred candidates=66669, exact=66653, unknown=0, pending=0 | 56687.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=82976831, GPU certified nonviolations=82976717, unique transferred candidates=66698, exact=66681, unknown=0, pending=0 | 56672.66 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=83034175, GPU certified nonviolations=83034061, unique transferred candidates=66758, exact=66748, unknown=0, pending=0 | 56678.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=83091519, GPU certified nonviolations=83091405, unique transferred candidates=66798, exact=66786, unknown=0, pending=0 | 56674.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=83148863, GPU certified nonviolations=83148749, unique transferred candidates=66846, exact=66838, unknown=0, pending=0 | 56660.99 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=83206207, GPU certified nonviolations=83206093, unique transferred candidates=66890, exact=66882, unknown=0, pending=0 | 56665.22 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=83263551, GPU certified nonviolations=83263437, unique transferred candidates=66946, exact=66934, unknown=0, pending=0 | 56674.32 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=83320895, GPU certified nonviolations=83320781, unique transferred candidates=66986, exact=66971, unknown=0, pending=0 | 56671.84 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=83378239, GPU certified nonviolations=83378125, unique transferred candidates=67019, exact=67003, unknown=0, pending=0 | 56660.28 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=83435583, GPU certified nonviolations=83435469, unique transferred candidates=67076, exact=67068, unknown=0, pending=0 | 56668.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=83492927, GPU certified nonviolations=83492813, unique transferred candidates=67124, exact=67112, unknown=0, pending=0 | 56669.80 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=83550271, GPU certified nonviolations=83550157, unique transferred candidates=67164, exact=67150, unknown=0, pending=0 | 56661.64 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=83607615, GPU certified nonviolations=83607501, unique transferred candidates=67207, exact=67199, unknown=0, pending=0 | 56653.27 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=83664959, GPU certified nonviolations=83664845, unique transferred candidates=67263, exact=67253, unknown=0, pending=0 | 56649.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=83722303, GPU certified nonviolations=83722189, unique transferred candidates=67303, exact=67292, unknown=0, pending=0 | 56651.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=83779647, GPU certified nonviolations=83779533, unique transferred candidates=67342, exact=67327, unknown=0, pending=0 | 56644.03 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=83836991, GPU certified nonviolations=83836877, unique transferred candidates=67398, exact=67390, unknown=0, pending=0 | 56652.40 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=83894335, GPU certified nonviolations=83894221, unique transferred candidates=67446, exact=67438, unknown=0, pending=0 | 56654.47 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=83951679, GPU certified nonviolations=83951565, unique transferred candidates=67494, exact=67482, unknown=0, pending=0 | 56648.39 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=84009023, GPU certified nonviolations=84008909, unique transferred candidates=67528, exact=67520, unknown=0, pending=0 | 56637.52 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=84066367, GPU certified nonviolations=84066253, unique transferred candidates=67584, exact=67573, unknown=0, pending=0 | 56644.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=84123711, GPU certified nonviolations=84123597, unique transferred candidates=67624, exact=67616, unknown=0, pending=0 | 56645.47 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=84181055, GPU certified nonviolations=84180941, unique transferred candidates=67664, exact=67654, unknown=0, pending=0 | 56637.08 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=84238399, GPU certified nonviolations=84238285, unique transferred candidates=67715, exact=67707, unknown=0, pending=0 | 56641.05 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=84295743, GPU certified nonviolations=84295629, unique transferred candidates=67763, exact=67751, unknown=0, pending=0 | 56648.15 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=84353087, GPU certified nonviolations=84352973, unique transferred candidates=67811, exact=67795, unknown=0, pending=0 | 56645.20 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=84410431, GPU certified nonviolations=84410317, unique transferred candidates=67840, exact=67823, unknown=0, pending=0 | 56633.47 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=84467775, GPU certified nonviolations=84467661, unique transferred candidates=67900, exact=67890, unknown=0, pending=0 | 56643.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=84525119, GPU certified nonviolations=84525005, unique transferred candidates=67940, exact=67928, unknown=0, pending=0 | 56642.66 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=84582463, GPU certified nonviolations=84582349, unique transferred candidates=67988, exact=67979, unknown=0, pending=0 | 56621.73 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=84639807, GPU certified nonviolations=84639693, unique transferred candidates=68032, exact=68024, unknown=0, pending=0 | 56631.19 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=84697151, GPU certified nonviolations=84697037, unique transferred candidates=68088, exact=68076, unknown=0, pending=0 | 56636.65 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=84754495, GPU certified nonviolations=84754381, unique transferred candidates=68128, exact=68115, unknown=0, pending=0 | 56635.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=84811839, GPU certified nonviolations=84811725, unique transferred candidates=68161, exact=68145, unknown=0, pending=0 | 56623.76 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=84869183, GPU certified nonviolations=84869069, unique transferred candidates=68219, exact=68211, unknown=0, pending=0 | 56631.65 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=84926527, GPU certified nonviolations=84926413, unique transferred candidates=68267, exact=68255, unknown=0, pending=0 | 56630.91 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=84983871, GPU certified nonviolations=84983757, unique transferred candidates=68307, exact=68291, unknown=0, pending=0 | 56619.73 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=85041215, GPU certified nonviolations=85041101, unique transferred candidates=68351, exact=68343, unknown=0, pending=0 | 56611.26 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:39+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=85065791, GPU certified nonviolations=85065677, unique transferred candidates=68375, exact=68367, unknown=0, pending=0 | 56607.60 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=85098559, GPU certified nonviolations=85098445, unique transferred candidates=68407, exact=68398, unknown=0, pending=0 | 56617.42 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=85155903, GPU certified nonviolations=85155789, unique transferred candidates=68447, exact=68435, unknown=0, pending=0 | 56618.18 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=85213247, GPU certified nonviolations=85213133, unique transferred candidates=68483, exact=68471, unknown=0, pending=0 | 56610.01 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=85270591, GPU certified nonviolations=85270477, unique transferred candidates=68539, exact=68531, unknown=0, pending=0 | 56616.37 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=85327935, GPU certified nonviolations=85327821, unique transferred candidates=68587, exact=68579, unknown=0, pending=0 | 56620.04 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=85385279, GPU certified nonviolations=85385165, unique transferred candidates=68635, exact=68620, unknown=0, pending=0 | 56615.35 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=85442623, GPU certified nonviolations=85442509, unique transferred candidates=68671, exact=68660, unknown=0, pending=0 | 56602.33 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=85499967, GPU certified nonviolations=85499853, unique transferred candidates=68727, exact=68717, unknown=0, pending=0 | 56606.65 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=85557311, GPU certified nonviolations=85557197, unique transferred candidates=68767, exact=68759, unknown=0, pending=0 | 56610.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=85614655, GPU certified nonviolations=85614541, unique transferred candidates=68807, exact=68793, unknown=0, pending=0 | 56600.48 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=85671999, GPU certified nonviolations=85671885, unique transferred candidates=68857, exact=68849, unknown=0, pending=0 | 56603.52 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=85729343, GPU certified nonviolations=85729229, unique transferred candidates=68905, exact=68893, unknown=0, pending=0 | 56606.44 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=85786687, GPU certified nonviolations=85786573, unique transferred candidates=68953, exact=68941, unknown=0, pending=0 | 56607.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=85844031, GPU certified nonviolations=85843917, unique transferred candidates=68982, exact=68966, unknown=0, pending=0 | 56598.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=85901375, GPU certified nonviolations=85901261, unique transferred candidates=69045, exact=69036, unknown=0, pending=0 | 56606.67 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=85958719, GPU certified nonviolations=85958605, unique transferred candidates=69085, exact=69072, unknown=0, pending=0 | 56607.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=86016063, GPU certified nonviolations=86015949, unique transferred candidates=69133, exact=69121, unknown=0, pending=0 | 56596.70 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=86073407, GPU certified nonviolations=86073293, unique transferred candidates=69175, exact=69167, unknown=0, pending=0 | 56602.88 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=86130751, GPU certified nonviolations=86130637, unique transferred candidates=69231, exact=69219, unknown=0, pending=0 | 56609.99 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:54:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=86188095, GPU certified nonviolations=86187981, unique transferred candidates=69271, exact=69256, unknown=0, pending=0 | 56609.97 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=86245439, GPU certified nonviolations=86245325, unique transferred candidates=69304, exact=69288, unknown=0, pending=0 | 56595.98 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=86302783, GPU certified nonviolations=86302669, unique transferred candidates=69362, exact=69354, unknown=0, pending=0 | 56599.92 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=86360127, GPU certified nonviolations=86360013, unique transferred candidates=69410, exact=69398, unknown=0, pending=0 | 56600.24 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=86417471, GPU certified nonviolations=86417357, unique transferred candidates=69450, exact=69434, unknown=0, pending=0 | 56585.61 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=86474815, GPU certified nonviolations=86474701, unique transferred candidates=69493, exact=69485, unknown=0, pending=0 | 56576.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=86532159, GPU certified nonviolations=86532045, unique transferred candidates=69549, exact=69537, unknown=0, pending=0 | 56583.60 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=86589503, GPU certified nonviolations=86589389, unique transferred candidates=69589, exact=69576, unknown=0, pending=0 | 56583.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=86646847, GPU certified nonviolations=86646733, unique transferred candidates=69625, exact=69613, unknown=0, pending=0 | 56573.60 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=86704191, GPU certified nonviolations=86704077, unique transferred candidates=69681, exact=69673, unknown=0, pending=0 | 56576.51 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=86761535, GPU certified nonviolations=86761421, unique transferred candidates=69729, exact=69721, unknown=0, pending=0 | 56581.91 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=86818879, GPU certified nonviolations=86818765, unique transferred candidates=69777, exact=69761, unknown=0, pending=0 | 56576.70 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=86876223, GPU certified nonviolations=86876109, unique transferred candidates=69813, exact=69805, unknown=0, pending=0 | 56564.84 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=86933567, GPU certified nonviolations=86933453, unique transferred candidates=69869, exact=69856, unknown=0, pending=0 | 56573.86 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=86990911, GPU certified nonviolations=86990797, unique transferred candidates=69909, exact=69898, unknown=0, pending=0 | 56573.75 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=87048255, GPU certified nonviolations=87048141, unique transferred candidates=69949, exact=69941, unknown=0, pending=0 | 56565.02 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=87105599, GPU certified nonviolations=87105485, unique transferred candidates=70000, exact=69992, unknown=0, pending=0 | 56565.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=87162943, GPU certified nonviolations=87162829, unique transferred candidates=70048, exact=70036, unknown=0, pending=0 | 56573.19 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=87220287, GPU certified nonviolations=87220173, unique transferred candidates=70096, exact=70082, unknown=0, pending=0 | 56568.27 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=87277631, GPU certified nonviolations=87277517, unique transferred candidates=70133, exact=70122, unknown=0, pending=0 | 56548.90 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=87334975, GPU certified nonviolations=87334860, unique transferred candidates=70190, exact=70182, unknown=0, pending=0 | 56557.98 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=87392319, GPU certified nonviolations=87392204, unique transferred candidates=70230, exact=70218, unknown=0, pending=0 | 56560.11 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=87449663, GPU certified nonviolations=87449548, unique transferred candidates=70278, exact=70270, unknown=0, pending=0 | 56549.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=87507007, GPU certified nonviolations=87506891, unique transferred candidates=70322, exact=70314, unknown=0, pending=0 | 56550.64 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=87564351, GPU certified nonviolations=87564235, unique transferred candidates=70378, exact=70366, unknown=0, pending=0 | 56550.14 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=87621695, GPU certified nonviolations=87621579, unique transferred candidates=70418, exact=70406, unknown=0, pending=0 | 56549.13 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=87679039, GPU certified nonviolations=87678923, unique transferred candidates=70451, exact=70435, unknown=0, pending=0 | 56542.00 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=87736383, GPU certified nonviolations=87736267, unique transferred candidates=70508, exact=70500, unknown=0, pending=0 | 56547.81 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=87793727, GPU certified nonviolations=87793611, unique transferred candidates=70556, exact=70544, unknown=0, pending=0 | 56549.98 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=87851071, GPU certified nonviolations=87850955, unique transferred candidates=70596, exact=70580, unknown=0, pending=0 | 56542.51 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=87908415, GPU certified nonviolations=87908299, unique transferred candidates=70640, exact=70632, unknown=0, pending=0 | 56536.84 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=87965759, GPU certified nonviolations=87965643, unique transferred candidates=70696, exact=70684, unknown=0, pending=0 | 56538.08 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=88023103, GPU certified nonviolations=88022987, unique transferred candidates=70736, exact=70724, unknown=0, pending=0 | 56538.60 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=88080447, GPU certified nonviolations=88080331, unique transferred candidates=70771, exact=70760, unknown=0, pending=0 | 56531.24 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=88137791, GPU certified nonviolations=88137675, unique transferred candidates=70827, exact=70819, unknown=0, pending=0 | 56535.17 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=88195135, GPU certified nonviolations=88195019, unique transferred candidates=70875, exact=70867, unknown=0, pending=0 | 56536.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=88252479, GPU certified nonviolations=88252363, unique transferred candidates=70920, exact=70904, unknown=0, pending=0 | 56527.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=88309823, GPU certified nonviolations=88309707, unique transferred candidates=70959, exact=70950, unknown=0, pending=0 | 56510.44 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:39+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=88318015, GPU certified nonviolations=88317899, unique transferred candidates=70967, exact=70959, unknown=0, pending=0 | 56501.86 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=88367167, GPU certified nonviolations=88367051, unique transferred candidates=71015, exact=71007, unknown=0, pending=0 | 56518.13 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=88424511, GPU certified nonviolations=88424395, unique transferred candidates=71055, exact=71047, unknown=0, pending=0 | 56522.10 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=88481855, GPU certified nonviolations=88481739, unique transferred candidates=71095, exact=71083, unknown=0, pending=0 | 56508.97 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=88539199, GPU certified nonviolations=88539083, unique transferred candidates=71145, exact=71137, unknown=0, pending=0 | 56514.44 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=88596543, GPU certified nonviolations=88596427, unique transferred candidates=71193, exact=71180, unknown=0, pending=0 | 56519.70 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=88653887, GPU certified nonviolations=88653771, unique transferred candidates=71241, exact=71229, unknown=0, pending=0 | 56516.08 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=88711231, GPU certified nonviolations=88711115, unique transferred candidates=71270, exact=71253, unknown=0, pending=0 | 56505.01 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=88768575, GPU certified nonviolations=88768459, unique transferred candidates=71330, exact=71321, unknown=0, pending=0 | 56512.00 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=88825919, GPU certified nonviolations=88825803, unique transferred candidates=71370, exact=71357, unknown=0, pending=0 | 56511.36 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=88883263, GPU certified nonviolations=88883147, unique transferred candidates=71418, exact=71406, unknown=0, pending=0 | 56500.19 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=88940607, GPU certified nonviolations=88940490, unique transferred candidates=71464, exact=71456, unknown=0, pending=0 | 56507.03 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=88997951, GPU certified nonviolations=88997834, unique transferred candidates=71520, exact=71507, unknown=0, pending=0 | 56506.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=89055295, GPU certified nonviolations=89055178, unique transferred candidates=71560, exact=71548, unknown=0, pending=0 | 56505.05 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=89112639, GPU certified nonviolations=89112522, unique transferred candidates=71593, exact=71577, unknown=0, pending=0 | 56496.96 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=89169983, GPU certified nonviolations=89169866, unique transferred candidates=71649, exact=71640, unknown=0, pending=0 | 56505.12 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=89227327, GPU certified nonviolations=89227210, unique transferred candidates=71697, exact=71685, unknown=0, pending=0 | 56509.37 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=89284671, GPU certified nonviolations=89284554, unique transferred candidates=71737, exact=71724, unknown=0, pending=0 | 56500.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=89342015, GPU certified nonviolations=89341898, unique transferred candidates=71780, exact=71772, unknown=0, pending=0 | 56498.74 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=89399359, GPU certified nonviolations=89399242, unique transferred candidates=71836, exact=71825, unknown=0, pending=0 | 56503.79 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:55:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=89456703, GPU certified nonviolations=89456586, unique transferred candidates=71876, exact=71864, unknown=0, pending=0 | 56501.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=89514047, GPU certified nonviolations=89513930, unique transferred candidates=71909, exact=71900, unknown=0, pending=0 | 56495.87 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=89571391, GPU certified nonviolations=89571274, unique transferred candidates=71965, exact=71957, unknown=0, pending=0 | 56500.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=89628735, GPU certified nonviolations=89628618, unique transferred candidates=72013, exact=72005, unknown=0, pending=0 | 56501.89 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=89686079, GPU certified nonviolations=89685962, unique transferred candidates=72061, exact=72045, unknown=0, pending=0 | 56498.40 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=89743423, GPU certified nonviolations=89743306, unique transferred candidates=72097, exact=72089, unknown=0, pending=0 | 56483.22 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=89800767, GPU certified nonviolations=89800650, unique transferred candidates=72153, exact=72144, unknown=0, pending=0 | 56487.11 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=89858111, GPU certified nonviolations=89857994, unique transferred candidates=72193, exact=72185, unknown=0, pending=0 | 56490.77 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=89915455, GPU certified nonviolations=89915338, unique transferred candidates=72233, exact=72220, unknown=0, pending=0 | 56480.77 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=89972799, GPU certified nonviolations=89972681, unique transferred candidates=72287, exact=72279, unknown=0, pending=0 | 56484.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=90030143, GPU certified nonviolations=90030025, unique transferred candidates=72335, exact=72323, unknown=0, pending=0 | 56484.63 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=90087487, GPU certified nonviolations=90087369, unique transferred candidates=72383, exact=72371, unknown=0, pending=0 | 56483.15 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=90144831, GPU certified nonviolations=90144713, unique transferred candidates=72412, exact=72395, unknown=0, pending=0 | 56470.61 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=90202175, GPU certified nonviolations=90202057, unique transferred candidates=72474, exact=72466, unknown=0, pending=0 | 56478.79 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=90259519, GPU certified nonviolations=90259401, unique transferred candidates=72514, exact=72502, unknown=0, pending=0 | 56481.40 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=90316863, GPU certified nonviolations=90316745, unique transferred candidates=72562, exact=72552, unknown=0, pending=0 | 56463.95 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=90374207, GPU certified nonviolations=90374089, unique transferred candidates=72607, exact=72599, unknown=0, pending=0 | 56472.94 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=90431551, GPU certified nonviolations=90431433, unique transferred candidates=72663, exact=72651, unknown=0, pending=0 | 56479.39 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=90488895, GPU certified nonviolations=90488777, unique transferred candidates=72703, exact=72687, unknown=0, pending=0 | 56478.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=90546239, GPU certified nonviolations=90546121, unique transferred candidates=72736, exact=72720, unknown=0, pending=0 | 56467.87 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=90603583, GPU certified nonviolations=90603465, unique transferred candidates=72793, exact=72784, unknown=0, pending=0 | 56469.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=90660927, GPU certified nonviolations=90660809, unique transferred candidates=72841, exact=72828, unknown=0, pending=0 | 56470.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=90718271, GPU certified nonviolations=90718153, unique transferred candidates=72881, exact=72869, unknown=0, pending=0 | 56462.28 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=90775615, GPU certified nonviolations=90775496, unique transferred candidates=72924, exact=72916, unknown=0, pending=0 | 56459.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=90832959, GPU certified nonviolations=90832840, unique transferred candidates=72979, exact=72967, unknown=0, pending=0 | 56463.38 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=90890303, GPU certified nonviolations=90890184, unique transferred candidates=73019, exact=73007, unknown=0, pending=0 | 56460.67 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=90947647, GPU certified nonviolations=90947528, unique transferred candidates=73055, exact=73043, unknown=0, pending=0 | 56454.27 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=91004991, GPU certified nonviolations=91004872, unique transferred candidates=73111, exact=73102, unknown=0, pending=0 | 56459.23 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=91062335, GPU certified nonviolations=91062216, unique transferred candidates=73159, exact=73151, unknown=0, pending=0 | 56462.71 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=91119679, GPU certified nonviolations=91119560, unique transferred candidates=73207, exact=73191, unknown=0, pending=0 | 56459.17 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=91177023, GPU certified nonviolations=91176903, unique transferred candidates=73244, exact=73235, unknown=0, pending=0 | 56447.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=91234367, GPU certified nonviolations=91234247, unique transferred candidates=73300, exact=73289, unknown=0, pending=0 | 56456.59 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=91291711, GPU certified nonviolations=91291591, unique transferred candidates=73340, exact=73332, unknown=0, pending=0 | 56459.81 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=91349055, GPU certified nonviolations=91348935, unique transferred candidates=73380, exact=73369, unknown=0, pending=0 | 56448.56 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=91406399, GPU certified nonviolations=91406279, unique transferred candidates=73430, exact=73422, unknown=0, pending=0 | 56458.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=91463743, GPU certified nonviolations=91463623, unique transferred candidates=73478, exact=73466, unknown=0, pending=0 | 56462.48 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=91521087, GPU certified nonviolations=91520967, unique transferred candidates=73526, exact=73512, unknown=0, pending=0 | 56459.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=91578431, GPU certified nonviolations=91578311, unique transferred candidates=73555, exact=73538, unknown=0, pending=0 | 56450.13 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=91635775, GPU certified nonviolations=91635655, unique transferred candidates=73616, exact=73608, unknown=0, pending=0 | 56458.03 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:39+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=91643967, GPU certified nonviolations=91643847, unique transferred candidates=73624, exact=73616, unknown=0, pending=0 | 56445.33 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=91693119, GPU certified nonviolations=91692999, unique transferred candidates=73656, exact=73644, unknown=0, pending=0 | 56460.17 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=91750463, GPU certified nonviolations=91750343, unique transferred candidates=73704, exact=73693, unknown=0, pending=0 | 56441.88 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=91807807, GPU certified nonviolations=91807687, unique transferred candidates=73745, exact=73737, unknown=0, pending=0 | 56450.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=91865151, GPU certified nonviolations=91865031, unique transferred candidates=73801, exact=73787, unknown=0, pending=0 | 56454.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=91922495, GPU certified nonviolations=91922375, unique transferred candidates=73841, exact=73829, unknown=0, pending=0 | 56455.83 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=91979839, GPU certified nonviolations=91979719, unique transferred candidates=73874, exact=73858, unknown=0, pending=0 | 56447.55 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=92037183, GPU certified nonviolations=92037062, unique transferred candidates=73931, exact=73923, unknown=0, pending=0 | 56452.83 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=92094527, GPU certified nonviolations=92094406, unique transferred candidates=73979, exact=73966, unknown=0, pending=0 | 56457.46 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=92151871, GPU certified nonviolations=92151750, unique transferred candidates=74019, exact=74003, unknown=0, pending=0 | 56451.44 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=92209215, GPU certified nonviolations=92209094, unique transferred candidates=74061, exact=74053, unknown=0, pending=0 | 56444.70 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=92266559, GPU certified nonviolations=92266438, unique transferred candidates=74117, exact=74107, unknown=0, pending=0 | 56453.27 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=92323903, GPU certified nonviolations=92323782, unique transferred candidates=74157, exact=74145, unknown=0, pending=0 | 56456.02 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=92381247, GPU certified nonviolations=92381126, unique transferred candidates=74191, exact=74181, unknown=0, pending=0 | 56445.89 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=92438591, GPU certified nonviolations=92438470, unique transferred candidates=74246, exact=74238, unknown=0, pending=0 | 56445.08 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=92495935, GPU certified nonviolations=92495814, unique transferred candidates=74294, exact=74286, unknown=0, pending=0 | 56448.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=92553279, GPU certified nonviolations=92553158, unique transferred candidates=74342, exact=74326, unknown=0, pending=0 | 56444.59 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=92610623, GPU certified nonviolations=92610502, unique transferred candidates=74375, exact=74363, unknown=0, pending=0 | 56433.00 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=92667967, GPU certified nonviolations=92667846, unique transferred candidates=74431, exact=74419, unknown=0, pending=0 | 56436.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:56:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=92725311, GPU certified nonviolations=92725190, unique transferred candidates=74471, exact=74462, unknown=0, pending=0 | 56437.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=92782655, GPU certified nonviolations=92782534, unique transferred candidates=74511, exact=74500, unknown=0, pending=0 | 56428.27 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=92839999, GPU certified nonviolations=92839878, unique transferred candidates=74560, exact=74552, unknown=0, pending=0 | 56436.47 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=92897343, GPU certified nonviolations=92897222, unique transferred candidates=74608, exact=74596, unknown=0, pending=0 | 56438.95 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=92954687, GPU certified nonviolations=92954566, unique transferred candidates=74656, exact=74644, unknown=0, pending=0 | 56433.53 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=93012031, GPU certified nonviolations=93011910, unique transferred candidates=74693, exact=74684, unknown=0, pending=0 | 56419.47 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=93069375, GPU certified nonviolations=93069254, unique transferred candidates=74749, exact=74738, unknown=0, pending=0 | 56425.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=93126719, GPU certified nonviolations=93126598, unique transferred candidates=74789, exact=74777, unknown=0, pending=0 | 56430.01 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=93184063, GPU certified nonviolations=93183942, unique transferred candidates=74837, exact=74823, unknown=0, pending=0 | 56419.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=93241407, GPU certified nonviolations=93241286, unique transferred candidates=74882, exact=74874, unknown=0, pending=0 | 56424.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=93298751, GPU certified nonviolations=93298630, unique transferred candidates=74938, exact=74925, unknown=0, pending=0 | 56428.77 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=93356095, GPU certified nonviolations=93355974, unique transferred candidates=74978, exact=74966, unknown=0, pending=0 | 56429.91 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=93413439, GPU certified nonviolations=93413318, unique transferred candidates=75011, exact=74994, unknown=0, pending=0 | 56421.19 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=93470783, GPU certified nonviolations=93470662, unique transferred candidates=75069, exact=75061, unknown=0, pending=0 | 56429.10 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=93528127, GPU certified nonviolations=93528006, unique transferred candidates=75117, exact=75105, unknown=0, pending=0 | 56429.26 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=93585471, GPU certified nonviolations=93585350, unique transferred candidates=75157, exact=75141, unknown=0, pending=0 | 56415.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=93642815, GPU certified nonviolations=93642694, unique transferred candidates=75199, exact=75191, unknown=0, pending=0 | 56411.48 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=93700159, GPU certified nonviolations=93700038, unique transferred candidates=75255, exact=75245, unknown=0, pending=0 | 56418.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=93757503, GPU certified nonviolations=93757382, unique transferred candidates=75295, exact=75283, unknown=0, pending=0 | 56417.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=93814847, GPU certified nonviolations=93814726, unique transferred candidates=75329, exact=75319, unknown=0, pending=0 | 56404.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=93872191, GPU certified nonviolations=93872070, unique transferred candidates=75385, exact=75377, unknown=0, pending=0 | 56409.99 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=93929535, GPU certified nonviolations=93929414, unique transferred candidates=75433, exact=75425, unknown=0, pending=0 | 56413.98 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=93986879, GPU certified nonviolations=93986758, unique transferred candidates=75481, exact=75464, unknown=0, pending=0 | 56407.42 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=94044223, GPU certified nonviolations=94044102, unique transferred candidates=75516, exact=75504, unknown=0, pending=0 | 56395.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=94101567, GPU certified nonviolations=94101446, unique transferred candidates=75572, exact=75561, unknown=0, pending=0 | 56401.16 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=94158911, GPU certified nonviolations=94158790, unique transferred candidates=75612, exact=75604, unknown=0, pending=0 | 56405.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=94216255, GPU certified nonviolations=94216134, unique transferred candidates=75652, exact=75644, unknown=0, pending=0 | 56395.57 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=94273599, GPU certified nonviolations=94273476, unique transferred candidates=75706, exact=75698, unknown=0, pending=0 | 56396.59 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=94330943, GPU certified nonviolations=94330820, unique transferred candidates=75754, exact=75742, unknown=0, pending=0 | 56405.69 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=94388287, GPU certified nonviolations=94388164, unique transferred candidates=75802, exact=75786, unknown=0, pending=0 | 56402.19 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=94445631, GPU certified nonviolations=94445508, unique transferred candidates=75831, exact=75814, unknown=0, pending=0 | 56391.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=94502975, GPU certified nonviolations=94502852, unique transferred candidates=75892, exact=75884, unknown=0, pending=0 | 56396.55 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=94560319, GPU certified nonviolations=94560196, unique transferred candidates=75932, exact=75920, unknown=0, pending=0 | 56401.15 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=94617663, GPU certified nonviolations=94617540, unique transferred candidates=75980, exact=75971, unknown=0, pending=0 | 56388.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=94675007, GPU certified nonviolations=94674884, unique transferred candidates=76021, exact=76013, unknown=0, pending=0 | 56390.60 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=94732351, GPU certified nonviolations=94732228, unique transferred candidates=76077, exact=76065, unknown=0, pending=0 | 56400.63 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=94789695, GPU certified nonviolations=94789572, unique transferred candidates=76117, exact=76105, unknown=0, pending=0 | 56399.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=94847039, GPU certified nonviolations=94846916, unique transferred candidates=76150, exact=76134, unknown=0, pending=0 | 56391.86 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=94904383, GPU certified nonviolations=94904259, unique transferred candidates=76209, exact=76201, unknown=0, pending=0 | 56397.65 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:40+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=94953535, GPU certified nonviolations=94953411, unique transferred candidates=76249, exact=76241, unknown=0, pending=0 | 56398.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=94961727, GPU certified nonviolations=94961603, unique transferred candidates=76257, exact=76245, unknown=0, pending=0 | 56400.01 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=95019071, GPU certified nonviolations=95018947, unique transferred candidates=76297, exact=76282, unknown=0, pending=0 | 56392.42 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=95076415, GPU certified nonviolations=95076290, unique transferred candidates=76341, exact=76333, unknown=0, pending=0 | 56385.06 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=95133759, GPU certified nonviolations=95133634, unique transferred candidates=76397, exact=76386, unknown=0, pending=0 | 56393.28 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=95191103, GPU certified nonviolations=95190978, unique transferred candidates=76437, exact=76425, unknown=0, pending=0 | 56395.59 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=95248447, GPU certified nonviolations=95248322, unique transferred candidates=76473, exact=76458, unknown=0, pending=0 | 56384.37 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=95305791, GPU certified nonviolations=95305666, unique transferred candidates=76529, exact=76521, unknown=0, pending=0 | 56391.44 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=95363135, GPU certified nonviolations=95363010, unique transferred candidates=76577, exact=76567, unknown=0, pending=0 | 56396.74 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=95420479, GPU certified nonviolations=95420354, unique transferred candidates=76623, exact=76607, unknown=0, pending=0 | 56390.96 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=95477823, GPU certified nonviolations=95477698, unique transferred candidates=76659, exact=76649, unknown=0, pending=0 | 56379.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=95535167, GPU certified nonviolations=95535042, unique transferred candidates=76715, exact=76703, unknown=0, pending=0 | 56386.61 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=95592511, GPU certified nonviolations=95592386, unique transferred candidates=76755, exact=76747, unknown=0, pending=0 | 56389.96 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=95649855, GPU certified nonviolations=95649730, unique transferred candidates=76795, exact=76782, unknown=0, pending=0 | 56379.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=95707199, GPU certified nonviolations=95707074, unique transferred candidates=76845, exact=76837, unknown=0, pending=0 | 56387.81 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=95764543, GPU certified nonviolations=95764418, unique transferred candidates=76893, exact=76881, unknown=0, pending=0 | 56391.36 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=95821887, GPU certified nonviolations=95821762, unique transferred candidates=76941, exact=76928, unknown=0, pending=0 | 56389.11 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=95879231, GPU certified nonviolations=95879106, unique transferred candidates=76970, exact=76953, unknown=0, pending=0 | 56379.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=95936575, GPU certified nonviolations=95936450, unique transferred candidates=77031, exact=77021, unknown=0, pending=0 | 56385.66 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:57:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=95993919, GPU certified nonviolations=95993794, unique transferred candidates=77071, exact=77059, unknown=0, pending=0 | 56386.48 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=96051263, GPU certified nonviolations=96051138, unique transferred candidates=77119, exact=77109, unknown=0, pending=0 | 56376.49 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=96108607, GPU certified nonviolations=96108482, unique transferred candidates=77162, exact=77154, unknown=0, pending=0 | 56385.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=96165951, GPU certified nonviolations=96165826, unique transferred candidates=77218, exact=77206, unknown=0, pending=0 | 56384.87 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=96223295, GPU certified nonviolations=96223170, unique transferred candidates=77258, exact=77244, unknown=0, pending=0 | 56380.66 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=96280639, GPU certified nonviolations=96280514, unique transferred candidates=77291, exact=77274, unknown=0, pending=0 | 56370.40 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=96337983, GPU certified nonviolations=96337858, unique transferred candidates=77347, exact=77339, unknown=0, pending=0 | 56373.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=96395327, GPU certified nonviolations=96395202, unique transferred candidates=77395, exact=77383, unknown=0, pending=0 | 56372.63 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=96452671, GPU certified nonviolations=96452546, unique transferred candidates=77435, exact=77419, unknown=0, pending=0 | 56363.36 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=96510015, GPU certified nonviolations=96509890, unique transferred candidates=77479, exact=77471, unknown=0, pending=0 | 56358.86 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=96567359, GPU certified nonviolations=96567234, unique transferred candidates=77535, exact=77524, unknown=0, pending=0 | 56365.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=96624703, GPU certified nonviolations=96624578, unique transferred candidates=77575, exact=77563, unknown=0, pending=0 | 56367.48 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=96682047, GPU certified nonviolations=96681922, unique transferred candidates=77608, exact=77599, unknown=0, pending=0 | 56357.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=96739391, GPU certified nonviolations=96739265, unique transferred candidates=77665, exact=77657, unknown=0, pending=0 | 56363.81 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=96796735, GPU certified nonviolations=96796609, unique transferred candidates=77713, exact=77705, unknown=0, pending=0 | 56369.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=96854079, GPU certified nonviolations=96853953, unique transferred candidates=77760, exact=77744, unknown=0, pending=0 | 56362.45 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=96911423, GPU certified nonviolations=96911297, unique transferred candidates=77795, exact=77784, unknown=0, pending=0 | 56354.27 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=96968767, GPU certified nonviolations=96968641, unique transferred candidates=77851, exact=77839, unknown=0, pending=0 | 56362.79 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=97026111, GPU certified nonviolations=97025985, unique transferred candidates=77891, exact=77881, unknown=0, pending=0 | 56360.15 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=97083455, GPU certified nonviolations=97083329, unique transferred candidates=77931, exact=77923, unknown=0, pending=0 | 56352.00 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=97140799, GPU certified nonviolations=97140673, unique transferred candidates=77985, exact=77977, unknown=0, pending=0 | 56355.20 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=97198143, GPU certified nonviolations=97198016, unique transferred candidates=78034, exact=78022, unknown=0, pending=0 | 56358.05 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=97255487, GPU certified nonviolations=97255360, unique transferred candidates=78082, exact=78070, unknown=0, pending=0 | 56354.56 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=97312831, GPU certified nonviolations=97312704, unique transferred candidates=78110, exact=78094, unknown=0, pending=0 | 56346.96 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=97370175, GPU certified nonviolations=97370048, unique transferred candidates=78170, exact=78160, unknown=0, pending=0 | 56352.67 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=97427519, GPU certified nonviolations=97427392, unique transferred candidates=78210, exact=78198, unknown=0, pending=0 | 56356.56 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=97484863, GPU certified nonviolations=97484736, unique transferred candidates=78258, exact=78250, unknown=0, pending=0 | 56346.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=97542207, GPU certified nonviolations=97542080, unique transferred candidates=78299, exact=78291, unknown=0, pending=0 | 56348.53 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=97599551, GPU certified nonviolations=97599424, unique transferred candidates=78355, exact=78342, unknown=0, pending=0 | 56353.94 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=97656895, GPU certified nonviolations=97656768, unique transferred candidates=78395, exact=78383, unknown=0, pending=0 | 56353.10 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=97714239, GPU certified nonviolations=97714112, unique transferred candidates=78428, exact=78412, unknown=0, pending=0 | 56346.03 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=97771583, GPU certified nonviolations=97771456, unique transferred candidates=78484, exact=78476, unknown=0, pending=0 | 56352.65 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=97828927, GPU certified nonviolations=97828800, unique transferred candidates=78532, exact=78520, unknown=0, pending=0 | 56354.71 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=97886271, GPU certified nonviolations=97886144, unique transferred candidates=78572, exact=78556, unknown=0, pending=0 | 56344.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=97943615, GPU certified nonviolations=97943488, unique transferred candidates=78616, exact=78608, unknown=0, pending=0 | 56339.42 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=98000959, GPU certified nonviolations=98000832, unique transferred candidates=78672, exact=78660, unknown=0, pending=0 | 56343.96 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=98058303, GPU certified nonviolations=98058176, unique transferred candidates=78712, exact=78700, unknown=0, pending=0 | 56341.80 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=98115647, GPU certified nonviolations=98115520, unique transferred candidates=78748, exact=78736, unknown=0, pending=0 | 56331.22 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=98172991, GPU certified nonviolations=98172864, unique transferred candidates=78804, exact=78796, unknown=0, pending=0 | 56331.84 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:40+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=98230335, GPU certified nonviolations=98230208, unique transferred candidates=78852, exact=78844, unknown=0, pending=0 | 56336.39 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=98230335, GPU certified nonviolations=98230208, unique transferred candidates=78852, exact=78844, unknown=0, pending=0 | 56336.20 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=98287679, GPU certified nonviolations=98287552, unique transferred candidates=78900, exact=78884, unknown=0, pending=0 | 56334.07 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=98345023, GPU certified nonviolations=98344896, unique transferred candidates=78936, exact=78925, unknown=0, pending=0 | 56325.22 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=98402367, GPU certified nonviolations=98402240, unique transferred candidates=78992, exact=78980, unknown=0, pending=0 | 56330.01 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=98459711, GPU certified nonviolations=98459584, unique transferred candidates=79032, exact=79024, unknown=0, pending=0 | 56333.33 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=98517055, GPU certified nonviolations=98516928, unique transferred candidates=79072, exact=79064, unknown=0, pending=0 | 56322.19 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=98574399, GPU certified nonviolations=98574272, unique transferred candidates=79122, exact=79114, unknown=0, pending=0 | 56324.39 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=98631743, GPU certified nonviolations=98631616, unique transferred candidates=79170, exact=79158, unknown=0, pending=0 | 56333.62 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=98689087, GPU certified nonviolations=98688960, unique transferred candidates=79218, exact=79203, unknown=0, pending=0 | 56332.52 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=98746431, GPU certified nonviolations=98746304, unique transferred candidates=79247, exact=79230, unknown=0, pending=0 | 56319.46 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=98803775, GPU certified nonviolations=98803648, unique transferred candidates=79309, exact=79301, unknown=0, pending=0 | 56327.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=98861119, GPU certified nonviolations=98860992, unique transferred candidates=79349, exact=79337, unknown=0, pending=0 | 56332.19 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=98918463, GPU certified nonviolations=98918336, unique transferred candidates=79397, exact=79389, unknown=0, pending=0 | 56321.42 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=98975807, GPU certified nonviolations=98975680, unique transferred candidates=79437, exact=79429, unknown=0, pending=0 | 56318.12 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=99033151, GPU certified nonviolations=99033024, unique transferred candidates=79492, exact=79480, unknown=0, pending=0 | 56319.34 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=99090495, GPU certified nonviolations=99090368, unique transferred candidates=79532, exact=79518, unknown=0, pending=0 | 56318.94 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=99147839, GPU certified nonviolations=99147712, unique transferred candidates=79565, exact=79549, unknown=0, pending=0 | 56313.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=99205183, GPU certified nonviolations=99205056, unique transferred candidates=79621, exact=79613, unknown=0, pending=0 | 56319.67 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:58:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=99262527, GPU certified nonviolations=99262400, unique transferred candidates=79669, exact=79655, unknown=0, pending=0 | 56319.24 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=99319871, GPU certified nonviolations=99319744, unique transferred candidates=79709, exact=79696, unknown=0, pending=0 | 56313.28 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=99377215, GPU certified nonviolations=99377088, unique transferred candidates=79751, exact=79743, unknown=0, pending=0 | 56309.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=99434559, GPU certified nonviolations=99434432, unique transferred candidates=79807, exact=79798, unknown=0, pending=0 | 56311.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=99491903, GPU certified nonviolations=99491776, unique transferred candidates=79847, exact=79835, unknown=0, pending=0 | 56313.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=99549247, GPU certified nonviolations=99549120, unique transferred candidates=79882, exact=79871, unknown=0, pending=0 | 56307.53 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=99606591, GPU certified nonviolations=99606464, unique transferred candidates=79938, exact=79930, unknown=0, pending=0 | 56311.02 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=99663935, GPU certified nonviolations=99663808, unique transferred candidates=79986, exact=79978, unknown=0, pending=0 | 56313.35 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=99721279, GPU certified nonviolations=99721152, unique transferred candidates=80034, exact=80022, unknown=0, pending=0 | 56310.80 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=99778623, GPU certified nonviolations=99778496, unique transferred candidates=80068, exact=80059, unknown=0, pending=0 | 56293.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=99835967, GPU certified nonviolations=99835840, unique transferred candidates=80124, exact=80114, unknown=0, pending=0 | 56297.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=99893311, GPU certified nonviolations=99893184, unique transferred candidates=80164, exact=80155, unknown=0, pending=0 | 56297.94 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=99950655, GPU certified nonviolations=99950528, unique transferred candidates=80204, exact=80195, unknown=0, pending=0 | 56288.13 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=100007999, GPU certified nonviolations=100007871, unique transferred candidates=80258, exact=80250, unknown=0, pending=0 | 56291.75 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=100065343, GPU certified nonviolations=100065215, unique transferred candidates=80306, exact=80294, unknown=0, pending=0 | 56299.73 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=100122687, GPU certified nonviolations=100122559, unique transferred candidates=80354, exact=80338, unknown=0, pending=0 | 56298.48 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=100180031, GPU certified nonviolations=100179903, unique transferred candidates=80383, exact=80366, unknown=0, pending=0 | 56285.03 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=100237375, GPU certified nonviolations=100237246, unique transferred candidates=80446, exact=80438, unknown=0, pending=0 | 56292.51 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=100294719, GPU certified nonviolations=100294590, unique transferred candidates=80486, exact=80476, unknown=0, pending=0 | 56286.02 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=100352063, GPU certified nonviolations=100351934, unique transferred candidates=80534, exact=80526, unknown=0, pending=0 | 56275.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=100409407, GPU certified nonviolations=100409278, unique transferred candidates=80577, exact=80568, unknown=0, pending=0 | 56281.13 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=100466751, GPU certified nonviolations=100466622, unique transferred candidates=80633, exact=80621, unknown=0, pending=0 | 56288.48 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=100524095, GPU certified nonviolations=100523966, unique transferred candidates=80673, exact=80660, unknown=0, pending=0 | 56284.67 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=100581439, GPU certified nonviolations=100581310, unique transferred candidates=80706, exact=80690, unknown=0, pending=0 | 56274.91 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=100638783, GPU certified nonviolations=100638654, unique transferred candidates=80763, exact=80755, unknown=0, pending=0 | 56281.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=100696127, GPU certified nonviolations=100695998, unique transferred candidates=80811, exact=80799, unknown=0, pending=0 | 56284.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=100753471, GPU certified nonviolations=100753342, unique transferred candidates=80851, exact=80836, unknown=0, pending=0 | 56274.02 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=100810815, GPU certified nonviolations=100810686, unique transferred candidates=80892, exact=80884, unknown=0, pending=0 | 56267.67 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=100868159, GPU certified nonviolations=100868030, unique transferred candidates=80947, exact=80935, unknown=0, pending=0 | 56272.92 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=100925503, GPU certified nonviolations=100925374, unique transferred candidates=80987, exact=80975, unknown=0, pending=0 | 56273.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=100982847, GPU certified nonviolations=100982718, unique transferred candidates=81023, exact=81011, unknown=0, pending=0 | 56267.23 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=101040191, GPU certified nonviolations=101040062, unique transferred candidates=81079, exact=81071, unknown=0, pending=0 | 56271.27 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=101097535, GPU certified nonviolations=101097406, unique transferred candidates=81127, exact=81119, unknown=0, pending=0 | 56275.40 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=101154879, GPU certified nonviolations=101154750, unique transferred candidates=81175, exact=81162, unknown=0, pending=0 | 56272.32 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=101212223, GPU certified nonviolations=101212094, unique transferred candidates=81210, exact=81201, unknown=0, pending=0 | 56265.85 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=101269567, GPU certified nonviolations=101269438, unique transferred candidates=81266, exact=81255, unknown=0, pending=0 | 56270.28 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=101326911, GPU certified nonviolations=101326782, unique transferred candidates=81306, exact=81298, unknown=0, pending=0 | 56271.90 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=101384255, GPU certified nonviolations=101384126, unique transferred candidates=81346, exact=81337, unknown=0, pending=0 | 56263.64 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=101441599, GPU certified nonviolations=101441470, unique transferred candidates=81396, exact=81388, unknown=0, pending=0 | 56267.90 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:40+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=101490751, GPU certified nonviolations=101490622, unique transferred candidates=81444, exact=81432, unknown=0, pending=0 | 56267.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=101498943, GPU certified nonviolations=101498814, unique transferred candidates=81444, exact=81432, unknown=0, pending=0 | 56268.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=101556287, GPU certified nonviolations=101556158, unique transferred candidates=81492, exact=81480, unknown=0, pending=0 | 56268.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=101613631, GPU certified nonviolations=101613502, unique transferred candidates=81521, exact=81504, unknown=0, pending=0 | 56258.69 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=101670975, GPU certified nonviolations=101670846, unique transferred candidates=81581, exact=81572, unknown=0, pending=0 | 56260.51 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=101728319, GPU certified nonviolations=101728190, unique transferred candidates=81621, exact=81612, unknown=0, pending=0 | 56260.71 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=101785663, GPU certified nonviolations=101785534, unique transferred candidates=81669, exact=81657, unknown=0, pending=0 | 56251.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=101843007, GPU certified nonviolations=101842878, unique transferred candidates=81711, exact=81703, unknown=0, pending=0 | 56257.07 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=101900351, GPU certified nonviolations=101900222, unique transferred candidates=81767, exact=81755, unknown=0, pending=0 | 56259.38 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=101957695, GPU certified nonviolations=101957566, unique transferred candidates=81807, exact=81794, unknown=0, pending=0 | 56261.96 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=102015039, GPU certified nonviolations=102014910, unique transferred candidates=81840, exact=81824, unknown=0, pending=0 | 56253.67 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=102072383, GPU certified nonviolations=102072254, unique transferred candidates=81897, exact=81888, unknown=0, pending=0 | 56258.66 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=102129727, GPU certified nonviolations=102129598, unique transferred candidates=81945, exact=81933, unknown=0, pending=0 | 56258.51 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=102187071, GPU certified nonviolations=102186942, unique transferred candidates=81985, exact=81969, unknown=0, pending=0 | 56253.02 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=102244415, GPU certified nonviolations=102244286, unique transferred candidates=82027, exact=82019, unknown=0, pending=0 | 56246.85 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=102301759, GPU certified nonviolations=102301630, unique transferred candidates=82083, exact=82071, unknown=0, pending=0 | 56253.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=102359103, GPU certified nonviolations=102358974, unique transferred candidates=82123, exact=82111, unknown=0, pending=0 | 56255.86 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=102416447, GPU certified nonviolations=102416318, unique transferred candidates=82157, exact=82147, unknown=0, pending=0 | 56248.72 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=102473791, GPU certified nonviolations=102473662, unique transferred candidates=82213, exact=82205, unknown=0, pending=0 | 56254.78 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=102531135, GPU certified nonviolations=102531006, unique transferred candidates=82261, exact=82253, unknown=0, pending=0 | 56261.01 GPU screened draws/s | best exact gap=0.

- 2026-11-15T19:59:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=102588479, GPU certified nonviolations=102588350, unique transferred candidates=82309, exact=82293, unknown=0, pending=0 | 56256.76 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=102645823, GPU certified nonviolations=102645693, unique transferred candidates=82344, exact=82332, unknown=0, pending=0 | 56244.61 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=102703167, GPU certified nonviolations=102703037, unique transferred candidates=82400, exact=82392, unknown=0, pending=0 | 56250.80 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=102760511, GPU certified nonviolations=102760381, unique transferred candidates=82440, exact=82431, unknown=0, pending=0 | 56253.78 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=102817855, GPU certified nonviolations=102817725, unique transferred candidates=82480, exact=82468, unknown=0, pending=0 | 56244.90 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=102875199, GPU certified nonviolations=102875068, unique transferred candidates=82529, exact=82522, unknown=0, pending=0 | 56251.75 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=102932543, GPU certified nonviolations=102932412, unique transferred candidates=82577, exact=82565, unknown=0, pending=0 | 56256.71 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=102989887, GPU certified nonviolations=102989756, unique transferred candidates=82625, exact=82609, unknown=0, pending=0 | 56256.48 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=103047231, GPU certified nonviolations=103047100, unique transferred candidates=82654, exact=82637, unknown=0, pending=0 | 56245.69 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=103104575, GPU certified nonviolations=103104444, unique transferred candidates=82717, exact=82708, unknown=0, pending=0 | 56254.51 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=103161919, GPU certified nonviolations=103161788, unique transferred candidates=82757, exact=82745, unknown=0, pending=0 | 56256.85 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=103219263, GPU certified nonviolations=103219132, unique transferred candidates=82805, exact=82795, unknown=0, pending=0 | 56245.22 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=103276607, GPU certified nonviolations=103276476, unique transferred candidates=82847, exact=82839, unknown=0, pending=0 | 56254.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=103333951, GPU certified nonviolations=103333820, unique transferred candidates=82903, exact=82891, unknown=0, pending=0 | 56259.62 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=103391295, GPU certified nonviolations=103391164, unique transferred candidates=82943, exact=82931, unknown=0, pending=0 | 56255.98 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=103448639, GPU certified nonviolations=103448508, unique transferred candidates=82976, exact=82960, unknown=0, pending=0 | 56247.60 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=103505983, GPU certified nonviolations=103505852, unique transferred candidates=83032, exact=83024, unknown=0, pending=0 | 56252.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=103563327, GPU certified nonviolations=103563196, unique transferred candidates=83080, exact=83068, unknown=0, pending=0 | 56250.62 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=103620671, GPU certified nonviolations=103620540, unique transferred candidates=83120, exact=83107, unknown=0, pending=0 | 56243.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=103678015, GPU certified nonviolations=103677884, unique transferred candidates=83164, exact=83156, unknown=0, pending=0 | 56237.44 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=103735359, GPU certified nonviolations=103735228, unique transferred candidates=83220, exact=83209, unknown=0, pending=0 | 56241.53 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=103792703, GPU certified nonviolations=103792572, unique transferred candidates=83260, exact=83248, unknown=0, pending=0 | 56242.28 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=103850047, GPU certified nonviolations=103849916, unique transferred candidates=83295, exact=83284, unknown=0, pending=0 | 56236.11 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=103907391, GPU certified nonviolations=103907260, unique transferred candidates=83351, exact=83343, unknown=0, pending=0 | 56242.05 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=103964735, GPU certified nonviolations=103964604, unique transferred candidates=83399, exact=83390, unknown=0, pending=0 | 56245.80 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=104022079, GPU certified nonviolations=104021948, unique transferred candidates=83447, exact=83433, unknown=0, pending=0 | 56241.70 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=104079423, GPU certified nonviolations=104079292, unique transferred candidates=83482, exact=83473, unknown=0, pending=0 | 56233.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=104136767, GPU certified nonviolations=104136636, unique transferred candidates=83538, exact=83526, unknown=0, pending=0 | 56239.36 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=104194111, GPU certified nonviolations=104193980, unique transferred candidates=83578, exact=83570, unknown=0, pending=0 | 56242.99 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=104251455, GPU certified nonviolations=104251324, unique transferred candidates=83618, exact=83610, unknown=0, pending=0 | 55943.00 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:45+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=104259647, GPU certified nonviolations=104259516, unique transferred candidates=83620, exact=83618, unknown=0, pending=0 | 55793.28 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=104308799, GPU certified nonviolations=104308668, unique transferred candidates=83668, exact=83660, unknown=0, pending=0 | 55805.02 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=104366143, GPU certified nonviolations=104366012, unique transferred candidates=83716, exact=83704, unknown=0, pending=0 | 55811.46 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=104423487, GPU certified nonviolations=104423356, unique transferred candidates=83764, exact=83750, unknown=0, pending=0 | 55811.44 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=104480831, GPU certified nonviolations=104480700, unique transferred candidates=83793, exact=83776, unknown=0, pending=0 | 55804.12 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=104538175, GPU certified nonviolations=104538044, unique transferred candidates=83853, exact=83845, unknown=0, pending=0 | 55806.05 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=104595519, GPU certified nonviolations=104595388, unique transferred candidates=83893, exact=83881, unknown=0, pending=0 | 55811.26 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=104652863, GPU certified nonviolations=104652732, unique transferred candidates=83941, exact=83933, unknown=0, pending=0 | 55803.20 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=104710207, GPU certified nonviolations=104710076, unique transferred candidates=83983, exact=83975, unknown=0, pending=0 | 55808.91 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=104767551, GPU certified nonviolations=104767420, unique transferred candidates=84039, exact=84027, unknown=0, pending=0 | 55814.99 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=104824895, GPU certified nonviolations=104824764, unique transferred candidates=84079, exact=84067, unknown=0, pending=0 | 55814.73 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=104882239, GPU certified nonviolations=104882108, unique transferred candidates=84112, exact=84095, unknown=0, pending=0 | 55809.05 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=104939583, GPU certified nonviolations=104939452, unique transferred candidates=84169, exact=84161, unknown=0, pending=0 | 55813.88 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=104996927, GPU certified nonviolations=104996796, unique transferred candidates=84217, exact=84202, unknown=0, pending=0 | 55818.99 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=105054271, GPU certified nonviolations=105054140, unique transferred candidates=84257, exact=84245, unknown=0, pending=0 | 55810.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:00:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=105111615, GPU certified nonviolations=105111484, unique transferred candidates=84299, exact=84291, unknown=0, pending=0 | 55809.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=105168959, GPU certified nonviolations=105168828, unique transferred candidates=84355, exact=84346, unknown=0, pending=0 | 55814.55 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=105226303, GPU certified nonviolations=105226172, unique transferred candidates=84395, exact=84383, unknown=0, pending=0 | 55815.32 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=105283647, GPU certified nonviolations=105283516, unique transferred candidates=84428, exact=84419, unknown=0, pending=0 | 55808.88 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=105340991, GPU certified nonviolations=105340860, unique transferred candidates=84484, exact=84474, unknown=0, pending=0 | 55815.80 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=105398335, GPU certified nonviolations=105398204, unique transferred candidates=84532, exact=84524, unknown=0, pending=0 | 55820.72 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=105455679, GPU certified nonviolations=105455548, unique transferred candidates=84580, exact=84564, unknown=0, pending=0 | 55816.70 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=105513023, GPU certified nonviolations=105512892, unique transferred candidates=84615, exact=84605, unknown=0, pending=0 | 55804.70 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=105570367, GPU certified nonviolations=105570236, unique transferred candidates=84671, exact=84662, unknown=0, pending=0 | 55812.78 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=105627711, GPU certified nonviolations=105627580, unique transferred candidates=84711, exact=84703, unknown=0, pending=0 | 55813.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=105685055, GPU certified nonviolations=105684924, unique transferred candidates=84751, exact=84741, unknown=0, pending=0 | 55806.44 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=105742399, GPU certified nonviolations=105742268, unique transferred candidates=84802, exact=84794, unknown=0, pending=0 | 55813.52 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=105799743, GPU certified nonviolations=105799612, unique transferred candidates=84850, exact=84837, unknown=0, pending=0 | 55818.16 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=105857087, GPU certified nonviolations=105856956, unique transferred candidates=84898, exact=84884, unknown=0, pending=0 | 55818.26 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=105914431, GPU certified nonviolations=105914300, unique transferred candidates=84927, exact=84910, unknown=0, pending=0 | 55808.86 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=105971775, GPU certified nonviolations=105971644, unique transferred candidates=84988, exact=84980, unknown=0, pending=0 | 55816.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=106029119, GPU certified nonviolations=106028988, unique transferred candidates=85028, exact=85016, unknown=0, pending=0 | 55821.05 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=106086463, GPU certified nonviolations=106086332, unique transferred candidates=85076, exact=85064, unknown=0, pending=0 | 55810.12 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=106143807, GPU certified nonviolations=106143676, unique transferred candidates=85119, exact=85111, unknown=0, pending=0 | 55816.88 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=106201151, GPU certified nonviolations=106201020, unique transferred candidates=85175, exact=85163, unknown=0, pending=0 | 55824.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=106258495, GPU certified nonviolations=106258364, unique transferred candidates=85215, exact=85203, unknown=0, pending=0 | 55824.07 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=106315839, GPU certified nonviolations=106315708, unique transferred candidates=85248, exact=85232, unknown=0, pending=0 | 55817.72 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=106373183, GPU certified nonviolations=106373051, unique transferred candidates=85305, exact=85297, unknown=0, pending=0 | 55822.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=106430527, GPU certified nonviolations=106430395, unique transferred candidates=85353, exact=85341, unknown=0, pending=0 | 55822.06 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=106487871, GPU certified nonviolations=106487739, unique transferred candidates=85393, exact=85379, unknown=0, pending=0 | 55818.05 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=106545215, GPU certified nonviolations=106545083, unique transferred candidates=85435, exact=85427, unknown=0, pending=0 | 55815.59 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=106602559, GPU certified nonviolations=106602427, unique transferred candidates=85491, exact=85481, unknown=0, pending=0 | 55819.20 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=106659903, GPU certified nonviolations=106659771, unique transferred candidates=85531, exact=85519, unknown=0, pending=0 | 55821.72 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=106717247, GPU certified nonviolations=106717115, unique transferred candidates=85565, exact=85555, unknown=0, pending=0 | 55816.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=106774591, GPU certified nonviolations=106774459, unique transferred candidates=85621, exact=85613, unknown=0, pending=0 | 55820.42 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=106831935, GPU certified nonviolations=106831803, unique transferred candidates=85669, exact=85661, unknown=0, pending=0 | 55823.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=106889279, GPU certified nonviolations=106889147, unique transferred candidates=85717, exact=85701, unknown=0, pending=0 | 55821.96 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=106946623, GPU certified nonviolations=106946491, unique transferred candidates=85752, exact=85739, unknown=0, pending=0 | 55814.84 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=107003967, GPU certified nonviolations=107003835, unique transferred candidates=85808, exact=85796, unknown=0, pending=0 | 55821.52 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=107061311, GPU certified nonviolations=107061179, unique transferred candidates=85848, exact=85840, unknown=0, pending=0 | 55819.65 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=107118655, GPU certified nonviolations=107118523, unique transferred candidates=85888, exact=85880, unknown=0, pending=0 | 55812.34 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=107175999, GPU certified nonviolations=107175867, unique transferred candidates=85936, exact=85928, unknown=0, pending=0 | 55820.10 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=107233343, GPU certified nonviolations=107233211, unique transferred candidates=85984, exact=85973, unknown=0, pending=0 | 55826.44 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=107290687, GPU certified nonviolations=107290555, unique transferred candidates=86028, exact=86012, unknown=0, pending=0 | 55824.24 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=107348031, GPU certified nonviolations=107347899, unique transferred candidates=86062, exact=86046, unknown=0, pending=0 | 55814.49 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=107405375, GPU certified nonviolations=107405243, unique transferred candidates=86120, exact=86111, unknown=0, pending=0 | 55820.72 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=107462719, GPU certified nonviolations=107462587, unique transferred candidates=86160, exact=86148, unknown=0, pending=0 | 55825.59 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=107520063, GPU certified nonviolations=107519931, unique transferred candidates=86208, exact=86200, unknown=0, pending=0 | 55815.99 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=107577407, GPU certified nonviolations=107577275, unique transferred candidates=86251, exact=86243, unknown=0, pending=0 | 55819.95 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=107634751, GPU certified nonviolations=107634619, unique transferred candidates=86307, exact=86295, unknown=0, pending=0 | 55827.87 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:45+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=107667519, GPU certified nonviolations=107667387, unique transferred candidates=86323, exact=86311, unknown=0, pending=0 | 55823.11 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=107692095, GPU certified nonviolations=107691963, unique transferred candidates=86347, exact=86334, unknown=0, pending=0 | 55827.39 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=107749439, GPU certified nonviolations=107749307, unique transferred candidates=86380, exact=86364, unknown=0, pending=0 | 55822.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=107806783, GPU certified nonviolations=107806651, unique transferred candidates=86438, exact=86429, unknown=0, pending=0 | 55829.65 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=107864127, GPU certified nonviolations=107863995, unique transferred candidates=86486, exact=86474, unknown=0, pending=0 | 55834.51 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=107921471, GPU certified nonviolations=107921339, unique transferred candidates=86526, exact=86512, unknown=0, pending=0 | 55828.83 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=107978815, GPU certified nonviolations=107978683, unique transferred candidates=86569, exact=86561, unknown=0, pending=0 | 55830.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=108036159, GPU certified nonviolations=108036027, unique transferred candidates=86625, exact=86615, unknown=0, pending=0 | 55837.45 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=108093503, GPU certified nonviolations=108093371, unique transferred candidates=86665, exact=86653, unknown=0, pending=0 | 55840.69 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=108150847, GPU certified nonviolations=108150715, unique transferred candidates=86698, exact=86689, unknown=0, pending=0 | 55837.22 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=108208191, GPU certified nonviolations=108208059, unique transferred candidates=86754, exact=86745, unknown=0, pending=0 | 55844.57 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=108265535, GPU certified nonviolations=108265403, unique transferred candidates=86802, exact=86793, unknown=0, pending=0 | 55848.06 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=108322879, GPU certified nonviolations=108322747, unique transferred candidates=86850, exact=86837, unknown=0, pending=0 | 55844.57 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=108380223, GPU certified nonviolations=108380090, unique transferred candidates=86886, exact=86877, unknown=0, pending=0 | 55840.78 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=108437567, GPU certified nonviolations=108437434, unique transferred candidates=86942, exact=86930, unknown=0, pending=0 | 55848.57 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:01:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=108494911, GPU certified nonviolations=108494778, unique transferred candidates=86982, exact=86974, unknown=0, pending=0 | 55851.78 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=108552255, GPU certified nonviolations=108552122, unique transferred candidates=87022, exact=87009, unknown=0, pending=0 | 55844.60 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=108609599, GPU certified nonviolations=108609466, unique transferred candidates=87071, exact=87063, unknown=0, pending=0 | 55849.84 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=108666943, GPU certified nonviolations=108666810, unique transferred candidates=87119, exact=87107, unknown=0, pending=0 | 55851.70 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=108724287, GPU certified nonviolations=108724154, unique transferred candidates=87167, exact=87155, unknown=0, pending=0 | 55852.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=108781631, GPU certified nonviolations=108781498, unique transferred candidates=87196, exact=87179, unknown=0, pending=0 | 55847.70 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=108838975, GPU certified nonviolations=108838842, unique transferred candidates=87256, exact=87247, unknown=0, pending=0 | 55853.49 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=108896319, GPU certified nonviolations=108896186, unique transferred candidates=87296, exact=87284, unknown=0, pending=0 | 55859.18 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=108953663, GPU certified nonviolations=108953530, unique transferred candidates=87344, exact=87333, unknown=0, pending=0 | 55854.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=109011007, GPU certified nonviolations=109010874, unique transferred candidates=87387, exact=87379, unknown=0, pending=0 | 55862.59 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=109068351, GPU certified nonviolations=109068218, unique transferred candidates=87443, exact=87432, unknown=0, pending=0 | 55869.65 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=109125695, GPU certified nonviolations=109125562, unique transferred candidates=87483, exact=87471, unknown=0, pending=0 | 55871.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=109183039, GPU certified nonviolations=109182906, unique transferred candidates=87516, exact=87500, unknown=0, pending=0 | 55867.93 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=109240383, GPU certified nonviolations=109240250, unique transferred candidates=87573, exact=87563, unknown=0, pending=0 | 55872.40 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=109297727, GPU certified nonviolations=109297594, unique transferred candidates=87621, exact=87608, unknown=0, pending=0 | 55876.83 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=109355071, GPU certified nonviolations=109354938, unique transferred candidates=87661, exact=87649, unknown=0, pending=0 | 55873.22 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=109412415, GPU certified nonviolations=109412282, unique transferred candidates=87703, exact=87695, unknown=0, pending=0 | 55873.98 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=109469759, GPU certified nonviolations=109469626, unique transferred candidates=87759, exact=87751, unknown=0, pending=0 | 55879.76 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=109527103, GPU certified nonviolations=109526970, unique transferred candidates=87799, exact=87787, unknown=0, pending=0 | 55882.35 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=109584447, GPU certified nonviolations=109584314, unique transferred candidates=87834, exact=87823, unknown=0, pending=0 | 55878.28 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=109641791, GPU certified nonviolations=109641657, unique transferred candidates=87891, exact=87883, unknown=0, pending=0 | 55886.28 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=109699135, GPU certified nonviolations=109699001, unique transferred candidates=87939, exact=87930, unknown=0, pending=0 | 55891.33 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=109756479, GPU certified nonviolations=109756345, unique transferred candidates=87987, exact=87972, unknown=0, pending=0 | 55888.00 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=109813823, GPU certified nonviolations=109813689, unique transferred candidates=88024, exact=88016, unknown=0, pending=0 | 55885.46 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=109871167, GPU certified nonviolations=109871033, unique transferred candidates=88080, exact=88069, unknown=0, pending=0 | 55893.88 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=109928511, GPU certified nonviolations=109928377, unique transferred candidates=88120, exact=88108, unknown=0, pending=0 | 55897.13 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=109985855, GPU certified nonviolations=109985721, unique transferred candidates=88159, exact=88152, unknown=0, pending=0 | 55890.79 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=110043199, GPU certified nonviolations=110043065, unique transferred candidates=88209, exact=88201, unknown=0, pending=0 | 55896.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=110100543, GPU certified nonviolations=110100409, unique transferred candidates=88257, exact=88245, unknown=0, pending=0 | 55901.89 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=110157887, GPU certified nonviolations=110157753, unique transferred candidates=88305, exact=88293, unknown=0, pending=0 | 55902.96 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=110215231, GPU certified nonviolations=110215097, unique transferred candidates=88334, exact=88317, unknown=0, pending=0 | 55897.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=110272575, GPU certified nonviolations=110272441, unique transferred candidates=88395, exact=88384, unknown=0, pending=0 | 55906.16 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=110329919, GPU certified nonviolations=110329785, unique transferred candidates=88435, exact=88422, unknown=0, pending=0 | 55911.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=110387263, GPU certified nonviolations=110387129, unique transferred candidates=88483, exact=88474, unknown=0, pending=0 | 55904.16 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=110444607, GPU certified nonviolations=110444473, unique transferred candidates=88524, exact=88516, unknown=0, pending=0 | 55909.51 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=110501951, GPU certified nonviolations=110501817, unique transferred candidates=88580, exact=88568, unknown=0, pending=0 | 55917.34 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=110559295, GPU certified nonviolations=110559161, unique transferred candidates=88620, exact=88608, unknown=0, pending=0 | 55919.19 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=110616639, GPU certified nonviolations=110616505, unique transferred candidates=88653, exact=88636, unknown=0, pending=0 | 55916.67 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=110673983, GPU certified nonviolations=110673849, unique transferred candidates=88711, exact=88702, unknown=0, pending=0 | 55923.36 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=110731327, GPU certified nonviolations=110731193, unique transferred candidates=88759, exact=88746, unknown=0, pending=0 | 55925.48 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=110788671, GPU certified nonviolations=110788537, unique transferred candidates=88799, exact=88787, unknown=0, pending=0 | 55921.72 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=110846015, GPU certified nonviolations=110845881, unique transferred candidates=88840, exact=88832, unknown=0, pending=0 | 55920.71 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=110903359, GPU certified nonviolations=110903225, unique transferred candidates=88896, exact=88886, unknown=0, pending=0 | 55929.13 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=110960703, GPU certified nonviolations=110960569, unique transferred candidates=88936, exact=88924, unknown=0, pending=0 | 55932.24 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=111018047, GPU certified nonviolations=111017913, unique transferred candidates=88971, exact=88960, unknown=0, pending=0 | 55929.04 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=111075391, GPU certified nonviolations=111075256, unique transferred candidates=89027, exact=89019, unknown=0, pending=0 | 55935.71 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=111132735, GPU certified nonviolations=111132600, unique transferred candidates=89075, exact=89065, unknown=0, pending=0 | 55942.78 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=111190079, GPU certified nonviolations=111189944, unique transferred candidates=89123, exact=89107, unknown=0, pending=0 | 55939.10 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:45+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=111239231, GPU certified nonviolations=111239096, unique transferred candidates=89143, exact=89127, unknown=0, pending=0 | 55934.47 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=111247423, GPU certified nonviolations=111247288, unique transferred candidates=89155, exact=89147, unknown=0, pending=0 | 55933.56 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=111304767, GPU certified nonviolations=111304632, unique transferred candidates=89211, exact=89200, unknown=0, pending=0 | 55943.15 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=111362111, GPU certified nonviolations=111361976, unique transferred candidates=89251, exact=89240, unknown=0, pending=0 | 55944.77 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=111419455, GPU certified nonviolations=111419320, unique transferred candidates=89291, exact=89283, unknown=0, pending=0 | 55939.62 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=111476799, GPU certified nonviolations=111476664, unique transferred candidates=89343, exact=89335, unknown=0, pending=0 | 55948.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=111534143, GPU certified nonviolations=111534008, unique transferred candidates=89391, exact=89379, unknown=0, pending=0 | 55954.67 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=111591487, GPU certified nonviolations=111591352, unique transferred candidates=89439, exact=89427, unknown=0, pending=0 | 55955.22 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=111648831, GPU certified nonviolations=111648696, unique transferred candidates=89468, exact=89451, unknown=0, pending=0 | 55952.26 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=111706175, GPU certified nonviolations=111706040, unique transferred candidates=89529, exact=89521, unknown=0, pending=0 | 55960.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=111763519, GPU certified nonviolations=111763384, unique transferred candidates=89569, exact=89555, unknown=0, pending=0 | 55964.55 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=111820863, GPU certified nonviolations=111820728, unique transferred candidates=89617, exact=89609, unknown=0, pending=0 | 55957.94 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=111878207, GPU certified nonviolations=111878072, unique transferred candidates=89658, exact=89650, unknown=0, pending=0 | 55965.03 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=111935551, GPU certified nonviolations=111935416, unique transferred candidates=89714, exact=89702, unknown=0, pending=0 | 55970.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=111992895, GPU certified nonviolations=111992760, unique transferred candidates=89754, exact=89738, unknown=0, pending=0 | 55972.05 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=112050239, GPU certified nonviolations=112050104, unique transferred candidates=89787, exact=89771, unknown=0, pending=0 | 55967.87 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:02:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=112107583, GPU certified nonviolations=112107448, unique transferred candidates=89843, exact=89835, unknown=0, pending=0 | 55974.01 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=112164927, GPU certified nonviolations=112164792, unique transferred candidates=89891, exact=89875, unknown=0, pending=0 | 55976.06 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=112222271, GPU certified nonviolations=112222136, unique transferred candidates=89931, exact=89916, unknown=0, pending=0 | 55970.74 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=112279615, GPU certified nonviolations=112279480, unique transferred candidates=89974, exact=89966, unknown=0, pending=0 | 55969.81 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=112336959, GPU certified nonviolations=112336824, unique transferred candidates=90030, exact=90018, unknown=0, pending=0 | 55974.23 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=112394303, GPU certified nonviolations=112394168, unique transferred candidates=90070, exact=90058, unknown=0, pending=0 | 55970.97 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=112451647, GPU certified nonviolations=112451512, unique transferred candidates=90105, exact=90094, unknown=0, pending=0 | 55965.65 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=112508991, GPU certified nonviolations=112508855, unique transferred candidates=90162, exact=90154, unknown=0, pending=0 | 55971.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=112566335, GPU certified nonviolations=112566199, unique transferred candidates=90210, exact=90202, unknown=0, pending=0 | 55976.77 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=112623679, GPU certified nonviolations=112623543, unique transferred candidates=90258, exact=90242, unknown=0, pending=0 | 55975.32 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=112681023, GPU certified nonviolations=112680887, unique transferred candidates=90292, exact=90284, unknown=0, pending=0 | 55970.95 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=112738367, GPU certified nonviolations=112738231, unique transferred candidates=90348, exact=90338, unknown=0, pending=0 | 55976.73 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=112795711, GPU certified nonviolations=112795575, unique transferred candidates=90388, exact=90380, unknown=0, pending=0 | 55980.85 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=112853055, GPU certified nonviolations=112852919, unique transferred candidates=90428, exact=90418, unknown=0, pending=0 | 55976.93 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=112910399, GPU certified nonviolations=112910263, unique transferred candidates=90476, exact=90468, unknown=0, pending=0 | 55982.35 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=112967743, GPU certified nonviolations=112967607, unique transferred candidates=90524, exact=90510, unknown=0, pending=0 | 55986.91 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=113025087, GPU certified nonviolations=113024951, unique transferred candidates=90572, exact=90556, unknown=0, pending=0 | 55987.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=113082431, GPU certified nonviolations=113082295, unique transferred candidates=90601, exact=90584, unknown=0, pending=0 | 55982.87 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=113139775, GPU certified nonviolations=113139638, unique transferred candidates=90663, exact=90655, unknown=0, pending=0 | 55988.01 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=113197119, GPU certified nonviolations=113196982, unique transferred candidates=90703, exact=90690, unknown=0, pending=0 | 55991.74 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=113254463, GPU certified nonviolations=113254326, unique transferred candidates=90751, exact=90743, unknown=0, pending=0 | 55983.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=113311807, GPU certified nonviolations=113311670, unique transferred candidates=90794, exact=90784, unknown=0, pending=0 | 55990.05 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=113369151, GPU certified nonviolations=113369014, unique transferred candidates=90850, exact=90838, unknown=0, pending=0 | 55997.26 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=113426495, GPU certified nonviolations=113426358, unique transferred candidates=90890, exact=90879, unknown=0, pending=0 | 55998.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=113483839, GPU certified nonviolations=113483702, unique transferred candidates=90923, exact=90907, unknown=0, pending=0 | 55994.36 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=113541183, GPU certified nonviolations=113541046, unique transferred candidates=90982, exact=90974, unknown=0, pending=0 | 56000.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=113598527, GPU certified nonviolations=113598390, unique transferred candidates=91030, exact=91018, unknown=0, pending=0 | 56002.61 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=113655871, GPU certified nonviolations=113655734, unique transferred candidates=91070, exact=91055, unknown=0, pending=0 | 55999.39 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=113713215, GPU certified nonviolations=113713078, unique transferred candidates=91113, exact=91105, unknown=0, pending=0 | 55996.31 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=113770559, GPU certified nonviolations=113770422, unique transferred candidates=91169, exact=91157, unknown=0, pending=0 | 56004.38 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=113827903, GPU certified nonviolations=113827766, unique transferred candidates=91209, exact=91195, unknown=0, pending=0 | 56007.86 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=113885247, GPU certified nonviolations=113885110, unique transferred candidates=91244, exact=91233, unknown=0, pending=0 | 56001.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=113942591, GPU certified nonviolations=113942454, unique transferred candidates=91300, exact=91292, unknown=0, pending=0 | 56008.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=113999935, GPU certified nonviolations=113999798, unique transferred candidates=91348, exact=91340, unknown=0, pending=0 | 56015.23 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=114057279, GPU certified nonviolations=114057142, unique transferred candidates=91396, exact=91380, unknown=0, pending=0 | 56014.33 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=114114623, GPU certified nonviolations=114114486, unique transferred candidates=91431, exact=91423, unknown=0, pending=0 | 56005.97 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=114171967, GPU certified nonviolations=114171830, unique transferred candidates=91487, exact=91475, unknown=0, pending=0 | 56011.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=114229311, GPU certified nonviolations=114229174, unique transferred candidates=91527, exact=91518, unknown=0, pending=0 | 56012.67 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=114286655, GPU certified nonviolations=114286518, unique transferred candidates=91567, exact=91559, unknown=0, pending=0 | 56007.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=114343999, GPU certified nonviolations=114343861, unique transferred candidates=91619, exact=91611, unknown=0, pending=0 | 56014.95 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=114401343, GPU certified nonviolations=114401205, unique transferred candidates=91667, exact=91655, unknown=0, pending=0 | 56021.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=114458687, GPU certified nonviolations=114458549, unique transferred candidates=91715, exact=91699, unknown=0, pending=0 | 56022.00 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=114516031, GPU certified nonviolations=114515893, unique transferred candidates=91743, exact=91727, unknown=0, pending=0 | 56018.36 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=114573375, GPU certified nonviolations=114573237, unique transferred candidates=91804, exact=91796, unknown=0, pending=0 | 56026.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=114630719, GPU certified nonviolations=114630581, unique transferred candidates=91844, exact=91832, unknown=0, pending=0 | 56030.97 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=114688063, GPU certified nonviolations=114687925, unique transferred candidates=91892, exact=91880, unknown=0, pending=0 | 56024.36 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=114745407, GPU certified nonviolations=114745269, unique transferred candidates=91934, exact=91926, unknown=0, pending=0 | 56033.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=114802751, GPU certified nonviolations=114802613, unique transferred candidates=91990, exact=91977, unknown=0, pending=0 | 56041.18 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:45+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=114810943, GPU certified nonviolations=114810805, unique transferred candidates=91990, exact=91990, unknown=0, pending=0 | 56032.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=114860095, GPU certified nonviolations=114859957, unique transferred candidates=92030, exact=92017, unknown=0, pending=0 | 56042.69 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=114917439, GPU certified nonviolations=114917301, unique transferred candidates=92063, exact=92047, unknown=0, pending=0 | 56038.05 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=114974783, GPU certified nonviolations=114974645, unique transferred candidates=92121, exact=92112, unknown=0, pending=0 | 56046.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=115032127, GPU certified nonviolations=115031989, unique transferred candidates=92169, exact=92155, unknown=0, pending=0 | 56053.65 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=115089471, GPU certified nonviolations=115089333, unique transferred candidates=92209, exact=92193, unknown=0, pending=0 | 56047.95 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=115146815, GPU certified nonviolations=115146677, unique transferred candidates=92251, exact=92243, unknown=0, pending=0 | 56042.89 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=115204159, GPU certified nonviolations=115204021, unique transferred candidates=92307, exact=92296, unknown=0, pending=0 | 56052.51 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=115261503, GPU certified nonviolations=115261365, unique transferred candidates=92347, exact=92335, unknown=0, pending=0 | 56055.60 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=115318847, GPU certified nonviolations=115318709, unique transferred candidates=92381, exact=92371, unknown=0, pending=0 | 56052.08 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=115376191, GPU certified nonviolations=115376053, unique transferred candidates=92436, exact=92428, unknown=0, pending=0 | 56058.76 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=115433535, GPU certified nonviolations=115433397, unique transferred candidates=92484, exact=92476, unknown=0, pending=0 | 56065.71 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=115490879, GPU certified nonviolations=115490741, unique transferred candidates=92532, exact=92516, unknown=0, pending=0 | 56061.98 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=115548223, GPU certified nonviolations=115548085, unique transferred candidates=92566, exact=92553, unknown=0, pending=0 | 56057.19 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=115605567, GPU certified nonviolations=115605429, unique transferred candidates=92622, exact=92611, unknown=0, pending=0 | 56065.78 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:03:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=115662911, GPU certified nonviolations=115662773, unique transferred candidates=92662, exact=92653, unknown=0, pending=0 | 56070.46 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=115720255, GPU certified nonviolations=115720117, unique transferred candidates=92702, exact=92694, unknown=0, pending=0 | 56063.91 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=115777599, GPU certified nonviolations=115777461, unique transferred candidates=92754, exact=92746, unknown=0, pending=0 | 56067.60 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=115834943, GPU certified nonviolations=115834805, unique transferred candidates=92802, exact=92790, unknown=0, pending=0 | 56073.88 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=115892287, GPU certified nonviolations=115892149, unique transferred candidates=92850, exact=92836, unknown=0, pending=0 | 56073.66 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=115949631, GPU certified nonviolations=115949493, unique transferred candidates=92878, exact=92862, unknown=0, pending=0 | 56068.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=116006975, GPU certified nonviolations=116006837, unique transferred candidates=92941, exact=92933, unknown=0, pending=0 | 56076.14 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=116064319, GPU certified nonviolations=116064181, unique transferred candidates=92981, exact=92969, unknown=0, pending=0 | 56077.94 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=116121663, GPU certified nonviolations=116121525, unique transferred candidates=93029, exact=93021, unknown=0, pending=0 | 56069.73 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=116179007, GPU certified nonviolations=116178869, unique transferred candidates=93072, exact=93064, unknown=0, pending=0 | 56075.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=116236351, GPU certified nonviolations=116236213, unique transferred candidates=93128, exact=93117, unknown=0, pending=0 | 56083.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=116293695, GPU certified nonviolations=116293557, unique transferred candidates=93168, exact=93155, unknown=0, pending=0 | 56084.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=116351039, GPU certified nonviolations=116350901, unique transferred candidates=93201, exact=93185, unknown=0, pending=0 | 56080.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=116408383, GPU certified nonviolations=116408245, unique transferred candidates=93258, exact=93250, unknown=0, pending=0 | 56086.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=116465727, GPU certified nonviolations=116465589, unique transferred candidates=93306, exact=93294, unknown=0, pending=0 | 56090.53 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=116523071, GPU certified nonviolations=116522933, unique transferred candidates=93346, exact=93333, unknown=0, pending=0 | 56086.46 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=116580415, GPU certified nonviolations=116580277, unique transferred candidates=93389, exact=93381, unknown=0, pending=0 | 56086.00 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=116637759, GPU certified nonviolations=116637621, unique transferred candidates=93445, exact=93436, unknown=0, pending=0 | 56093.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=116695103, GPU certified nonviolations=116694965, unique transferred candidates=93485, exact=93473, unknown=0, pending=0 | 56095.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=116752447, GPU certified nonviolations=116752309, unique transferred candidates=93518, exact=93509, unknown=0, pending=0 | 56090.26 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=116809791, GPU certified nonviolations=116809653, unique transferred candidates=93573, exact=93565, unknown=0, pending=0 | 56097.15 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=116867135, GPU certified nonviolations=116866997, unique transferred candidates=93621, exact=93611, unknown=0, pending=0 | 56102.69 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=116924479, GPU certified nonviolations=116924341, unique transferred candidates=93669, exact=93655, unknown=0, pending=0 | 56100.40 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=116981823, GPU certified nonviolations=116981685, unique transferred candidates=93701, exact=93691, unknown=0, pending=0 | 56098.17 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=117039167, GPU certified nonviolations=117039029, unique transferred candidates=93757, exact=93746, unknown=0, pending=0 | 56102.55 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=117096511, GPU certified nonviolations=117096373, unique transferred candidates=93797, exact=93788, unknown=0, pending=0 | 56106.42 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=117153855, GPU certified nonviolations=117153717, unique transferred candidates=93837, exact=93829, unknown=0, pending=0 | 56101.15 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=117211199, GPU certified nonviolations=117211061, unique transferred candidates=93889, exact=93881, unknown=0, pending=0 | 56106.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=117268543, GPU certified nonviolations=117268405, unique transferred candidates=93937, exact=93923, unknown=0, pending=0 | 56111.11 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=117325887, GPU certified nonviolations=117325749, unique transferred candidates=93984, exact=93968, unknown=0, pending=0 | 56110.90 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=117383231, GPU certified nonviolations=117383093, unique transferred candidates=94014, exact=93997, unknown=0, pending=0 | 56107.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=117440575, GPU certified nonviolations=117440437, unique transferred candidates=94073, exact=94065, unknown=0, pending=0 | 56114.66 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=117497919, GPU certified nonviolations=117497781, unique transferred candidates=94113, exact=94101, unknown=0, pending=0 | 56117.76 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=117555263, GPU certified nonviolations=117555125, unique transferred candidates=94161, exact=94153, unknown=0, pending=0 | 56111.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=117612607, GPU certified nonviolations=117612469, unique transferred candidates=94202, exact=94194, unknown=0, pending=0 | 56117.12 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=117669951, GPU certified nonviolations=117669813, unique transferred candidates=94258, exact=94246, unknown=0, pending=0 | 56122.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=117727295, GPU certified nonviolations=117727157, unique transferred candidates=94298, exact=94287, unknown=0, pending=0 | 56123.12 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=117784639, GPU certified nonviolations=117784501, unique transferred candidates=94331, exact=94315, unknown=0, pending=0 | 56119.12 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=117841983, GPU certified nonviolations=117841845, unique transferred candidates=94388, exact=94380, unknown=0, pending=0 | 56126.81 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=117899327, GPU certified nonviolations=117899189, unique transferred candidates=94436, exact=94424, unknown=0, pending=0 | 56130.05 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=117956671, GPU certified nonviolations=117956533, unique transferred candidates=94476, exact=94460, unknown=0, pending=0 | 56126.61 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=118014015, GPU certified nonviolations=118013877, unique transferred candidates=94517, exact=94509, unknown=0, pending=0 | 56122.76 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=118071359, GPU certified nonviolations=118071221, unique transferred candidates=94573, exact=94565, unknown=0, pending=0 | 56129.97 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=118128703, GPU certified nonviolations=118128565, unique transferred candidates=94613, exact=94601, unknown=0, pending=0 | 56132.39 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=118186047, GPU certified nonviolations=118185909, unique transferred candidates=94650, exact=94637, unknown=0, pending=0 | 56129.56 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=118243391, GPU certified nonviolations=118243253, unique transferred candidates=94706, exact=94698, unknown=0, pending=0 | 56135.92 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=118300735, GPU certified nonviolations=118300597, unique transferred candidates=94754, exact=94745, unknown=0, pending=0 | 56139.08 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=118358079, GPU certified nonviolations=118357941, unique transferred candidates=94802, exact=94789, unknown=0, pending=0 | 56138.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:45+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=118374463, GPU certified nonviolations=118374325, unique transferred candidates=94810, exact=94802, unknown=0, pending=0 | 56126.15 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=118415423, GPU certified nonviolations=118415285, unique transferred candidates=94836, exact=94828, unknown=0, pending=0 | 56133.83 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=118472767, GPU certified nonviolations=118472629, unique transferred candidates=94892, exact=94881, unknown=0, pending=0 | 56140.36 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=118530111, GPU certified nonviolations=118529973, unique transferred candidates=94932, exact=94924, unknown=0, pending=0 | 56142.85 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=118587455, GPU certified nonviolations=118587317, unique transferred candidates=94972, exact=94960, unknown=0, pending=0 | 56138.40 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=118644799, GPU certified nonviolations=118644661, unique transferred candidates=95022, exact=95014, unknown=0, pending=0 | 56144.70 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=118702143, GPU certified nonviolations=118702005, unique transferred candidates=95070, exact=95058, unknown=0, pending=0 | 56150.92 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=118759487, GPU certified nonviolations=118759349, unique transferred candidates=95118, exact=95103, unknown=0, pending=0 | 56151.22 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=118816831, GPU certified nonviolations=118816693, unique transferred candidates=95146, exact=95130, unknown=0, pending=0 | 56147.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=118874175, GPU certified nonviolations=118874037, unique transferred candidates=95207, exact=95197, unknown=0, pending=0 | 56155.87 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=118931519, GPU certified nonviolations=118931381, unique transferred candidates=95247, exact=95235, unknown=0, pending=0 | 56159.17 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=118988863, GPU certified nonviolations=118988725, unique transferred candidates=95295, exact=95283, unknown=0, pending=0 | 56149.98 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=119046207, GPU certified nonviolations=119046069, unique transferred candidates=95337, exact=95329, unknown=0, pending=0 | 56155.70 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=119103551, GPU certified nonviolations=119103413, unique transferred candidates=95393, exact=95381, unknown=0, pending=0 | 56163.84 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=119160895, GPU certified nonviolations=119160757, unique transferred candidates=95433, exact=95417, unknown=0, pending=0 | 56165.47 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=119218239, GPU certified nonviolations=119218101, unique transferred candidates=95466, exact=95450, unknown=0, pending=0 | 56160.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:04:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=119275583, GPU certified nonviolations=119275445, unique transferred candidates=95524, exact=95516, unknown=0, pending=0 | 56168.16 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=119332927, GPU certified nonviolations=119332789, unique transferred candidates=95572, exact=95560, unknown=0, pending=0 | 56171.72 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=119390271, GPU certified nonviolations=119390133, unique transferred candidates=95612, exact=95596, unknown=0, pending=0 | 56169.17 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=119447615, GPU certified nonviolations=119447477, unique transferred candidates=95655, exact=95647, unknown=0, pending=0 | 56163.15 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=119504959, GPU certified nonviolations=119504821, unique transferred candidates=95711, exact=95699, unknown=0, pending=0 | 56169.55 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=119562303, GPU certified nonviolations=119562165, unique transferred candidates=95751, exact=95739, unknown=0, pending=0 | 56171.56 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=119619647, GPU certified nonviolations=119619509, unique transferred candidates=95785, exact=95775, unknown=0, pending=0 | 56168.20 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=119676991, GPU certified nonviolations=119676853, unique transferred candidates=95841, exact=95833, unknown=0, pending=0 | 56174.18 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=119734335, GPU certified nonviolations=119734197, unique transferred candidates=95889, exact=95881, unknown=0, pending=0 | 56181.06 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=119791679, GPU certified nonviolations=119791541, unique transferred candidates=95937, exact=95921, unknown=0, pending=0 | 56179.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=119849023, GPU certified nonviolations=119848885, unique transferred candidates=95970, exact=95962, unknown=0, pending=0 | 56174.65 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=119906367, GPU certified nonviolations=119906229, unique transferred candidates=96026, exact=96018, unknown=0, pending=0 | 56182.44 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=119963711, GPU certified nonviolations=119963573, unique transferred candidates=96066, exact=96056, unknown=0, pending=0 | 56184.32 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=120021055, GPU certified nonviolations=120020917, unique transferred candidates=96106, exact=96097, unknown=0, pending=0 | 56178.56 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=120078399, GPU certified nonviolations=120078261, unique transferred candidates=96156, exact=96148, unknown=0, pending=0 | 56185.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=120135743, GPU certified nonviolations=120135605, unique transferred candidates=96204, exact=96192, unknown=0, pending=0 | 56192.11 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=120193087, GPU certified nonviolations=120192949, unique transferred candidates=96252, exact=96238, unknown=0, pending=0 | 56190.83 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=120250431, GPU certified nonviolations=120250293, unique transferred candidates=96281, exact=96264, unknown=0, pending=0 | 56186.40 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=120307775, GPU certified nonviolations=120307637, unique transferred candidates=96340, exact=96332, unknown=0, pending=0 | 56195.08 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=120365119, GPU certified nonviolations=120364981, unique transferred candidates=96380, exact=96368, unknown=0, pending=0 | 56200.75 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=120422463, GPU certified nonviolations=120422325, unique transferred candidates=96428, exact=96420, unknown=0, pending=0 | 56193.91 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=120479807, GPU certified nonviolations=120479668, unique transferred candidates=96471, exact=96463, unknown=0, pending=0 | 56197.77 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=120537151, GPU certified nonviolations=120537012, unique transferred candidates=96527, exact=96514, unknown=0, pending=0 | 56204.49 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=120594495, GPU certified nonviolations=120594356, unique transferred candidates=96567, exact=96555, unknown=0, pending=0 | 56207.74 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=120651839, GPU certified nonviolations=120651700, unique transferred candidates=96600, exact=96583, unknown=0, pending=0 | 56204.23 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=120709183, GPU certified nonviolations=120709044, unique transferred candidates=96659, exact=96651, unknown=0, pending=0 | 56210.56 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=120766527, GPU certified nonviolations=120766388, unique transferred candidates=96707, exact=96695, unknown=0, pending=0 | 56216.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=120823871, GPU certified nonviolations=120823732, unique transferred candidates=96747, exact=96731, unknown=0, pending=0 | 56212.35 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=120881215, GPU certified nonviolations=120881076, unique transferred candidates=96788, exact=96780, unknown=0, pending=0 | 56210.13 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=120938559, GPU certified nonviolations=120938420, unique transferred candidates=96844, exact=96832, unknown=0, pending=0 | 56216.00 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=120995903, GPU certified nonviolations=120995764, unique transferred candidates=96884, exact=96872, unknown=0, pending=0 | 56217.52 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=121053247, GPU certified nonviolations=121053108, unique transferred candidates=96917, exact=96908, unknown=0, pending=0 | 56212.86 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=121110591, GPU certified nonviolations=121110452, unique transferred candidates=96972, exact=96964, unknown=0, pending=0 | 56219.27 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=121167935, GPU certified nonviolations=121167796, unique transferred candidates=97020, exact=97012, unknown=0, pending=0 | 56226.04 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=121225279, GPU certified nonviolations=121225140, unique transferred candidates=97068, exact=97052, unknown=0, pending=0 | 56224.04 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=121282623, GPU certified nonviolations=121282484, unique transferred candidates=97102, exact=97092, unknown=0, pending=0 | 56218.69 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=121339967, GPU certified nonviolations=121339828, unique transferred candidates=97158, exact=97150, unknown=0, pending=0 | 56227.74 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=121397311, GPU certified nonviolations=121397172, unique transferred candidates=97198, exact=97189, unknown=0, pending=0 | 56231.72 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=121454655, GPU certified nonviolations=121454516, unique transferred candidates=97238, exact=97230, unknown=0, pending=0 | 56225.76 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=121511999, GPU certified nonviolations=121511860, unique transferred candidates=97288, exact=97280, unknown=0, pending=0 | 56230.69 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=121569343, GPU certified nonviolations=121569204, unique transferred candidates=97336, exact=97327, unknown=0, pending=0 | 56237.81 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=121626687, GPU certified nonviolations=121626548, unique transferred candidates=97384, exact=97372, unknown=0, pending=0 | 56239.86 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=121684031, GPU certified nonviolations=121683892, unique transferred candidates=97413, exact=97396, unknown=0, pending=0 | 56234.71 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=121741375, GPU certified nonviolations=121741236, unique transferred candidates=97472, exact=97463, unknown=0, pending=0 | 56240.84 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=121798719, GPU certified nonviolations=121798580, unique transferred candidates=97512, exact=97500, unknown=0, pending=0 | 56245.32 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=121856063, GPU certified nonviolations=121855924, unique transferred candidates=97560, exact=97548, unknown=0, pending=0 | 56238.02 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=121913407, GPU certified nonviolations=121913268, unique transferred candidates=97602, exact=97594, unknown=0, pending=0 | 56238.33 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=121970751, GPU certified nonviolations=121970612, unique transferred candidates=97658, exact=97648, unknown=0, pending=0 | 56242.49 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:45+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=121978943, GPU certified nonviolations=121978804, unique transferred candidates=97658, exact=97658, unknown=0, pending=0 | 56235.24 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=122028095, GPU certified nonviolations=122027956, unique transferred candidates=97698, exact=97686, unknown=0, pending=0 | 56245.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=122085439, GPU certified nonviolations=122085300, unique transferred candidates=97731, exact=97715, unknown=0, pending=0 | 56240.81 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=122142783, GPU certified nonviolations=122142644, unique transferred candidates=97788, exact=97780, unknown=0, pending=0 | 56247.51 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=122200127, GPU certified nonviolations=122199988, unique transferred candidates=97836, exact=97824, unknown=0, pending=0 | 56252.40 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=122257471, GPU certified nonviolations=122257332, unique transferred candidates=97876, exact=97860, unknown=0, pending=0 | 56250.06 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=122314815, GPU certified nonviolations=122314676, unique transferred candidates=97918, exact=97910, unknown=0, pending=0 | 56249.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=122372159, GPU certified nonviolations=122372020, unique transferred candidates=97974, exact=97964, unknown=0, pending=0 | 56254.04 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=122429503, GPU certified nonviolations=122429364, unique transferred candidates=98014, exact=98002, unknown=0, pending=0 | 56257.05 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=122486847, GPU certified nonviolations=122486708, unique transferred candidates=98048, exact=98038, unknown=0, pending=0 | 56253.61 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=122544191, GPU certified nonviolations=122544052, unique transferred candidates=98104, exact=98096, unknown=0, pending=0 | 56260.06 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=122601535, GPU certified nonviolations=122601396, unique transferred candidates=98152, exact=98144, unknown=0, pending=0 | 56266.64 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=122658879, GPU certified nonviolations=122658740, unique transferred candidates=98200, exact=98187, unknown=0, pending=0 | 56264.63 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=122716223, GPU certified nonviolations=122716084, unique transferred candidates=98232, exact=98224, unknown=0, pending=0 | 56259.32 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=122773567, GPU certified nonviolations=122773428, unique transferred candidates=98288, exact=98279, unknown=0, pending=0 | 56266.16 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:05:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=122830911, GPU certified nonviolations=122830772, unique transferred candidates=98328, exact=98320, unknown=0, pending=0 | 56267.04 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=122888255, GPU certified nonviolations=122888116, unique transferred candidates=98368, exact=98358, unknown=0, pending=0 | 56263.08 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=122945599, GPU certified nonviolations=122945460, unique transferred candidates=98417, exact=98409, unknown=0, pending=0 | 56268.48 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=123002943, GPU certified nonviolations=123002804, unique transferred candidates=98465, exact=98453, unknown=0, pending=0 | 56271.79 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=123060287, GPU certified nonviolations=123060148, unique transferred candidates=98513, exact=98501, unknown=0, pending=0 | 56271.96 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=123117631, GPU certified nonviolations=123117492, unique transferred candidates=98541, exact=98525, unknown=0, pending=0 | 56268.38 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=123174975, GPU certified nonviolations=123174836, unique transferred candidates=98602, exact=98592, unknown=0, pending=0 | 56274.33 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=123232319, GPU certified nonviolations=123232180, unique transferred candidates=98642, exact=98630, unknown=0, pending=0 | 56278.53 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=123289663, GPU certified nonviolations=123289524, unique transferred candidates=98690, exact=98678, unknown=0, pending=0 | 56272.76 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=123347007, GPU certified nonviolations=123346868, unique transferred candidates=98732, exact=98724, unknown=0, pending=0 | 56276.96 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=123404351, GPU certified nonviolations=123404212, unique transferred candidates=98788, exact=98775, unknown=0, pending=0 | 56283.42 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=123461695, GPU certified nonviolations=123461556, unique transferred candidates=98828, exact=98816, unknown=0, pending=0 | 56285.65 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=123519039, GPU certified nonviolations=123518900, unique transferred candidates=98861, exact=98845, unknown=0, pending=0 | 56281.66 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=123576383, GPU certified nonviolations=123576244, unique transferred candidates=98917, exact=98909, unknown=0, pending=0 | 56288.16 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=123633727, GPU certified nonviolations=123633588, unique transferred candidates=98965, exact=98951, unknown=0, pending=0 | 56292.94 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=123691071, GPU certified nonviolations=123690932, unique transferred candidates=99005, exact=98989, unknown=0, pending=0 | 56288.93 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=123748415, GPU certified nonviolations=123748276, unique transferred candidates=99048, exact=99040, unknown=0, pending=0 | 56287.14 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=123805759, GPU certified nonviolations=123805620, unique transferred candidates=99104, exact=99094, unknown=0, pending=0 | 56295.23 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=123863103, GPU certified nonviolations=123862964, unique transferred candidates=99144, exact=99129, unknown=0, pending=0 | 56296.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=123920447, GPU certified nonviolations=123920308, unique transferred candidates=99177, exact=99168, unknown=0, pending=0 | 56290.95 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=123977791, GPU certified nonviolations=123977652, unique transferred candidates=99233, exact=99225, unknown=0, pending=0 | 56295.61 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=124035135, GPU certified nonviolations=124034996, unique transferred candidates=99281, exact=99273, unknown=0, pending=0 | 56301.35 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=124092479, GPU certified nonviolations=124092340, unique transferred candidates=99326, exact=99310, unknown=0, pending=0 | 56299.22 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=124149823, GPU certified nonviolations=124149683, unique transferred candidates=99364, exact=99355, unknown=0, pending=0 | 56294.47 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=124207167, GPU certified nonviolations=124207027, unique transferred candidates=99420, exact=99410, unknown=0, pending=0 | 56303.23 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=124264511, GPU certified nonviolations=124264371, unique transferred candidates=99460, exact=99448, unknown=0, pending=0 | 56306.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=124321855, GPU certified nonviolations=124321715, unique transferred candidates=99500, exact=99488, unknown=0, pending=0 | 56299.60 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=124379199, GPU certified nonviolations=124379059, unique transferred candidates=99549, exact=99540, unknown=0, pending=0 | 56305.65 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=124436543, GPU certified nonviolations=124436403, unique transferred candidates=99597, exact=99585, unknown=0, pending=0 | 56312.07 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=124493887, GPU certified nonviolations=124493747, unique transferred candidates=99645, exact=99629, unknown=0, pending=0 | 56312.08 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:28+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=124551231, GPU certified nonviolations=124551091, unique transferred candidates=99674, exact=99657, unknown=0, pending=0 | 56308.23 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=124608575, GPU certified nonviolations=124608435, unique transferred candidates=99734, exact=99724, unknown=0, pending=0 | 56314.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=124665919, GPU certified nonviolations=124665779, unique transferred candidates=99774, exact=99761, unknown=0, pending=0 | 56320.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=124723263, GPU certified nonviolations=124723123, unique transferred candidates=99822, exact=99814, unknown=0, pending=0 | 56314.11 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=124780607, GPU certified nonviolations=124780467, unique transferred candidates=99866, exact=99858, unknown=0, pending=0 | 56319.34 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:32+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=124837951, GPU certified nonviolations=124837811, unique transferred candidates=99922, exact=99910, unknown=0, pending=0 | 56324.21 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=124895295, GPU certified nonviolations=124895155, unique transferred candidates=99962, exact=99947, unknown=0, pending=0 | 56324.27 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=124952639, GPU certified nonviolations=124952499, unique transferred candidates=99995, exact=99980, unknown=0, pending=0 | 56318.77 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=125009983, GPU certified nonviolations=125009843, unique transferred candidates=100053, exact=100045, unknown=0, pending=0 | 56325.69 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=125067327, GPU certified nonviolations=125067187, unique transferred candidates=100101, exact=100088, unknown=0, pending=0 | 56324.61 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=125124671, GPU certified nonviolations=125124531, unique transferred candidates=100141, exact=100126, unknown=0, pending=0 | 56321.08 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=125182015, GPU certified nonviolations=125181875, unique transferred candidates=100183, exact=100175, unknown=0, pending=0 | 56320.28 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=125239359, GPU certified nonviolations=125239219, unique transferred candidates=100239, exact=100231, unknown=0, pending=0 | 56327.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=125296703, GPU certified nonviolations=125296563, unique transferred candidates=100279, exact=100267, unknown=0, pending=0 | 56330.26 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=125354047, GPU certified nonviolations=125353907, unique transferred candidates=100314, exact=100303, unknown=0, pending=0 | 56317.61 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=125411391, GPU certified nonviolations=125411251, unique transferred candidates=100370, exact=100361, unknown=0, pending=0 | 56318.32 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=125468735, GPU certified nonviolations=125468595, unique transferred candidates=100418, exact=100410, unknown=0, pending=0 | 56319.23 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=125526079, GPU certified nonviolations=125525939, unique transferred candidates=100466, exact=100452, unknown=0, pending=0 | 56315.15 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:46+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=125534271, GPU certified nonviolations=125534131, unique transferred candidates=100466, exact=100466, unknown=0, pending=0 | 56302.74 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=125583423, GPU certified nonviolations=125583282, unique transferred candidates=100500, exact=100490, unknown=0, pending=0 | 56310.50 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=125640767, GPU certified nonviolations=125640626, unique transferred candidates=100556, exact=100547, unknown=0, pending=0 | 56318.47 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=125698111, GPU certified nonviolations=125697970, unique transferred candidates=100596, exact=100588, unknown=0, pending=0 | 56321.58 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=125755455, GPU certified nonviolations=125755314, unique transferred candidates=100636, exact=100623, unknown=0, pending=0 | 56312.75 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=125812799, GPU certified nonviolations=125812657, unique transferred candidates=100685, exact=100677, unknown=0, pending=0 | 56316.30 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=125870143, GPU certified nonviolations=125870001, unique transferred candidates=100733, exact=100721, unknown=0, pending=0 | 56322.73 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=125927487, GPU certified nonviolations=125927345, unique transferred candidates=100781, exact=100765, unknown=0, pending=0 | 56320.70 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=125984831, GPU certified nonviolations=125984689, unique transferred candidates=100810, exact=100793, unknown=0, pending=0 | 56315.87 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=126042175, GPU certified nonviolations=126042033, unique transferred candidates=100871, exact=100862, unknown=0, pending=0 | 56322.08 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=126099519, GPU certified nonviolations=126099377, unique transferred candidates=100911, exact=100898, unknown=0, pending=0 | 56323.79 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=126156863, GPU certified nonviolations=126156721, unique transferred candidates=100959, exact=100948, unknown=0, pending=0 | 56316.26 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=126214207, GPU certified nonviolations=126214065, unique transferred candidates=100999, exact=100991, unknown=0, pending=0 | 56323.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=126271551, GPU certified nonviolations=126271409, unique transferred candidates=101055, exact=101043, unknown=0, pending=0 | 56326.41 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:06:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=126328895, GPU certified nonviolations=126328753, unique transferred candidates=101095, exact=101082, unknown=0, pending=0 | 56324.67 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=126386239, GPU certified nonviolations=126386097, unique transferred candidates=101128, exact=101112, unknown=0, pending=0 | 56319.27 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=126443583, GPU certified nonviolations=126443441, unique transferred candidates=101186, exact=101178, unknown=0, pending=0 | 56324.47 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:02+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=126500927, GPU certified nonviolations=126500785, unique transferred candidates=101234, exact=101222, unknown=0, pending=0 | 56327.16 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=126558271, GPU certified nonviolations=126558129, unique transferred candidates=101274, exact=101260, unknown=0, pending=0 | 56323.35 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=126615615, GPU certified nonviolations=126615473, unique transferred candidates=101317, exact=101309, unknown=0, pending=0 | 56319.83 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=126672959, GPU certified nonviolations=126672817, unique transferred candidates=101373, exact=101361, unknown=0, pending=0 | 56324.62 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=126730303, GPU certified nonviolations=126730161, unique transferred candidates=101413, exact=101399, unknown=0, pending=0 | 56321.93 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=126787647, GPU certified nonviolations=126787505, unique transferred candidates=101445, exact=101437, unknown=0, pending=0 | 56316.52 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=126844991, GPU certified nonviolations=126844849, unique transferred candidates=101501, exact=101493, unknown=0, pending=0 | 56322.63 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=126902335, GPU certified nonviolations=126902193, unique transferred candidates=101549, exact=101540, unknown=0, pending=0 | 56324.36 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=126959679, GPU certified nonviolations=126959537, unique transferred candidates=101597, exact=101585, unknown=0, pending=0 | 56322.05 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=127017023, GPU certified nonviolations=127016881, unique transferred candidates=101630, exact=101622, unknown=0, pending=0 | 56315.25 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=127074367, GPU certified nonviolations=127074225, unique transferred candidates=101686, exact=101674, unknown=0, pending=0 | 56319.38 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=127131711, GPU certified nonviolations=127131569, unique transferred candidates=101726, exact=101718, unknown=0, pending=0 | 56320.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=127189055, GPU certified nonviolations=127188913, unique transferred candidates=101766, exact=101756, unknown=0, pending=0 | 56314.59 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=127246399, GPU certified nonviolations=127246257, unique transferred candidates=101820, exact=101812, unknown=0, pending=0 | 56319.91 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=127303743, GPU certified nonviolations=127303601, unique transferred candidates=101868, exact=101854, unknown=0, pending=0 | 56323.39 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=127361087, GPU certified nonviolations=127360945, unique transferred candidates=101916, exact=101904, unknown=0, pending=0 | 56323.13 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=127418431, GPU certified nonviolations=127418289, unique transferred candidates=101945, exact=101928, unknown=0, pending=0 | 56316.70 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:19+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=127475775, GPU certified nonviolations=127475633, unique transferred candidates=102007, exact=101996, unknown=0, pending=0 | 56321.45 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:20+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=127533119, GPU certified nonviolations=127532977, unique transferred candidates=102047, exact=102035, unknown=0, pending=0 | 56324.92 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:21+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=127590463, GPU certified nonviolations=127590321, unique transferred candidates=102095, exact=102082, unknown=0, pending=0 | 56316.33 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:22+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=127647807, GPU certified nonviolations=127647664, unique transferred candidates=102137, exact=102129, unknown=0, pending=0 | 56319.35 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:23+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=127705151, GPU certified nonviolations=127705008, unique transferred candidates=102193, exact=102181, unknown=0, pending=0 | 56322.62 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:24+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=127762495, GPU certified nonviolations=127762352, unique transferred candidates=102233, exact=102221, unknown=0, pending=0 | 56324.06 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:25+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=127819839, GPU certified nonviolations=127819696, unique transferred candidates=102266, exact=102250, unknown=0, pending=0 | 56318.74 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:26+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=127877183, GPU certified nonviolations=127877040, unique transferred candidates=102321, exact=102313, unknown=0, pending=0 | 56324.92 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:27+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=127934527, GPU certified nonviolations=127934384, unique transferred candidates=102369, exact=102357, unknown=0, pending=0 | 56325.17 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:29+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=127991871, GPU certified nonviolations=127991728, unique transferred candidates=102409, exact=102393, unknown=0, pending=0 | 56319.00 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:30+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=128049215, GPU certified nonviolations=128049072, unique transferred candidates=102450, exact=102442, unknown=0, pending=0 | 56317.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=128106559, GPU certified nonviolations=128106416, unique transferred candidates=102506, exact=102496, unknown=0, pending=0 | 56320.15 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:31+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=128163903, GPU certified nonviolations=128163760, unique transferred candidates=102546, exact=102534, unknown=0, pending=0 | 56321.40 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:33+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=128221247, GPU certified nonviolations=128221104, unique transferred candidates=102583, exact=102570, unknown=0, pending=0 | 56313.68 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:34+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=128278591, GPU certified nonviolations=128278448, unique transferred candidates=102639, exact=102630, unknown=0, pending=0 | 56320.96 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:35+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=128335935, GPU certified nonviolations=128335792, unique transferred candidates=102687, exact=102678, unknown=0, pending=0 | 56321.81 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:36+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=128393279, GPU certified nonviolations=128393136, unique transferred candidates=102735, exact=102719, unknown=0, pending=0 | 56319.53 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:37+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=128450623, GPU certified nonviolations=128450480, unique transferred candidates=102767, exact=102759, unknown=0, pending=0 | 56313.61 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:38+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=128507967, GPU certified nonviolations=128507824, unique transferred candidates=102823, exact=102813, unknown=0, pending=0 | 56316.29 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:39+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=128565311, GPU certified nonviolations=128565168, unique transferred candidates=102863, exact=102854, unknown=0, pending=0 | 56318.35 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:40+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=128622655, GPU certified nonviolations=128622512, unique transferred candidates=102903, exact=102895, unknown=0, pending=0 | 56310.34 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:41+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=128679999, GPU certified nonviolations=128679855, unique transferred candidates=102953, exact=102945, unknown=0, pending=0 | 56313.02 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:42+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=128737343, GPU certified nonviolations=128737199, unique transferred candidates=103001, exact=102989, unknown=0, pending=0 | 56318.94 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:43+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=128794687, GPU certified nonviolations=128794543, unique transferred candidates=103049, exact=103033, unknown=0, pending=0 | 56317.80 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:44+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=128852031, GPU certified nonviolations=128851887, unique transferred candidates=103078, exact=103061, unknown=0, pending=0 | 56308.15 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:45+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=128909375, GPU certified nonviolations=128909231, unique transferred candidates=103140, exact=103129, unknown=0, pending=0 | 56315.04 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:46+00:00 | 20261115T192936-gpu-seed20261119 | progress | device=cuda, GPU pipeline | generated draws=128942143, GPU certified nonviolations=128941999, unique transferred candidates=103164, exact=103152, unknown=0, pending=0 | 56314.19 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:46+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=128966719, GPU certified nonviolations=128966575, unique transferred candidates=103180, exact=103168, unknown=0, pending=0 | 56317.81 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:47+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=129024063, GPU certified nonviolations=129023919, unique transferred candidates=103228, exact=103220, unknown=0, pending=0 | 56310.07 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:48+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=129081407, GPU certified nonviolations=129081263, unique transferred candidates=103269, exact=103261, unknown=0, pending=0 | 56311.60 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:49+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=129138751, GPU certified nonviolations=129138607, unique transferred candidates=103325, exact=103313, unknown=0, pending=0 | 56317.71 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:50+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=129196095, GPU certified nonviolations=129195951, unique transferred candidates=103365, exact=103349, unknown=0, pending=0 | 56318.09 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:51+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=129253439, GPU certified nonviolations=129253295, unique transferred candidates=103398, exact=103382, unknown=0, pending=0 | 56311.34 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:52+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=129310783, GPU certified nonviolations=129310639, unique transferred candidates=103454, exact=103446, unknown=0, pending=0 | 56317.66 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:53+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=129368127, GPU certified nonviolations=129367983, unique transferred candidates=103502, exact=103489, unknown=0, pending=0 | 56321.42 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:54+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=129425471, GPU certified nonviolations=129425327, unique transferred candidates=103542, exact=103526, unknown=0, pending=0 | 56313.82 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:55+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=129482815, GPU certified nonviolations=129482671, unique transferred candidates=103582, exact=103574, unknown=0, pending=0 | 56309.98 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:56+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=129540159, GPU certified nonviolations=129540015, unique transferred candidates=103637, exact=103625, unknown=0, pending=0 | 56314.49 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:57+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=129597503, GPU certified nonviolations=129597359, unique transferred candidates=103677, exact=103665, unknown=0, pending=0 | 56314.99 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:58+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=129654847, GPU certified nonviolations=129654703, unique transferred candidates=103709, exact=103701, unknown=0, pending=0 | 56309.35 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:07:59+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=129712191, GPU certified nonviolations=129712047, unique transferred candidates=103765, exact=103757, unknown=0, pending=0 | 56312.92 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:08:00+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=129769535, GPU certified nonviolations=129769391, unique transferred candidates=103813, exact=103805, unknown=0, pending=0 | 56314.96 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:08:01+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=129826879, GPU certified nonviolations=129826735, unique transferred candidates=103861, exact=103849, unknown=0, pending=0 | 56312.66 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:08:03+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=129884223, GPU certified nonviolations=129884079, unique transferred candidates=103893, exact=103885, unknown=0, pending=0 | 56306.35 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:08:04+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=129941567, GPU certified nonviolations=129941423, unique transferred candidates=103949, exact=103938, unknown=0, pending=0 | 56309.44 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:08:05+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=129998911, GPU certified nonviolations=129998767, unique transferred candidates=103989, exact=103981, unknown=0, pending=0 | 56309.96 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:08:06+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=130056255, GPU certified nonviolations=130056111, unique transferred candidates=104029, exact=104017, unknown=0, pending=0 | 56302.83 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:08:07+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=130113599, GPU certified nonviolations=130113455, unique transferred candidates=104078, exact=104070, unknown=0, pending=0 | 56307.93 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:08:08+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=130170943, GPU certified nonviolations=130170799, unique transferred candidates=104126, exact=104115, unknown=0, pending=0 | 56310.84 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:08:09+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=130228287, GPU certified nonviolations=130228143, unique transferred candidates=104174, exact=104162, unknown=0, pending=0 | 56310.54 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:08:10+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=130285631, GPU certified nonviolations=130285487, unique transferred candidates=104203, exact=104186, unknown=0, pending=0 | 56302.14 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:08:11+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=130342975, GPU certified nonviolations=130342831, unique transferred candidates=104264, exact=104255, unknown=0, pending=0 | 56307.61 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:08:12+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=130400319, GPU certified nonviolations=130400175, unique transferred candidates=104304, exact=104290, unknown=0, pending=0 | 56306.81 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:08:13+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=130457663, GPU certified nonviolations=130457519, unique transferred candidates=104352, exact=104342, unknown=0, pending=0 | 56299.03 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:08:14+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=130515007, GPU certified nonviolations=130514863, unique transferred candidates=104394, exact=104386, unknown=0, pending=0 | 56298.99 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:08:15+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=130572351, GPU certified nonviolations=130572207, unique transferred candidates=104450, exact=104438, unknown=0, pending=0 | 56303.35 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:08:16+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=130629695, GPU certified nonviolations=130629551, unique transferred candidates=104490, exact=104477, unknown=0, pending=0 | 56301.43 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:08:17+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=130687039, GPU certified nonviolations=130686895, unique transferred candidates=104523, exact=104507, unknown=0, pending=0 | 56296.87 GPU screened draws/s | best exact gap=0.

- 2026-11-15T20:08:18+00:00 | 20261115T192936-gpu-seed20261119 | scheduled sync | device=cuda, GPU pipeline | generated draws=130744383, GPU certified nonviolations=130744239, unique transferred candidates=104580, exact=104571, unknown=0, pending=0 | 56302.27 GPU screened draws/s | best exact gap=0.
