# Enterprise deployment reference — Project 03

**Status:** Manifests are a starter/reference, not a verified production deployment.

## Build and publish

1. Train/evaluate on an approved, licensed dataset and record the model card.
2. Approve a trusted model artifact and publish it to controlled storage.
3. Build and scan the Docker image, pin dependencies and publish to a private or approved registry.
4. Replace the image placeholder in `deploy/kubernetes/deployment.yaml` with an immutable digest.
5. Provision a Kubernetes/OpenShift cluster, metrics-server, suitable storage, ingress authentication, observability and secret management.
6. Prepopulate `vision-model-pvc` with `smoke_resnet18.pt` or an approved compatible model. **The demo smoke weights are not production-accurate.**
7. Deploy `storage.yaml`, `deployment.yaml`, `availability.yaml`; for OpenShift optionally deploy `deploy/openshift/route.yaml`.
8. Confirm two replicas are on separate nodes/failure domains; test readiness, liveness, rollouts, disruption budget, autoscaling and rollback.

## Critical integration limitations

- `ReadOnlyMany` PVCs depend on your storage provider; use an init container/artifact downloader or object store CSI if unavailable.
- OpenShift restricted security policies may require an arbitrary UID-compatible image and writable home/temp configuration; adapt and validate before deployment.
- The inference API has **no built-in authentication or rate limiting**. Place it behind a secure gateway.
- HPA requires working metrics-server and resource requests; multi-node HA requires topology spread or anti-affinity and separate worker nodes.
- The demo model is trained on random tensors and has no meaningful classification accuracy.
- Production release gates should include image scanning, signed artifact provenance, real-dataset evaluation, performance tests and incident/rollback drills.
