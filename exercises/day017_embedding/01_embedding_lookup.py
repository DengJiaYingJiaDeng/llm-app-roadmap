import torch
import torch.nn as nn


# 假设词表只有 6 个 token
vocab = {
    "我": 0,
    "喜欢": 1,
    "机器": 2,
    "学习": 3,
    "猫": 4,
    "狗": 5,
}

# vocab_size = 6
# embedding_dim = 4

embedding = nn.Embedding(
    num_embeddings=6,
    embedding_dim=4
)

token_ids = torch.tensor([
    0,1,3
])

vectors = embedding(token_ids)

print("token_ids:")
print(token_ids)

print("\nEmbedding vectors:")
print(vectors)

print("\nshape:")
print(vectors.shape)

print("\nEmbedding weight:")
print(embedding.weight)

print("\nEmbedding weight shape:")
print(embedding.weight.shape)

token_id = torch.tensor([3])

vector_from_embedding = embedding(token_id)

vector_from_weight = embedding.weight[3]


print("\n通过 Embedding 获取:")
print(vector_from_embedding)

print("\n直接访问 weight[3]:")
print(vector_from_weight)

one_hot = torch.nn.functional.one_hot(
    torch.tensor([0,1,4]),
    num_classes=6
)

print("\nOne-hot:")
print(one_hot)

print("shape:")
print(one_hot.shape)
