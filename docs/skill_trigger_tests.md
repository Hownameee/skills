# Skill Trigger Test Matrix

Use these prompts in a fresh Codex or Antigravity session to verify both positive activation and near-neighbor exclusion. Send one prompt at a time. The negative prompt should not select the skill named in that row.

| Expected skill | Positive trigger prompt | Near-neighbor negative prompt |
| --- | --- | --- |
| `ai_init_agents_docs` | Inspect this repository and initialize its root and nested AGENTS.md guidance from the code and real validation commands. | Review this existing SKILL.md for routing clarity and portable frontmatter. |
| `ai_secure_prompt_engineer` | Design a secure system prompt for a shell-capable agent, including trust boundaries, tool authorization, and prompt-injection tests. | Threat-model this implemented RAG application and its tool calls. |
| `ai_skill_authoring` | Improve this existing SKILL.md with precise routing boundaries, progressive disclosure, safety gates, and positive and negative trigger tests. | Inspect this repository and initialize its AGENTS.md files. |
| `analysis_blindspot_finder` | Find hidden assumptions and failure modes in this launch decision, rank their impact, and propose disconfirming tests. | Extract the source-backed claims and insights from this transcript. |
| `analysis_code_graph_rag_tools` | Use the indexed code graph to trace this function's callers, implementations, and repository source evidence. | Review this local diff for exploitable security defects. |
| `analysis_wisdom_extractor` | Extract source-traceable claims, insights, contradictions, facts, and short quotations from this transcript. | Challenge this launch plan's assumptions and identify blindspots. |
| `backend_api_design` | Design a REST invoice API with authorization, errors, cursor pagination, idempotency, and compatibility rules. | Write Playwright API tests for the existing invoice endpoints. |
| `core_code_quality` | Refactor this function for cohesion, clear naming, safe error propagation, and repository-consistent behavior. | Patch these documentation files while preserving formatting and unrelated changes. |
| `core_file_operations` | Modify these exact files safely, preserving user changes, encoding, permissions, and formatting, then verify the diff. | Analyze this repository's dependencies and propose a recovery-aware implementation plan. |
| `core_reasoning_and_context` | Analyze the live repository before changing behavior, separating evidence, assumptions, risks, and recovery options. | Reduce context usage and stop this task from expanding beyond the requested scope. |
| `core_token_and_focus_optimization` | Keep this long repository task within scope using targeted reads, bounded output, and a concise evidence handoff. | Refactor this function's error handling and naming. |
| `data_sql_data_modeling` | Review this relational schema and migration for constraints, tenant isolation, locking, query plans, and rollback safety. | Design the public REST contract that exposes these records. |
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

Run `python3 scripts/validate_skills.py`, synchronize the canonical packages to the selected host, and start a fresh session before testing. Confirm that each positive prompt activates the expected skill and that its paired negative prompt does not. Record host and version when results differ between Codex and Antigravity.
