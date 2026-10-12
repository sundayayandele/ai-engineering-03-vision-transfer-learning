# Dataset strategy and licensing

**Starter candidates:** CIFAR-10 (small images, classroom experimentation), Oxford-IIIT Pet (transfer-learning exercises), and domain-specific licensed image sets. Verify each dataset's original license, attribution requirements, download restrictions and intended use before using or distributing it.

Prevent leakage: split by subject/identity or collection event where appropriate; freeze test sets; record provenance, class imbalance and preprocessing. Do not commit image datasets to Git. Synthetic random tensors in the CI lab are for pipeline verification only.
