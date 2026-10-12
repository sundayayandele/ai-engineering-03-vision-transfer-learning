# Project 03 — Vision Transfer Learning

**Two tracks:** Educational / Portfolio and Enterprise / Production reference architecture.

Build an image classifier using PyTorch and pretrained torchvision ResNet18, with a reproducible training/evaluation pipeline, FastAPI inference, Docker, Kubernetes/OpenShift and cloud-neutral deployment guidance.

> **Status:** Initial project scaffold. CI, dataset experiments, cloud deployments, GPU performance and production readiness must be validated before claiming success.

## Learning track

1. Fork this repository and create a branch `learner/first-lab`.
2. Enable GitHub Actions in your fork after reviewing the workflows.
3. Run the **education-smoke** workflow using a CPU-only synthetic-image smoke test (no paid GPU required).
4. Run tests, inspect logs and document model accuracy on a licensed real dataset separately.
5. Follow [the learner lab](docs/learning/GITHUB-RUNNERS-LAB.md).

## Enterprise track

Reference designs cover TOGAF 10, ArchiMate-inspired viewpoints, C4, model lifecycle governance, security, observability, scalable inference and cloud-neutral infrastructure. **Architecture documentation is not evidence of a production deployment.**

## Quick start

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
python scripts/train_smoke.py
pytest -q
uvicorn app.main:app --reload
```

## API

- `GET /health/live` — process liveness
- `GET /health/ready` — model readiness
- `POST /predict` — upload an image file and receive top class probabilities


## Architectural Diagrams & Infographics
![Architectural Diagrams & Infographics](/diagrams/a_clean_infographic_diagram_on_a_white_background.png)

![Architectural Diagrams & Infographics](/diagrams/a_large_infographic_diagram_with_a_clean_modern_fl.png)

![Architectural Diagrams & Infographics](/diagrams/a_wide_colorful_infographic_diagram_with_clean_ve.png)

## Documentation

- [Learning lab](docs/learning/GITHUB-RUNNERS-LAB.md)
- [TOGAF 10 architecture](docs/architecture/TOGAF10-ARCHITECTURE.md)
- [ArchiMate-inspired viewpoints](docs/architecture/ARCHIMATE-VIEWPOINTS.md)
- [C4 diagrams and editable Mermaid](diagrams/source/)
- [Capacity planning](docs/infrastructure/CAPACITY-PLANNING.md)
- [TCO](docs/COST-TCO.md)
- [Datasets and licensing](docs/datasets/DATASETS.md)
- [Security](docs/security/SECURITY.md)

## Safety and licensing

Use public datasets only under their own licenses. Do not commit personal images, datasets, secrets, model weights or generated artifacts. Pretrained torchvision weights may download from the internet when enabled; the offline smoke lab uses random initialization and synthetic inputs and **does not establish real-world accuracy**.

## License

MIT for project source code; third-party datasets and pretrained weights have separate terms.
