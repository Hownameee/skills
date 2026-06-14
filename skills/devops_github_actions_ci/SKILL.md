---
name: devops_github_actions_ci
description: GitHub Actions CI/CD workflow standards for secure, reliable, and maintainable automation.
---

# Specialist GitHub Actions CI/CD

## 1. Workflow Design

- Keep workflows small, named by purpose, and scoped to clear events.
- Split fast validation from slow release or deployment jobs.
- Use `concurrency` for branches, pull requests, and deployments where duplicate runs create noise or risk.
- Prefer reusable workflows for shared organization patterns.
- Always define explicit job permissions instead of relying on broad defaults.

## 2. Security

- Set `permissions: read-all` or minimal per-job permissions, then elevate only where necessary.
- Prefer OpenID Connect for cloud deployments instead of long-lived cloud secrets.
- Never store sensitive data as plaintext in workflow YAML.
- Never log secrets, tokens, signed URLs, private keys, or generated credentials.
- Treat pull request titles, branch names, issue text, commit messages, and workflow inputs as untrusted input.
- Pass untrusted context through environment variables or action inputs before shell use.
- Pin high-risk third-party actions to full commit SHAs when security matters.
- Require CODEOWNERS review for `.github/workflows/**`.

## 3. Reliability

- Use official setup actions where available.
- Cache dependencies by lockfile hash, not broad directory names.
- Keep matrix builds explicit and bounded.
- Upload artifacts only when they are needed for debugging, deployment, or release evidence.
- Use timeouts on jobs that call external services.

## 4. Debugging Failed CI

- Read the failing job log before editing workflow files.
- Identify whether the failure is dependency install, test, lint, build, credential, permission, cache, or runner environment.
- Reproduce locally when the project provides equivalent commands.
- Fix the underlying project or environment issue before changing CI to hide the failure.
- After edits, verify the YAML syntax and rerun only the minimum required jobs.
