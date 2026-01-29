import torch

print("PyTorch version:", torch.__version__)
print("MPS available:", torch.backends.mps.is_available())  # Apple Silicon GPU support
x = torch.tensor([1.0, 2.0, 3.0])
print(x * 2)
