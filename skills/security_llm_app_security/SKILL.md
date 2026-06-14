---
name: security_llm_app_security
description: LLM and AI agent application security rules for prompt injection, tool access, retrieval, and output handling.
---

# Specialist LLM App Security

## 1. Threat Model

- Treat the model as a probabilistic component, not a security boundary.
- Treat user input, retrieved documents, webpages, emails, files, tool results, and model outputs as untrusted.
- Assume prompt injection can appear indirectly inside content the model reads.
- Minimize the damage a compromised model response can cause.

## 2. Tool And Agent Design

- Grant the minimum tools required for the current task.
- Require explicit user approval for irreversible, financial, destructive, credential, or external-message actions.
- Separate read tools from write tools and gate writes more strictly.
- Validate tool arguments outside the model before execution.
- Keep allowlists for hosts, file paths, commands, recipients, and schemas where possible.

## 3. Retrieval And Context

- Do not let retrieved content override system, developer, policy, or user instructions.
- Label retrieved content as data and preserve source boundaries.
- Prefer citations or source IDs for factual claims that depend on retrieval.
- Avoid mixing private and public corpora without explicit access control.
- Enforce tenant, user, and document-level authorization before retrieval.

## 4. Output Handling

- Validate structured model output against a schema before use.
- Escape or sanitize model output before rendering in HTML, Markdown, SQL, shell, or code contexts.
- Do not execute model-generated code, shell, SQL, or configuration without review and sandboxing.
- Add rate limits, token limits, recursion limits, and budget controls.

## 5. Evaluation

- Test direct prompt injection, indirect prompt injection, data exfiltration, excessive agency, unsafe tool arguments, and malformed output.
- Include negative tests where the model must refuse or ask for confirmation.
- Log security-relevant model and tool decisions without storing sensitive prompt content unnecessarily.
