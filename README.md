# GreenOps

**A Cloud-Native Platform for Energy-Efficient and SLA-Aware Workload Scheduling**

GreenOps is a student research and engineering project that combines a cloud-hosted developer platform with an energy- and carbon-aware workload scheduling prototype. The project is organized into two phases:

- **Phase 1 — Cloud platform foundation:** infrastructure automation, containerized applications, CI/CD, Kubernetes deployment, a developer portal, and monitoring.
- **Phase 2 — Sustainable scheduling:** workload modelling, energy and carbon estimation, SLA-aware scheduling, optimization experiments, and a sustainability dashboard.

## Research foundation

The instructor-selected base paper is:

> *A Comprehensive Model for Energy-Efficient and SLA-Aware Task Scheduling in the Cloud–Edge Computing Continuum*, IEEE Transactions on Sustainable Computing, Early Access.

The complete paper has not yet been obtained. Therefore, the exact mathematical formulation, decision variables, constraints, objective functions, and experimental settings are **pending verification against the full paper**. No implementation in this repository should be described as an exact reproduction until that verification is complete.

## Proposed implementation direction

The infrastructure is intended to be cloud-hosted. Cloud/edge/fog tiers, renewable generation, and battery behaviour may initially be represented as logical simulation inputs rather than physical edge devices or batteries. The final scope will be confirmed after extracting the paper's model.

Potential technologies (subject to free-tier and compatibility checks):

- Cloud VM: OCI Always Free, subject to region capacity and current terms
- Containerization: Docker
- Orchestration: K3s/Kubernetes
- CI/CD: GitHub Actions
- Container registry: GitHub Container Registry (GHCR)
- Infrastructure as Code: Terraform
- Backend: Python/FastAPI
- Developer portal: Streamlit
- Monitoring: Prometheus/Grafana
- Optimization: Python MILP solver and NSGA-II library, selected after paper review

## Repository layout

```text
phase1/       Cloud platform, CI/CD, Kubernetes, platform portal, monitoring
phase2/       Workload, energy, carbon, optimization, scheduler, dashboard
research/     Base paper notes, literature review, methodology
 docs/        Architecture and project planning documents
```

## Project status

**Current milestone:** repository foundation and research extraction.

Not yet implemented: cloud resources, CI/CD workflows, Kubernetes workloads, optimization algorithms, or emissions calculations.

## Responsible evaluation

All reported energy and carbon values must state their source, assumptions, units, and whether they are measured or estimated. Baseline and optimized schedulers must be compared using the same workload inputs and evaluation conditions. SLA violations and scheduling delay must be reported alongside energy and emissions.

## Getting started

See [`docs/PROJECT_PLAN.md`](docs/PROJECT_PLAN.md) and [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md). The exact algorithm design is intentionally pending full-paper review.
