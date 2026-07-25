---
name: ai_init_agents_docs
description: "Create or update repository instruction files from evidence in the current checkout. Use when initializing or auditing Codex AGENTS.md guidance or Antigravity rule files for a concrete project; use ai_skill_authoring instead for reusable SKILL.md design."
---

# Repository Agent Instructions

## Scope And Boundaries

Turn verified repository conventions into concise instructions that future agents can follow.

Possible targets include:

- Codex `AGENTS.md` or `AGENTS.override.md` files
- Antigravity `.agents/rules` files when that host and format are explicitly in scope
- a small set of questions for conventions that cannot be established from files or user confirmation

Do not use this skill to design a reusable `SKILL.md`; use `ai_skill_authoring`. Do not assume that Codex and Antigravity discover, scope, or prioritize repository instructions identically.

## Evidence Rules

- Treat live code, executable scripts, CI, and explicit user confirmation as stronger evidence than prose documentation.
- Label statements as verified, inferred, or unknown while drafting. Put only verified facts and explicitly approved policies into enforceable rules.
- Use `TODO(user)` or an `Open Questions` section for unresolved conventions; never invent commands, ownership, architecture, or host behavior.
- Preserve useful human-authored instructions and unrelated changes. Resolve contradictions from evidence or ask when the choice materially affects future work.
- Keep generic engineering advice out of repository instructions unless it records an intentional repository policy.

## Host Discovery Matrix

Record which behavior was verified instead of presenting a cross-host assumption as fact:

| Host | Verified model |
| --- | --- |
| Codex | Reads global guidance, then project files from repository root toward the working directory. In each directory, an override file wins over the regular file; closer project guidance overrides earlier guidance. Discovery occurs when the session starts, so use a fresh session to test changes. |
| Antigravity | Rules live under `.agents/rules`; skills can live under `.agents/skills`. Confirm current rule scope and activation in the installed host. Do not claim that nested `AGENTS.md` precedence applies. |
| Other host | Consult its current local or official documentation before choosing filenames, limits, scope, or precedence. |

For Codex, keep the combined project guidance below its configured instruction-size limit; the default is 32 KiB. Keep each Antigravity rule file below its documented 12,000-character limit.

## Workflow

### 1. Preflight

1. Confirm repository root, working directory, requested hosts, and whether the task is create, merge, or audit.
2. Inspect version-control status before editing and preserve unrelated changes.
3. Find all existing repository instruction files, including nested files and host-specific rules.
4. Read the files that apply to the target path before proposing another layer.
5. Check repository documentation for canonical commands or instruction-generation scripts.

### 2. Build An Evidence Map

Inspect only relevant sources:

- stack and versions: manifests, lockfiles, tool-version files, and container definitions
- commands: README, Makefile, task runners, package scripts, CI, and development containers
- structure and flow: entrypoints, routes, services, data access, workers, state, shared libraries, and public interfaces
- conventions: representative source files, tests, migrations, generated code, and naming patterns
- safety: authentication, authorization, billing, secrets, personal data, infrastructure, deployment, and production workflows
- contribution process: test requirements, branches, commits, reviews, releases, and ownership

Trace at least one representative runtime path instead of inferring architecture from directory names. Record evidence locations so questionable rules can be checked.

### 3. Resolve Material Unknowns

Ask one compact set of questions only for choices that would materially change durable guidance, such as canonical commands, target hosts, module ownership, or production approval policy. If safe defaults are authorized, keep unresolved facts explicitly marked.

### 4. Choose The Smallest Instruction Set

- Put stable repository-wide rules at the root.
- Add a path-scoped file only when its commands, architecture, generated-code policy, or safety rules differ.
- Link to canonical local documentation instead of copying it.
- Do not create one file per directory or duplicate parent rules.
- If multiple hosts are requested, share stable content where the hosts truly consume the same file; otherwise generate the smallest host-specific representation and document the distinction.

### 5. Write Observable Rules

Prefer:

- `Run <existing command> after changing <scope>` over `test thoroughly`.
- `Do not edit <generated path>; run <generator>` over `avoid generated files`.
- path and symbol examples taken from the current checkout
- explicit approval gates for destructive changes, migrations, deployments, secrets, production data, billing, authentication, authorization, and public communication
- concise precedence language and links to specialized local skills

Avoid generic style advice, unverified commands, stale README content, framework patterns absent from the checkout, and rules that depend on one agent UI.

Use this root shape only when the sections are relevant:

```markdown
# Agent Operating Guide

## Scope And Precedence
## Project Snapshot
## Repository Structure
## Commands
## Architecture And Code Flow
## Naming Conventions
## Generated And External Files
## Testing And Verification
## Safety And Approvals
## Git Convention
## Module Instructions
## Open Questions
```

## Merge And Safety Rules

When files already exist:

- preserve human-owned sections and unrelated changes
- merge duplicate rules into the closest correct scope
- move path-specific rules downward only when that improves correctness
- mark stale commands for confirmation instead of silently treating them as valid
- explain any conflict whose resolution changes behavior

Do not add files outside user scope, change production configuration, or perform destructive repository operations as part of documentation initialization.

## Verification Checklist

- Frontmatter or rule-file syntax is valid for the selected host.
- Local links and referenced paths exist.
- Safe, cheap commands were verified; unrun commands are identified.
- Root and nested guidance have no unexplained contradiction or duplication.
- Commands, code flow, naming, generated paths, verification, safety, and unresolved questions are covered where relevant.
- Instruction files stay within current host size limits.
- A fresh host session can summarize the applicable sources and precedence correctly.
- The final version-control diff contains only intended instruction changes.

## Output Contract

Report:

1. files created or changed and why each scope is necessary
2. evidence used and material assumptions
3. validations run and validations deferred
4. unresolved questions or host-compatibility risks

## Trigger Examples

Should trigger:

- “Initialize Codex instructions for this monorepo.”
- “Audit our root and backend AGENTS.md against the actual project.”
- “Convert these verified conventions into Antigravity repository rules.”

Should not trigger:

- “Create a reusable Docker skill.” Use `ai_skill_authoring`.
- “Explain how this service works.” Use repository analysis or documentation guidance.
