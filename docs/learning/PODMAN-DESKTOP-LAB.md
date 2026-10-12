# Project 03 — Podman Desktop local lab

This guide runs the **Educational / Portfolio** image-classification smoke model locally with Podman Desktop. The synthetic, randomly initialized model is **not** a validated vision classifier.

## Prerequisites

- Git and Python 3.12; allow at least 8 GiB RAM and 10–20 GiB free disk for PyTorch dependencies and container images.
- [Podman Desktop](https://podman-desktop.io/) and a working Podman engine. On Windows/macOS, create and start a **Podman machine** in Podman Desktop's onboarding screen. On Linux, start the rootless Podman service as appropriate.
- Optional: Postman for the HTTP API lab.

## 1. Clone your fork and create a branch

```bash
git clone https://github.com/YOUR_USERNAME/ai-engineering-03-vision-transfer-learning.git
cd ai-engineering-03-vision-transfer-learning
git switch -c learner/podman-lab
```

Replace YOUR_USERNAME with your GitHub account. The lab changes remain on your branch.

## 2. Check Podman Desktop

Open Podman Desktop. Complete onboarding, install Podman if prompted and start the Podman machine (Windows/macOS). Confirm the engine is connected in the dashboard. In a terminal:

```bash
podman version
podman info
```

Windows/macOS: if the machine is not running, use Podman Desktop's **Podman machine** start action or `podman machine start`. On Linux rootless Podman generally does not require a machine.

## 3. Train the educational model on the host

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python scripts/train_smoke.py
pytest -q
```

On Windows PowerShell: `py -3.12 -m venv .venv`, then `.venv\Scripts\Activate.ps1`. Confirm `artifacts/smoke_resnet18.pt` exists. Do not commit this artifact.

## 4. Build the inference image

```bash
podman build -t project03-vision-inference:local .
```

The image contains the application but not the trained model. The model will be mounted read-only at runtime.

## 5. Run the container

From the repository root on Linux/macOS/WSL/Git Bash:

```bash
podman run -d --name project03-vision \
  -p 127.0.0.1:8000:8000 \
  --cpus 2 --memory 2g \
  --security-opt no-new-privileges \
  -e MODEL_PATH=/app/artifacts/smoke_resnet18.pt \
  -v "$PWD/artifacts:/app/artifacts:ro" \
  project03-vision-inference:local
```

On SELinux-enforcing Linux hosts, a read-only bind mount may require `:ro,Z` instead of `:ro` for relabeling. Do **not** use privileged mode to work around mount issues. On Windows PowerShell replace `$PWD/artifacts` with a path resolved for the Podman machine, for example `${PWD}/artifacts`, and use PowerShell line continuation or a single command line. Host-to-VM volume sharing depends on your Podman machine configuration.

Inspect:

```bash
podman ps
podman logs project03-vision
podman stats --no-stream project03-vision
```

## 6. Test endpoints in a browser or Postman

- `GET http://127.0.0.1:8000/health/live` → 200
- `GET http://127.0.0.1:8000/health/ready` → 200 once the model is loaded
- `GET http://127.0.0.1:8000/docs` → interactive OpenAPI docs
- Postman: **POST** `http://127.0.0.1:8000/predict` → **Body → form-data** → key `file`, type **File**, select a JPEG/PNG under 5 MiB → **Send**.

The JSON contains `classes`, `probabilities` and a warning about the synthetic smoke model. These predictions have no meaningful real-world accuracy.

## 7. Cleanup

```bash
podman rm -f project03-vision
```

Optional: remove the locally built image with `podman rmi project03-vision-inference:local`. Preserve the trained artifact only if you need to repeat the lab.

## Troubleshooting

| Symptom | Resolution |
|---|---|
| Podman cannot connect | Start the Podman machine (Windows/macOS), check `podman info` |
| Port 8000 in use | Stop the other process or change the host-side port |
| Ready endpoint 503 | Train first; inspect artifact path, mount, file permissions and logs |
| Permission denied on Linux bind mount | Review rootless UID mapping and SELinux relabeling (`:ro,Z`) |
| Host path not mounted on Windows/macOS | Check Podman machine file sharing and absolute path resolution |
| Out of memory | Increase Podman machine resources and retry with sufficient host RAM |
| Prediction returns 422 | Use Postman form-data key `file`, type File |
| Image build takes time | PyTorch dependencies and image layers are large; check disk capacity |

## Optional Podman Compose

Podman Desktop can support Compose through an installed Compose provider. Provider availability and commands vary. The committed `compose.yaml` is designed for Docker Compose; use the explicit `podman build` and `podman run` steps above for the most predictable lab. For Kubernetes, see the separate [enterprise deployment guide](../DEPLOYMENT.md). A single desktop machine is not an HA cluster.
