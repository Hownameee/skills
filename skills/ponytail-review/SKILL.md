---
name: ponytail-review
description: "Review the current diff exclusively for over-engineering, including removable code, reinvented standard-library behavior, unnecessary dependencies, speculative abstractions, and dead flexibility. Use for ponytail-review, simplify-review, or what-can-we-delete requests; do not use as a correctness, security, or performance review."
---

# Ponytail Review

Adapted from `DietrichGebert/ponytail` at commit
`2ed6c52c9d7e5e56942508591085fd45dea277d3`. The MIT notice is in
`../ponytail/LICENSE`.

Review the current diff for unnecessary complexity. Report what to cut and
what, if anything, replaces it. Do not apply fixes unless the user separately
asks for implementation.

## Format

Use `<file>:L<line>: <tag> <what>. <replacement>.` One line per finding,
ranked by the largest defensible reduction first.

Tags:

- `delete:` dead code, unused flexibility, or a speculative feature; replacement is nothing.
- `stdlib:` hand-rolled behavior already provided by the standard library; name the function.
- `native:` code or a dependency duplicating a platform feature; name the feature.
- `yagni:` an abstraction with one implementation, configuration nobody sets, or a layer with one caller.
- `shrink:` the same required behavior expressed more clearly with less code; show the shorter form.

## Scoring

End with `net: -<N> lines possible.` Treat the number as an estimate based on
the proposed changes, not a measured result. If nothing can be defensibly cut,
say `Lean already. Ship.`

## Boundaries

This skill covers complexity only. Route correctness defects, security issues,
and performance problems to their specialist reviews. Never flag required
validation, security controls, accessibility, or the repository's smallest
meaningful verification check as bloat.
