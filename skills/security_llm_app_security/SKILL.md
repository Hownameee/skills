---
name: security_llm_app_security
description: "Threat-model and secure LLM, RAG, memory, multi-agent, and tool-using applications against injection, data leakage, and excessive agency. Use when designing or reviewing an AI application or its security tests; do not treat the model as an authorization boundary or execute adversarial side effects without explicit authorization."
---

# LLM And Agent Application Security

## Scope And Security Model

- Treat the model as a probabilistic component, not a security boundary.
- Treat user input, prompts, retrieved documents, webpages, emails, files, multimodal content, memory, tool descriptions, tool results, other agents, and model output as untrusted.
- Assume a model will eventually follow an adversarial instruction. Design so that this does not grant unauthorized access or effects.
- Keep identity, authentication, authorization, tenant isolation, policy enforcement, accounting, and approval outside the model.
- Do not execute attack payloads against real users, production data, external systems, or billable/destructive tools without explicit scope and authorization.

## Map The System

Before proposing controls, map the affected component and its trust boundaries. Expand along relevant data or control flows; mark absent subsystems as not applicable rather than requiring unrelated architecture discovery:

1. Principals, users, service identities, tenants, roles, and administrators.
2. Trust zones and data classifications.
3. System, developer, user, retrieved, memory, tool, and model-output channels.
4. Models and providers, retention settings, fallback providers, training use, region, and egress.
5. Ingestion, indexes, vector stores, caches, memory, logs, analytics, and evaluation datasets.
6. Every tool, credential, network destination, file path, database, recipient, and side effect.
7. Approval boundaries, asynchronous jobs, retries, delegation, and human review.

For each boundary, state the attacker, asset, entry point, precondition, action, impact, preventive control, detective control, and test.

## Instruction And Data Separation

- Preserve explicit authority ordering in code and prompt construction.
- Label retrieved and tool-provided content as data with provenance. Delimiters and warnings improve clarity but are not security controls by themselves.
- Never let content claim a higher authority, request hidden prompts, override policy, expand tools, change recipients, or grant itself approval.
- Minimize secrets in model context. Do not rely on "do not reveal" instructions to protect a secret already provided to the model.
- Treat direct and indirect injection, encoded instructions, image or document injection, tool-output injection, and cross-agent messages as equivalent trust-boundary problems.

## Identity, Retrieval, And Memory

- Authorize before retrieval using server-controlled user, tenant, document, field, and purpose constraints. Never ask the model which documents the user may access.
- Preserve access-control metadata through chunking, embeddings, indexes, caches, citations, and reranking.
- Separate private and public corpora and tenant namespaces unless a verified policy explicitly permits mixing.
- Protect ingestion with source authentication, provenance, malware and content handling, duplicate control, freshness, and deletion propagation.
- Treat long-term memory as a write-capable data store: authenticate writes, scope them by tenant and subject, validate provenance, expire stale data, and support inspection and deletion.
- Do not store secrets or sensitive personal data in prompts, embeddings, memory, traces, or evaluation sets unless required and protected by policy.

## Tool And Agent Controls

- Grant the minimum read and write capabilities required for the current step. Use task-scoped credentials rather than ambient broad credentials.
- Validate tool arguments with code-level schemas and semantic policy: exact path, host, method, recipient, resource, amount, tenant, and operation.
- Bind approval to the specific action and arguments shown to the user. Revalidate authorization and arguments immediately before execution.
- Separate planning from execution and read tools from write tools. A model-generated plan is not approval.
- Use allowlists for destinations and resources; block private-network and metadata endpoints unless specifically required to prevent SSRF.
- Prefer fixed binaries and structured argument arrays over shell execution. Parameterize database access.
- Sandbox untrusted code and files with CPU, memory, process, filesystem, network, time, and output limits.
- Make side-effecting tools idempotent where possible. Bound retries and detect duplicate external actions.
- Constrain delegation depth, tool-call count, token use, fan-out, and total cost. Propagate the original user's identity and scope to every sub-agent.
- Require explicit approval for destructive, financial, credential, production, privacy-sensitive, or external-message actions.

## Output And Sink Safety

- Validate structured output against a strict schema, reject unknown fields where appropriate, and enforce domain invariants after parsing.
- Encode for the destination context: HTML text, HTML attribute, URL, Markdown renderer, JSON, SQL, shell, and code are different sinks.
- Use parameterized SQL and APIs. Do not concatenate model output into queries.
- Do not execute model-generated code, commands, configuration, migrations, or network requests without review, policy validation, and sandboxing.
- Treat streaming partial output as untrusted; do not trigger a side effect before the complete object passes validation.

## Monitoring And Response

- Log security-relevant decisions, policy results, tool identities, normalized arguments, approvals, denials, and outcomes with correlation IDs.
- Redact prompts, tool output, secrets, personal data, credentials, and retrieved content according to retention policy.
- Monitor denial spikes, unusual tool sequences, cross-tenant access attempts, cost anomalies, recursive loops, and output-validation failures.
- Provide a kill switch for tools and ingestion, credential revocation, model/provider rollback, and affected-memory or index cleanup.

## Adversarial Test Matrix

For every test, specify input, trust channel, expected allow/deny/approval behavior, prohibited side effect, and observable assertion. Select cases for the mapped channels and capabilities; record material exclusions and cover applicable risks from:

- direct and indirect prompt injection;
- system-prompt, secret, and cross-tenant data exfiltration;
- poisoned retrieval, memory, tool description, and tool output;
- confused-deputy and cross-user actions;
- path, host, URL, recipient, and argument smuggling;
- SSRF and private-network access;
- malformed, oversized, duplicate, and streaming output;
- recursive delegation, retry storms, denial of service, and budget exhaustion;
- fallback-provider and partial-outage behavior.

Run destructive payloads only in an isolated test environment with synthetic data and inert tools.

## Verification Checklist

Apply these checks to the affected boundaries and implemented capabilities. Expand when evidence shows a connected risk; do not require provider, memory, or delegation tests for absent features.

- The data-flow and trust-boundary model covers provider, retrieval, memory, tools, agents, logging, and side effects.
- Authorization and tenant isolation are enforced outside the model at every data and tool boundary.
- Tool arguments, approvals, credentials, egress, retries, and resource budgets are bounded.
- Output is validated and encoded for its actual sink.
- Positive and negative tests assert both the response and absence of unauthorized effects.
- Logs and evaluation data minimize sensitive content and support incident investigation.
- Kill switches, rollback, and revocation paths are documented and tested at the authorized level.
