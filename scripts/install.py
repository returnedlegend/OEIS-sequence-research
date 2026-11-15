"""Create a local environment, install CPU/CUDA PyTorch, verify, and test."""
from pathlib import Path
import argparse
import os
import subprocess
import tempfile
import venv


ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--device', choices=('cuda', 'cpu'), default='cuda')
    parser.add_argument('--venv', type=Path, default=ROOT / '.venv')
    args = parser.parse_args()
    environment = args.venv.resolve()
    venv.create(environment, with_pip=True)
    python = environment / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')

    def run(*command):
        subprocess.run([str(python), *map(str, command)], cwd=ROOT, check=True)

    run('-m', 'pip', 'install', '--cache-dir', ROOT / '.cache/pip', '-r', ROOT / 'requirements.lock')
    tag = 'cu126' if args.device == 'cuda' else 'cpu'
    run('-m', 'pip', 'install', '--cache-dir', ROOT / '.cache/pip',
        f'torch==2.14.1+{tag}', '--index-url', f'https://download.pytorch.org/whl/{tag}')
    run('-m', 'pip', 'check')
    if args.device == 'cuda':
        run(ROOT / 'scripts/check_cuda.py')
    # Keep test scratch/cache independent of other Windows users or sandboxes.
    with tempfile.TemporaryDirectory(prefix='oeis-tests-') as scratch:
        run('-m', 'pytest', '-q', '--basetemp', Path(scratch) / 'tmp',
            '-o', f'cache_dir={Path(scratch) / "cache"}')
    print(f'Environment ready: {python}', flush=True)


if __name__ == '__main__':
    main()
