import torch
from torch.utils.data import Dataset, DataLoader


class BinaryDataset(Dataset):
    def __init__(self, num_samples=1000):
        torch.manual_seed(42)

        class_0 = torch.randn(num_samples // 2, 2) + torch.tensor([0.0, 0.0])

        class_1 = torch.randn(num_samples // 2, 2) + torch.tensor([4.0, 4.0])

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


dataset = BinaryDataset()

loader = DataLoader(
    dataset,
    batch_size=32,
    shuffle=True
)

print("dataset size:", len(dataset))
print("batch 数量:", len(loader))

for batch_X, batch_y in loader:
    print("batch_X shape:", batch_X.shape)
    print("batch_y shape:", batch_y.shape)
    break