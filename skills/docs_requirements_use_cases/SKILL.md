---
name: docs_requirements_use_cases
description: Requirements and use-case documentation rules for SRS, user stories, acceptance criteria, actors, flows, constraints, non-functional requirements, and traceability.
---

# Specialist Requirements And Use Cases

## 1. Scope

Use this skill when creating or reviewing software requirements specifications, product requirements, user stories, use cases, acceptance criteria, feature briefs, functional requirements, or non-functional requirements.

## 2. Requirements Quality

- Write requirements as verifiable statements of need, capability, constraint, or quality target.
- Separate business goals, user needs, system behavior, assumptions, constraints, and implementation decisions.
- Avoid ambiguous words such as fast, easy, robust, seamless, scalable, or secure unless they have measurable criteria.
- Include source, owner, priority, rationale, and status for requirements that affect scope or contract.
- Maintain traceability from requirement to design, implementation, test, and release decision when project risk justifies it.

## 3. Functional Requirements

- Define actors, permissions, preconditions, triggers, main flow, alternate flows, error flows, and postconditions.
- State system responsibilities and external-system responsibilities separately.
- Specify inputs, validations, outputs, state changes, notifications, audit events, and side effects.
- Cover edge cases, failure modes, retries, concurrency, idempotency, accessibility, localization, and data retention when relevant.
- Keep UI wording, API contracts, and business rules aligned.

## 4. User Stories And Acceptance Criteria

- Use user stories to capture who needs what outcome and why; do not hide technical work behind fake users.
- Make acceptance criteria testable and observable.
- Prefer scenario-style criteria for workflows with important branches.
- Define done in terms of behavior, security, data, observability, documentation, and rollout requirements where applicable.
- Split stories that mix unrelated actors, workflows, or release risks.

## 5. Non-Functional Requirements

- Document quality attributes such as performance, availability, security, privacy, usability, accessibility, compliance, reliability, operability, and maintainability.
- Express quality requirements with measurable thresholds, operating conditions, and evidence source.
- Identify regulatory, platform, browser, device, data residency, and integration constraints.
- State assumptions and dependencies that could invalidate estimates or designs.
- Include out-of-scope items to prevent accidental scope expansion.

## 6. Review Checklist

- Confirm each requirement is necessary, unambiguous, feasible, testable, and traceable at the required level.
- Confirm use cases include alternate and failure flows, not only happy paths.
- Confirm acceptance criteria can be verified without reading the author's mind.
- Confirm non-functional requirements have measurable targets or explicit review gates.
- Confirm requirements do not prematurely mandate implementation unless a constraint requires it.
