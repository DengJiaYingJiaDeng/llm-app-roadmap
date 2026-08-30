import torch
import torch.nn as nn
from transformers import AutoTokenizer


MODEL_NAME = "google-bert/bert-base-multilingual-cased"

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME
)


texts = [
    "我喜欢机器学习",
    "机器学习很有意思"
]


encoded = tokenizer(
    texts,
    padding=True,
    truncation=True,
    return_tensors="pt"
)


input_ids = encoded["input_ids"]
attention_mask = encoded["attention_mask"]


print("input_ids:")
print(input_ids)

print("\ninput_ids shape:")
print(input_ids.shape)

print("\nattention_mask:")
print(attention_mask)

VOCAB_SIZE = tokenizer.vocab_size

EMBED_DIM = 32


token_embedding = nn.Embedding(
    num_embeddings=VOCAB_SIZE,
    embedding_dim=EMBED_DIM
)


token_vectors = token_embedding(
    input_ids
)


print("\nToken embedding shape:")
print(token_vectors.shape)

batch_size,seq_len = input_ids.shape

position_ids = torch.arange(
    seq_len
)

print("\nposition_ids:")
print(position_ids)

position_ids = position_ids.unsqueeze(0)

print(position_ids)
print(position_ids.shape)

position_ids = position_ids.expand(
    batch_size,
    seq_len
)

MAX_LENGTH = 512


position_embedding = nn.Embedding(
    num_embeddings=MAX_LENGTH,
    embedding_dim=EMBED_DIM
)


position_vectors = position_embedding(
    position_ids
)


print("\nPosition embedding shape:")
print(position_vectors.shape)

x = token_vectors + position_vectors


print("\nFinal embedding shape:")
print(x.shape)


class TokenPositionEmbedding(nn.Module):
    def __init__(
        self,
        vocab_size: int,
        embed_dim: int,
        max_length: int
    ):
        super().__init__()

        self.token_embedding = nn.Embedding(
            vocab_size,
            embed_dim
        )

        self.position_embedding = nn.Embedding(
            max_length,
            embed_dim
        )

    def forward(self, input_ids):
        batch_size, seq_len = input_ids.shape

        positions = torch.arange(
            seq_len,
            device=input_ids.device
        )

        positions = positions.unsqueeze(0).expand(
            batch_size,
            seq_len
        )

        token_vectors = self.token_embedding(
            input_ids
        )

        position_vectors = self.position_embedding(
            positions
        )

        return token_vectors + position_vectors

embedding_layer = TokenPositionEmbedding(
    vocab_size=tokenizer.vocab_size,
    embed_dim=32,
    max_length=512
)


x = embedding_layer(input_ids)


print("\nModule output shape:")
print(x.shape)