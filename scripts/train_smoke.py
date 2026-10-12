"""Tiny CPU-only smoke training on synthetic image tensors, not real accuracy."""
from pathlib import Path

import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

from vision_transfer.model import build_model


def main() -> None:
    torch.manual_seed(42)
    torch.set_num_threads(2)
    images = torch.rand(8, 3, 64, 64)
    labels = torch.randint(0, 2, (8,))
    loader = DataLoader(TensorDataset(images, labels), batch_size=4)
    model = build_model(num_classes=2, pretrained=False, freeze_backbone=True)
    optimizer = torch.optim.Adam(model.fc.parameters(), lr=0.001)
    loss_fn = nn.CrossEntropyLoss()
    model.train()
    for x, y in loader:
        optimizer.zero_grad()
        loss = loss_fn(model(x), y)
        loss.backward()
        optimizer.step()
    output = Path("artifacts")
    output.mkdir(exist_ok=True)
    torch.save(model.state_dict(), output / "smoke_resnet18.pt")
    print(f"Synthetic smoke training complete; last_loss={loss.item():.4f}")


if __name__ == "__main__":
    main()
