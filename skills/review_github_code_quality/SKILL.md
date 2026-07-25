---
name: review_github_code_quality
description: "Review code changes and prepare or publish evidence-based GitHub pull-request communication. Use for local code reviews, PR descriptions, inline review comments, or opening and updating PRs; default to read-only and do not publish, open, approve, merge, close, label, push, or message unless explicitly requested."
---

# GitHub Code Review And Communication

## Select The Mode

Choose one mode before acting:

- **Local review:** inspect code and report findings. Do not modify GitHub or repository state.
- **Draft communication:** prepare a PR description, review, or comment for the user. Do not publish it.
- **Publish:** create or update a PR, review, comment, label, approval, or other GitHub state only when the user explicitly asks for that exact action.

A request to review does not authorize a push, PR, comment, approval, merge, close, label, assignment, or public security disclosure. Use `devops_git_workflow` for staging, commits, pushes, and history changes.

## Establish Review Scope

1. Read repository instructions and contribution guidance.
2. Identify the intended base, head, issue or requirement, and review mode. Do not assume that the current branch is the PR base.
3. Inspect the complete diff, including renamed, deleted, generated, migration, dependency, configuration, and test files.
4. Read enough surrounding code to understand changed behavior, then inspect callers, callees, contracts, data models, authorization boundaries, and relevant tests.
5. Check current CI results or local validation only when available and authorized. Distinguish pre-existing failures from regressions.
6. State any material scope limit, such as unavailable generated output, missing dependencies, no runtime environment, or an inaccessible PR.

For large diffs, triage high-risk surfaces first: authentication, authorization, input boundaries, migrations, concurrency, external effects, public APIs, secrets, billing, and deployment configuration.

## Finding Verification

Before reporting a finding:

- Trace a realistic input or state to the affected code.
- Confirm that an existing guard, caller, test, framework guarantee, or deployment constraint does not prevent it.
- Explain the observable impact and affected users or systems.
- Check whether the issue was introduced by the reviewed change rather than merely pre-existing.
- Prefer one high-confidence finding over several speculative warnings.
- If a claim depends on an assumption, label it and name the evidence needed to confirm it.

Do not report personal style preferences as defects. Formatting can be a finding when it causes a parse error, semantic change, broken generated output, or enforced-linter failure.

## Severity And Finding Format

Use the repository's severity scheme when one exists. Otherwise:

- **Critical:** readily exploitable or catastrophic production, security, or data-loss impact.
- **High:** likely severe correctness, security, availability, or migration failure.
- **Medium:** bounded but real functional or operational defect.
- **Low:** limited impact with clear value in correcting.

Write each finding as:

```markdown
### [Severity] Concise defect title

- Location: path and narrow line reference
- Evidence: what the code does and why the guard is insufficient
- Trigger: concrete input, state, or execution sequence
- Impact: observable consequence
- Suggested fix: smallest viable correction
- Verification: test or check that proves the correction
```

Order findings by severity. Keep questions and non-blocking nits in separate sections. If no defects are found, say so and report validation and residual coverage limits.

## GitHub Communication

- Be concise, factual, respectful, and specific to the code. Critique behavior, not the author.
- Anchor inline comments to the narrowest changed line that demonstrates the defect.
- Do not claim to have run tests, reproduce behavior, or inspect files that were not actually checked.
- Avoid duplicating the same root cause across multiple inline comments; use one primary finding and reference affected sites.
- Do not expose secrets, private customer data, exploit details unsuitable for a public repository, or internal links.
- For a possible undisclosed vulnerability, stop public publication and use the repository's private security process.

## Opening Or Updating A Pull Request

Before an explicitly requested GitHub mutation:

1. Confirm repository, remote, branch, upstream, base branch, and whether a PR already exists.
2. Ensure only requested commits are on the branch and inspect the final diff.
3. Run or inspect the required validation and CI state.
4. Prepare a title and body that describe scope, motivation, implementation, validation, migration or rollback, risks, and issue linkage without unsupported claims.
5. Show the draft first when the requested wording or target is materially ambiguous.
6. Execute only the authorized action and verify its returned URL or state.

Do not approve your own work, merge, close, enable auto-merge, change reviewers, apply labels, or publish comments merely because a PR was opened.

## Licensing And Attribution

- When substantial code or documentation is copied or adapted, inspect the source license and comply with its notice, attribution, copyleft, and distribution requirements.
- Do not assume that every permissive license requires the same placement or that a link alone is sufficient.
- Do not add or alter unrelated repository licensing automatically. Stop and explain the conflict when compatibility or attribution is unclear.

## Completion Checklist

- Base/head, requirements, diff scope, and relevant surrounding behavior were inspected.
- Every finding has evidence, a trigger, an impact, and a feasible verification step.
- Findings, questions, nits, and coverage limits are separated.
- No external GitHub or Git state changed beyond the explicitly authorized action.
- Published content and final URLs or states were verified after mutation.
