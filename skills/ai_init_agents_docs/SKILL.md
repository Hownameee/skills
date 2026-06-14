---
name: ai_init_agents_docs
description: "Init agents docs workflow for creating or updating repo-level and nested AGENTS.md files for Codex and Antigravity with repository structure, code flow, backend/frontend conventions, state layout, naming rules, verification, safety, and git workflow. Use when the user says \"init agents\", asks to initialize agent docs for a new software project, or wants AGENTS.md to capture repo conventions."
---

# Specialist Init Agents Docs

## 1. Scope

Use this skill when the user asks to initialize, generate, review, or update Codex/Antigravity instruction files for a software project, especially repo-level `AGENTS.md` and nested module-level `AGENTS.md` files.

Supported outputs include:

- root `AGENTS.md`
- nested `backend/AGENTS.md`, `frontend/AGENTS.md`, `infra/AGENTS.md`, app/package/service-level `AGENTS.md`, or equivalent
- concise follow-up questions for conventions that cannot be proven from the repository

## 2. Core Rule

Do not invent project conventions. Discover what can be proven from the repository, infer only when evidence is strong, and ask concise questions for missing context before writing durable instructions. If the user says to proceed with defaults, write placeholders as `TODO(user)` instead of pretending uncertain conventions are facts.

## 3. Discovery Pass

Before editing, inspect the project for:

- stack and package manager: `package.json`, lockfiles, `pyproject.toml`, `requirements*.txt`, `go.mod`, `pom.xml`, `build.gradle`, `Cargo.toml`, `.tool-versions`, Docker files
- commands: README, Makefile, Justfile, Taskfile, package scripts, CI workflows, compose files
- repository structure: top-level directories, apps/packages/services, shared libraries, module ownership, public APIs, docs, diagrams
- code flow: backend request path, frontend route/page path, state/data-fetching path, event/job/worker path, and dependency direction
- backend conventions: controller/route/handler, service/use-case, repository/DAO, adapter/client, DTO/schema/entity, validation, authorization, transaction, migration, and test layout
- frontend conventions: route/page files, page-only components, reusable `components/`, hooks, API clients, forms, state stores, styling, assets, and test layout
- state management conventions: Redux slices, selectors, thunks, RTK Query/services, Zustand stores, contexts/providers, cache invalidation, and generated client usage
- naming conventions: directories, files, components, hooks, services, repositories, controllers, DTOs, tests, migrations, env vars, branches, commits, PR titles
- generated or vendored paths: `dist`, `build`, `target`, `.next`, generated clients, protobuf output, ORM output, lockfiles, snapshots
- risky workflows: migrations, deployment, auth, billing, secrets, production data, infrastructure, public communication
- existing instruction files: `AGENTS.md`, nested `AGENTS.md`, and Codex/Antigravity-specific repository guidance

Summarize discovered facts and label uncertain items as questions, not facts.

## 4. Context Questions

Ask only for missing information that affects durable instructions. Prefer one compact question block instead of many back-and-forth turns.

Ask about:

- primary stack, package manager, runtime versions, and monorepo tooling
- canonical install, dev, build, lint, format, test, typecheck, migration, and local-run commands
- repository map: apps, services, packages, shared libraries, infra, generated-code locations
- module ownership: which directories need nested `AGENTS.md`
- backend flow: for example `controller -> service -> repository -> database`, `route -> use-case -> adapter`, or another project-specific sequence
- backend layer rules: where validation, authorization, transactions, DTO mapping, external clients, and domain logic belong
- frontend flow: route/page ownership, page-local components, reusable components, hooks, forms, API clients, styling, and asset placement
- state management layout: Redux feature folders, slices, selectors, thunks, RTK Query/services, contexts/providers, cache rules, and store naming
- naming conventions by artifact type: files, folders, components, hooks, services, repositories, DTOs, tests, migrations, env vars
- test expectations by change type and layer
- migration, deployment, rollback, release, and production-data safety rules
- security-sensitive areas such as auth, billing, secrets, permissions, PII, audit logs, and tenant isolation
- git flow: branch naming, commit message format, PR size, review expectations, changelog/release notes, merge strategy
- whether the instruction files should target Codex, Antigravity, or both

If the user cannot answer yet, create an `Open Questions` section in `AGENTS.md` and keep uncertain items out of enforceable rules.

## 5. File Planning

Create or update the smallest useful set of files:

- Root `AGENTS.md`: stable repository-wide facts, file structure, commands, architecture flow, naming, safety rules, verification, git convention, skill routing, and links to local docs.
- Nested `AGENTS.md`: only for directories with different stack, commands, architecture flow, naming, generated files, deployment, or safety rules.
- Reference docs: link existing README, architecture docs, ADRs, API docs, and runbooks instead of duplicating long material.

Do not create path-specific files just because directories exist. Create them only when they reduce ambiguity.

## 6. Content Standards

Write instructions that are:

- concise, observable, and specific to the repository or module
- detailed where the agent needs deterministic behavior: structure, flow, naming, commands, safety, and verification
- backed by file evidence, command evidence, or explicit user confirmation
- clear about precedence when multiple instruction systems coexist
- explicit about generated files that agents must not edit
- explicit about migrations, deployment, production data, billing, auth, and security approvals
- organized with small tables or code blocks when they make conventions faster to scan

Avoid:

- generic coding advice that applies to every repo
- long motivational text
- duplicated rules across root and nested files
- commands that were not verified or confirmed
- stale instructions copied from old README files without checking current repo state
- framework patterns that are not used by the repository

## 7. Recommended Root AGENTS.md Shape

Use this structure unless the repository already has a better local convention:

```markdown
# Agent Operating Guide

## Scope And Precedence

## Project Snapshot

## Repository Structure

## Commands

## Architecture And Code Flow

## Backend Conventions

## Frontend Conventions

## State Management

## Naming Conventions

## Generated And External Files

## Testing And Verification

## Safety And Approvals

## Git Convention

## Documentation And Decisions

## Module Instructions

## Open Questions
```

Keep root instructions stable and repository-wide. Move module-specific details into nested files when they differ by path.

## 8. Recommended Convention Tables

Use compact tables when conventions are detailed:

```markdown
## Repository Structure

| Path | Purpose | Agent notes |
| --- | --- | --- |
| `backend/` | API service | Follow `backend/AGENTS.md` for layer rules. |
| `frontend/` | Web app | Page-only components stay near the route. |

## Architecture And Code Flow

| Flow | Path | Rules |
| --- | --- | --- |
| Backend request | `controller -> service -> repository -> database` | Keep business logic in services; repositories do persistence only. |
| Frontend page | `page -> page components -> shared components -> hooks/API client` | Promote components to shared only after reuse. |

## Naming Conventions

| Artifact | Convention | Example |
| --- | --- | --- |
| React component | `PascalCase.tsx` | `UserMenu.tsx` |
| Hook | `useThing.ts` | `useCurrentUser.ts` |
| Migration | timestamped descriptive name | `202606150945_add_users_table.sql` |
```

Replace examples with repository-specific facts or `TODO(user)` questions.

## 9. Recommended Nested AGENTS.md Shapes

Use the relevant shape for module-specific files.

Backend:

```markdown
# Agent Guide: Backend

## Scope

## Commands

## Request Flow

## Layer Responsibilities

## DTO, Entity, Repository, And Migration Rules

## Tests

## Local Safety Rules
```

Frontend:

```markdown
# Agent Guide: Frontend

## Scope

## Commands

## Route And Page Layout

## Component Placement

## State, API, And Data Fetching

## Styling And Assets

## Tests
```

Infra:

```markdown
# Agent Guide: Infra

## Scope

## Commands

## Environment Layout

## Plan, Apply, And Rollback Rules

## State, Secrets, And Production Safety

## Verification
```

Nested files should add or override only what differs from the root file.

## 10. Update Rules

When files already exist:

- preserve useful current rules
- merge duplicate content into the closest correct file before removing repetition
- mark stale or unverified commands for user confirmation instead of deleting silently
- keep root instructions broad and move module-specific details down
- do not overwrite custom human-maintained sections without explaining the merge
- keep a short `Open Questions` section for conventions that need human confirmation

## 11. Validation

After writing files:

- check links and referenced paths exist when they are local
- verify commands that are safe and cheap to run
- report commands that were not run
- run repository validation if the repo has a validator
- inspect the final `AGENTS.md` for these required convention areas:
  - file structure
  - code flow
  - naming conventions
  - commands
  - tests/verification
  - generated/external files
  - safety approvals
  - git convention
  - open questions for unknown conventions

For Codex, suggest testing with:

```text
Summarize the current instructions that apply before doing work.
```

For Antigravity, suggest starting a fresh agent in the repository and asking it to summarize the applicable `AGENTS.md` instructions before editing.
