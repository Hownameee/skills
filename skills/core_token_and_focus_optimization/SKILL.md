---
name: core_token_and_focus_optimization
description: "Control context size, search depth, tool output, and solution scope during long or multi-source tasks. Use when work risks context overload or over-engineering; not as a reason to omit evidence, validation failures, or required detail."
---

# Context And Focus Optimization

## Scope

Maintain a compact, accurate working set while completing context-heavy tasks. Optimize for useful evidence per token and smallest sufficient solution—not for minimal output at the expense of correctness.

Use this skill for:

- unfamiliar or large repositories
- long-running investigations
- multi-document or multi-source synthesis
- large logs, generated output, or repeated tool calls
- tasks prone to speculative abstractions or scope drift

Do not use it to shorten a response that the user requested in detail or to suppress errors, safety concerns, source attribution, failing tests, assumptions, or residual risk.

## Active Working Set

Track only information needed to finish the current scope:

- current user objective and deliverable
- explicit constraints and authorization boundaries
- repository state and affected paths
- verified facts with source pointers
- decisions and their rationale
- active hypothesis or next action
- validation results, errors, and unresolved risks

Discard duplicate prose and superseded hypotheses after recording why they changed. Preserve precise error text, commands, file/line references, contract details, and security evidence when they affect the next decision.

## Focus Workflow

1. Define the exact outcome, constraints, and completion criteria.
2. Inventory the relevant surface before opening many files.
3. Form a narrow question for each search or command.
4. Read the smallest region that can answer it, then expand only when dependencies require it.
5. Record findings with stable file, line, section, URL, or command references.
6. Stop gathering when evidence is sufficient for the current decision.
7. Implement the smallest maintainable solution that meets the actual requirement.
8. Validate at the narrowest meaningful layer, then widen only when risk or failure demands it.
9. Summarize durable state when the working set becomes difficult to reconstruct accurately.

## Efficient Discovery

- Search symbols, filenames, configuration keys, and error strings before broad reads.
- Inspect manifests, entrypoints, and tests to locate authoritative behavior.
- Batch independent read-only checks when results do not depend on one another.
- Avoid repeating a read unless the file may have changed or a new question requires different context.
- Prefer targeted source and official documentation over broad secondary research.
- Keep large optional references unloaded until a concrete decision needs them.
- Do not map an entire repository when one runtime path answers the question.

## Tool And Output Discipline

- Set focused paths, queries, date ranges, or line ranges.
- Bound command output and request the smallest useful result set.
- Filter large logs by time, component, request ID, severity, or error signature.
- Summarize noisy output immediately and retain the command plus exact evidence pointer.
- Avoid printing secrets, personal data, huge JSON payloads, minified assets, dependency trees, or generated files into the conversation.
- Use deterministic repository scripts rather than repeatedly reconstructing the same operation.
- Parallelize only independent tasks; excessive parallelism duplicates context and creates conflicting edits.
- Never discard the first meaningful failure merely because later output is shorter.

## Scope And Anti-Over-Engineering

Before adding a layer, abstraction, dependency, service, configuration switch, or broad refactor, require at least one:

- explicit user requirement
- demonstrated duplication of the same knowledge
- current correctness, security, performance, or maintenance need
- established repository pattern that the change must follow

Prefer a local, reversible change when future requirements are hypothetical. Do not refactor adjacent code, add compatibility modes, or create documentation artifacts unless they are required for the requested behavior or safe operation.

Avoid false economy:

- concise code that hides error handling
- one function that mixes unrelated responsibilities merely to reduce lines
- skipped tests or evidence to save time
- summaries that remove qualifiers or uncertainty
- premature abstraction sold as future-proofing

## Compaction And Handoff

Compact when context has substantial repetition, completed phases, superseded hypotheses, or output volume—not after an arbitrary number of turns.

Use this handoff shape:

```markdown
## Goal
## Scope And Constraints
## Verified State
## Decisions
## Files Or Systems Changed
## Validation And Exact Failures
## Remaining Work And Risks
## Next Safe Action
```

Include stable source pointers and distinguish verified facts from inference. Create or update a persistent handoff file only when the user requests it or the repository already uses one.

## Safety

- Never compress away approval requirements, destructive targets, production impact, secret handling, or external side effects.
- Preserve the latest user correction as authoritative and retire superseded scope.
- Do not tell the user to edit old messages, change interfaces, or start a new conversation as a routine optimization.
- Do not claim exact token, speed, or quality improvements without measurement.
- Do not hide uncertainty or fabricate a conclusion to avoid another tool call.

## Verification Checklist

- The active objective and completion criteria remain visible.
- Every retained fact has sufficient evidence or is labeled as an assumption.
- Searches and reads were driven by specific questions.
- Tool output is bounded without losing decisive failures.
- The implementation contains no unrequested abstraction or scope expansion.
- Validation matches the change risk and all failures are reported.
- A compact handoff could reconstruct the next action without replaying the full conversation.

## Trigger Examples

Should trigger:

- “Analyze this large monorepo without filling the context window.”
- “Keep this long debugging session focused and produce a compact handoff.”
- “Review this proposal for over-engineering.”

Should not trigger:

- “Give me the full detailed audit with evidence.”
- “Skip the failing tests to keep the answer short.”
