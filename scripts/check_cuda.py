"""Fail unless a real CUDA matrix product agrees with its CPU reference."""
import json
import platform

import torch


def main():
    if not torch.cuda.is_available():
        raise SystemExit('No usable CUDA device is available.')
    matrix = torch.arange(1024, dtype=torch.float32).reshape(32, 32)
    gpu_matrix = matrix.to('cuda')
    product = gpu_matrix @ gpu_matrix.T
    torch.cuda.synchronize()
    torch.testing.assert_close(product.cpu(), matrix @ matrix.T)
    print(json.dumps({
        'python': platform.python_version(),
        'torch': torch.__version__,
        'cuda_runtime': torch.version.cuda,
        'device': str(product.device),
        'gpu': torch.cuda.get_device_name(0),
        'compute_capability': torch.cuda.get_device_capability(0),
        'compiled_architectures': torch.cuda.get_arch_list(),
        'operation': '32x32 float32 matrix @ matrix.T',
        'cpu_reference_agrees': True,
        'checksum': product.sum().item(),
    }, indent=2))


if __name__ == '__main__':
    main()
