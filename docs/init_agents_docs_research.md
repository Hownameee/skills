# Init Agents Docs Research Notes

This note records sources used to create `ai_init_agents_docs`.

## Sources

- OpenAI Codex AGENTS.md docs: <https://developers.openai.com/codex/guides/agents-md>
- AGENTS.md open format: <https://agents.md/>
- Agent Skills best practices: <https://agentskills.io/best-practices>

## Findings

- Codex reads global and project `AGENTS.md` files before work, and supports layering plus nested project instructions.
- The open AGENTS.md format recommends setup commands, build/test commands, code style, security considerations, and nested files for subprojects.
- This repository targets Codex and Antigravity only, so the skill should not generate other agent-specific files unless the user changes that scope later.
- Public guidance converges on concise, specific, validated instructions. Long generic instruction files add cost and can reduce reliability.
