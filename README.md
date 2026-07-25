# Antigravity AI Agent Skills

This repository stores 34 focused AI-agent skills targeting Codex and Antigravity. Each skill lives in its own category-prefixed directory and contains a single `SKILL.md` entrypoint with valid YAML frontmatter. Validate discovery and trigger behavior in the installed host before claiming cross-host compatibility.

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

- [core_reasoning_and_context](./skills/core_reasoning_and_context/SKILL.md): risk-scaled repository discovery, evidence gathering, assumptions, planning, and bounded recovery.
- [core_token_and_focus_optimization](./skills/core_token_and_focus_optimization/SKILL.md): context budgeting, scope control, targeted retrieval, concise handoffs, and anti-over-engineering.
- [core_file_operations](./skills/core_file_operations/SKILL.md): capability-neutral file discovery, safe minimal edits, user-change preservation, and post-edit verification.
- [core_code_quality](./skills/core_code_quality/SKILL.md): repository-aware refactoring, cohesion, naming, error handling, logging, comments, and safe output handling.

### AI Instructions

- [ai_skill_authoring](./skills/ai_skill_authoring/SKILL.md): portable Codex and Antigravity skill/rule authoring, routing boundaries, progressive disclosure, and trigger validation.
- [ai_init_agents_docs](./skills/ai_init_agents_docs/SKILL.md): evidence-backed initialization or update of Codex `AGENTS.md` guidance and Antigravity repository rules.
- [ai_secure_prompt_engineer](./skills/ai_secure_prompt_engineer/SKILL.md): secure system and developer prompt design with trust boundaries, tool authorization, injection defenses, and adversarial tests.

### Backend

- [backend_api_design](./skills/backend_api_design/SKILL.md): REST/HTTP resource contracts, methods, errors, pagination, retries, compatibility, security, and client ergonomics.

### Testing

- [testing_test_strategy](./skills/testing_test_strategy/SKILL.md): risk-based selection of unit, integration, contract, end-to-end, regression, and reliability coverage.
- [testing_playwright_testing](./skills/testing_playwright_testing/SKILL.md): Playwright API tests using the existing suite and built-in `request` fixture, with isolation, cleanup, and precise assertions.

### DevOps

- [devops_docker](./skills/devops_docker/SKILL.md): Dockerfile, image build, Compose, runtime security, health-check, and build-context guidance.
- [devops_docker_cleanup](./skills/devops_docker_cleanup/SKILL.md): inventory-first project or host-wide cleanup of Docker containers, images, volumes, networks, and build cache.
- [devops_env_setup](./skills/devops_env_setup/SKILL.md): repository-selected Node.js runtime and package-manager discovery for non-interactive shells and Git hooks.
- [devops_git_workflow](./skills/devops_git_workflow/SKILL.md): exact staging, atomic commits, safe amendments, hook-aware validation, and explicitly authorized pushes.
- [devops_github_actions_ci](./skills/devops_github_actions_ci/SKILL.md): GitHub Actions event trust, least-privilege permissions, pinned actions, CI reliability, and deployment safety.
- [devops_kubernetes](./skills/devops_kubernetes/SKILL.md): Kubernetes and Helm/Kustomize discovery, rendering, diffing, workload safety, rollout verification, and controlled deployment.

### Security

- [security_oauth_oidc_security](./skills/security_oauth_oidc_security/SKILL.md): OAuth 2.0 and OpenID Connect flow selection, client and token validation, redirects, sessions, provider changes, and security tests.
- [security_llm_app_security](./skills/security_llm_app_security/SKILL.md): threat modeling for prompt injection, retrieval poisoning, tool access, tenant isolation, output handling, and adversarial tests.
- [security_dependency_supply_chain](./skills/security_dependency_supply_chain/SKILL.md): dependency intake and updates, lockfiles, provenance, vulnerability triage, licenses, SBOMs, and release integrity.
- [security_secure_code_review](./skills/security_secure_code_review/SKILL.md): evidence-first review for exploitable defects, privacy leaks, and high-risk regressions.
- [security_incident_analyzer](./skills/security_incident_analyzer/SKILL.md): evidence-tagged incident timelines, impact, indicators, root cause, and authorized response planning.

### Data

- [data_sql_data_modeling](./skills/data_sql_data_modeling/SKILL.md): relational schemas, constraints, tenant-safe queries, query plans, indexes, and recoverable migrations.

### Performance

- [performance_performance_optimization](./skills/performance_performance_optimization/SKILL.md): reproducible profiling and benchmark loops for latency, throughput, memory, resource use, and Core Web Vitals.

### Docs

- [docs_technical_documentation](./skills/docs_technical_documentation/SKILL.md): evidence-backed README files, setup guides, runbooks, API usage guides, troubleshooting, and developer documentation.
- [docs_software_architecture](./skills/docs_software_architecture/SKILL.md): stakeholder-driven architecture views for context, structure, runtime, deployment, data, trust boundaries, and quality tradeoffs.
- [docs_architecture_decision_records](./skills/docs_architecture_decision_records/SKILL.md): focused ADRs with context, options, outcomes, consequences, status, and follow-up validation.
- [docs_requirements_use_cases](./skills/docs_requirements_use_cases/SKILL.md): testable requirements and use cases with actors, flows, constraints, acceptance criteria, and traceability.
- [docs_project_plan](./skills/docs_project_plan/SKILL.md): scoped milestones, dependencies, owners, validation gates, rollout, status, and project closure.
- [docs_engineering_design_spec](./skills/docs_engineering_design_spec/SKILL.md): implementable technical solution specs with alternatives, interfaces, migration, risks, rollout, and verification.

### Review

- [review_github_code_quality](./skills/review_github_code_quality/SKILL.md): evidence-based local code review and explicitly authorized GitHub pull-request communication.

### Analysis

- [analysis_blindspot_finder](./skills/analysis_blindspot_finder/SKILL.md): evidence-aware blindspot analysis with failure modes, confidence, counterevidence, and mitigations.
- [analysis_code_graph_rag_tools](./skills/analysis_code_graph_rag_tools/SKILL.md): using Code-Graph-RAG MCP tools to investigate indexed source repositories with graph, semantic, and source evidence.
- [analysis_wisdom_extractor](./skills/analysis_wisdom_extractor/SKILL.md): source-traceable extraction of summaries, claims, insights, contradictions, facts, and quotations from large inputs.

### Writing

- [writing_professional_cv_writer](./skills/writing_professional_cv_writer/SKILL.md): evidence-bound CV, resume, and cover-letter drafting, review, and role tailoring without fabricated ATS scores or claims.

## Validation

Validate the repository before installing or sharing skills:

```bash
python3 scripts/validate_skills.py
```

The validator checks package layout, duplicate names, matching folder names, and required `name` plus `description` frontmatter.
