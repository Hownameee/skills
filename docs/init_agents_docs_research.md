# Init Agents Docs Research Notes

This note records sources used to create `ai_init_agents_docs`.

## Sources

- OpenAI Codex AGENTS.md docs: <https://developers.openai.com/codex/guides/agents-md>
- AGENTS.md open format: <https://agents.md/>
- Google Antigravity Rules docs: <https://antigravity.google/docs/ide-rules>
- Google Antigravity Skills docs: <https://antigravity.google/docs/skills>
- Gemini CLI skill discovery docs: <https://geminicli.com/docs/cli/using-agent-skills/>
- Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?: <https://arxiv.org/abs/2602.11988>
- On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents: <https://arxiv.org/abs/2601.20404>

## Findings

- Codex reads global and project `AGENTS.md` files before work, and supports layering plus nested project instructions.
- Codex supports verification prompts that ask it to summarize loaded instructions and active instruction sources.
- The open AGENTS.md format recommends project overview, build/test commands, code style, testing instructions, security considerations, commit/PR guidance, deployment notes, and nested files for subprojects.
- Antigravity documents workspace rules under `.agents/rules` and workspace skills under `.agents/skills`; its rule activation and precedence model is separate from Codex `AGENTS.md` discovery.
- This repository targets Codex and Antigravity, so the skill should choose the smallest verified host-specific representation instead of assuming both hosts consume the same instruction file.
- Public guidance converges on concise, specific, validated instructions. Long generic instruction files add cost and can reduce reliability.
- Research is mixed: one 2026 study found generated/developer context files can reduce task success when they add unnecessary requirements, while another found AGENTS.md files were associated with lower median runtime and output-token use. The safe default is to document minimal but concrete repo-specific conventions that remove ambiguity without adding generic obligations.
- For software engineering repos, the useful AGENTS.md content is not just commands. It should capture repository structure, backend/frontend flow, state-management layout, naming conventions, generated-file boundaries, safety approvals, verification gates, and git flow.
- Do not claim that Antigravity follows Codex `AGENTS.md` layering or nested-file precedence. Verify the active Antigravity version and rule configuration when generating Antigravity-specific guidance.
