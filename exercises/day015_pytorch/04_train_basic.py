import torch
import torch.nn as nn
from torch.utils.data import Dataset,DataLoader


# =========================
# 1. Dataset
# =========================
class BinaryDataset(Dataset):
    def __init__(self,num_samples=1000):
        torch.manual_seed(42)

        class_0 = torch.randn(num_samples // 2,2)
        class_1 = torch.randn(num_samples // 2,2) + torch.tensor([4.0,4.0])

        self.X = torch.cat([class_0,class_1])

        self.y = torch.cat([
            torch.zeros(num_samples // 2),
            torch.ones(num_samples // 2)
        ])

    def __len__(self):
        return len(self.X)

    def __getitem__(self, index):
        return self.X[index],self.y[index]

# =========================
# 2. Model
# =========================
class BinaryMLP(nn.Module):
    def __init__(self):
        super().__init__()

        self.net = nn.Sequential(
            nn.Linear(2,16),
            nn.ReLU(),

            nn.Linear(16,8),
            nn.ReLU(),

            nn.Linear(8,1)
        )

    def forward(self,x):
        return self.net(x)


# =========================
# 3. 数据
# =========================
dataset = BinaryDataset()

train_loader = DataLoader(
    dataset,
    batch_size=32,
    shuffle=True
)

# =========================
# 4. 模型
# =========================
model = BinaryMLP()

# =========================
# 5. Loss
# =========================
loss_fn = nn.BCEWithLogitsLoss()

# =========================
# 6. Optimizer
# =========================
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)


# =========================
# 7. Training Loop
# =========================
num_epochs = 20

for epoch in range(num_epochs):

    model.train()

    total_loss = 0.0
    correct = 0
    total = 0

    for batch_X, batch_y in train_loader:

        batch_y = batch_y.unsqueeze(1)

        optimizer.zero_grad()

        logits = model(batch_X)

        loss = loss_fn(logits, batch_y)

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

        # logits → probability
        probs = torch.sigmoid(logits)

        # probability → 0 / 1
        predictions = (probs >= 0.5).float()

        correct += (predictions == batch_y).sum().item()
        total += batch_y.size(0)

    avg_loss = total_loss / len(train_loader)

    accuracy = correct / total

    print(
        f"Epoch [{epoch + 1:02d}/{num_epochs}] "
        f"Loss: {avg_loss:.4f} "
        f"Accuracy: {accuracy:.4f}"
    )