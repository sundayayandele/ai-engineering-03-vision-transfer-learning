"""ResNet18 image classification utilities.

Pretrained weights are opt-in. The educational smoke test does not download weights.
"""
from __future__ import annotations

import torch
from torch import nn
from torchvision.models import ResNet18_Weights, resnet18


def build_model(num_classes: int = 2, pretrained: bool = False, freeze_backbone: bool = True) -> nn.Module:
    if num_classes < 2:
        raise ValueError("num_classes must be >= 2")
    weights = ResNet18_Weights.DEFAULT if pretrained else None
    model = resnet18(weights=weights)
    if freeze_backbone:
        for param in model.parameters():
            param.requires_grad = False
    model.fc = nn.Linear(model.fc.in_features, num_classes)
    return model


def predict_probabilities(model: nn.Module, batch: torch.Tensor) -> torch.Tensor:
    model.eval()
    with torch.inference_mode():
        return torch.softmax(model(batch), dim=1)
