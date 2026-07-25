---
name: docs_technical_documentation
description: "Create or review task-focused README files, setup guides, runbooks, API usage guides, troubleshooting material, and developer documentation grounded in the current repository. Use when readers need accurate instructions or operational reference. Do not use for ADRs, architecture docs, requirements, design specs, or project plans."
---

# Specialist Technical Documentation

## 1. Scope And Document Type

Identify the reader's job before choosing a format:

| Reader need | Document type |
| --- | --- |
| Understand and start a repository | README |
| Install or configure a system | Setup guide |
| Perform a routine or incident operation | Runbook |
| Call or integrate with an interface | API/integration guide |
| Diagnose a known symptom | Troubleshooting guide |
| Contribute or maintain code | Developer guide |

Route decisions, architecture, requirements, engineering designs, and project planning to their dedicated documentation skills.

## 2. Discovery Before Writing

1. Define the primary audience, prerequisite knowledge, task, starting state, and successful end state.
2. Read repository instructions and the current document, if it exists.
3. Inspect the canonical implementation sources: scripts, CLI help, configuration schema, manifests, API contracts, tests, examples, and package metadata.
4. Find the project's existing validation, lint, build, and documentation commands.
5. Record OS, shell, version, permission, network, credential, and environment assumptions.
6. Identify generated documentation and its source; edit the source rather than generated output.

Separate verified behavior, inferred behavior, and unverified prerequisites. Do not copy stale commands from neighboring documents.

## 3. Authoring Workflow

### Step 1: Design The Shortest Correct Path

- Lead with purpose, prerequisites, expected outcome, and the minimal safe procedure.
- Put optional configuration and advanced explanations after the main path.
- Use task-oriented headings and one action per numbered step.
- State the working directory and target environment when commands depend on them.
- Show expected output or an observable state when it helps the reader detect failure.

### Step 2: Write Verifiable Instructions

- Use commands copied from canonical repository scripts or verified tool help.
- Explain placeholders before commands and make them visually unmistakable.
- Keep conceptual explanation separate from runnable procedures.
- Document defaults, precedence, units, valid values, and restart/reload behavior for configuration.
- Use stable application error text or symptom descriptions in troubleshooting.
- Link canonical local or upstream references rather than duplicating volatile material.

Never claim a command is safe, idempotent, or production-ready without evidence.

### Step 3: Add Safety At The Point Of Risk

- Warn immediately before destructive, privileged, production, billing, security-policy, or data-changing steps.
- Provide preview, backup, rollback, or recovery procedures where practical.
- Never include real tokens, credentials, customer data, private URLs, or internal-only screenshots.
- Clearly distinguish development examples from production procedures.
- Do not ask readers to disable TLS verification, hooks, authorization, or security controls as a generic workaround.

### Step 4: Add Focused Troubleshooting

For each common failure, provide:

```markdown
### Observable symptom

Cause: confirmed likely cause and relevant precondition.

Check:
1. Safe diagnostic command or inspection.

Resolution:
1. Minimal corrective action.

Expected result: concrete verification.
```

Do not list speculative fixes without a diagnostic discriminator.

## 4. Minimum Content By Type

- **README:** purpose, status, prerequisites, quick start, verification, key configuration, tests, architecture/docs links, contribution path.
- **Setup guide:** supported versions, installation, configuration, initialization, validation, upgrade/uninstall references, troubleshooting.
- **Runbook:** scope, trigger, access, safeguards, diagnostics, actions, verification, rollback/escalation, ownership.
- **API guide:** base URL/environment, authentication, request/response examples, errors, pagination, limits, idempotency, versioning.
- **Troubleshooting:** symptoms, discriminating checks, likely causes, corrections, verification, escalation evidence.
- **Developer guide:** repository map, environment, edit/test loop, conventions, generated files, debugging, contribution workflow.

Include only applicable content; avoid empty template sections.

## 5. Edge Cases

Check for:

- OS, shell, architecture, and package-manager differences.
- Commands that require a specific working directory.
- Existing files or state that make a step non-idempotent.
- Offline, proxy, permission, port-conflict, and version-mismatch behavior.
- Environment-variable precedence and secret handling.
- Container versus host commands.
- Upgrade and downgrade paths.
- Generated docs, translated siblings, shared snippets, anchors, and relative links.
- Deprecated features, version-specific flags, and screenshots that drift faster than text.

## 6. Validation Checklist

- Run safe commands in a disposable or non-production context when possible.
- Verify command names, flags, paths, prerequisites, environment variables, and expected outcomes.
- Validate code and configuration examples with the relevant parser, compiler, schema, or test.
- Run the repository's Markdown, spelling, documentation-build, and link checks when present.
- Check internal links, anchors, external canonical URLs, and referenced files.
- Search for placeholders, secrets, private data, stale names, unsupported claims, and inconsistent terminology.
- Read the procedure from a fresh reader's starting state and verify every assumed transition.
- State exactly which commands or environments could not be validated.

## 7. Output Contract

Return the completed or reviewed documentation, canonical sources checked, commands and links validated, unverified assumptions, and residual risks. In review mode, prioritize incorrect or unsafe instructions over style observations.
