---
name: devops_kubernetes
description: Kubernetes workload and cluster rules for secure, reliable, production-ready manifests.
---

# Specialist Kubernetes

## 1. Workload Basics

- Define resource requests and limits for every long-running workload.
- Use readiness probes for traffic gating and liveness probes only for true deadlock recovery.
- Prefer rolling updates with explicit surge/unavailable settings for user-facing services.
- Use labels and selectors consistently; never change immutable selectors casually.
- Store configuration in ConfigMaps and secrets through the platform's secret mechanism, not inline plaintext.

## 2. Security

- Run containers as non-root unless the image proves it cannot.
- Set `allowPrivilegeEscalation: false` where possible.
- Drop Linux capabilities by default and add back only the required capability.
- Use read-only root filesystems when the workload supports it.
- Avoid privileged pods, host networking, host PID/IPC, and hostPath mounts unless explicitly required.
- Scope service accounts and RBAC to least privilege.

## 3. Reliability

- Add PodDisruptionBudgets for workloads that must survive voluntary disruption.
- Use topology spread or anti-affinity for critical replicas.
- Keep startup, readiness, and liveness thresholds aligned with real boot and dependency behavior.
- Ensure graceful shutdown handles SIGTERM and drains in-flight requests.
- Define horizontal or vertical scaling based on measured signals, not guesses.

## 4. Review And Deployment

- Render templates before review.
- Check namespace, image tag, image pull policy, secrets, service account, and ingress exposure.
- Avoid mutable `latest` tags in production.
- Roll out with observability: watch events, pod status, rollout status, error rates, and latency.
- Keep rollback instructions ready before applying production changes.
