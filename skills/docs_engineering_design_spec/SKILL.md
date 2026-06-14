---
name: docs_engineering_design_spec
description: Engineering design spec rules for technical proposals, alternatives, API/data changes, migration plans, risks, rollout, observability, and review readiness.
---

# Specialist Engineering Design Spec

## 1. Scope

Use this skill when creating or reviewing engineering design documents, technical specs, RFCs, implementation proposals, migration designs, integration designs, or feature design briefs.

## 2. Problem Framing

- Start with the problem, context, goals, non-goals, stakeholders, and current system constraints.
- Link to requirements, architecture docs, ADRs, incidents, metrics, or customer evidence that justify the work.
- Define success criteria and the evidence that will prove the design worked.
- Separate user-visible behavior from internal implementation details.
- State assumptions and open questions explicitly.

## 3. Proposed Design

- Describe the design at the right level: API, data model, control flow, components, jobs, storage, permissions, and operational behavior.
- Include diagrams when they clarify boundaries, sequence, deployment, data flow, or failure handling.
- Specify compatibility, migration, rollout, rollback, and cleanup steps.
- Document data classification, security controls, authorization, privacy, audit, and abuse cases where relevant.
- Explain how the design handles errors, retries, idempotency, concurrency, partial failure, and observability.

## 4. Alternatives And Tradeoffs

- Include considered alternatives and why they were rejected.
- Evaluate tradeoffs against goals, constraints, quality attributes, delivery risk, operational burden, and future maintainability.
- Do not pretend there are no downsides; document known limitations and follow-up work.
- Escalate irreversible or cross-cutting decisions into ADRs when they will outlive the implementation.

## 5. Review Readiness

- Include implementation phases small enough for review and rollback.
- Define test strategy: unit, integration, contract, end-to-end, migration, performance, security, and manual acceptance where needed.
- Include operational readiness: dashboards, alerts, runbooks, support handoff, and incident response.
- Identify dependency owners and required approvals before work starts.
- Keep the spec current during implementation or clearly mark it as historical.

## 6. Review Checklist

- Confirm the problem and success criteria are clear before judging the solution.
- Confirm proposed changes are specific enough to implement and test.
- Confirm alternatives, risks, migration, rollout, and rollback are covered.
- Confirm security, privacy, data, observability, and operations were considered.
- Confirm unresolved questions are assigned owners or blocking status.
