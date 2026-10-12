"""Image classifier demo API; no model weights downloaded at runtime."""
from __future__ import annotations

import io
import os
from pathlib import Path

import torch
from fastapi import FastAPI, File, HTTPException, UploadFile
from PIL import Image, UnidentifiedImageError
from torchvision import transforms

from vision_transfer.model import build_model, predict_probabilities

app = FastAPI(title="Project 03 Vision Transfer Learning")
model = None
transform = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.ToTensor(),
])


@app.on_event("startup")
def load_model() -> None:
    global model
    artifact = Path(os.getenv("MODEL_PATH", "artifacts/smoke_resnet18.pt"))
    if artifact.is_file():
        candidate = build_model(num_classes=2, pretrained=False)
        candidate.load_state_dict(torch.load(artifact, map_location="cpu", weights_only=True))
        candidate.eval()
        model = candidate


@app.get("/health/live")
def live() -> dict:
    return {"status": "alive"}


@app.get("/health/ready")
def ready() -> dict:
    if model is None:
        raise HTTPException(status_code=503, detail="Model artifact not loaded")
    return {"status": "ready"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)) -> dict:
    if model is None:
        raise HTTPException(status_code=503, detail="Model artifact not loaded")
    data = await file.read(5 * 1024 * 1024 + 1)
    if len(data) > 5 * 1024 * 1024:
        raise HTTPException(status_code=413, detail="Image exceeds 5 MiB")
    try:
        image = Image.open(io.BytesIO(data)).convert("RGB")
    except (UnidentifiedImageError, OSError) as exc:
        raise HTTPException(status_code=400, detail="Invalid image") from exc
    batch = transform(image).unsqueeze(0)
    probabilities = predict_probabilities(model, batch)[0].tolist()
    return {"classes": ["class_0", "class_1"], "probabilities": probabilities,
            "note": "Synthetic smoke model; predictions are not meaningful"}
