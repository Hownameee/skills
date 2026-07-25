---
name: devops_git_workflow
description: "Inspect and safely change Git repository state through exact staging, atomic commits, amendments, and pushes. Use when the user asks to inspect Git changes, stage, commit, amend, push, or otherwise change history; do not create or rewrite history, discard changes, bypass hooks, or contact a remote unless the user authorizes that action."
---

# Git Workflow Rules

## Scope And Authority

- If the user writes `commit` in the request, read and apply this skill before taking Git actions.
- Treat inspection, staging, committing, amending, pushing, rebasing, resetting, and force-pushing as different actions. Authorization for one does not authorize the others.
- A request to `commit and push` authorizes the resulting ordinary commit and non-force push, but not an amend, rebase, reset, merge, conflict resolution that discards work, or force-push.
- Do not stage or commit unrelated user changes. Preserve unknown work and stop if it cannot be separated safely.
- Never use destructive commands such as `git reset --hard`, `git clean`, or checkout-based file restoration unless the exact destructive operation and target are explicitly authorized.

## Preflight

Run read-only checks from the repository root before staging or changing history:

```bash
git rev-parse --show-toplevel
git status --short --branch
git branch --show-current
git diff --
git diff --cached --
git log --oneline -n 10
```

- Detect detached `HEAD`, an in-progress merge, rebase, cherry-pick, or revert, unresolved conflicts, and unexpected staged files.
- Attribute each changed and untracked path to the requested task before including it.
- Inspect relevant repository instructions, ignore rules, contribution guidance, and existing commit history.
- If another process or user changes an in-scope file during the task, reread and reconcile it before staging.

## Build The Commit

1. Group only logically coupled changes. Keep independently reversible work in separate commits when the request authorizes all of it.
2. Run the narrowest meaningful formatter, linter, test, typecheck, or build before staging.
3. Stage exact paths:

   ```bash
   git add -- <path> [<path>...]
   ```

   Avoid `git add -A`, `git add .`, and broad globs unless the user explicitly wants every reviewed change included.

4. Review the exact candidate commit:

   ```bash
   git diff --cached --stat
   git diff --cached --
   git diff --cached --check
   ```

5. Check for secrets, private keys, tokens, credentials, production data, unexpectedly large binaries, dependency directories, build output, caches, and editor files.
6. Commit with hooks enabled. Do not use `--no-verify`, alter hooks, or suppress failing checks.

## Commit Contents

- Follow repository policy for generated files and lockfiles; neither category is universally included or excluded.
- Commit application lockfiles such as `package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`, or equivalent when the approved dependency graph changes and the repository tracks them.
- Do not hand-edit generated lockfiles. Use the repository's selected package manager and inspect the resulting diff.
- Include generated source, migrations, snapshots, or artifacts only when they are canonical project outputs required by the change.
- Do not create or broaden `.gitignore` merely because it is absent. Change ignore rules only when required by the task and after verifying that they will not hide intended source files.
- Never stage `.env` files, private keys, tokens, raw credentials, or confidential data.

## Commit Message

- Match the clear convention in recent repository history, including scope, casing, and subject style.
- When no convention is evident, use a concise imperative subject or an appropriate Conventional Commit prefix.
- Describe why the change exists; do not claim tests, behavior, or files that are not in the staged diff.
- Do not create an empty commit unless the user explicitly requests it.

## Amend And History Rewrites

- Amend only when the user explicitly asks to amend and the exact target commit is confirmed.
- Before amending, verify the current `HEAD`, inspect its contents, and determine whether it has been pushed or may be shared.
- Treat rebase, reset, commit replacement, and force-push as history rewrites requiring explicit authorization.
- Never amend another contributor's commit merely to keep history tidy.

## Push Workflow

Push only when the user explicitly requests it:

1. Inspect the configured remotes and current branch.
2. Determine the upstream and ahead/behind state. Do not invent a remote or branch.
3. Stop on detached `HEAD`, unexpected divergence, missing credentials, protected-branch rejection, or a non-fast-forward result. Do not automatically pull, merge, rebase, or switch branches.
4. Use an ordinary push. Force-push requires separate explicit approval; when approved, prefer `--force-with-lease` over `--force`.
5. Do not claim the push succeeded until the command succeeds and the remote branch is confirmed.

## Post-Execution Verification

```bash
git show --stat --oneline --decorate HEAD
git status --short --branch
```

- Confirm the committed paths and message match the requested scope.
- Confirm no intended change was left staged accidentally and no unrelated change was included.
- Report the branch, commit hash, commit subject, validation performed, hook result, push result if requested, and any remaining working-tree changes.
