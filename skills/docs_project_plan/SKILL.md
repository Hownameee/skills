---
name: docs_project_plan
description: Software project plan rules for scope, milestones, deliverables, risks, dependencies, roles, communication, quality gates, rollout, and tracking.
---

# Specialist Software Project Plan

## 1. Scope

Use this skill when creating or reviewing software project plans, implementation plans, delivery plans, rollout plans, milestone plans, migration plans, or engineering execution briefs.

## 2. Plan Foundation

- State the problem, desired outcome, success metrics, non-goals, and decision owner.
- Define scope in terms of deliverables, affected systems, users, data, environments, and operational responsibilities.
- Identify assumptions, constraints, dependencies, external teams, vendor dependencies, and required approvals.
- Choose planning detail based on risk: more detail for security, data, migration, compliance, production, or cross-team work.
- Keep the plan linked to requirements, architecture decisions, design specs, and issue trackers instead of duplicating everything.

## 3. Work Breakdown

- Break work into milestones or phases with clear entry and exit criteria.
- For each milestone, list deliverables, owner, dependencies, validation evidence, and rollback or fallback path.
- Include discovery, implementation, test, documentation, rollout, monitoring, and cleanup work.
- Make sequencing explicit when ordering matters for migrations, compatibility, customer impact, or risk reduction.
- Keep estimates tied to uncertainty and call out unknowns that need spikes or prototypes.

## 4. Risk And Quality Management

- Maintain a risk register with probability, impact, trigger, mitigation, owner, and review cadence.
- Include quality gates for security review, privacy review, performance, accessibility, data integrity, operational readiness, and support handoff when relevant.
- Define test strategy across unit, integration, end-to-end, migration, rollback, load, and acceptance tests.
- Plan observability: logs, metrics, traces, dashboards, alerts, and success criteria for launch.
- Document decisions required before build, before rollout, and before project closure.

## 5. Communication And Change Control

- Identify stakeholders, approvers, contributors, informed parties, and escalation paths.
- Define reporting cadence, status format, decision log location, and how scope changes are approved.
- Track open questions and decisions separately from completed facts.
- Update the plan when scope, dates, dependencies, or risk changes; do not let stale plans become false authority.
- Include launch, support, incident, rollback, and post-launch review ownership.

## 6. Review Checklist

- Confirm scope, non-goals, success metrics, owners, and milestones are explicit.
- Confirm risks, dependencies, approvals, and sequencing are visible.
- Confirm validation evidence is defined before implementation starts.
- Confirm rollout and rollback paths are credible.
- Confirm the plan has an update owner and cadence.
