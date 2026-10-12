import pytest
import torch

from vision_transfer.model import build_model, predict_probabilities


def test_probabilities_sum_to_one():
    model = build_model(pretrained=False)
    result = predict_probabilities(model, torch.rand(1, 3, 64, 64))
    assert result.shape == (1, 2)
    assert result.sum().item() == pytest.approx(1.0, abs=1e-5)


def test_invalid_classes():
    with pytest.raises(ValueError):
        build_model(num_classes=1)
