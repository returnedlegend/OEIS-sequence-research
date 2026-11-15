# OEIS-sequence-research

A reproducible experimental search for graphs close to Reed's conjectured bound:

`chi(G) <= ceil((Delta(G) + omega(G) + 1) / 2)`.

**No counterexample has been found.** Tight known graphs are validation controls,
not new discoveries. Finite experiments cannot establish the conjecture.

## Completed experiments

CPU runs on November 15, 2026 (UTC); each count is per run and may overlap other runs.

| Run | Budget | Distinct labeled graphs screened | Exact verifications | Unknown | Best gap |
| --- | ---: | ---: | ---: | ---: | ---: |
| Initial smoke, n <= 24 | 15 s | 2,628 | 2,534 | 1 | 0 |
| Broad degree-preserving search, n <= 40 | 600 s | 67,086 | 63,938 | 1 | 0 |
| Triangle-free pilot, n <= 40 | 120 s | 7,473 | 7,451 | 1 | 0 |

The broad run averaged 111.81 uniquely screened graphs/s. The focused pilot
averaged 62.27/s under concurrent CPU load. These runs do not establish a
speed advantage for either method. The 136 broad-run saved parameter
representatives all agreed with the independent verifier. The best
triangle-free controls include the known Chvatal graph (n=12, Delta=4,
omega=2, chi=4) and Mycielski(C5) (n=11, Delta=5, omega=2, chi=4).
No novelty is claimed. Full records are in `runs/` and `RESEARCH_LOG.md`.

Validation on the Windows NVIDIA host: **110 tests passed, none skipped**, including
CUDA mutation/coloring certificates, bounded parallel verification, preservation
of unresolved candidates, background Git pushes, and the cross-process search lock.

## Environment

The original CPU experiments used Python 3.12. The local Windows setup uses
Python 3.13.17, the locked NetworkX/OR-Tools dependencies, and
**PyTorch 2.14.1+cu126 (CUDA 12.6)** on an NVIDIA GeForce RTX 2070 with Max-Q
Design (8 GB, compute capability 7.5; NVIDIA driver 610.91).
An actual CUDA float32 matrix multiplication agrees with its CPU reference;
the triangle-free mutation invariants also pass on CUDA.

Windows PowerShell, from this checkout:

```powershell
python scripts/install.py --device cuda
.\.venv\Scripts\Activate.ps1
python scripts/check_cuda.py
python -m src.search --seconds 3600 --device cuda --seed 20261117 --max-vertices 50 --triangle-free --sync
```

For the GPU pipeline (8,192 graphs per batch by default):

```powershell
python -m src.search --gpu-pipeline --triangle-free --device cuda --seconds 3600 --max-vertices 50 --seed 20261119 --verifier-workers 4 --audit-per-batch 8 --sync --stop-file .cache/gpu-search.stop
```

The stop-file path must be absent when starting. To request a clean checkpoint
and shutdown from another PowerShell session, create it with
`New-Item .cache/gpu-search.stop -ItemType File`. The file remains present after
shutdown; use a fresh path for another run or remove the old request explicitly.

This pipeline keeps populations on the GPU and performs degree-preserving
triangle-free swaps plus four parallel DSATUR coloring trials. It independently
checks the returned colorings against every edge on the GPU. If a proper
coloring uses no more than `ceil((Delta + 3)/2)` colors, the graph cannot violate
Reed's inequality: an edge gives a clique lower bound of 2. This proves
nonviolation without claiming the exact chromatic number.

Every graph whose coloring bound leaves a positive gap possible goes to exact
verification. Up to eight other tight/near candidates per batch are sampled for
exact checks and construction records. Four CPU processes perform these checks
while GPU generation continues. Bounded queues apply backpressure rather than
discarding possible violations. Unfinished candidates, including solver
timeouts for possible violations, retain their adjacency in `pending.jsonl`.
These pending records require later verification and are never counted as exact.

GPU screened/certified counts are **generated instances, potentially repeated**.
Only the transferred candidates are deduplicated across the run. A large GPU
screening count therefore does not establish millions of distinct graphs or
millions of exact chromatic-number calculations. The GPU mode runs persistent
random walks within its seed degree sequences; it is not exhaustive.

On the RTX 2070, an isolated 45-second experiment screened 4,898,816 GPU
instances and completed 3,898 distinct exact verifications. The original loop
completed 1,144 exact verifications in the same time budget. GPU utilization
averaged 51% across the monitored process lifetime, peaking at 77%. These runs
used different selection policies, and excluded Git network time. Records and
commands are in `runs/gpu-pipeline-benchmark-20261115/`.

Linux:

```bash
bash scripts/install.sh --device cuda
source .venv/bin/activate
```

The portable installer creates `.venv`, installs `requirements.lock`, installs
PyTorch from the official CUDA 12.6 wheel index, checks dependency consistency,
verifies a CUDA tensor operation, and runs the tests. Use `--device cpu` to
explicitly install the CPU build instead. The CUDA runtime is bundled with the
wheel; a separate CUDA toolkit is not required. Supported PyTorch wheel commands
are documented by [PyTorch](https://pytorch.org/get-started/previous-versions/).
The program fails explicitly when CUDA is requested but absent. Checkpoint pushes
require Git credentials and a repository-local Git author identity.

## Run and verify

From this checkout:

```bash
python -m src.search --seconds 3600 --device auto --seed 20261115 --triangle-free --sync
python -m src.verify best_candidates/GRAPH_ID.json --time-limit 60
python src/independent_verify.py best_candidates/GRAPH_ID.json --time-limit 60
```

The default runtime budget is one hour. Use `--seconds` to set a finite budget;
The portable `--stop-file` option requests a final checkpoint. Ctrl-C or SIGTERM
can also request shutdown where the host delivers those signals to Python;
Windows process termination is not a graceful signal. Solver/model initialization
and Git operations add some wall time. The GPU pipeline preserves unfinished
verification jobs and waits for its bounded worker processes to exit.
Only one search per output directory is allowed. No service or GPU process is assumed to
survive cloud environment shutdown. A new invocation starts a fresh reproducible
search; previous logs and saved parameter representatives are retained.

`--sync` opts into Git commits and pushes to `origin`'s `main` branch. Sync occurs
after seeds, every 15 minutes or 50,000 uniquely screened labeled graphs, and at
shutdown. Push failures are logged and retried after a clean-tree rebase; they do
not kill the search. Failed rebases are aborted. Without `--sync`, results remain
local. No force push is used. Progress is reported every 10 minutes by default.
The GPU pipeline checkpoints every 50,000 generated instances or 15 minutes.
Staging and committing happen between batch updates. Network pushes run in a
single background thread and may combine multiple completed commits while a
previous push is in flight; final shutdown waits for the latest checkpoint.

## Method and limits

- Seeds: odd cycles, Mycielski constructions, Petersen and Chvatal graphs,
  circulants, Andrasfai graphs, Mobius ladders, and complete/bipartite controls.
- PyTorch batches degree-preserving double-edge swaps. These preserve maximum
  degree, but can change clique number, connectivity and chromatic number.
  Optional `--triangle-free` rejects swaps introducing triangles and mutates
  parents of degree >= 3 where available. It retains odd-cycle seed controls.
  Default mode explores the broader structured seed mix.
- A proper greedy coloring gives an upper bound `U` on chi; an explicit clique
  gives a lower bound `L` on omega. The screen
  `U - ceil((Delta + L + 1)/2)` is an **upper bound on the true gap**. Only
  candidates with screen >= -1 go to CP-SAT. This cannot discard a positive-gap
  graph when the screen's bounds are valid.
- CP-SAT proves maximum clique and minimum coloring. An optimal clique matching
  a proper coloring is also an exact proof. FEASIBLE/UNKNOWN solver outcomes
  are never treated as optimality or as counterexamples.
- A separate standard-library branch-and-bound/backtracking verifier recomputes
  saved representatives, within its time budget. Both must agree before a
  positive-gap graph enters `COUNTEREXAMPLE/`; that folder also gets a standalone
  `verify.py`. Computational agreement should still receive independent review.
- Evolution retains structured seeds and a bounded pool of verified candidates
  with gap >= -1 and clique lower bound <= 3. It is a heuristic, not exhaustive.
  Degree-preserving moves cannot reach degree sequences absent from the seeds.
  Larger orders and other mutations remain future experiments. GPU execution is
  verified; small-graph searches still spend substantial time in CPU exact solvers,
  so using CUDA does not itself demonstrate a throughput advantage.

## Artifacts

- `src/`: tensor mutations, controller, CP-SAT verifier, independent verifier.
- `best_candidates/`: exact gap-zero representatives, one per
  `(n, edges, Delta, omega, chi)` tuple across runs. No graph novelty is implied.
- `near_misses/`: representatives with exact gap -1.
- `runs/`: configuration, per-verification JSONL records (rotated every 10,000
  records in new runs), and summary statistics.
  Deduplication is by labeled adjacency matrix, not graph isomorphism. Generated,
  screened, exact, skipped, duplicate and unknown counts are separate.
- `RESEARCH_LOG.md`: append-only UTC experiment checkpoints.
- `COUNTEREXAMPLE/`: created only if independent exact verifiers agree on gap > 0.

The tests include brute-force checks of small graphs, known exact graph families,
malformed-input rejection, timeout handling, false-claim rejection, conservative
screening, and invariants of the mutation operator.
