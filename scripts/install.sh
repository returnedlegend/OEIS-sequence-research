#!/usr/bin/env bash
set -euo pipefail
cd /workspace/OEIS-sequence-research
python3 -m venv /workspace/oeis-venv
/workspace/oeis-venv/bin/python -m pip install --cache-dir /workspace/.cache/pip -r requirements.lock
/workspace/oeis-venv/bin/python -m pip install --cache-dir /workspace/.cache/pip 'torch==2.15.0+cpu' --index-url https://download.pytorch.org/whl/cpu
/workspace/oeis-venv/bin/python -m pytest -q
