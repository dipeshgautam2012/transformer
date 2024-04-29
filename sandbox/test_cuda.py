import torch

# Create a tensor
x = torch.tensor([[1, 2], [3, 4]])

# Print the tensor
print("Tensor:")
print(x)

# Check if CUDA is available
if torch.cuda.is_available():
    device = torch.device("cuda")
    print("CUDA is available")
else:
    device = torch.device("cpu")
    print("CUDA is not available")

# Move the tensor to the appropriate device
x = x.to(device)

# Perform a simple operation
y = x + 1

# Print the result
print("Result:")
print(y)
