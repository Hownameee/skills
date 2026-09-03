---
name: ponytail-debt
description: "Collect `ponytail:` comments into a read-only debt ledger containing each deliberate shortcut, its ceiling, and its upgrade trigger. Use for ponytail-debt, deferred-shortcut, or Ponytail-ledger requests; do not modify code or persist the ledger unless the user explicitly asks."
---

# Ponytail Debt

Adapted from `DietrichGebert/ponytail` at commit
`2ed6c52c9d7e5e56942508591085fd45dea277d3`. The MIT notice is in
`../ponytail/LICENSE`.

Collect deliberate Ponytail shortcuts so a deferral cannot quietly become
permanent.

## Scan

Search the repository for comment markers while respecting its ignore rules:

```bash
rg -n '(#|//) ?ponytail:'
```

Add other comment prefixes when the repository's languages require them.
Exclude prose that merely documents the convention.

## Output

Group findings by file and emit one row per marker:

`<file>:<line>, <what was simplified>. ceiling: <named limit>. upgrade: <trigger>.`

The convention is `ponytail: <ceiling>, <upgrade path or trigger>`. Tag any
marker without an actionable upgrade condition as `no-trigger`.

End with `<N> markers, <M> with no trigger.` If none exist, say
`No ponytail: debt. Clean ledger.`

## Boundaries

Read and report only. Use version-control attribution only when requested.
Persist the ledger to a file only after the user explicitly requests that
write.
