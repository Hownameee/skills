---
name: analysis_blindspot_finder
description: "Find hidden assumptions, biases, failure modes, and weak evidence in a plan, decision, argument, or strategy. Use for pre-mortems and critical challenge; not for diagnosing a person's psychology or rewriting the plan itself."
---

# Specialist Blindspot Finder

## Scope

Challenge the reasoning supplied by the user and surface consequential risks that are easy to miss. Analyze the decision or argument, not the character, intelligence, mental health, or protected traits of its author.

Use this skill for:

- plans, proposals, forecasts, strategies, and architecture decisions
- assumptions behind an argument or recommendation
- pre-mortems, red-team reviews, and decision-quality checks
- important omissions, incentives, dependencies, or second-order effects

Do not replace a requested security review, legal review, medical assessment, or implementation design. Route those tasks to the relevant specialist and use this skill only as a complementary challenge pass.

## Inputs And Assumptions

Establish:

- decision, desired outcome, and time horizon
- alternatives considered and the apparent default
- evidence, assumptions, constraints, and definitions of success
- affected stakeholders and decision owner
- reversibility, cost of failure, and detection delay
- known unknowns and missing evidence

Ask a question only when a missing fact would materially change the analysis. Otherwise state the assumption and proceed.

## Analysis Workflow

1. Restate the decision or central claim without strengthening it.
2. Separate supplied facts, stated assumptions, inferred assumptions, and unknowns.
3. Identify the strongest argument for the current position before challenging it.
4. Generate candidate blindspots across the lenses below.
5. Connect each candidate to a plausible failure mechanism and affected outcome.
6. Search for disconfirming evidence or a counterexample that would weaken the finding.
7. Merge duplicates and remove generic observations that could apply to any plan.
8. Prioritize by likely impact, plausibility, time-to-detection, and reversibility.
9. Attach a practical question, experiment, control, or mitigation to each retained finding.

## Challenge Lenses

Use only relevant lenses:

- **Evidence:** selection bias, survivorship bias, weak proxies, stale data, small samples, and correlation treated as causation
- **Framing:** false binary, omitted alternatives, scope errors, local optimization, and ambiguous success criteria
- **Base rates:** ignored precedent, reference classes, regression to the mean, and unrealistic timelines
- **Incentives:** stakeholder conflicts, gaming, adoption friction, principal-agent problems, and political constraints
- **Dependencies:** single points of failure, vendor assumptions, coordination costs, and hidden operational ownership
- **Execution:** skills, capacity, sequencing, monitoring, rollback, maintenance, and incident response
- **Second-order effects:** feedback loops, displacement, path dependence, externalities, and behavior changes
- **Risk:** security, privacy, safety, compliance, financial exposure, reputation, and irreversible data loss
- **Uncertainty:** model error, unknown unknowns, correlated failures, and overly narrow scenarios

## Finding Format

Use a variable number of findings based on evidence and consequence. Prefer a short prioritized set over padded output.

For each finding include:

```markdown
### [Severity] Concise blindspot
- Basis: supplied fact, inference, or unknown that supports the concern
- Failure mode: how the assumption could produce harm
- Confidence: high, medium, or low, with a brief reason
- Disconfirming evidence: what would reduce or remove the concern
- Next check: a question, experiment, control, or mitigation
```

Use `Critical` only when impact is severe, plausible, and difficult to reverse. Do not use numerical probabilities without a defensible model.

If the user requests a table or concise list, preserve the same evidence, consequence, confidence, and next-check fields in that format.

## Safety And Pitfalls

- Do not fabricate private motives, psychological conditions, demographic traits, or intent.
- Do not treat disagreement as bias.
- Do not equate missing context with proof that a failure exists.
- Do not bury the strongest risk among equal-weight observations.
- Do not recommend destructive, deceptive, illegal, or unauthorized tests.
- For high-stakes domains, label the limits of this analysis and recommend qualified review where appropriate.

## Verification Checklist

- The decision or claim is represented fairly.
- Every finding identifies a specific assumption or omission.
- Facts, inferences, and unknowns are visibly distinct.
- Findings are non-duplicative and prioritized by consequence.
- Each failure mode is plausible and tied to an outcome.
- Counterevidence and a practical next check are included.
- Sensitive conclusions are not inferred from insufficient evidence.

## Trigger Examples

Should trigger:

- “Find the blindspots in this migration plan.”
- “Run a pre-mortem on our launch strategy.”
- “What assumptions make this argument fragile?”

Should not trigger:

- “Diagnose why this employee behaves this way.”
- “Implement the database migration.”
- “Perform a formal legal compliance review.”
