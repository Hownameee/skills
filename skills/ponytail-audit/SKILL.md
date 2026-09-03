---
name: ponytail-audit
description: "Audit an entire repository for over-engineering and return a ranked list of code, dependencies, wrappers, configuration, and abstractions that can be deleted or replaced with standard-library or native features. Use for ponytail-audit, repository bloat, or whole-codebase simplification requests; do not apply fixes or replace correctness, security, or performance audits."
---

# Ponytail Audit

Adapted from `DietrichGebert/ponytail` at commit
`2ed6c52c9d7e5e56942508591085fd45dea277d3`. The MIT notice is in
`../ponytail/LICENSE`.

Apply the Ponytail review across the whole repository rather than only the
current diff. Scan selectively, support every finding with a source location,
and rank the largest defensible reduction first.

## Tags

- `delete:` dead code, unused flexibility, or a speculative feature; replacement is nothing.
- `stdlib:` hand-rolled behavior already provided by the standard library; name the function.
- `native:` code or a dependency duplicating a platform feature; name the feature.
- `yagni:` an abstraction with one implementation, configuration nobody sets, or a layer with one caller.
- `shrink:` the same required behavior expressed more clearly with less code; show the shorter form.

## Hunt

Look for dependencies duplicating standard or platform features,
single-implementation interfaces, factories with one product, wrappers that
only delegate, dead feature flags and configuration, and hand-rolled standard
library behavior. Confirm usage before calling anything dead.

## Output

Use `<tag> <what to cut>. <replacement>. [path:line]`, one line per finding.
End with `net: -<N> lines, -<M> dependencies possible.` Treat these as review
estimates. If nothing can be defensibly cut, say `Lean already. Ship.`

## Boundaries

This is a read-only complexity audit. Correctness bugs, security holes, and
performance problems are out of scope and should be routed to specialist
passes. Do not apply findings without an explicit implementation request.
