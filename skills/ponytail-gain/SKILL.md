---
name: ponytail-gain
description: "Display Ponytail's upstream benchmark claims as a compact, read-only scoreboard with explicit source and non-repository caveats. Use only for ponytail-gain, Ponytail impact, or Ponytail scoreboard requests; do not estimate savings for the current repository or present upstream claims as independently verified current measurements."
---

# Ponytail Gain

Adapted from `DietrichGebert/ponytail` at commit
`2ed6c52c9d7e5e56942508591085fd45dea277d3`. The MIT notice is in
`../ponytail/LICENSE`.

Display the following upstream scoreboard when invoked. It is a one-shot,
read-only response and must not change mode or persist state.

The figures are claims bundled with the imported Ponytail snapshot, based on
its benchmark medians across five tasks and three models. They are not an
independent measurement, a current external verification, or a result for the
user's repository. Source methodology:
`https://github.com/DietrichGebert/ponytail/tree/2ed6c52c9d7e5e56942508591085fd45dea277d3/benchmarks`.

## Scoreboard

```text
  ponytail gain                upstream benchmark · 5 tasks · 3 models

  Lines of code   no-skill  ████████████████████  100%
                  ponytail  ██▌·················    6–20%   ▼ 80–94%
  Cost            no-skill  ████████████████████  100%
                  ponytail  █████▌··············   23–53%  ▼ 47–77%
  Speed           ponytail  ▸ 3–6× faster

  This repo:  @ponytail-debt  shortcuts explicitly deferred
              @ponytail-audit complexity that may still be removable
```

## Honesty Boundary

Never invent per-repository savings. The unbuilt alternative was not measured,
so there is no valid baseline to subtract. Preserve the upstream qualification
and source whenever displaying the card.

## Boundaries

One-shot display only. Do not edit files, change a mode, or persist state.
