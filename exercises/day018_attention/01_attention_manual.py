import torch
import math


X = torch.tensor([
    [1.0, 0.0],
    [0.0, 1.0],
    [1.0, 1.0],
])


print("X:")
print(X)

print("\nX shape:")
print(X.shape)

Q = X
K = X
V = X

print("\nQ shape:", Q.shape)
print("K shape:", K.shape)
print("V shape:", V.shape)

scores = Q @ K.T

print("\nRaw attention scores:")
print(scores)

print("\nScores shape:")
print(scores.shape)

d_k = Q.shape[-1]

scaled_scores = scores / math.sqrt(d_k)

print("\nScaled scores:")
print(scaled_scores)

weights = torch.softmax(
    scaled_scores,
    dim=-1
)

print("\nAttention weights:")
print(weights)

print("\n每一行求和:")
print(weights.sum(dim=-1))

output = weights @ V

print("\nAttention output:")
print(output)

print("\nOutput shape:")
print(output.shape)