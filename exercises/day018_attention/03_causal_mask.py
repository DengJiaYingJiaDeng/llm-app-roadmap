import torch

seq_len = 5

mask = torch.triu(
    torch.ones(
        seq_len,
        seq_len
    ),
    diagonal=1
).bool()

print("Causal mask:")
print(mask)

scores = torch.tensor([
    [1.0, 2.0, 3.0, 4.0, 5.0],
    [1.0, 2.0, 3.0, 4.0, 5.0],
    [1.0, 2.0, 3.0, 4.0, 5.0],
    [1.0, 2.0, 3.0, 4.0, 5.0],
    [1.0, 2.0, 3.0, 4.0, 5.0],
])

masked_scores = scores.masked_fill(
    mask,
    float("-inf")
)

print("\nMasked scores:")
print(masked_scores)

weights = torch.softmax(
    masked_scores,
    dim=-1
)

print("\nAttention weights:")
print(weights)
