# Project 03 — Local lab: Docker Desktop, Rancher Desktop, Postman

**Scope:** Educational/Portfolio CPU-only synthetic smoke test. The ResNet18 weights are randomly initialized and the resulting predictions **do not** represent meaningful image classification. The production track requires an approved dataset, real pretrained weights, evaluation and security controls.

## Prerequisites

- Git, Python 3.12, at least 8 GiB free RAM recommended, and 10–20 GiB free disk for image/dependency installation.
- Choose **Docker Desktop** (Windows/macOS/Linux) or **Rancher Desktop** (Windows/macOS/Linux).
- Postman desktop/web with desktop agent, or curl. On Windows use PowerShell or a Git Bash terminal.
- CPU-only mode works; no GPU or cloud subscription is required.
- For Rancher Desktop choose **dockerd (moby)** container engine so the `docker` and `docker compose` commands below work. With containerd, switch to dockerd or adapt commands to nerdctl.

## Step 1 — Clone your learner copy

Fork https://github.com/sundayayandele/ai-engineering-03-vision-transfer-learning, then clone **your fork**:

```bash
git clone https://github.com/YOUR_USERNAME/ai-engineering-03-vision-transfer-learning.git
cd ai-engineering-03-vision-transfer-learning
git switch -c learner/local-lab
```

## Step 2 — Start Docker Desktop or Rancher Desktop

Start the desktop application and wait until its engine is running. On Rancher Desktop, enable dockerd (moby). Verify:

```bash
docker version
docker compose version
```

For Docker Desktop, the default Linux containers mode is expected. Windows users should run commands from Git Bash/WSL, or adapt `source` for PowerShell.

## Step 3 — Train the local smoke model

Create a Python virtual environment (macOS/Linux/WSL/Git Bash):

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python scripts/train_smoke.py
pytest -q
ls -lh artifacts/smoke_resnet18.pt
```

PowerShell activation is `.venv\Scripts\Activate.ps1`. If `python3.12` is unavailable on Windows, use `py -3.12 -m venv .venv`.

**Expected:** The training command writes `artifacts/smoke_resnet18.pt`. This artifact is ignored by Git and is mounted read-only into the inference container. Do not commit it.

## Step 4 — Build and run the API container

```bash
docker compose build
docker compose up -d
docker compose ps
docker compose logs --tail=50 inference
```

The Compose configuration binds port 8000 to **127.0.0.1** only, limits the container to 2 CPUs and 2 GiB memory, and mounts the locally trained artifact at `/app/artifacts/smoke_resnet18.pt`.

Test in your browser:

- http://127.0.0.1:8000/health/live → HTTP 200, `{"status":"alive"}`
- http://127.0.0.1:8000/health/ready → HTTP 200, `{"status":"ready"}`
- http://127.0.0.1:8000/docs → interactive OpenAPI page

If readiness is 503, run `docker compose logs inference` and verify the artifact exists and is readable. If your host lacks sufficient RAM/disk, adjust Docker Desktop/Rancher Desktop resource allocations.

## Step 5 — Test image inference with Postman

1. Create a new Postman HTTP request.
2. Select **POST** and enter `http://127.0.0.1:8000/predict`.
3. Choose **Body → form-data**.
4. Add a field named **file**. Change its type from **Text** to **File**.
5. Choose a small local JPEG/PNG image (less than 5 MiB), then **Send**.
6. Expect HTTP 200 and JSON keys `classes`, `probabilities`, and `note`.
7. Try a text file as `file`: expect HTTP 400 for an invalid image.
8. Upload a file larger than 5 MiB: expect HTTP 413.

Postman sets the multipart boundary automatically. Do not manually force `Content-Type: application/json` or a bare `multipart/form-data` header for the upload.

### Equivalent curl command

```bash
curl -i http://127.0.0.1:8000/health/ready
curl -i -F "file=@./example.jpg" http://127.0.0.1:8000/predict
```

Replace `example.jpg` with a real local image path. **Never upload personal or sensitive images** to a publicly exposed demo.

## Step 6 — Observe and clean up

```bash
docker stats --no-stream
docker compose logs --tail=100 inference
docker compose down
```

Record screenshots/logs for your portfolio: branch, commit SHA, test output, successful health checks, sample prediction, CPU/memory observation and cleanup. Keep generated files out of Git.

## Optional Rancher Desktop Kubernetes/OpenShift exploration

Rancher Desktop can optionally enable a local Kubernetes cluster. The `deploy/kubernetes/` manifests are **reference templates**, not a one-command working local deployment: the image placeholder must be replaced, the model PVC must be prepopulated and compatible with the StorageClass, and cluster ingress/storage prerequisites must be met. See [Enterprise deployment guide](../DEPLOYMENT.md). Do not claim a working HA deployment on a single laptop.

## Troubleshooting

| Problem | Resolution |
|---|---|
| `docker: command not found` | Start desktop engine; Rancher Desktop should use dockerd/moby; check PATH |
| Port 8000 already in use | Stop conflicting service or change host port in `compose.yaml` |
| Container returns 503 ready | Train model first; check artifact mount, filename and permissions |
| Docker build fails with no space | Free disk and Docker image cache; Python/PyTorch image layers are large |
| Image POST returns 422 | Use Postman Body → form-data, key `file`, type File |
| Prediction scores look random | Expected: synthetic smoke model is not trained on a real dataset |
| `torch.load` fails | Ensure model was generated by this project's script and package versions are compatible |

## Next: real transfer learning

For a genuine vision experiment, select a licensed image dataset, use approved pretrained torchvision weights, implement stratified/group-aware splits, fine-tune, report per-class metrics, and document model limitations. This smoke lab is not evidence of real-world performance.
