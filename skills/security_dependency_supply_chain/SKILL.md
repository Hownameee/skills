---
name: security_dependency_supply_chain
description: Dependency and software supply-chain security rules for package selection, updates, provenance, and releases.
---

# Specialist Dependency & Supply Chain Security

## 1. Dependency Intake

- Prefer standard library and existing project dependencies before adding a new package.
- Check package purpose, maintainer reputation, release history, license, source repository, and transitive dependency size.
- Reject packages with unclear ownership, suspicious install scripts, obfuscated code, or unrelated broad permissions.
- Avoid adding dependencies for trivial helpers.

## 2. Versioning And Lockfiles

- Keep lockfiles committed for applications.
- Update dependencies intentionally with release notes and compatibility review.
- Avoid broad unbounded version ranges for production applications.
- Do not mix package managers for the same dependency graph.

## 3. Build And Release Integrity

- Prefer reproducible builds where the ecosystem supports them.
- Generate provenance or attestations for release artifacts when supported by the CI/CD platform.
- Sign or verify critical release artifacts when the project already has a signing workflow.
- Pin base images and high-risk CI actions to immutable references when security matters.

## 4. Vulnerability Handling

- Triage vulnerabilities by exploitability in this project, not CVSS alone.
- Prefer minimal upgrades that preserve compatibility for urgent security fixes.
- Add regression tests for vulnerable behavior when feasible.
- Remove abandoned, duplicate, or unused dependencies during security cleanup.
