---
name: core_code_quality
description: "Review or improve source code for clarity, cohesion, error handling, naming, duplication, and secure boundaries. Use during implementation or refactoring; repository and language conventions take precedence over this cross-language baseline."
---

# Code Quality Standards

## Scope And Precedence

Apply these rules as a cross-language review baseline. First follow the repository's current architecture, formatter, linter, language idioms, public contracts, generated-code policy, and tests. Do not impose a different style merely because it is personally preferred.

Optimize for correctness and maintainability in the requested scope. Do not turn a focused bug fix into a broad refactor without authorization.

## Workflow

1. Read the applicable repository instructions and inspect current changes.
2. Trace the affected behavior through callers, callees, contracts, side effects, and tests.
3. State the invariant that must remain true.
4. Identify the smallest quality problem that affects correctness, comprehension, testability, or change risk.
5. Apply a focused change consistent with local conventions.
6. Review the diff for behavior changes, unnecessary abstractions, and accidental formatting churn.
7. Run the narrowest meaningful formatter, static check, test, or build.

## Cohesion And Functions

- A function should represent one cohesive operation at one abstraction level.
- Treat length, nesting, branch count, repeated setup, mixed side effects, and difficulty naming or testing as refactoring signals—not universal limits.
- Extract a helper only when it clarifies a meaningful operation, isolates a policy or side effect, enables reuse of the same knowledge, or materially improves testing.
- Avoid fragmented “helper soup,” pass-through wrappers, and abstractions with only hypothetical future value.
- Preserve transaction, locking, resource-lifetime, short-circuit, and error semantics when splitting code.
- Prefer guard clauses when they make the main path clearer, but do not obscure required cleanup.

## Naming

- Use the repository's domain vocabulary and distinguish operations with different semantics.
- Prefer names that reveal purpose, unit, scope, and side effect where those are not obvious.
- Short conventional names are acceptable for small local scopes, mathematical notation, callbacks, and language idioms.
- Extract literals when they encode policy, repeat with shared meaning, require units, or benefit from validation. Leave obvious one-off literals local.
- Avoid misleading boolean names, ambiguous abbreviations, redundant type words, and renames that create large low-value diffs.

## Comments And Documentation

- Explain non-obvious intent, invariants, business rules, compatibility constraints, risk, or tradeoffs.
- Document public contracts when the language or repository expects it.
- Do not narrate syntax or leave comments that merely restate clear code.
- Update or remove stale comments when behavior changes.
- Keep required license, generator, API, lint, suppression, and security annotations intact.
- Prefer clearer structure over a long explanatory comment, but retain a comment when the reason cannot be encoded safely in code.

## Duplication And Abstraction

- Remove duplicate business knowledge when both copies must change together.
- Do not merge code that only looks similar but has different ownership, lifecycle, or change reasons.
- Prefer a local duplicate over a premature shared abstraction when the common rule is not yet stable.
- Place shared behavior at the lowest layer that legitimately owns it; avoid generic `utils` dumping grounds.
- Check that an abstraction reduces conceptual load rather than moving complexity behind indirection.

## Errors And Boundaries

Choose behavior from the contract:

| Situation | Preferred response |
| --- | --- |
| Invalid external input | Reject at the boundary with a stable, non-sensitive error. |
| Expected absence | Use the language's option/result/not-found convention. |
| Recoverable transient failure | Retry only when safe, bounded, observable, and idempotent. |
| Lower-layer failure | Add useful context and preserve the cause or error code. |
| Irrecoverable invariant violation | Fail before further side effects and make the failure observable. |
| Deliberately ignored error | Document why it is safe and satisfy the local lint convention. |

- Do not both log and rethrow at every layer. Log once where the application owns handling or operational context.
- Never log credentials, tokens, cookies, authorization headers, personal data, or raw production payloads.
- Avoid catching overly broad exceptions unless cleanup, translation, aggregation, or a process boundary requires it.
- `null`, optional values, result types, exceptions, and status codes are all valid when they match the established contract.
- Validate external input and cross-boundary assumptions; do not scatter duplicate validation throughout trusted internal code.

## Secure Boundaries

- Use parameterized database APIs and structured process execution; never interpolate untrusted data into SQL or a shell command.
- Encode untrusted content for the specific output context: HTML text, HTML attribute, URL, JavaScript, CSS, SQL, or shell are different contexts.
- Prefer framework auto-escaping and safe DOM APIs. Do not treat input sanitization as a universal substitute for output encoding.
- Enforce authentication and authorization at trusted server-side boundaries.
- Use allowlists, size limits, timeouts, bounded concurrency, and safe defaults where the threat model requires them.
- Do not weaken security, validation, or auditability merely to simplify code.

## Common Anti-Patterns

- refactoring and behavior changes mixed without tests
- generic abstractions created for one call site
- a catch block that hides an operation's failure
- error messages containing secrets or raw payloads
- a constant extracted for every literal regardless of meaning
- comments that disagree with executable behavior
- broad formatting changes that obscure the functional diff

## Verification Checklist

- Public behavior and compatibility are preserved or intentionally documented.
- Functions are cohesive and helpers earn their abstraction cost.
- Names follow local vocabulary and make units or effects clear.
- Error behavior matches caller expectations and preserves useful causes.
- Logs and errors do not expose sensitive data.
- Inputs, outputs, database calls, and process execution use context-appropriate controls.
- The diff is scoped and contains no unrelated cleanup.
- Targeted formatter, static checks, tests, or build pass; skipped checks are named.

## Trigger Examples

Should trigger:

- “Refactor this handler without changing behavior.”
- “Review this code for maintainability and error-handling problems.”

Should not trigger:

- “Design our whole service architecture.”
- “Perform an exploit-focused security review.” Use the secure review skill.
