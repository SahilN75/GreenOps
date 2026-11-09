# GreenOps — Project Plan

## Working title

**GreenOps: A Cloud-Native Platform for Energy-Efficient and SLA-Aware Workload Scheduling**

## Problem statement

Cloud workload schedulers must allocate tasks while balancing resource availability, energy use, carbon impact, and service-level requirements. This project proposes a cloud-hosted platform that provides an automated application-delivery workflow and an experimental scheduling engine for evaluating energy- and SLA-aware workload allocation.

## Objectives

1. Build a cloud-hosted environment for deploying and monitoring containerized applications.
2. Automate test, build, image publication, and deployment through CI/CD.
3. Provide standardized self-service deployment operations through a lightweight developer portal.
4. Model workloads, compute-resource tiers, energy use, carbon intensity, and SLA requirements based on the selected IEEE paper.
5. Implement and evaluate the paper's scheduling approach to the extent feasible within the project timeline.
6. Compare the proposed approach with suitable baseline schedulers using consistent workloads and metrics.

## Two phases

### Phase 1 — Cloud platform foundation

- Provision a small cloud VM only after checking current free-tier terms, regional capacity, and budget controls.
- Install a lightweight Kubernetes distribution (candidate: K3s).
- Containerize a sample service.
- Create GitHub Actions workflows for tests, image build, registry push, and deployment.
- Define infrastructure and deployment configuration as code.
- Add a minimal developer portal and service/cluster monitoring.

**Exit criteria:** a code change triggers a tested container build and deployment to the cloud-hosted cluster; deployment and health status are visible.

### Phase 2 — Sustainable scheduling research prototype

- Extract the base paper's exact model and experimental assumptions.
- Define workload and resource inputs.
- Implement energy/carbon and SLA calculations from verified definitions.
- Implement the selected optimization method(s) and baseline(s).
- Connect scheduling decisions to a Kubernetes Job execution prototype where feasible.
- Visualize schedules, resource use, SLA outcomes, energy estimates, and carbon estimates.

**Exit criteria:** repeatable experiments compare baseline and proposed scheduling under the same input scenarios, with assumptions and limitations documented.

## Research integrity gate

The full IEEE paper is not yet available in the project workspace. Do not invent its equations, constraints, parameter values, or reported results. Mark all such items as pending until the full text is reviewed.

## Initial six-week schedule

| Week | Target |
|---|---|
| 1 | Obtain/review paper; confirm model; repository and cloud feasibility |
| 2 | VM, container runtime, K3s, sample service |
| 3 | CI/CD, registry, automated deployment |
| 4 | Developer portal, monitoring, Phase 1 evaluation |
| 5 | Workload/energy/SLA model and optimization prototype |
| 6 | Baseline comparison, dashboard, report and demonstration |

This is a target plan, not a guarantee. If cloud provisioning or the paper's model is more complex than expected, prioritize a reliable end-to-end prototype and transparent evaluation.

## Initial metrics to investigate

- Total estimated energy (kWh)
- Estimated grid carbon emissions (gCO2e)
- SLA violation count/rate and penalty, if defined by the paper
- Task completion time and waiting time
- Resource utilization
- Solver runtime / algorithm runtime
- Feasibility rate and deadline misses

Final metric definitions must follow the paper and the chosen experimental model.
