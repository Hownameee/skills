---
name: ponytail-help
description: "Show a concise reference for the installed Ponytail skills, their activation names, intensity levels, and standalone-versus-plugin behavior. Use for ponytail-help, Ponytail commands, or how-to-use-Ponytail requests; do not activate a persistent mode or modify configuration."
---

# Ponytail Help

Adapted from `DietrichGebert/ponytail` at commit
`2ed6c52c9d7e5e56942508591085fd45dea277d3`. The MIT notice is in
`../ponytail/LICENSE`.

Display this reference when invoked. It is a one-shot response and does not
write files, change configuration, or persist mode state.

## Levels

| Level | Request | Behavior |
| --- | --- | --- |
| **lite** | `use ponytail lite` | Build what was requested and name a materially simpler alternative. |
| **full** | `use ponytail` | Enforce the YAGNI, existing-code, standard-library, native, and minimum-code ladder. Default. |
| **ultra** | `use ponytail ultra` | Challenge speculative requirements and prefer deletion while honoring explicit requirements. |

In this standalone installation, the requested level applies to the current
task. Persistent levels, environment configuration, and automatic lifecycle
injection require the upstream Ponytail plugin.

## Skills

| Skill | Codex activation | Purpose |
| --- | --- | --- |
| **ponytail** | `@ponytail` | Produce the smallest correct implementation. |
| **ponytail-review** | `@ponytail-review` | Review the current diff for removable complexity. |
| **ponytail-audit** | `@ponytail-audit` | Audit the whole repository for removable complexity. |
| **ponytail-debt** | `@ponytail-debt` | Collect `ponytail:` shortcut comments into a ledger. |
| **ponytail-gain** | `@ponytail-gain` | Display the qualified upstream benchmark card. |
| **ponytail-help** | `@ponytail-help` | Display this reference. |

Hosts may also activate a skill from a matching natural-language request.
Slash-command syntax and exact discovery behavior depend on the host.

## Plugin-Only Features

The upstream plugin adds persistent `lite`, `full`, `ultra`, and `off` modes,
lifecycle hooks, subagent injection, environment/config defaults, and host
plugin update commands. Those features are intentionally not part of this
skill-only import.

Upstream documentation: `https://github.com/DietrichGebert/ponytail`.

## Boundaries

Help only. Do not change modes, configuration, or files.
