# GreenOps — Initial Architecture (Provisional)

This is a high-level planning architecture. Exact scheduling logic and model inputs are pending full-paper review.

## Phase 1 — Cloud platform

```text
Developer
   |
   v
GitHub repository
   |
   v
GitHub Actions: lint/test -> build container -> publish image to GHCR
   |
   v
Cloud VM (candidate: OCI) -> K3s cluster -> sample application
                              |                 |
                              |                 +-> health endpoint
                              +-> metrics -> Prometheus -> Grafana

Developer portal (Streamlit) -> FastAPI platform backend -> approved deployment workflow
Terraform -> provisions/configures supported cloud infrastructure
```

## Phase 2 — scheduling research prototype

```text
Workload traces / synthetic workload scenarios
                  |
                  v
          Workload model
                  |
                  v
     Resource and tier model (simulated)
                  |
       +----------+----------+
       |                     |
       v                     v
 Energy/carbon model     SLA model
       |                     |
       +----------+----------+
                  |
                  v
       Optimization / scheduler
       (paper formulation to verify)
                  |
                  v
      Baseline and proposed schedules
                  |
                  v
     Experimental evaluation/dashboard
                  |
                  v
  Optional Kubernetes Job execution adapter
```

## Design boundaries

- The platform is cloud-hosted; logical edge/fog tiers may be simulated.
- Renewable generation and battery storage are modelled only if the full paper's formulation and available data support them.
- Do not claim physical data-centre energy measurements unless the measurement source genuinely provides them.
- Keep the optimization experiment reproducible independently of the Kubernetes deployment layer.
