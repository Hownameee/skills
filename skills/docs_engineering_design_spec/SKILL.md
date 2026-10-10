---
name: docs_engineering_design_spec
description: "Create or review an engineering design spec that turns confirmed requirements into an implementable technical solution with alternatives, interfaces, migration, risks, rollout, and verification. Use for RFCs, feature designs, and integration or migration proposals. Do not use for decision-only ADRs, architecture overviews, requirements documents, or delivery plans."
---

# Specialist Engineering Design Spec

## 1. Scope And Document Depth

This skill explains **how a proposed change will work** and why that solution is suitable.

Choose the smallest sufficient mode:

- **Lightweight design:** local, reversible change with one owner and no contract, data, security, or operational risk.
- **Full design:** cross-component work, public contracts, migrations, sensitive data, authentication, production risk, vendor integration, or irreversible decisions.
- **Review:** evaluate an existing design without silently filling its unknowns.

Use an ADR for a durable decision and its rationale, architecture documentation for the wider system, requirements documentation for needed behavior, and a project plan for sequencing and ownership.

## 2. Preflight Discovery

Before writing:

1. Inspect the current implementation, entry points, interfaces, data model, deployment configuration, tests, and operational documentation affected by the proposal.
2. Link canonical requirements, architecture docs, ADRs, incidents, metrics, research, or customer evidence.
3. Identify stakeholders, decision owner, implementers, operators, security/privacy reviewers, and affected consumers.
4. Record verified facts, assumptions, constraints, and unresolved questions separately.
5. Confirm the requested decision, deadline if supplied, and evidence that will define success.

Do not invent system behavior, owners, dates, traffic, costs, vendor guarantees, or approvals.

## 3. Design Workflow

### Step 1: Frame The Problem

State:

- Current behavior and why it is insufficient.
- Goals, non-goals, and affected users or systems.
- Functional and quality requirements.
- Constraints and invariants that must remain true.
- Measurable success criteria and baseline when available.

Keep implementation preferences out of the problem statement.

### Step 2: Compare Viable Options

Include the status quo when it is viable. Evaluate options against the same criteria:

| Criterion | Questions |
| --- | --- |
| Correctness | Does it preserve required invariants? |
| Compatibility | Which clients, data, and deployments are affected? |
| Security/privacy | What trust or data boundary changes? |
| Reliability | How does it fail and recover? |
| Performance/cost | What capacity assumptions drive it? |
| Delivery | What skills, dependencies, and migration are required? |
| Operability | Can operators observe, support, and roll it back? |

Name the recommendation, tradeoffs, rejected alternatives, and conditions that would change the decision.

### Step 3: Specify The Proposed System

Describe only applicable elements:

- Component responsibilities, ownership, and boundaries.
- API, event, file, or job contracts.
- Data model, invariants, lifecycle, retention, and migration.
- Control flow and state transitions.
- Authentication, authorization, tenant isolation, privacy, audit, and abuse controls.
- Error handling, timeouts, retry budget, backoff, idempotency, concurrency, and partial failure.
- Capacity assumptions, expected load, resource limits, and cost drivers.
- Configuration, feature flags, secrets, and environment differences.
- Logs, metrics, traces, dashboards, alerts, and support signals.

Use diagrams only when they make a boundary, sequence, state transition, deployment, or data flow clearer than prose. Label trust boundaries and protocols.

### Step 4: Design Migration And Rollout

- Preserve compatibility across mixed-version deployment where required.
- Break data changes into expand, backfill, validate, cut over, and contract phases.
- Define feature-flag or cohort strategy, rollout increments, observation windows, and abort thresholds.
- Define rollback for code, configuration, traffic, and data. If data rollback is impossible, document forward recovery.
- Include cleanup criteria for flags, dual writes, deprecated fields, temporary jobs, and compatibility code.

### Step 5: Define Verification

Map risks and requirements to evidence:

- Unit, integration, contract, end-to-end, migration, rollback, performance, security, and acceptance tests as applicable.
- Pre-production validation and representative test data.
- Launch health signals and post-launch success measurements.
- Failure injection or degraded-dependency testing for important recovery paths.

## 4. Safety And Stop Conditions

- Require explicit approval before changing production, billing, identity-provider configuration, public contracts, or production data.
- Never place credentials, private customer data, or raw sensitive payloads in a design.
- State regulatory, retention, deletion, and residency implications when sensitive data changes.
- Flag vendor lock-in, irreversible data transforms, one-way migrations, and missing rollback prominently.
- Continue evidence-backed portions of a draft or review when the requirement owner, authorization model, data ownership, or success criteria are unresolved. Mark affected design choices as provisional or blocked, explain what would resolve them, and defer only the dependent decisions or actions; do not invent facts or imply implementation approval.

## 5. Edge Cases To Test

Consider duplicate delivery, replay, out-of-order events, stale reads, concurrent writes, partial batch failure, clock skew, retries after timeout, mixed-version nodes, schema drift, dependency outage, quota exhaustion, corrupt historical data, tenant boundary errors, rollback during backfill, and operator error.

Include only relevant cases, but explain why high-impact classes are not applicable.

## 6. Minimum Output Structure

```markdown
# Title
## Status And Owners
## Summary
## Context And Evidence
## Goals And Non-Goals
## Requirements And Constraints
## Options And Decision
## Proposed Design
## Security, Privacy, And Operations
## Migration, Rollout, And Rollback
## Verification
## Risks And Alternatives
## Open Questions
```

Omit irrelevant sections in lightweight mode rather than filling them with generic prose.

## 7. Review Checklist

- The proposal traces to verified requirements and current system evidence.
- The design is specific enough to implement and test.
- Interfaces, data, failure handling, security, and operations are explicit where relevant.
- Alternatives use the same comparison criteria.
- Compatibility, migration, rollout, rollback, and cleanup are credible.
- Every unresolved item has an owner or is marked as a blocker; unknown owners remain `TBD`.
- Referenced paths and links exist, diagrams agree with prose, and examples match the proposed contracts.
- The final output states validation performed and residual risk.
