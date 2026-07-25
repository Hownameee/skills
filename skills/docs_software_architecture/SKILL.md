---
name: docs_software_architecture
description: "Create or review evidence-backed software architecture documentation using only the views needed to explain system context, structure, runtime, deployment, data, trust boundaries, and quality tradeoffs. Use for architecture overviews and C4 or arc42-style material. Do not use for implementation specs, ADRs, requirements, or project plans."
---

# Specialist Software Architecture Documentation

## 1. Scope And Audience

Architecture documentation explains durable system structure and behavior to support concrete stakeholder questions. It is not a source-code inventory or a mandatory collection of every possible view.

Before writing, identify:

- Primary readers: engineers, operators, security reviewers, auditors, product owners, or new maintainers.
- Decisions, changes, incidents, or maintenance tasks the document must support.
- Intended scope and abstraction level.
- Document owner, canonical location, update trigger, and review cadence.

Use ADRs for durable decisions, design specs for proposed implementation, requirements documents for needed behavior, and project plans for delivery.

## 2. Evidence Discovery

Inspect the live sources that define architecture:

1. Runtime entry points and composition roots.
2. Package/module boundaries and major dependencies.
3. Public APIs, events, jobs, storage schemas, and integrations.
4. Deployment manifests, infrastructure configuration, networking, and environment topology.
5. Authentication, authorization, secrets, tenant, and data boundaries.
6. Existing diagrams, architecture docs, ADRs, runbooks, tests, and ownership files.

Trace representative runtime flows from entry point through dependencies and side effects. Label statements as verified, inferred, or unknown. Never present a planned or assumed component as currently deployed.

## 3. Select Views From Questions

Choose only views that answer a reader's question:

| Question | Useful view |
| --- | --- |
| Who and what interacts with the system? | System context |
| What are the deployable/runtime responsibilities? | Container/service |
| Where is behavior implemented? | Component/module |
| How does a scenario execute or fail? | Runtime/sequence |
| Where and how does it run? | Deployment |
| How does information move and persist? | Data flow/lifecycle |
| Where can trust change? | Threat/trust-boundary |

Code-level diagrams are appropriate only when source navigation or a critical design mechanism requires them.

## 4. Documentation Workflow

### Step 1: Establish Drivers

- State business context, goals, non-goals, constraints, and top quality attributes.
- Express important quality attributes as scenarios with stimulus, environment, response, and measurable target when evidence exists.
- Link decisions to ADRs rather than duplicating their full rationale.

### Step 2: Describe Context And Boundaries

- Name users, external systems, ownership, protocols, data exchanged, availability assumptions, and trust boundaries.
- Identify system-of-record responsibility and authoritative data owner.
- Distinguish synchronous, asynchronous, batch, control-plane, and data-plane interactions.

### Step 3: Describe Structure And Runtime

- Give each component one clear responsibility and owner.
- Document public interfaces and dependency direction.
- Trace normal, degraded, failure, retry, recovery, and administrative flows where relevant.
- Include consistency, idempotency, concurrency, timeout, and backpressure behavior when architectural.

### Step 4: Describe Deployment And Operations

- Show processes, workloads, networks, regions/zones, data stores, gateways, queues, and external dependencies at the required level.
- Distinguish development, test, staging, and production only where topology or controls differ materially.
- Document scaling, failover, backup/restore, observability, secrets, and operational ownership.

### Step 5: Record Cross-Cutting Concerns

Cover applicable authentication, authorization, tenant isolation, encryption, privacy, audit, resilience, configuration, observability, cost, and compliance rules. Link canonical details instead of duplicating volatile procedures.

## 5. Diagram Conventions

- Prefer text-based diagrams when the repository can render and review them.
- Give every diagram a title, scope, abstraction level, legend, and version or last-verified date.
- Label relationships with direction, intent, protocol, and important data—not only arrows.
- Mark trust boundaries and external ownership explicitly.
- Keep names identical across prose, code, manifests, and diagrams.
- Avoid decorative icons, crossed edges, mixed abstraction levels, and databases or queues with unexplained ownership.
- Provide a short prose interpretation so the document remains accessible without rendering.

## 6. Safety And Edge Cases

- Do not include secrets, private endpoints, customer data, or exploitable operational detail beyond the intended audience.
- Avoid unsupported availability, capacity, compliance, or security claims.
- Address, when relevant, multi-region failover, network partitions, queue duplication, stale caches, schema/version skew, tenant isolation, disaster recovery, third-party outage, operator paths, and ownership gaps.
- Stop when the documented scope, deployed topology, data ownership, or trust boundary cannot be established reliably.

## 7. Validation Checklist

- Trace every major component, interface, and deployment claim to current code, configuration, or a cited canonical source.
- Confirm diagrams and prose agree with each other.
- Verify referenced file paths, document links, protocols, and ownership.
- Walk at least one normal flow and one important failure or recovery flow.
- Confirm data lifecycle and trust boundaries are visible.
- Render or lint diagrams using existing repository tooling when available.
- Mark planned, deprecated, inferred, and unknown elements explicitly.
- Record owner, canonical location, last verification, and events that require an update.

## 8. Output Contract

Return the audience and questions, selected views, evidence-backed architecture narrative and diagrams, constraints and quality drivers, risks and unknowns, validation performed, and freshness metadata. Omit views that do not answer a stated question.
