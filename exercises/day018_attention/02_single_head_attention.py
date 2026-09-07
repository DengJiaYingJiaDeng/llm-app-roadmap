import math
import torch
import torch.nn as nn

class SingleHeadSelfAttention(nn.Module):

    def __init__(
        self,
        embed_dim,
        head_dim
    ):
        super().__init__()

        self.head_dim = head_dim

        self.q_proj = nn.Linear(
            embed_dim,
            head_dim,
            bias=False
        )

        self.k_proj = nn.Linear(
            embed_dim,
            head_dim,
            bias=False
        )

        self.v_proj = nn.Linear(
            embed_dim,
            head_dim,
            bias=False
        )


    def forward(
        self,
        x,
        causal=False
    ):

        Q = self.q_proj(x)
        K = self.k_proj(x)
        V = self.v_proj(x)


        scores = (
            Q
            @ K.transpose(-2, -1)
        )

        scores = (
            scores
            / math.sqrt(self.head_dim)
        )


        if causal:

            seq_len = x.shape[1]

            mask = torch.triu(
                torch.ones(
                    seq_len,
                    seq_len,
                    device=x.device
                ),
                diagonal=1
            ).bool()

            scores = scores.masked_fill(
                mask,
                float("-inf")
            )


        weights = torch.softmax(
            scores,
            dim=-1
        )


        output = weights @ V


        return output, weights

torch.manual_seed(42)

batch_size = 2
seq_len = 5
embed_dim = 8
head_dim = 4

x = torch.randn(
    batch_size,
    seq_len,
    embed_dim
)

attention = SingleHeadSelfAttention(
    embed_dim=embed_dim,
    head_dim=head_dim
)

output,weights = attention(
    x,
    causal=True
)


print("x shape:")
print(x.shape)

print("\noutput shape:")
print(output.shape)

print("\nattention weights shape:")
print(weights.shape)