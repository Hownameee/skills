---
name: docs_software_architecture
description: Software architecture documentation rules for arc42, C4, ISO 42010-style views, quality attributes, constraints, risks, and stakeholder communication.
---

# Specialist Software Architecture Documentation

## 1. Scope

Use this skill when creating or reviewing software architecture documents, architecture overviews, C4 diagrams, arc42-style docs, system context, container/component views, runtime views, deployment views, or architecture review material.

## 2. Audience And Purpose

- Identify the primary reader: engineer, architect, operator, security reviewer, product owner, executive, auditor, or new maintainer.
- State what decision or maintenance task the document should support.
- Separate the architecture of the system from the document that describes it.
- Prefer just-enough documentation that explains durable structure, decisions, tradeoffs, and quality concerns.
- Keep implementation details only when they explain an architectural constraint or recurring design rule.

## 3. Required Content

- Start with goals, non-goals, business context, and the top quality attributes that drive architecture.
- Document constraints such as regulation, organization, existing systems, budgets, runtime, deployment, data, and security boundaries.
- Define system context: users, neighboring systems, external interfaces, protocols, trust boundaries, and ownership.
- Describe solution strategy: core architectural choices, decomposition approach, key patterns, and why they fit the quality goals.
- Include static structure, runtime behavior, deployment topology, cross-cutting concepts, known decisions, risks, and glossary.

## 4. Views And Diagrams

- Use C4-style abstraction levels when helpful: system context, containers, components, and code-level detail only when necessary.
- Give every diagram a title, scope, audience, notation legend, and date or version.
- Label relationships with intent and protocol, not only arrows.
- Keep diagrams consistent with text and source reality; update or remove stale diagrams quickly.
- Prefer diagrams that answer stakeholder questions over decorative comprehensive maps.

## 5. Quality Attributes And Tradeoffs

- Express quality requirements as scenarios with trigger, environment, response, and measurable target where feasible.
- Tie major design decisions to quality goals such as availability, latency, modifiability, security, privacy, operability, scalability, and cost.
- Document rejected alternatives when they explain important tradeoffs or future constraints.
- Capture risks, assumptions, technical debt, and review follow-ups explicitly.
- Link detailed ADRs instead of duplicating decision rationale in multiple places.

## 6. Review Checklist

- Confirm the document names stakeholders and the questions it answers.
- Confirm context, boundaries, external systems, and interfaces are unambiguous.
- Confirm diagrams and text agree with current code, infrastructure, and deployment reality.
- Confirm quality attributes, constraints, decisions, risks, and glossary are present.
- Confirm the document is maintainable: owners, location, update trigger, and review cadence are clear.
