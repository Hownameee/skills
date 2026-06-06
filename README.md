# Antigravity AI Agent Skills 🚀

Welcome to the **Antigravity AI Agent Skills** repository! This project serves as a comprehensive, production-grade set of guidelines, rules, and best practices designed to make AI coding agents (like Antigravity, Cursor, Claude Code) smarter, more disciplined, and highly token-efficient.

These rules have been meticulously researched and adapted from top global standards (including `awesome-cursorrules`, `fabric`, and `agent-skills-standard`) to prevent AI hallucinations, stop over-engineering, and enforce clean code practices.

## 📁 Repository Structure

The skills are modularized into 6 core files, each targeting a specific domain of AI operation:

### 1. 🧠 [reasoning_and_context.md](./reasoning_and_context.md)

**Core Philosophy:** *Think before you type.*

- Forces the AI to use "Planning Mode" for complex tasks.
- Implements "Virtual Whiteboarding" and "Deep Thinking" to map out edge cases before execution.
- Prevents hallucinated API calls by checking dependencies (`package.json`, `pom.xml`) first.
- Introduces the `re-gen` UI Bug Recovery protocol.

### 2. ⚡ [token_and_focus_optimization.md](./token_and_focus_optimization.md)

**Core Philosophy:** *Simplicity and Efficiency.*

- **YAGNI (You Aren't Gonna Need It):** Strict bans on over-engineering and unsolicited refactoring.
- **Observation Masking:** Prevents raw JSON/log dumps from polluting the context window.
- **Context Compaction:** Forces the AI to routinely compress its memory to maintain focus.
- **CTFC Framework:** Adheres to Context, Task, Format, and Constraints rigidly.

### 3. 🧹 [code_quality.md](./code_quality.md)

**Core Philosophy:** *Clean, secure, and maintainable.*

- **Strict Commenting:** Only document *business logic* (the "Why"), never the "How".
- **Fail Fast:** Never swallow errors; always log with context.
- **Security Standards:** Prevent SQL injections, sanitize outputs (XSS), and avoid hardcoding magic numbers.

### 4. 🗂️ [file_operations.md](./file_operations.md)

**Core Philosophy:** *Transparent and Verifiable.*

- Forces the AI to use native UI Replacement tools instead of silent background scripts (`sed`/`awk`).
- **Preserve Formatting:** Respects original tabs, spaces, and quote styles.
- **Immediate Verification:** Mandates linting, building, and testing immediately after any modification.

### 5. 🐳 [docker.md](./docker.md)

**Core Philosophy:** *Secure and slim deployments.*

- Enforces multi-stage builds and lightweight bases (`alpine`/`slim`).
- Strictly bans running containers as `root`.
- Mandates resource cleanup (`--rm`, `docker system prune`) and proper `HEALTHCHECK` instructions.

### 6. 🐙 [git_github.md](./git_github.md)

**Core Philosophy:** *Clean history and secure commits.*

- Enforces Conventional Commits (`feat:`, `fix:`, `chore:`).
- Strictly prevents committing generated files (`node_modules/`, `target/`) and forces `.gitignore` verification.
- Recommends using `git commit --amend` for minor fixes to keep the commit history clean.

## 🛠️ How to Use

If you are using an AI agent capable of reading local directories, simply instruct it with:

> *"Please read and strictly follow all the rules defined in the `skills` directory before starting any task."*

The AI will absorb these guidelines and immediately upgrade its behavior, writing cleaner code and drastically reducing its token usage.
