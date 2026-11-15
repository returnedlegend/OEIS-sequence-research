# OEIS-sequence-research

A reproducible experimental search for graphs close to Reed's conjectured bound:

`chi(G) <= ceil((Delta(G) + omega(G) + 1) / 2)`.

**No counterexample has been found.** Tight known graphs are validation controls,
not new discoveries. Finite experiments cannot establish the conjecture.

## Environment

Python 3.12, NetworkX, OR-Tools CP-SAT and PyTorch. The current cloud instance has
five CPU cores and **no exposed NVIDIA GPU**. Search uses PyTorch on CPU here;
the CUDA path is implemented but has not been exercised on GPU hardware.

```bash
bash scripts/install.sh
source /workspace/oeis-venv/bin/activate
python -m pytest -q
```

`requirements.lock` pins the tested Python dependencies; the install script pins
CPU PyTorch separately. On another machine, create a virtual environment and
install that lock file, then install a CUDA-enabled PyTorch build appropriate to
its driver from the official PyTorch wheel index. Check
`python -c 'import torch; print(torch.cuda.is_available())'` before requesting
`--device cuda`. The program fails explicitly when CUDA is requested but absent.

## Run and verify

From this checkout:

```bash
python -m src.search --seconds 3600 --device auto --seed 20261115 --triangle-free --sync
python -m src.verify best_candidates/GRAPH_ID.json --time-limit 60
python src/independent_verify.py best_candidates/GRAPH_ID.json --time-limit 60
```

The default runtime budget is one hour. Use `--seconds` to set a finite budget;
Ctrl-C or SIGTERM stops after the current bounded solver call and writes a final
checkpoint. Solver/model initialization and Git operations add some wall time.
Only one search per output directory is allowed. No service or GPU process is assumed to
survive cloud environment shutdown. A new invocation starts a fresh reproducible
search; previous logs and saved parameter representatives are retained.

`--sync` opts into Git commits and pushes to `origin`'s `main` branch. Sync occurs
after seeds, every 15 minutes or 50,000 uniquely screened labeled graphs, and at
shutdown. Push failures are logged and retried after a clean-tree rebase; they do
not kill the search. Failed rebases are aborted. Without `--sync`, results remain
local. No force push is used. Progress is reported every 10 minutes by default.

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
  Larger orders, other mutations, and GPU throughput remain future experiments.

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
