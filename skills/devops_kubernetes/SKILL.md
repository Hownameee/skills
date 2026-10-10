---
name: devops_kubernetes
description: "Design, review, render, diff, deploy, and troubleshoot Kubernetes manifests, Helm charts, and Kustomize overlays. Use for Kubernetes workload or cluster configuration; do not mutate a live cluster, production configuration, secrets, RBAC, or persistent data without explicit authorization."
---

# Kubernetes Workloads And Cluster Changes

## Scope And Operating Mode

- Determine whether the task is local review, manifest editing, rendered validation, live diagnosis, or live mutation.
- Default to repository and manifest inspection. Access to a cluster does not authorize changing it.
- Identify the desired-state owner: GitOps controller, Helm release, Kustomize overlay, operator, or raw manifests. Change the canonical source rather than creating configuration drift.
- Require explicit authorization covering the operation and target before any live `apply`, `patch`, `edit`, `delete`, `scale`, `rollout restart`, Helm install/upgrade/rollback, secret or RBAC change, production mutation, or persistent-data operation. Reuse that authorization while its scope holds; ask again for an uncovered action or newly discovered material impact.

## Preflight

For local editing or review, inspect the relevant canonical source and render inputs. Apply live context, rollout, and recovery checks before cluster work that depends on them:

1. Inspect repository instructions, chart or overlay structure, environment-specific values, deployment workflow, and rollback documentation.
2. Identify Kubernetes version, namespaces, CRDs, operators, admission policies, service mesh, ingress controller, storage classes, and GitOps ownership relevant to the resource.
3. For authorized live work, record the exact context and namespace:

   ```bash
   kubectl config current-context
   kubectl config view --minify
   kubectl auth can-i <verb> <resource> --namespace <namespace>
   ```

4. Confirm the image reference, expected replicas, rollout strategy, traffic path, data compatibility, observability, and rollback target.
5. Stop dependent live work if context, namespace, desired-state owner, production status, or the required rollback path is ambiguous. Continue local inspection and preparation when safe, clearly separating unresolved deployment details from verified local results.

## Manifest Review

### Workload And Reliability

- Pin production images to an immutable digest or repository-approved immutable tag; never use `latest`.
- Define measured CPU and memory requests. Add limits according to workload behavior and repository policy; account for throttling and OOM risk.
- Use startup probes for slow initialization, readiness for traffic gating, and liveness only for unrecoverable deadlock. Do not make dependency outages trigger restart storms.
- Align `terminationGracePeriodSeconds`, `preStop`, SIGTERM handling, and load-balancer draining.
- Validate rolling-update surge and unavailable values against capacity and availability requirements.
- Use PodDisruptionBudgets only when replicas and maintenance behavior make the budget satisfiable.
- Evaluate topology spread or anti-affinity for critical replicas.
- Check HPA signals and ensure requests make utilization-based scaling meaningful.

### Security And Exposure

- Run as non-root with explicit user/group settings when supported.
- Set `allowPrivilegeEscalation: false`, drop capabilities by default, use the runtime-default seccomp profile, and prefer a read-only root filesystem.
- Avoid privileged containers, host namespaces, host ports, and `hostPath` unless the requirement and risk are explicit.
- Use dedicated least-privilege service accounts and set `automountServiceAccountToken: false` when API access is unnecessary.
- Keep secrets out of manifests, rendered output, command lines, diffs, and logs. Reference the platform's existing secret mechanism.
- Review Service type, Ingress/Gateway exposure, TLS, NetworkPolicy, and source restrictions.

### Resource Integrity

- Keep labels and selectors consistent. Treat immutable selectors, PVCs, storage classes, and many Job fields as migration-sensitive.
- Validate ConfigMap and Secret rollout behavior; configuration changes may not restart pods automatically.
- Check CRD and controller ordering before creating custom resources.
- Account for admission mutation when comparing submitted and live objects.

## Render And Validate

Use the repository's existing commands first. Typical read-only checks are:

```bash
helm template <release> <chart> --namespace <namespace> --values <values-file>
kubectl kustomize <overlay>
kubectl apply --dry-run=client -f <rendered-file>
```

- Review the fully rendered resources, not templates alone.
- Run existing schema, policy, lint, and chart tests.
- If cluster access is authorized, run server-side dry-run and `kubectl diff` against the exact context and namespace. Treat `kubectl diff` exit code `1` as differences and values greater than `1` as an error.
- Review defaulted or admission-mutated fields, RBAC, ownership labels, image pull secrets, and namespace placement.
- Do not treat client-side dry-run as proof that the API server, CRDs, admission policies, or permissions will accept a resource.

## Deploy And Observe

After explicit authorization:

1. Reconfirm context, namespace, rendered diff, change window, owner, and rollback plan immediately before mutation.
2. Apply through the owning GitOps, Helm, or repository deployment workflow. Do not directly apply over a GitOps-managed resource unless explicitly authorized as an emergency action.
3. Observe rollout status with an explicit timeout:

   ```bash
   kubectl rollout status deployment/<name> --namespace <namespace> --timeout=<duration>
   ```

4. Check pods, events, controller status, application health, error rate, latency, saturation, and dependency health. Redact sensitive values.
5. Stop or roll back when the agreed threshold is crossed; do not repeatedly restart a failing workload without a diagnosis.

## Rollback And Edge Cases

- Prefer reverting the canonical GitOps source. Use Helm rollback or workload rollout undo only when compatible with the owning workflow and explicitly authorized.
- A manifest rollback does not roll back schema or persistent data. Validate backward compatibility before deployment.
- Treat StatefulSets, PVC resizing, storage-class changes, finalizers, CRD upgrades, and namespace deletion as high-risk operations with dedicated recovery plans.
- Jobs may be non-idempotent, CronJobs may overlap, and retries may duplicate external effects.
- A PodDisruptionBudget can block maintenance; an HPA can fight manual scaling; sidecars can prevent pod termination.

## Completion Checklist

Apply checks for the selected mode; local editing does not require a live rollout. Report unrun live checks only when relevant to the requested outcome.

- Canonical source, environment, context, and namespace were identified.
- Rendered output, schema/policy checks, dry-run, and diff were reviewed at the level authorized.
- No secret value appeared in source, output, or logs.
- Live mutation had explicit authorization and used the intended owner.
- Rollout and application health were verified, or the exact unrun commands and reason were reported.
- Final output lists changed resources, validation, live actions, rollback status, and residual data or availability risk.
