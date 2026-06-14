---
name: security_secure_code_review
description: Secure code review workflow for finding exploitable defects, privacy leaks, and high-risk regressions in code changes.
---

# Specialist Secure Code Review

## 1. Scope

Use this skill when reviewing a pull request, diff, generated code, or security-sensitive implementation for exploitable defects and privacy or compliance regressions.

## 2. Review Setup

- Start from the changed threat surface: new inputs, outputs, auth paths, storage, dependencies, jobs, network calls, and privileged operations.
- Read the surrounding caller and callee code before judging a diff hunk.
- Separate findings from style preferences; report only issues with a plausible failure mode or security impact.
- Prefer file and line-specific findings with concrete exploit or regression reasoning.
- Use existing security tests, static analysis, dependency scans, and framework conventions as evidence, not as substitutes for review.

## 3. High-Risk Checks

- Access control: missing tenant, owner, role, object-level, or state-transition checks.
- Injection: SQL, NoSQL, LDAP, shell, template, path traversal, SSRF, XML, deserialization, and unsafe eval patterns.
- Secret handling: hardcoded credentials, token logging, unsafe env exposure, weak key rotation, or leaked private config.
- Cryptography: custom crypto, weak randomness, insecure modes, missing authentication, or broken certificate validation.
- Data exposure: excessive API responses, verbose errors, logs, analytics, cache headers, backups, or client-side storage.
- Business logic: replay, race conditions, duplicate submission, price/permission tampering, webhook spoofing, and missing idempotency.

## 4. AI-Generated Code Biases

- Assume generated code may pass happy-path tests while still containing security defects.
- Verify imports, APIs, defaults, and middleware ordering against actual project dependencies.
- Watch for plausible-looking but nonexistent framework security features.
- Require tests or explicit reasoning for authorization, validation, error handling, and rollback behavior.
- Do not accept "standard practice" claims without local evidence or official documentation.

## 5. Output Format

- Lead with findings ordered by severity.
- For each finding include location, impact, trigger condition, and a concrete remediation direction.
- Mark uncertainty explicitly when evidence is incomplete.
- Keep summaries short and secondary to actionable findings.
- If no issues are found, state remaining coverage limits such as missing tests, unreviewed generated files, or unavailable runtime evidence.
