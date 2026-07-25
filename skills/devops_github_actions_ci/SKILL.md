---
name: devops_github_actions_ci
description: "Design, review, and troubleshoot GitHub Actions workflows for CI, release, and deployment with least-privilege permissions. Use for files under .github/workflows or reusable actions; do not publish releases, change secrets or cloud roles, approve environments, or deploy without explicit authorization."
---

# GitHub Actions CI/CD

## Scope And Authority

- Distinguish local workflow editing, read-only run diagnosis, rerunning a job, changing repository settings, publishing a release, and deployment. Authorization for one does not authorize the others.
- Ask before adding or broadening write permissions, creating or changing secrets, variables, environments, approval rules, OIDC trust, cloud roles, release publication, or deployment.
- Treat workflow files as production code: they can expose credentials, execute untrusted code, and mutate external systems.

## Preflight

1. Read repository instructions, existing workflows, local or composite actions, dependency lockfiles, release documentation, and required checks.
2. Identify each trigger, actor trust level, token permissions, secret availability, environment, runner type, external service, and side effect.
3. For a failed run, inspect the exact failing step and logs before editing. Classify dependency, test, build, permission, credential, runner, cache, artifact, rate-limit, or external-service failure.
4. Reproduce the underlying project command locally when the repository provides an equivalent command.
5. Preserve the existing package manager, runtime setup, cache strategy, and reusable-workflow contract unless the task requires changing them.

## Event Trust Model

- `pull_request` code and metadata are untrusted. Its default restricted token and lack of secrets for forks are security boundaries, not inconveniences to bypass.
- `pull_request_target` runs in the trusted base context. Never check out or execute the pull request head, install its dependencies, run its scripts, or consume its artifacts in a job with secrets or write permissions.
- `workflow_run` is privileged only when intentionally designed. Validate the source workflow, repository, branch, event, conclusion, and artifact provenance before using its outputs.
- Treat `workflow_dispatch` inputs, issue and PR text, commit messages, branch names, matrix values, and API responses as untrusted.
- Do not interpolate untrusted expressions directly into `run:` scripts. Pass them through a typed action input or environment variable and quote them for the active shell.
- Do not let untrusted workflows populate caches or artifacts later consumed by privileged jobs without a verified trust boundary.

## Permissions, Identity, And Secrets

- Start with `permissions: {}` or the repository's minimal read baseline, then grant the smallest per-job permissions.
- Give `id-token: write` only to the job that obtains an OIDC token. Restrict the cloud trust policy by repository, workflow, ref or protected environment, subject, and audience.
- Prefer short-lived OIDC credentials to long-lived cloud keys when the existing platform supports it.
- Never print secrets, tokens, signed URLs, credentials, private keys, full cloud responses, or sensitive environment dumps.
- Avoid broad `secrets: inherit` in reusable workflows. Pass only the named secrets required by the called contract.
- Pin third-party actions to full commit SHAs when repository policy permits, retaining a comment with the reviewed release version. Review action ownership and source before adding it.
- Protect workflow and local-action paths with the repository's ownership and branch-review controls when available.

## Workflow Design

- Keep workflows small and named by purpose. Separate untrusted validation from privileged release or deployment.
- Use existing project scripts rather than duplicating long shell logic in YAML.
- Type reusable-workflow and manual inputs, validate enumerated values, and provide least-privilege defaults.
- Bound matrices and dynamic fan-out. Use explicit `timeout-minutes` for jobs and steps that can hang.
- Use `concurrency` with a stable, trust-safe group and choose cancellation behavior deliberately. Never interpolate attacker-controlled text into a privileged concurrency key without normalization.
- Retry only known transient external operations, with bounded attempts and backoff. Do not hide deterministic test failures.
- Specify the shell when shell semantics matter and enable fail-fast behavior appropriate to that shell.

## Dependencies, Caches, And Artifacts

- Derive dependency cache keys from operating system, runtime, architecture when relevant, package manager, and the canonical lockfile hash.
- Do not cache secrets, credentials, build signing material, or arbitrary workspace state.
- Separate cache namespaces for trusted and untrusted events when poisoning could cross the trust boundary.
- Upload only necessary artifacts, use the minimum retention period, avoid sensitive content, and validate artifact source and integrity before privileged use.
- Treat downloaded artifacts as untrusted files until their producing workflow, commit, and expected contents are verified.

## Release And Deployment Gates

- Use protected environments and required reviewers for production where repository policy supports them.
- Pin the artifact or image being promoted; rebuilds can produce a different result.
- Serialize deployments when concurrent changes could conflict.
- Define health checks, rollback, and partial-failure handling before deployment.
- Do not approve a protected environment, publish a package or release, create a tag, upload signing material, or deploy unless the user explicitly requests the action.

## Validation

1. Review the workflow diff, including permissions, events, expressions, action SHAs, shells, cache keys, artifacts, and environment selection.
2. Parse YAML with the repository's existing tooling.
3. Run `actionlint` when it is already installed or provided by the repository:

   ```bash
   actionlint .github/workflows/*.yml .github/workflows/*.yaml
   ```

4. Run the equivalent local lint, test, build, or packaging command where practical.
5. For an authorized remote rerun, rerun only the minimum failed workflow or job and inspect the result. A manual run does not prove fork-event safety.
6. Verify that no secret value entered logs or artifacts and that permissions did not broaden unexpectedly.

## Completion Checklist

- Trigger and fork trust boundaries are documented and preserved.
- Permissions, secrets, OIDC claims, third-party actions, expressions, caches, and artifacts were reviewed.
- Jobs have bounded time and fan-out; deployment jobs have concurrency and recovery behavior.
- YAML and available workflow linting passed.
- The underlying project command passed locally or the validation limit is explicit.
- No release, deployment, secret, role, environment, or external state changed without explicit authorization.
