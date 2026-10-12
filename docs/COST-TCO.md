# TCO comparison — planning framework

Do not treat these estimates as live quotes. Fill in region/provider-specific prices before purchase.

| Deployment | Fixed monthly components | Variable components | Operational considerations |
|---|---|---|---|
| GitHub educational runner | Eligible standard runner minutes may be free | Usage beyond plan and artifact storage | Ephemeral, not hosting, no guaranteed GPU |
| Low-cost VPS | VM, block storage, backups | Egress, snapshots | Simple pilot; single VM not HA |
| AWS | EKS/EC2 or ECS, EBS, S3, ALB | GPU hours, traffic, monitoring | Managed control plane may dominate small workloads |
| Azure | AKS/VM, disk, Blob, load balancer | GPU hours, bandwidth, logs | Check cluster tier and region |
| GCP | GKE/Compute Engine, persistent disk, Cloud Storage | GPU hours, network, observability | Check cluster management fees |
| Private cloud | Servers, power, rack, network, storage | Capacity expansion, support, staffing | High up-front capital and operations |

**Formula:** monthly TCO = compute + storage + network + orchestration + observability + security + backup + support + labor + amortized capital. Separate training GPU hours from always-on inference. Compare CPU inference first for low traffic. Capture currency, date, region, HA assumptions and utilization.
