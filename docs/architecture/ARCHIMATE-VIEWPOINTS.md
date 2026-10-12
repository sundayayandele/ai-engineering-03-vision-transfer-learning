# ArchiMate-inspired viewpoints

This mapping uses ArchiMate concepts descriptively; it is **not** an exported standards-validated ArchiMate model.

| Layer | Actors/components | Services/artifacts |
|---|---|---|
| Business | Learner, Data Steward, ML Engineer, Operations | Dataset approval, classification, review |
| Application | Training Pipeline, Model Registry, Inference API, Observability | Training job, model version, predictions, alerts |
| Technology | Kubernetes/OpenShift, CPU/GPU nodes, object storage | Container runtime, persistent storage, networking |
| Motivation | Accuracy, reproducibility, privacy, cost controls | Policies, architecture decisions, evaluation gates |

Relationships: Business users consume Application services; Application components execute on Technology nodes; governance constrains all layers.
