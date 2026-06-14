---
name: ai_init_agents_docs
description: Init agents docs workflow for creating or updating repo-level and nested AGENTS.md files for Codex and Antigravity. Use when the user says "init agents" or asks to initialize agent docs for a new software project.
---

# Specialist Init Agents Docs

## 1. Scope

Use this skill when the user asks to initialize, generate, review, or update Codex/Antigravity instruction files for a software project, especially repo-level `AGENTS.md` and nested module-level `AGENTS.md` files.

Supported outputs include:

- `AGENTS.md`
- nested `backend/AGENTS.md`, `frontend/AGENTS.md`, `infra/AGENTS.md`, package-level `AGENTS.md`, or equivalent

## 2. Core Rule

Do not invent project conventions. Discover what can be proven from the repository, then ask concise questions for missing context before writing durable instructions.

## 3. Discovery Pass

Before editing, inspect the project for:

- stack and package manager: `package.json`, lockfiles, `pyproject.toml`, `requirements*.txt`, `go.mod`, `pom.xml`, `build.gradle`, `Cargo.toml`, `.tool-versions`, Docker files
- commands: README, Makefile, Justfile, Taskfile, package scripts, CI workflows, compose files
- architecture boundaries: top-level directories, apps/packages/services, imports, module names, docs, diagrams
- generated or vendored paths: `dist`, `build`, `target`, `.next`, generated clients, protobuf output, ORM output, lockfiles, snapshots
- risky workflows: migrations, deployment, auth, billing, secrets, production data, infrastructure, public communication
- existing instruction files: `AGENTS.md`, nested `AGENTS.md`, and Codex/Antigravity-specific repository guidance

Summarize discovered facts and label uncertain items as questions, not facts.

## 4. Context Questions

Ask only for missing information that affects durable instructions. Prefer one compact question block instead of many back-and-forth turns.

Ask about:

- primary stack, package manager, runtime versions, and monorepo tooling
- canonical install, dev, build, lint, format, test, typecheck, and migration commands
- repo architecture: apps, services, packages, shared libraries, infra, generated-code locations
- module ownership: which directories need nested `AGENTS.md`
- code style conventions not enforceable by tooling
- test expectations by change type
- migration, deployment, rollback, release, and production-data safety rules
- security-sensitive areas such as auth, billing, secrets, permissions, PII, and audit logs
- git, branch, commit, PR, review, and changelog conventions
- whether the instruction files should target Codex, Antigravity, or both

If the user says to proceed with defaults, write conservative placeholders marked as questions or `TODO(user)`.

## 5. File Planning

Create or update the smallest useful set of files:

- Root `AGENTS.md`: stable repository-wide facts, commands, safety rules, verification, skill routing, and links to local docs.
- Nested `AGENTS.md`: only for directories with different stack, commands, ownership, generated files, deployment, or safety rules.
Do not create path-specific files just because directories exist. Create them only when they reduce ambiguity.

## 6. Content Standards

Write instructions that are:

- concise and observable
- specific to the repository or module
- easy to validate by reading files or running commands
- free of secrets, private tokens, confidential customer data, and unverified production details
- clear about precedence when multiple instruction systems coexist
- explicit about generated files that agents must not edit
- explicit about migrations, deployment, production data, billing, auth, and security approvals

Avoid:

- generic coding advice that applies to every repo
- long motivational text
- duplicated rules across root and nested files
- commands that were not verified or confirmed
- stale instructions copied from old README files without checking current repo state

## 7. Recommended Root AGENTS.md Shape

Use this structure unless the repository already has a better local convention:

```markdown
# Agent Operating Guide

## Scope And Precedence

## Project Snapshot

## Commands

## Architecture Boundaries

## Generated And External Files

## Coding Standards

## Testing And Verification

## Safety And Approvals

## Git And Review

## Documentation

## Module Instructions
```

Keep the file short. Link to existing docs instead of copying long explanations.

## 8. Recommended Nested AGENTS.md Shape

Use this for module-specific files:

```markdown
# Agent Guide: <module>

## Scope

## Module Commands

## Local Architecture

## Generated Files

## Local Safety Rules

## Verification
```

Nested files should add or override only what differs from the root file.

## 9. Update Rules

When files already exist:

- preserve useful current rules
- remove duplicates only after merging unique content into the correct location
- mark stale or unverified commands for user confirmation instead of deleting silently
- keep root instructions broad and move module-specific details down
- do not overwrite custom human-maintained sections without explaining the merge

## 10. Validation

After writing files:

- check links and referenced paths exist when they are local
- verify commands that are safe and cheap to run
- report commands that were not run
- run repository validation if the repo has a validator
- provide a short list of questions still needing user confirmation

For Codex, suggest testing with:

```text
Summarize the current instructions that apply before doing work.
```

For Antigravity, suggest starting a fresh agent in the repository and asking it to summarize the applicable `AGENTS.md` instructions before editing.
