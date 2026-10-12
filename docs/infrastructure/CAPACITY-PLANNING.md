# Capacity planning (illustrative; validate by benchmark)

| Profile | Replicas | CPU each | RAM each | Storage | GPU |
|---|---:|---:|---:|---:|---|
| Educational CPU lab | 1 ephemeral job | 2–4 vCPU runner typical; verify actual | 4–8 GiB planning | 5–15 GiB ephemeral budget | None |
| Small pilot inference | 2 | 1–2 vCPU | 2–4 GiB | 20–50 GiB artifacts/logs | Optional |
| Production inference | 3+ across nodes | 2–4 vCPU | 4–8 GiB | 100+ GiB plus object store | Workload dependent |
| Fine-tuning worker | 1+ batch worker | 4–16 vCPU | 16–64 GiB | 100–500 GiB | Optional 8–24+ GiB VRAM |

**Notes:** ResNet18 inference can run on CPU. Training/fine-tuning throughput and GPU needs depend on image resolution, batch size, architecture and dataset size. These are planning bands, not benchmarked guarantees. HA requires independent failure domains, probes, scaling and observability.
