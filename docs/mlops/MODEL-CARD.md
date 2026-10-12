# Model card — ResNet18 vision transfer learning

**Current model:** Educational synthetic-data smoke model, 2 classes, random initialization, frozen ResNet18 backbone, trained classifier head. **Not a real transfer-learning evaluation and not suitable for production decisions.**

**Intended use:** CI training/inference pipeline verification.

**Not intended for:** Clinical, identity, safety-critical, employment or consequential classification.

**Production prerequisites:** Approved labeled dataset, documented licenses, dataset split methodology, pretrained weight provenance, domain metrics (precision, recall, F1, per-class confusion matrix), calibration, bias/error review, robustness testing, drift detection, versioned registry and rollback approval.

**Artifact handling:** Store weights outside Git; verify integrity before loading.
