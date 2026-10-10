# Antigravity AI Agent Skills

This repository stores focused AI-agent skills targeting Codex and Antigravity. Each skill lives in its own directory and contains a single `SKILL.md` entrypoint with valid YAML frontmatter. First-party skills use category-prefixed names; imported skills may preserve upstream names for invocation compatibility. Validate discovery and trigger behavior in the installed host before claiming cross-host compatibility.

## Repository Structure

```text
skills/
  <skill-name>/
    SKILL.md
scripts/
  install_skills.py
  validate_skills.py
README.md
```

Root-level skill markdown files are intentionally not used. Keeping one canonical package per skill avoids duplicate instructions across agents and keeps future installs predictable.

## Skill Catalog

### Core

- [core_reasoning_and_context](./skills/core_reasoning_and_context/SKILL.md): risk-scaled repository discovery, evidence gathering, assumptions, planning, and bounded recovery.
- [core_token_and_focus_optimization](./skills/core_token_and_focus_optimization/SKILL.md): context budgeting, scope control, targeted retrieval, concise handoffs, and anti-over-engineering.
- [core_code_quality](./skills/core_code_quality/SKILL.md): repository-aware refactoring, cohesion, naming, error handling, logging, comments, and safe output handling.

### Ponytail

Imported and adapted from [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) commit `2ed6c52c9d7e5e56942508591085fd45dea277d3` under the MIT license. This is a portable skill-only integration; upstream lifecycle hooks and persistent plugin modes are not included.

- [ponytail](./skills/ponytail/SKILL.md): explicit minimal-code mode using YAGNI, existing code, standard-library and native features, and the smallest correct implementation.
- [ponytail-review](./skills/ponytail-review/SKILL.md): read-only review of the current diff for removable complexity and over-engineering.
- [ponytail-audit](./skills/ponytail-audit/SKILL.md): read-only repository-wide audit for removable code, dependencies, wrappers, configuration, and abstractions.
- [ponytail-debt](./skills/ponytail-debt/SKILL.md): collect deliberate `ponytail:` shortcuts into a ceiling-and-upgrade-trigger ledger.
- [ponytail-gain](./skills/ponytail-gain/SKILL.md): display the qualified upstream benchmark scoreboard without inventing repository-specific savings.
- [ponytail-help](./skills/ponytail-help/SKILL.md): reference for installed skills, intensity levels, activation, and plugin-only behavior.

### AI Instructions

- [ai-skill-creator](./skills/ai-skill-creator/SKILL.md): Anthropic's workflow for creating, editing, testing, benchmarking, packaging, and optimizing an individual skill. Imported from [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/skill-creator) with a local package-name adaptation, supporting resources, and the [Apache 2.0 license](./skills/ai-skill-creator/LICENSE.txt). The evaluation and description-optimization scripts require Claude CLI; Codex and Antigravity execution compatibility has not been validated.
- [ai_skill_authoring](./skills/ai_skill_authoring/SKILL.md): collection-wide audits and consolidation for routing ownership, portable package policy, and cross-host governance. It does not own individual-skill creation or improvement.
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
- [deep-dive-explainer](./skills/deep-dive-explainer/SKILL.md): source-grounded, first-principles technical concept deep dives with adaptive structure, examples, trade-offs, and citations.

### Review

- [review_github_code_quality](./skills/review_github_code_quality/SKILL.md): evidence-based local code review and explicitly authorized GitHub pull-request communication.

### Analysis

- [analysis_blindspot_finder](./skills/analysis_blindspot_finder/SKILL.md): evidence-aware blindspot analysis with failure modes, confidence, counterevidence, and mitigations.
- [analysis_wisdom_extractor](./skills/analysis_wisdom_extractor/SKILL.md): source-traceable extraction of summaries, claims, insights, contradictions, facts, and quotations from large inputs.

### Writing

- [writing_professional_cv_writer](./skills/writing_professional_cv_writer/SKILL.md): evidence-bound CV, resume, and cover-letter drafting, review, and role tailoring without fabricated ATS scores or claims.

## Validation

Validate the repository before installing or sharing skills:

```bash
python3 scripts/validate_skills.py
```

The validator checks package layout, matching folder names, and required `name` plus `description` frontmatter. It checks this repository's simple single-line frontmatter format; it is not a general YAML parser. Evaluation directories named `skills/<name>-workspace/` without a root `SKILL.md` are excluded, including their baseline snapshots. Nested skills inside installable packages and other directories missing an entrypoint are rejected.

Run the installer and validation regression tests without writing to global targets:

```bash
python3 -B -m unittest discover -s tests -v
```

Use the [trigger matrix](./docs/skill_trigger_tests.md) for host routing checks and [regression scenarios](./evals/evals.json) for instruction-following checks. See [validation results and limitations](./docs/skill_validation_results.md) for the latest recorded evidence.

Keep evaluation outputs and snapshots in a temporary directory or an ignored `skills/<name>-workspace/` directory. Keep reusable test prompts in `evals/`. These outputs are not skill packages and are not installed.

## Installation

Install or update all repository skills and instruction guides to global (`~/.gemini/config`, `~/.codex`) targets:

```bash
python3 scripts/install_skills.py
```

The installer replaces matching repository packages, including their supporting files, and updates the global `AGENTS.md` guides. Independently installed skills and hidden system directories are preserved; it does not prune packages absent from this repository. Only directories containing a root `SKILL.md` are copied. An installation failure returns a nonzero exit status and names the error; earlier successfully copied packages may already be updated.
