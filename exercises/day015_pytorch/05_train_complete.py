import random
import numpy as np
import torch
import torch.nn as nn

from torch.utils.data import Dataset, DataLoader, random_split


SEED = 42
BATCH_SIZE = 32
NUM_EPOCHS = 100
LEARNING_RATE = 0.001
PATIENCE = 5


def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)

    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)


set_seed(SEED)


class BinaryDataset(Dataset):
    def __init__(self, num_samples=1000):
        class_0 = torch.randn(
            num_samples // 2,
            2
        )

        class_1 = torch.randn(
            num_samples // 2,
            2
        ) + torch.tensor([4.0, 4.0])

        self.X = torch.cat([
            class_0,
            class_1
        ])

        self.y = torch.cat([
            torch.zeros(num_samples // 2),
            torch.ones(num_samples // 2)
        ])

    def __len__(self):
        return len(self.X)

    def __getitem__(self, index):
        return self.X[index], self.y[index]


class BinaryMLP(nn.Module):
    def __init__(self):
        super().__init__()

        self.net = nn.Sequential(
            nn.Linear(2, 16),
            nn.ReLU(),
            nn.Linear(16, 8),
            nn.ReLU(),
            nn.Linear(8, 1)
        )

    def forward(self, x):
        return self.net(x)


def train_one_epoch(
    model,
    loader,
    loss_fn,
    optimizer,
    device
):
    model.train()

    total_loss = 0.0
    correct = 0
    total = 0

    for batch_X, batch_y in loader:

        batch_X = batch_X.to(device)
        batch_y = batch_y.to(device)

        batch_y = batch_y.unsqueeze(1)

        optimizer.zero_grad()

        logits = model(batch_X)

        loss = loss_fn(
            logits,
            batch_y
        )

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

        probs = torch.sigmoid(logits)

        predictions = (
            probs >= 0.5
        ).float()

        correct += (
            predictions == batch_y
        ).sum().item()

        total += batch_y.size(0)

    avg_loss = total_loss / len(loader)
    accuracy = correct / total

    return avg_loss, accuracy


def evaluate(
    model,
    loader,
    loss_fn,
    device
):
    model.eval()

    total_loss = 0.0
    correct = 0
    total = 0

    with torch.no_grad():

        for batch_X, batch_y in loader:

            batch_X = batch_X.to(device)
            batch_y = batch_y.to(device)

            batch_y = batch_y.unsqueeze(1)

            logits = model(batch_X)

            loss = loss_fn(
                logits,
                batch_y
            )

            total_loss += loss.item()

            probs = torch.sigmoid(logits)

            predictions = (
                probs >= 0.5
            ).float()

            correct += (
                predictions == batch_y
            ).sum().item()

            total += batch_y.size(0)

    avg_loss = total_loss / len(loader)
    accuracy = correct / total

    return avg_loss, accuracy


dataset = BinaryDataset(
    num_samples=1000
)


train_size = int(
    len(dataset) * 0.8
)

val_size = (
    len(dataset) - train_size
)


generator = torch.Generator().manual_seed(SEED)

train_dataset, val_dataset = random_split(
    dataset,
    [train_size, val_size],
    generator=generator
)


train_loader = DataLoader(
    train_dataset,
    batch_size=BATCH_SIZE,
    shuffle=True
)


val_loader = DataLoader(
    val_dataset,
    batch_size=BATCH_SIZE,
    shuffle=False
)


device = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)

print("Device:", device)
print("Train size:", len(train_dataset))
print("Validation size:", len(val_dataset))


model = BinaryMLP().to(device)


loss_fn = nn.BCEWithLogitsLoss()


optimizer = torch.optim.Adam(
    model.parameters(),
    lr=LEARNING_RATE
)


best_val_loss = float("inf")
epochs_without_improvement = 0


for epoch in range(NUM_EPOCHS):

    train_loss, train_acc = train_one_epoch(
        model,
        train_loader,
        loss_fn,
        optimizer,
        device
    )

    val_loss, val_acc = evaluate(
        model,
        val_loader,
        loss_fn,
        device
    )

    print(
        f"Epoch [{epoch + 1:03d}/{NUM_EPOCHS}] "
        f"Train Loss: {train_loss:.4f} "
        f"Train Acc: {train_acc:.4f} | "
        f"Val Loss: {val_loss:.4f} "
        f"Val Acc: {val_acc:.4f}"
    )

    if val_loss < best_val_loss:

        best_val_loss = val_loss
        epochs_without_improvement = 0

        torch.save(
            model.state_dict(),
            "best_model.pt"
        )

        print("  -> Best model saved.")

    else:

        epochs_without_improvement += 1

        print(
            f"  -> No improvement: "
            f"{epochs_without_improvement}/{PATIENCE}"
        )

        if epochs_without_improvement >= PATIENCE:

            print("Early stopping!")

            break


best_model = BinaryMLP().to(device)

best_model.load_state_dict(
    torch.load(
        "best_model.pt",
        map_location=device
    )
)


best_val_loss, best_val_acc = evaluate(
    best_model,
    val_loader,
    loss_fn,
    device
)


print("\n========== BEST MODEL ==========")

print(
    f"Validation Loss: "
    f"{best_val_loss:.4f}"
)

print(
    f"Validation Accuracy: "
    f"{best_val_acc:.4f}"
)