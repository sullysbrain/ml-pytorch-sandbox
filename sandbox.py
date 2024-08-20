import torch

torch.__version__

if (torch.cuda.is_available()):
    print("CUDA is available")

if (torch.backends.mps.is_available()):
    print("M3 Macbook GPU:  MPS is available")
else:
    print("CUDA is not available")


