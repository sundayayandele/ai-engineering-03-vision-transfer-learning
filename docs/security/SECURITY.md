# Security and responsible vision AI

- Never commit identifiable or sensitive images, secrets or model artifacts.
- Validate MIME/content and image dimensions; enforce upload size limits, rate limiting and authentication at the ingress.
- Record dataset licenses, privacy basis, consent where needed and retention/deletion rules.
- Pin dependency and container versions for release; scan images and dependencies.
- Store model weights in controlled artifact storage; verify hashes and provenance before loading.
- Audit model changes and release approvals; monitor drift and inappropriate use.
- Review fairness, accessibility and error costs for the actual image classification domain.

The initial FastAPI app is a learning demo; it does not implement production auth, ingress controls or all listed security controls.
