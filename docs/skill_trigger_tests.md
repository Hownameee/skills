# Skill Trigger Test Matrix

Use these prompts in a fresh Codex or Antigravity session to verify both positive activation and near-neighbor exclusion. Send one prompt at a time. The negative prompt should not select the skill named in that row.

| Expected skill | Positive trigger prompt | Near-neighbor negative prompt |
| --- | --- | --- |
| `ai_init_agents_docs` | Inspect this repository and initialize its root and nested AGENTS.md guidance from the code and real validation commands. | Review this existing SKILL.md for routing clarity and portable frontmatter. |
| `ai_secure_prompt_engineer` | Design a secure system prompt for a shell-capable agent, including trust boundaries, tool authorization, and prompt-injection tests. | Threat-model this implemented RAG application and its tool calls. |
| `ai_skill_authoring` | Audit this skill collection for duplicated responsibilities, assign one owner to each workflow, and update its routing documentation. | Improve this one release-notes skill, test it against representative inputs, and package it. |
| `ai-skill-creator` | Improve this existing weekly-release-notes skill, compare it with a baseline on representative inputs, and package the result. | Audit this collection for ownership overlap between its review skills. |
| `analysis_blindspot_finder` | Find hidden assumptions and failure modes in this launch decision, rank their impact, and propose disconfirming tests. | Extract the source-backed claims and insights from this transcript. |
| `analysis_wisdom_extractor` | Extract source-traceable claims, insights, contradictions, facts, and short quotations from this transcript. | Challenge this launch plan's assumptions and identify blindspots. |
| `backend_api_design` | Design a REST invoice API with authorization, errors, cursor pagination, idempotency, and compatibility rules. | Write Playwright API tests for the existing invoice endpoints. |
| `core_code_quality` | Refactor this function for cohesion, clear naming, safe error propagation, and repository-consistent behavior. | Patch these documentation files while preserving formatting and unrelated changes. |
| `core_reasoning_and_context` | Analyze the live repository before changing behavior, separating evidence, assumptions, risks, and recovery options. | Reduce context usage and stop this task from expanding beyond the requested scope. |
| `core_token_and_focus_optimization` | Keep this long repository task within scope using targeted reads, bounded output, and a concise evidence handoff. | Refactor this function's error handling and naming. |
| `data_sql_data_modeling` | Review this relational schema and migration for constraints, tenant isolation, locking, query plans, and rollback safety. | Design the public REST contract that exposes these records. |
| `deep-dive-explainer` | Teach me HTTP/2 multiplexing from first principles, including stream internals, a practical example, limitations, and source-backed trade-offs. | Document the current repository's deployed architecture using only evidence from its code and manifests. |
| `devops_docker` | Improve this Dockerfile and Compose setup for reproducible builds, non-root runtime, health checks, and verified configuration. | Inventory and remove unused Docker images, volumes, and build cache. |
| `devops_docker_cleanup` | Inventory Docker disk usage, obtain the required approval, and safely remove the requested unused resources. | Review this Dockerfile and Compose build without deleting Docker resources. |
| `devops_env_setup` | Node is unavailable in this non-interactive shell; detect and load the runtime and package manager selected by the repository. | Review the staged diff and create an authorized Git commit. |
| `devops_git_workflow` | Inspect Git state, stage only these files, validate the staged diff and hooks, then create the requested atomic commit. | Secure this GitHub Actions workflow and pin third-party actions. |
| `devops_github_actions_ci` | Review this GitHub Actions workflow for event trust, least privilege, pinned actions, cache safety, and reliable CI. | Optimize the Docker image built by this workflow. |
| `devops_kubernetes` | Render and diff these Kubernetes overlays, review workload safety, and define rollout verification without mutating production. | Improve this local Docker Compose setup. |
| `docs_architecture_decision_records` | Write an ADR for choosing PostgreSQL over DynamoDB with context, options, decision, consequences, and status. | Design how asynchronous invoice processing will work end to end. |
| `docs_engineering_design_spec` | Write an engineering design spec for asynchronous invoice processing with alternatives, interfaces, migration, rollout, and verification. | Turn this approved design into milestones, owners, dependencies, and delivery gates. |
| `docs_project_plan` | Create an execution plan with scoped milestones, owners, dependencies, exit evidence, rollout, and closure criteria. | Document the current system context, runtime flows, and deployment topology. |
| `docs_requirements_use_cases` | Write testable requirements and use cases with actors, flows, constraints, acceptance criteria, and traceability. | Choose and specify the technical architecture that implements these requirements. |
| `docs_software_architecture` | Document the current system using only the context, runtime, deployment, data, and trust-boundary views stakeholders need. | Improve this README's quick start and troubleshooting instructions. |
| `docs_technical_documentation` | Rewrite this README from the live scripts with prerequisites, a verified quick start, expected results, and troubleshooting. | Record the durable decision to adopt PostgreSQL as an ADR. |
| `performance_performance_optimization` | Profile this endpoint with a reproducible workload, identify the bottleneck, change one factor, and compare benchmark results. | Refactor this short function for readability without claiming a performance problem. |
| `ponytail` | Use Ponytail full mode to implement the smallest correct solution, checking existing code, standard-library, and native options first. | Implement this authentication change with the repository's security workflow; I did not request Ponytail or a minimalism pass. |
| `ponytail-review` | Run a Ponytail review of this diff and report only removable over-engineering without applying fixes. | Review this diff for correctness, security vulnerabilities, and regressions. |
| `ponytail-audit` | Audit this whole repository with Ponytail and rank the code, dependencies, wrappers, and abstractions we could remove. | Perform a whole-repository security audit for exploitable vulnerabilities. |
| `ponytail-debt` | Collect every `ponytail:` marker into a read-only ledger and flag entries without upgrade triggers. | Search the repository for general TODO comments and implement them. |
| `ponytail-gain` | Show the Ponytail gain scoreboard with its upstream-source and non-repository caveats. | Measure the actual before-and-after performance and code-size impact of this repository change. |
| `ponytail-help` | Show how to activate each installed Ponytail skill and explain which mode features require the upstream plugin. | Install or configure the upstream Ponytail plugin and lifecycle hooks. |
| `review_github_code_quality` | Review this pull request locally and draft evidence-based findings with severity, file links, and validation limits. | Audit this source tree specifically for exploitable security vulnerabilities without PR communication. |
| `security_dependency_supply_chain` | Review this proposed dependency update for necessity, lockfile changes, provenance, vulnerabilities, licenses, and release integrity. | Review this application diff for an authorization vulnerability. |
| `security_incident_analyzer` | Turn this incident evidence into a confidence-tagged timeline, impact assessment, indicators, root cause, and authorized response plan. | Review this code change for defects that could enable a future breach. |
| `security_llm_app_security` | Threat-model this multi-tenant RAG agent for indirect injection, retrieval poisoning, confused-deputy tools, and data leakage. | Write the system prompt that constrains this agent's tool use. |
| `security_oauth_oidc_security` | Review this OIDC authorization-code flow for PKCE, redirects, issuer and audience validation, sessions, and key rotation. | Design object-level authorization for this REST resource API. |
| `security_secure_code_review` | Perform an evidence-first secure review of this diff for reachable vulnerabilities, privacy leaks, and high-risk regressions. | Summarize this completed breach report as an incident timeline. |
| `testing_playwright_testing` | Add isolated Playwright API tests using the existing configuration and built-in request fixture, with negative cases and cleanup. | Design the overall unit, integration, contract, and end-to-end test strategy. |
| `testing_test_strategy` | Create a risk-based test strategy choosing unit, integration, contract, end-to-end, regression, and reliability coverage. | Implement the invoice API tests with Playwright's built-in request fixture. |
| `writing_professional_cv_writer` | Tailor this CV and cover letter to the job description using only verified experience and a transparent requirement-evidence matrix. | Extract general lessons and source-backed quotations from this career transcript. |

## Expected Runtime Note

Run `python3 scripts/validate_skills.py`, synchronize the canonical packages to an authorized test host, and start a fresh session before testing. Confirm that each positive prompt activates the expected skill and that its paired negative prompt does not. Record host and version when results differ between Codex and Antigravity. Static inspection is not evidence of host activation.

## Natural Requests And Overlapping Routes

The explicit prompts above check direct activation. Also test these without naming the intended skill. Record the primary skill and any supporting skills separately; an explicit user skill selection takes precedence over inferred routing.

| Request | Expected primary skill or behavior |
| --- | --- |
| We keep loading two instruction files for every skill edit. Inspect this collection, assign one owner to each responsibility, and remove the duplicated routing. | `ai_skill_authoring` |
| This release-notes skill already exists. Tighten its workflow, compare it against my current version using three example releases, and package it. | `ai-skill-creator` |
| I know basic databases but not concurrency control. Build me a rigorous learning path through MVCC, then explain one transaction timeline and when MVCC is the wrong model. | `deep-dive-explainer` |
| Inspect this checkout and write the agent instructions for its backend directory using the commands it actually has. | `ai_init_agents_docs` |
| Which wrappers and abstractions in this diff can we delete? Report findings only. | `ponytail-review` |
| Look across the whole repository for abstractions or dependencies we can remove. Rank the candidates without editing. | `ponytail-audit` |
| Implement this little CSV conversion with the simplest solution using tools already installed. | `ponytail` |
| Collect the deliberate shortcuts and their upgrade conditions from our Ponytail comments; don't implement them. | `ponytail-debt` |
| Show the upstream Ponytail benchmark claims, including what they do and don't prove about this project. | `ponytail-gain` |
| Which Ponytail commands are installed, and which features need its plugin? | `ponytail-help` |
| We added payment retry behavior. Which unit, integration, and contract cases would cover the risks without duplicating coverage? | `testing_test_strategy` |
| Write up why we chose PostgreSQL, alternatives we rejected, and when we should revisit the decision. | `docs_architecture_decision_records` |
| Turn this feature brief into user stories and observable acceptance criteria; don't choose the architecture yet. | `docs_requirements_use_cases` |
| Review this changed ownership check for ways one tenant could read another tenant's invoices. | `security_secure_code_review` |
| Add a checkout browser test using the suite already in this project. | Follow browser-test conventions; do not use the Playwright API-only workflow or search indefinitely for a missing skill. |

## Recording Results

For each execution record prompt, expected primary skill, observed primary/supporting skills, host/version, tested revision or file hashes, outcome, and evidence. Use `not run` for missing execution, and distinguish static routing review from fresh-host activation. Do not infer success from package validation.

The [behavior scenarios](../evals/evals.json) separately exercise useful completion, factual grounding, authorization reuse, and proportional verification. Their assertions test outcomes after a skill is supplied; they do not measure automatic activation. Record results and limitations in [skill_validation_results.md](./skill_validation_results.md).
