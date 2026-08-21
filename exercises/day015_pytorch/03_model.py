import torch
import torch.nn as nn

class BinaryMLP(nn.Module):
    def __init__(self):
        super().__init__()

        self.net = nn.Sequential(
            nn.Linear(2,16),
            nn.ReLU(),

            nn.Linear(16, 8),
            nn.ReLU(),

            nn.Linear(8, 1)
        )

    def forward(self, x):
        print("输入:", x.shape)

        x = self.net[0](x)
        print("Linear 2->16:", x.shape)

        x = self.net[1](x)
        print("ReLU:", x.shape)

        x = self.net[2](x)
        print("Linear 16->8:", x.shape)

        x = self.net[3](x)
        print("ReLU:", x.shape)

        x = self.net[4](x)
        print("Linear 8->1:", x.shape)

        return x

model = BinaryMLP()

print(model)

X = torch.tensor([
    [1.0,2.0],
    [8.0,9.0],
    [3.0,4.0]
])

output = model(X)

print("\n输入 shape:", X.shape)
print("输出 shape:", output.shape)
print("模型输出:")
print(output)

for name, param in model.named_parameters():
    print(name)
    print("shape:", param.shape)

total_params = sum(
    p.numel()
    for p in model.parameters()
)

print("总参数量：",total_params)

prob = torch.sigmoid(output)

print("logits:")
print(output)

print("概率:")
print(prob)