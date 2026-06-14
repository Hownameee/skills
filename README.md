# Antigravity AI Agent Skills

This repository stores focused AI-agent skills as Codex-compatible packages. Each skill lives in its own category-prefixed directory and contains a single `SKILL.md` entrypoint with valid YAML frontmatter.

## Repository Structure

```text
skills/
  <category>_<skill-name>/
    SKILL.md
scripts/
  validate_skills.py
README.md
```

Root-level skill markdown files are intentionally not used. Keeping one canonical package per skill avoids duplicate instructions across agents and keeps future installs predictable.

## Skill Catalog

### Core

- [core_reasoning_and_context](./skills/core_reasoning_and_context/SKILL.md): planning, context gathering, dependency checking, and recovery behavior.
- [core_token_and_focus_optimization](./skills/core_token_and_focus_optimization/SKILL.md): YAGNI, context control, token economy, and focus discipline.
- [core_file_operations](./skills/core_file_operations/SKILL.md): transparent file edits, formatting preservation, and post-edit verification.
- [core_code_quality](./skills/core_code_quality/SKILL.md): maintainability, fail-fast error handling, naming, comments, DRY, and secure defaults.

### AI Instructions

- [ai_skill_authoring](./skills/ai_skill_authoring/SKILL.md): creating, reviewing, consolidating, and maintaining Codex and Antigravity SKILL.md, AGENTS.md, and repository instruction files.
- [ai_init_agents_docs](./skills/ai_init_agents_docs/SKILL.md): initialize repo-level and nested AGENTS.md files for Codex and Antigravity with discovered file structure, code flow, naming, state layout, verification, safety, and git conventions.
- [ai_secure_prompt_engineer](./skills/ai_secure_prompt_engineer/SKILL.md): secure, reliable, auditable system prompt production.

### Backend

- [backend_python_best_practices](./skills/backend_python_best_practices/SKILL.md): Python structure, virtual environments, typing, Ruff, pytest, and docstrings.
- [backend_node_typescript_backend](./skills/backend_node_typescript_backend/SKILL.md): Node.js and TypeScript backend runtime, async, security, API, and testing standards.
- [backend_java_springboot](./skills/backend_java_springboot/SKILL.md): Java Spring Boot architecture, SOLID, JPA, DTOs, and testing.
- [backend_go_best_practices](./skills/backend_go_best_practices/SKILL.md): Go package design, explicit errors, concurrency, testing, and formatting.
- [backend_api_design](./skills/backend_api_design/SKILL.md): REST/HTTP API contracts, resource modeling, compatibility, pagination, and API security.
- [backend_graphql_security](./skills/backend_graphql_security/SKILL.md): GraphQL schema, resolver authorization, query limit, and production security rules.
- [backend_realtime_api_security](./skills/backend_realtime_api_security/SKILL.md): WebSocket and gRPC transport, auth, message validation, limits, and monitoring.

### Frontend

- [frontend_react_nextjs](./skills/frontend_react_nextjs/SKILL.md): React, TypeScript, Next.js App Router, server actions, and frontend control flow.
- [frontend_sveltekit](./skills/frontend_sveltekit/SKILL.md): SvelteKit load functions, form actions, server-only code, routing, security, and deployment.

### Testing

- [testing_test_strategy](./skills/testing_test_strategy/SKILL.md): unit, integration, end-to-end, contract, regression, and flaky-test strategy.
- [testing_frontend_testing](./skills/testing_frontend_testing/SKILL.md): Cypress, Playwright, Vitest, Testing Library, selectors, isolation, secrets, and reliable UI tests.
- [testing_playwright_testing](./skills/testing_playwright_testing/SKILL.md): Playwright API testing guidelines using `pw-api-plugin` and Zod.

### DevOps

- [devops_docker](./skills/devops_docker/SKILL.md): secure, slim, multi-stage container builds and Compose hygiene.
- [devops_git_workflow](./skills/devops_git_workflow/SKILL.md): Git history, conventional commits, branch safety, and workflow hygiene.
- [devops_github_actions_ci](./skills/devops_github_actions_ci/SKILL.md): secure and reliable GitHub Actions CI/CD workflow design.
- [devops_kubernetes](./skills/devops_kubernetes/SKILL.md): Kubernetes workload security, reliability, rollout review, and production manifest checks.

### Security

- [security_oauth_oidc_security](./skills/security_oauth_oidc_security/SKILL.md): OAuth 2.0 and OpenID Connect flow, token, redirect, scope, and provider security.
- [security_llm_app_security](./skills/security_llm_app_security/SKILL.md): LLM app and AI agent security for prompt injection, tool access, retrieval, and output handling.
- [security_dependency_supply_chain](./skills/security_dependency_supply_chain/SKILL.md): dependency intake, lockfiles, provenance, and vulnerability handling.
- [security_secure_code_review](./skills/security_secure_code_review/SKILL.md): secure review workflow for exploitable defects, privacy leaks, and AI-generated code risks.
- [security_incident_analyzer](./skills/security_incident_analyzer/SKILL.md): extracting essential information from cybersecurity incidents.

### Data

- [data_sql_data_modeling](./skills/data_sql_data_modeling/SKILL.md): relational schema design, constraints, indexes, query safety, and data integrity.

### Performance

- [performance_performance_optimization](./skills/performance_performance_optimization/SKILL.md): profiling, Core Web Vitals, backend latency, memory, and resource optimization.

### Docs

- [docs_technical_documentation](./skills/docs_technical_documentation/SKILL.md): README, guide, API doc, and developer instruction standards.
- [docs_software_architecture](./skills/docs_software_architecture/SKILL.md): architecture docs, arc42, C4, ISO 42010-style views, quality attributes, constraints, risks, and stakeholder communication.
- [docs_architecture_decision_records](./skills/docs_architecture_decision_records/SKILL.md): ADRs, decision logs, context, options, outcomes, consequences, status, and follow-up validation.
- [docs_requirements_use_cases](./skills/docs_requirements_use_cases/SKILL.md): SRS, requirements, user stories, use cases, acceptance criteria, actors, flows, constraints, and traceability.
- [docs_project_plan](./skills/docs_project_plan/SKILL.md): project plans, milestones, deliverables, risks, dependencies, roles, communication, quality gates, rollout, and tracking.
- [docs_engineering_design_spec](./skills/docs_engineering_design_spec/SKILL.md): technical proposals, design specs, alternatives, API/data changes, migration plans, risks, rollout, and observability.

### Review

- [review_github_code_quality](./skills/review_github_code_quality/SKILL.md): GitHub code review, PR communication, and review behavior.

### Analysis

- [analysis_blindspot_finder](./skills/analysis_blindspot_finder/SKILL.md): identifying cognitive blindspots, biases, and flawed assumptions.
- [analysis_wisdom_extractor](./skills/analysis_wisdom_extractor/SKILL.md): extracting wisdom, insights, and facts from large text inputs.

### Writing

- [writing_professional_cv_writer](./skills/writing_professional_cv_writer/SKILL.md): ATS-friendly CV and cover letter writing and review.

## Validation

Validate the repository before installing or sharing skills:

```bash
python3 scripts/validate_skills.py
```

The validator checks package layout, duplicate names, matching folder names, and required `name` plus `description` frontmatter.
