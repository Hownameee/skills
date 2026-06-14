# Init Agents Docs Research Notes

This note records sources used to create `ai_init_agents_docs`.

## Sources

- OpenAI Codex AGENTS.md docs: <https://developers.openai.com/codex/guides/agents-md>
- AGENTS.md open format: <https://agents.md/>
- Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?: <https://arxiv.org/abs/2602.11988>
- On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents: <https://arxiv.org/abs/2601.20404>

## Findings

- Codex reads global and project `AGENTS.md` files before work, and supports layering plus nested project instructions.
- Codex supports verification prompts that ask it to summarize loaded instructions and active instruction sources.
- The open AGENTS.md format recommends project overview, build/test commands, code style, testing instructions, security considerations, commit/PR guidance, deployment notes, and nested files for subprojects.
- This repository targets Codex and Antigravity only, so the skill should not generate other agent-specific files unless the user changes that scope later.
- Public guidance converges on concise, specific, validated instructions. Long generic instruction files add cost and can reduce reliability.
- Research is mixed: one 2026 study found generated/developer context files can reduce task success when they add unnecessary requirements, while another found AGENTS.md files were associated with lower median runtime and output-token use. The safe default is to document minimal but concrete repo-specific conventions that remove ambiguity without adding generic obligations.
- For software engineering repos, the useful AGENTS.md content is not just commands. It should capture repository structure, backend/frontend flow, state-management layout, naming conventions, generated-file boundaries, safety approvals, verification gates, and git flow.
- No stable public Antigravity-specific AGENTS.md documentation surfaced in the search. Keep output standard Markdown AGENTS.md-compatible and scoped to Codex/Antigravity unless the user provides Antigravity-specific behavior.
