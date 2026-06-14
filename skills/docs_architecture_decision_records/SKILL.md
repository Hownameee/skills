---
name: docs_architecture_decision_records
description: Architecture Decision Record rules for documenting significant software decisions, context, options, outcomes, consequences, status, and follow-up validation.
---

# Specialist Architecture Decision Records

## 1. Scope

Use this skill when creating, reviewing, or organizing Architecture Decision Records, decision logs, technical decision proposals, or lightweight design decision documentation.

## 2. Decision Selection

- Write an ADR for decisions that are hard to reverse, architecturally significant, risky, cross-team, expensive, security-sensitive, or likely to be questioned later.
- Do not write ADRs for routine implementation choices that are obvious from code and cheap to change.
- Keep one decision per ADR.
- Link related ADRs instead of merging separate decisions into one record.
- Create the ADR near the time of decision; do not reconstruct rationale from memory unless explicitly marked as retrospective.

## 3. ADR Content

- Use a stable title that states the decision, not a vague topic.
- Record status: proposed, accepted, rejected, deprecated, superseded, or replaced.
- Describe context and problem statement before the chosen option.
- List considered options with meaningful pros, cons, risks, and constraints.
- State the decision outcome and why it wins under the current constraints.
- Document consequences, including operational burden, migration cost, security impact, and known drawbacks.

## 4. Repository Organization

- Store ADRs in a predictable docs location such as `docs/decisions/` or the repository's established decision directory.
- Use stable filenames with a sortable prefix or date plus a short dashed title.
- Keep numbering rules consistent inside a project.
- Categorize large ADR sets by architectural area only when discoverability suffers.
- Link ADRs from architecture docs, project plans, epics, or implementation PRs when they explain current behavior.

## 5. Review And Maintenance

- Review ADRs for clarity, evidence, stakeholder input, and whether alternatives were fairly represented.
- Mark superseded decisions instead of editing history to hide the original context.
- Add confirmation criteria: what evidence will show the decision worked or needs revisiting.
- Revisit ADRs when constraints, scale, regulation, incidents, or business goals change.
- Avoid duplicating long implementation details; link to specs, diagrams, or code instead.

## 6. Review Checklist

- Confirm the record explains why the decision matters.
- Confirm options, outcome, and consequences are explicit.
- Confirm status and supersession links are current.
- Confirm sensitive details, secrets, and confidential vendor terms are not exposed.
- Confirm the ADR can be understood without private chat history.
