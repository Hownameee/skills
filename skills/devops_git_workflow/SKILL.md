---
name: devops_git_workflow
description: Best practices and rules for Git workflows.
---

# Git Workflow Rules

## 1. Context Verification Before Actions

- **ALWAYS** check the current state before modifying history or pushing code.
- Run `git status` to see unstaged/staged files.
- Run `git branch` to ensure you are on the correct branch.
- Run `git diff` to review your own changes before creating a commit.

## 2. Commit Conventions (Conventional Commits)

- Use standard prefixes:
  - `feat:` (new feature for the user)
  - `fix:` (bug fix for the user)
  - `docs:` (changes to the documentation)
  - `style:` (formatting, missing semi colons, etc; no production code change)
  - `refactor:` (refactoring production code, e.g. renaming a variable)
  - `test:` (adding missing tests, refactoring tests)
  - `chore:` (updating grunt tasks etc; no production code change)
- Keep messages concise and imperative (e.g., "feat: add user login" NOT "added user login").
- **Check Project History:** ALWAYS run `git log --oneline -n 10` before committing to observe and match the specific commit message conventions, formatting, or prefixes previously used in the repository.

## 3. Atomic Commits

- Do not lump unrelated changes into a single commit.
- If you fix a bug and add a feature, split them into two commits.
- **Use `--amend` for minor fixes:** If you just made a commit and realize you made a tiny typo or linting error, use `git commit --amend --no-edit` instead of creating a new "fix typo" commit, to keep the history clean.

## 4. Security & Exclusions

- **NEVER** commit `.env` files, `.pem` keys, API keys, or any sensitive credentials.
- **NEVER** commit auto-generated files, dependencies, or build directories. Examples: `package-lock.json`, `target/`, `venv/`, `__pycache__/`, `node_modules/`, etc.
- **ALWAYS** verify that a `.gitignore` exists. If it does not exist, you MUST create it and add the above directories/files before committing.
- Only commit source code and files that are absolutely necessary.
