# Agent Operating Guide

This file provides durable repository guidance for Codex and Antigravity agents that read `AGENTS.md`-style instruction files. Keep this file concise and stable. Put detailed repeatable workflows in `skills/<name>/SKILL.md`. First-party skills use category-prefixed names; imported skills may preserve upstream names when invocation compatibility requires it.

## Scope And Precedence

- Apply these rules to work in this repository unless a nested `AGENTS.md`, direct user instruction, or higher-priority system/developer instruction says otherwise.
- Treat direct user instructions for the current task as more specific than this file.
- Use local skills for detailed task workflows; do not duplicate full skill content here.
- If two local rules conflict, follow the rule closest to the files being edited and report the conflict briefly.

## Default Workflow

- Inspect relevant files and current repository state before editing.
- State assumptions when requirements are incomplete, then proceed with the safest reasonable interpretation.
- Keep changes scoped to the request.
- Prefer the smallest maintainable solution that satisfies the task.
- Preserve unrelated user changes and never revert work you did not make unless explicitly asked.
- Verify changes with the narrowest meaningful validation available.

## Skill Routing

Use these skills when the task matches their scope:

| Task area | Skill |
| --- | --- |
| Init or update repo-level and nested `AGENTS.md` with file structure, code flow, naming, verification, safety, and git conventions | `ai_init_agents_docs` |
| Audit or consolidate skill collections, routing ownership, portability policy, and reusable instruction rules | `ai_skill_authoring` |
| Create, edit, test, benchmark, package, or optimize an individual skill | `ai-skill-creator` |
| Secure system prompts and prompt-injection tests | `ai_secure_prompt_engineer` |
| Context gathering, planning, assumptions, and recovery strategy | `core_reasoning_and_context` |
| Token discipline, focus, and anti-over-engineering | `core_token_and_focus_optimization` |
| Code quality, comments, naming, DRY, and fail-fast errors | `core_code_quality` |
| Git status, diffs, branches, commits, and ignored files | `devops_git_workflow` |
| Dockerfile, image build, Compose, and container runtime work | `devops_docker` |
| Docker cleanup, pruning, reset, or disk reclamation | `devops_docker_cleanup` |
| GitHub Actions and Kubernetes work | `devops_github_actions_ci`, `devops_kubernetes` |
| Environment loading, Node/npm runtime setup, Husky/commit hook environments | `devops_env_setup` |
| REST and HTTP API contract design or review | `backend_api_design` |
| SQL schema, constraints, indexes, and query review | `data_sql_data_modeling` |
| Test strategy or Playwright API tests | `testing_test_strategy`, `testing_playwright_testing` |
| Architecture docs, ADRs, requirements, use cases, project plans, design specs, README docs | matching `docs_*` skill |
| Source-grounded technical concept deep dives and learning walkthroughs | `deep-dive-explainer` |
| Secure code review, LLM app security, OAuth/OIDC, dependency supply chain, incidents | matching `security_*` skill |
| GitHub PR/review communication | `review_github_code_quality` |
| Performance profiling and optimization | `performance_performance_optimization` |
| CV and cover letter writing | `writing_professional_cv_writer` |
| Blindspot or wisdom extraction analysis | matching `analysis_*` skill |
| Explicit minimal-code mode, over-engineering review or audit, Ponytail shortcut ledger, benchmark card, or help | matching `ponytail*` skill |

For domains without a listed skill, use repository conventions and available tooling. Do not assume a matching frontend, language, protocol, or CLI-administration skill is installed. Honor explicit skill selection and reuse completed checks when several skills apply.

## Coding Standards

- Match existing framework, language idioms, naming, formatting, and file organization.
- Validate external input at system boundaries.
- Keep functions focused and readable; extract helpers only when they reduce real duplication or complexity.
- Write comments only for non-obvious intent, business rules, tradeoffs, or risk. Do not narrate syntax.
- Avoid logging secrets, tokens, private data, authorization headers, cookies, or raw production payloads.

## Verification

- Prefer existing project scripts over invented commands.
- After code changes, run the narrowest meaningful formatter, linter, typecheck, unit test, build, or targeted integration test.
- If validation cannot be run, say exactly why and name the command that should be run later.
- Do not mark work complete when tests are failing unless the failure is unrelated and clearly explained.

## Approval And Safety

- Ask before destructive operations such as deleting data, resetting history, force-pushing, dropping databases, rotating secrets, or changing production configuration.
- Ask before adding new production dependencies, background services, external network integrations, or broad permission changes.
- Treat migrations, billing, authentication, authorization, secrets, public communication, and production data as high-risk areas.
- Existing explicit authorization covers the same action and scope; ask again only for uncovered actions, changed targets, or newly discovered material consequences.
- Do not use credentials from chat history, logs, screenshots, or accidental files unless the user explicitly confirms they are intended for this task.

## Git

- Use `devops_git_workflow` for detailed Git workflow rules.
- If the user writes `commit` anywhere in the request, first read and apply `skills/devops_git_workflow/SKILL.md` before staging, committing, amending, or pushing.
- Check repository state before edits when git state matters.
- Do not commit, amend, reset, rebase, push, or force-push unless the user asks.
- Never include `.env`, private keys, tokens, build artifacts, dependency directories, caches, or generated secrets in commits.

## Documentation

- Update documentation when behavior, setup, commands, APIs, configuration, or operational procedures change.
- Keep docs task-focused: prerequisites, steps, expected outcome, validation, and troubleshooting.
- Use the specific `docs_*` skill for architecture, ADR, requirement, use-case, project-plan, design-spec, and technical documentation work.
- Prefer links to local canonical docs over duplicating long reference material.

## Environment

- Use `devops_env_setup` when Node.js, a package manager, or a Node-based Git hook is unavailable or resolves to the wrong version.
- Inspect repository version files and package-manager metadata before selecting an already-installed runtime manager. Do not assume NVM, hardcode a user path, choose an implicit latest version, install tooling, or change global defaults without approval.
- Run Node-based Git hooks from the same verified environment as the project commands, and never bypass hooks to work around environment setup.

## Final Response

- Summarize the concrete files changed and validation run.
- Call out any skipped validation or residual risk.
- Keep final answers concise unless the user asks for detail.
