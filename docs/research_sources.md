# Documentation Skill Research Sources

This note records the main public sources used to curate the software-engineering documentation skills. It is a source index and rationale note, not a copied template.

## Documentation Best-Practice Sources

- ISO/IEC/IEEE 42010:2022 architecture description overview: <https://www.iso.org/standard/74393.html>
- arc42 architecture documentation template overview: <https://arc42.org/overview>
- C4 model official site: <https://c4model.com/>
- Markdown Architectural Decision Records: <https://adr.github.io/madr/>
- IEEE/ISO/IEC 29148-2018 requirements engineering overview: <https://standards.ieee.org/ieee/29148/6937/>
- Mountain Goat Software user stories guide: <https://www.mountaingoatsoftware.com/agile/user-stories>
- PMI PMBOK guide overview: <https://www.pmi.org/standards/pmbok>
- Google developer documentation style guide: <https://developers.google.com/style>

## Skill And Rule Ecosystem Sources

- OpenAI skill authoring guide: <https://developers.openai.com/codex/skills>
- Open Agent Skills specification: <https://agentskills.io/specification>
- Open Agent Skills best practices: <https://agentskills.io/best-practices>
- Google Antigravity skills guide: <https://antigravity.google/docs/skills>
- Gemini CLI skill best practices: <https://geminicli.com/docs/cli/skills-best-practices/>
- Gemini CLI skill discovery and precedence: <https://geminicli.com/docs/cli/using-agent-skills/>
- OpenAI Codex AGENTS.md discovery: <https://developers.openai.com/codex/guides/agents-md>
- Google Antigravity workspace rules: <https://antigravity.google/docs/ide-rules>

## Rationale

- Keep `docs_technical_documentation` general for README, guide, and API documentation hygiene.
- Add separate skills for architecture docs, ADRs, requirements/use cases, project plans, and engineering design specs because each has different trigger language, structure, and review gates.
- Prefer concise procedural skills over bundled templates to avoid copying licensed standards or public templates verbatim.
- Link to standards and open guidance as source material; encode reusable review behavior in local skills.
- Put activation keywords and nearby exclusions in `description`, because hosts inspect metadata before loading the full skill.
- Keep host-neutral workflows in `SKILL.md` and describe Codex, Gemini CLI, or Antigravity discovery and permission behavior only when verified against current host documentation.
