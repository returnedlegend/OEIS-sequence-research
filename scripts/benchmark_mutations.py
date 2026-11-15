"""Reproduce a small labeled-graph mutation retention experiment."""
from datetime import datetime, timezone
import json
from pathlib import Path
import random
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import torch
from src.graphs import mutate_batch, seed_graphs
from src.constrained_graphs import is_triangle_free, mutate_triangle_free_batch


def main():
    torch.set_num_threads(1)
    rows = []
    for name, parent in seed_graphs(12):
        if name not in ('chvatal', 'mycielski_C5_1'):
            continue
        for label, mutate in (('unconstrained', mutate_batch), ('triangle_free', mutate_triangle_free_batch)):
            start = time.monotonic()
            children = mutate([parent], 256, random.Random(20261115), device='cpu', swap_attempts=8)
            elapsed = time.monotonic() - start
            retained = [a for a in children if is_triangle_free(a)]
            rows.append(dict(parent=name, operator=label, children=len(children),
                             triangle_free=len(retained), changed=sum(a != parent for a in children),
                             unique_triangle_free=len({tuple(map(tuple, a)) for a in retained}),
                             elapsed_seconds=elapsed))
    print(json.dumps({'timestamp_utc': datetime.now(timezone.utc).isoformat(),
                      'device': 'cpu', 'torch_version': torch.__version__,
                      'seed': 20261115, 'swap_attempts': 8, 'rows': rows,
                      'caveat': 'Single microbenchmark; labeled uniqueness, not isomorphism classes. No chi claims.'}, indent=2))


if __name__ == '__main__':
    main()
