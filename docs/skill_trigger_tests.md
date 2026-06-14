# Skill Trigger Test Matrix

Use these prompts after restarting Codex to verify that the expected skill is selected. Each prompt is intentionally short and task-specific.

| Expected skill | Test prompt |
| --- | --- |
| `ai_secure_prompt_engineer` | Write a secure system prompt for an agent that can call shell tools and must resist prompt injection. |
| `ai_skill_authoring` | Create a new SKILL.md for reviewing Terraform modules and make sure the description triggers correctly. |
| `analysis_blindspot_finder` | Find blindspots in this launch plan and output only the requested risk bullets. |
| `analysis_wisdom_extractor` | Extract wisdom, insights, facts, quotes, habits, and recommendations from this transcript. |
| `backend_api_design` | Design a REST API for invoices with pagination, error responses, compatibility, and authorization rules. |
| `backend_go_best_practices` | Review this Go package for idiomatic error handling, concurrency safety, and test structure. |
| `backend_graphql_security` | Review this GraphQL schema and resolvers for authorization, query depth, introspection, and resolver security. |
| `backend_java_springboot` | Implement a Spring Boot service using DTOs, JPA, SOLID boundaries, and tests. |
| `backend_node_typescript_backend` | Build a secure Node.js TypeScript backend endpoint with validation, async error handling, and tests. |
| `backend_python_best_practices` | Set up a Python project with typing, virtual environment, Ruff, pytest, and clean module structure. |
| `backend_realtime_api_security` | Review a WebSocket and gRPC API for transport security, auth, validation, limits, and monitoring. |
| `core_code_quality` | Refactor this function for clearer naming, smaller responsibilities, fail-fast errors, and useful comments only. |
| `core_file_operations` | Modify these files carefully while preserving formatting and verifying the result afterward. |
| `core_reasoning_and_context` | Analyze this repo before changing code; identify dependencies, assumptions, and recovery plan. |
| `core_token_and_focus_optimization` | Reduce over-engineering and token usage while keeping the implementation focused on this exact task. |
| `data_sql_data_modeling` | Review this SQL schema for constraints, indexes, tenant filters, transactions, and migration safety. |
| `devops_docker` | Improve this Dockerfile and Compose setup for multi-stage builds, non-root users, pinned images, and health checks. |
| `devops_git_workflow` | Check git status, review diffs, and prepare an atomic conventional commit without including generated files. |
| `devops_github_actions_ci` | Create a secure GitHub Actions workflow with pinned actions, least privilege permissions, caching, and CI checks. |
| `devops_kubernetes` | Review these Kubernetes manifests for resources, probes, security context, rollout safety, and production readiness. |
| `docs_architecture_decision_records` | Write an ADR for choosing PostgreSQL over DynamoDB, including context, options, consequences, and status. |
| `docs_engineering_design_spec` | Write an engineering design spec for adding async invoice processing with alternatives, migration, rollout, risks, and observability. |
| `docs_project_plan` | Create a software project plan with scope, milestones, deliverables, dependencies, risks, quality gates, rollout, and tracking. |
| `docs_requirements_use_cases` | Write requirements and use cases with actors, flows, acceptance criteria, constraints, non-functional requirements, and traceability. |
| `docs_software_architecture` | Document the software architecture using C4-style views, quality attributes, constraints, risks, and stakeholder context. |
| `docs_technical_documentation` | Improve this README with prerequisites, setup commands, expected output, troubleshooting, and accurate developer guidance. |
| `frontend_react_nextjs` | Build a Next.js App Router page with React, TypeScript, server actions, safe data loading, and frontend state. |
| `frontend_sveltekit` | Implement a SvelteKit route with load functions, form actions, server-only code, cookies, and progressive enhancement. |
| `performance_performance_optimization` | Profile and optimize this slow endpoint for latency, memory, throughput, and Core Web Vitals impact. |
| `review_github_code_quality` | Review this GitHub PR and communicate findings with accurate file links, no invented changes, and concise comments. |
| `security_dependency_supply_chain` | Review these dependencies for lockfile safety, package reputation, provenance, vulnerability handling, and release integrity. |
| `security_incident_analyzer` | Analyze this breach report and extract affected systems, timeline, root cause, impact, indicators, and containment actions. |
| `security_llm_app_security` | Review this LLM app for prompt injection, tool access, retrieval risks, output handling, and auditability. |
| `security_oauth_oidc_security` | Review this OAuth/OIDC flow for redirect URI safety, PKCE, scopes, tokens, sessions, and client security. |
| `security_secure_code_review` | Perform a secure code review of this diff for exploitable defects, privacy leaks, and high-risk regressions. |
| `testing_frontend_testing` | Write frontend tests with Testing Library, Playwright, or Cypress using stable selectors, isolation, and reliable waits. |
| `testing_playwright_testing` | Write Playwright API tests using pw-api-plugin and Zod to validate status codes and response schemas. |
| `testing_test_strategy` | Create a test strategy covering unit, integration, end-to-end, contract, regression, and flaky-test risk. |
| `writing_professional_cv_writer` | Rewrite this CV and cover letter to be ATS-friendly, concise, achievement-focused, and role-targeted. |

## Expected Runtime Note

Codex loads installed skill metadata at startup. Restart Codex after changing `/home/nam/.codex/skills`, then send one prompt at a time and confirm the expected skill appears in the active skill list or behavior.
