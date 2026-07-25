---
name: core_reasoning_and_context
description: "Gather evidence, trace behavior, manage assumptions, and recover from failed hypotheses before repository work. Use for ambiguous, multi-file, unfamiliar, or high-risk tasks; not as a reason to block clear low-risk work with ritual approval."
---

# Evidence And Context Strategy

## Operating Principle

Make the smallest defensible decision from current evidence. Scale discovery, planning, communication, and verification to uncertainty, impact, reversibility, and user authorization.

Provide concise conclusions, evidence, assumptions, and tradeoffs. Do not expose hidden chain-of-thought or require the user to approve an internal reasoning process.

## Classify The Request

Before acting, identify the mode:

| Mode | Default behavior |
| --- | --- |
| Answer or explain | Read relevant evidence and respond; do not mutate state. |
| Review or audit | Inspect the complete requested scope and report evidence-first findings; edit only if asked. |
| Diagnose | Reproduce or trace the cause; do not implement a fix unless requested. |
| Change or build | Make the smallest scoped change and verify it. |
| External or high-risk action | Resolve exact targets, explain consequence, and obtain required authority. |

Distinguish user intent from actions that merely seem helpful. Read-only checks and normal local implementation steps are usually in scope; deployments, public communication, credentials, production data, destructive changes, and materially broader work are not implied.

## Risk-Scaled Planning

Use a written or user-approved plan when the user requests one or when work is multi-stage, coordination-heavy, difficult to reverse, or involves production, migration, security, or public effects. Keep a lightweight mental checklist for clear, local, reversible work.

Do not create a plan file unless requested or useful as a durable project artifact. A plan does not expand authorization.

## Evidence Hierarchy

Prefer:

1. direct user constraints and current repository instructions
2. live checkout, executable behavior, tests, manifests, generated configuration, and version-control state
3. canonical local documentation and architecture decisions
4. version-matched official documentation
5. third-party explanations
6. explicit inference

Label inference and uncertainty. Do not convert filenames, comments, stale documents, or failing tests into confirmed behavior without corroboration.

## Context Workflow

1. Confirm scope, mode, deliverable, and explicit constraints.
2. Inspect repository root, applicable instructions, version-control state, and manifests.
3. Search before reading broadly; follow symbols, configuration, and tests from the requested behavior.
4. Trace one real path from entrypoint through callers, dependencies, side effects, and observable output.
5. Compare documentation with executable evidence and record mismatches.
6. Check installed versions before using an API or recommending version-sensitive behavior.
7. Form a testable hypothesis and choose the cheapest discriminating check.
8. Act, observe, and update the hypothesis from new evidence.
9. Stop discovery when evidence is sufficient for the requested decision; do not map the entire repository without need.

Use host-neutral capabilities such as inventory, search, focused read, patch, execute, diff, and validate rather than assuming a particular tool name.

## Questions And Assumptions

Ask only when:

- alternatives would produce materially different results
- an irreversible or external action lacks authority
- the exact target cannot be resolved safely
- required secrets, accounts, or business policy cannot be discovered
- a high-risk ambiguity cannot be bounded with a reversible approach

For low-risk gaps, state a reasonable assumption and proceed. Group non-blocking questions and continue with independent work. Never ask for confirmation merely to demonstrate understanding.

## Dependency And API Checks

- Read the repository manifest, lockfile, runtime version, and current usage.
- Prefer local types, source, generated clients, or installed documentation.
- Consult current official documentation when the fact is version-sensitive or absent locally.
- Use an isolated scratch reproduction only when it is safe, bounded, and does not mutate project or external state.
- Do not install a package, change production dependencies, or contact an external service without appropriate authority.

## Failure Recovery

When a check or change fails:

1. Preserve the exact error and operation that produced it.
2. Classify likely cause: assumption, environment, permission, dependency, data, concurrency, or code.
3. Gather one new piece of evidence that distinguishes the leading causes.
4. Revise the hypothesis; do not repeat the same action without changed evidence or parameters.
5. Try the safest bounded alternative.
6. Revert only changes owned by the current task when rollback is needed.
7. Report a blocker when further progress requires new authority or external state.

Do not hide failed validation or weaken tests to obtain a passing result.

## Communication

- Before tool-heavy work, state the immediate objective and relevant assumption.
- During long work, report concise milestones, findings, or changed risk.
- Lead final responses with the outcome, followed by files, validation, and residual risk.
- Share evidence and decision rationale, not private internal deliberation.
- Distinguish confirmed facts, inference, and unvalidated recommendations.

## Verification Checklist

- The final action matches the user's requested mode and scope.
- Applicable repository instructions and current changes were considered.
- The real behavior path or contract was traced far enough to support the conclusion.
- Version-sensitive claims were checked against the installed version or current official source.
- Material assumptions are explicit; unnecessary questions did not block progress.
- Failures changed the next hypothesis rather than causing blind retries.
- Validation is proportional to risk and skipped checks are named.
- No external, destructive, or high-risk action exceeded authorization.

## Trigger Examples

Should trigger:

- “Understand this unfamiliar repository before changing the request flow.”
- “Diagnose why this integration fails without guessing.”
- “Plan this multi-stage migration and identify assumptions.”

Should not trigger:

- “Rename this confirmed local variable.”
- “Repeat your previous answer.”
