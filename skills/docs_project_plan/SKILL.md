---
name: docs_project_plan
description: "Create or review an execution plan that organizes confirmed work into scoped milestones, dependencies, owners, validation gates, rollout, and closure. Use for implementation, migration, delivery, or cross-team planning. Do not use to invent the technical solution, write requirements, or record an architecture decision."
---

# Specialist Software Project Plan

## 1. Scope And Planning Mode

This skill describes **how approved work will be delivered and controlled**.

Choose:

- **Lightweight checklist:** small, reversible, single-owner work with few dependencies.
- **Phased plan:** cross-team, migration, security, data, production, compliance, vendor, or long-running work.
- **Review:** test whether an existing plan is complete, feasible, current, and verifiable.

Use requirements and design artifacts as inputs. Do not use a plan to conceal unresolved product or technical decisions.

## 2. Preflight Discovery

1. Inspect the current repository or system state relevant to the plan.
2. Link canonical requirements, designs, ADRs, issues, release policy, runbooks, and operational constraints.
3. Confirm the outcome, scope, non-goals, decision owner, affected environments, and completion evidence.
4. Identify dependencies, external teams, vendors, approvals, maintenance windows, and resource constraints.
5. Record facts, estimates, assumptions, and open questions separately.

Never invent people, commitments, dates, budgets, or estimates. Use `TBD` with a resolution owner when information is unavailable.

## 3. Work Breakdown Workflow

### Step 1: Establish Boundaries

Define:

- Deliverables and explicitly excluded work.
- Affected systems, users, data, environments, and operations.
- Success metrics, quality constraints, and closure criteria.
- Required decisions and approval gates.

### Step 2: Build Milestones

Each milestone must produce independently reviewable evidence:

| Field | Meaning |
| --- | --- |
| Milestone | Outcome, not an activity bucket |
| Status | Not started, in progress, blocked, complete, or cancelled |
| Owner | Confirmed owner or `TBD` |
| Dependencies | Required predecessor or external input |
| Deliverables | Concrete artifacts or behavior |
| Exit evidence | Test, review, metric, or approval |
| Fallback | Rollback, containment, or alternate path |

Include discovery, implementation, test, documentation, security/privacy review, rollout, observation, support handoff, and cleanup only when applicable.

### Step 3: Sequence And Estimate

- Mark the critical path and work that can run in parallel.
- State why ordering matters for compatibility, data, security, or risk.
- Express estimates with assumptions and confidence; use ranges for uncertainty.
- Create a spike only for a named uncertainty, with a time box and decision output.
- Include contingency for material external dependencies without disguising it as certainty.

### Step 4: Manage Risk And Quality

For each material risk, record probability, impact, trigger, mitigation, contingency, owner, and review point.

Define relevant gates for:

- Functional and regression testing.
- Security, privacy, accessibility, and compliance review.
- Data integrity, migration rehearsal, and rollback.
- Performance and capacity.
- Operational readiness, dashboards, alerts, and runbooks.
- User or stakeholder acceptance.

No milestone is complete until its exit evidence exists.

### Step 5: Plan Rollout And Closure

- Define rollout units, environments, cohorts, feature flags, observation windows, and abort thresholds.
- Name rollback or forward-recovery actions and their decision authority.
- Assign launch, support, incident, and post-launch monitoring ownership.
- Include cleanup for temporary flags, compatibility paths, test data, deprecated behavior, and temporary infrastructure.
- Close only after acceptance evidence, operational handoff, documentation, residual-risk acceptance, and follow-up ownership are recorded.

## 4. Status And Change Control

Use a compact status update:

```markdown
Status: On track | At risk | Blocked
Completed: verified outcomes since the last update
Next: immediate milestones and owners
Decisions: resolved or needed, with due owner
Risks: changed probability, impact, or mitigation
Scope/date changes: approved change and reason
```

- Keep decisions, risks, actions, and completed facts distinct.
- Update dependencies and the critical path when scope or timing changes.
- Record who approved a material scope, cost, date, or risk change.
- Mark stale plans historical rather than leaving them as false authority.

## 5. Safety And Edge Cases

- Require explicit approval for production changes, destructive migrations, security-policy changes, public communication, or spending commitments.
- Do not place secrets, credentials, or unnecessary personal data in plans.
- Address blocked owners, cancelled work, unavailable vendors, missed maintenance windows, partial rollout, failed rollback, incident interruption, staffing changes, and dependencies outside the team's control.
- Stop when the plan depends on an unapproved design, unknown destructive scope, or unresolved owner for a critical action.

## 6. Verification Checklist

- Scope, non-goals, outcome, and completion evidence agree with source requirements.
- Every milestone has an outcome, owner or `TBD`, dependency, exit evidence, and fallback where needed.
- The critical path and parallel work are visible.
- Dates and estimates are sourced or explicitly uncertain.
- Risks, approvals, rollout, rollback, observation, support, and cleanup are covered proportionally.
- Links and referenced artifacts exist.
- Completed work has evidence; status is not inferred from elapsed time.
- The plan states its update owner, cadence, and last-reviewed date.

## 7. Output Contract

Return the plan, assumptions, unresolved decisions, critical path, risk register, validation gates, and current residual risks. In review mode, list blocking omissions first and do not silently rewrite unconfirmed facts.
