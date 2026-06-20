---
name: devops_env_setup
description: Environment setup rules to load Node.js/npm via nvm and configure PATH in non-interactive agent shells (e.g., for running npm commands or committing with husky hooks).
---

# Environment Setup and Node.js Runtime Configuration

## 1. Scope

Use this skill when running Node.js, npm, npx, yarn, pnpm commands, or Git actions (like `git commit` which might trigger husky hooks) that require Node.js, and the command fails or might fail due to `node` or `npm` not being found in the default non-interactive PATH.

## 2. Auto-Detecting and Sourcing NVM

In non-interactive agent shell sessions (like those created by `run_command` without sourcing profile scripts), `nvm` and `node` are typically not loaded. You must automatically locate and source nvm from the user's home directory.

To ensure Node.js is available:

- **Check Home Directory**: Look for nvm installation directory at `$HOME/.nvm` (typically `/home/nam/.nvm` on this system).
- **Source NVM Script**: Prepend your terminal command with NVM sourcing logic.

### Canonical Loading Command

```bash
export NVM_DIR="$HOME/.nvm" && [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" && <actual_command>
```

Replace `<actual_command>` with the command you need to run (e.g., `npm install`, `npm run dev`, or `git commit -m "..."`).

## 3. Handling Husky and Pre-commit Hooks

Husky and other git hooks depend on the environment from which `git commit` is executed. If `git commit` is run without Node.js in the PATH, the husky hooks will fail with errors like `command not found: node`.

When running git commits in repositories that use husky:

1. **Always** check if the repository uses git hooks (e.g. check for a `.husky` directory, `husky` in `package.json`, or `.git/hooks`).
2. If hooks are present, prepend the `git commit` command with the NVM loading script:

   ```bash
   export NVM_DIR="$HOME/.nvm" && [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" && git commit -m "..."
   ```

## 4. Alternative: Prepending Node bin to PATH

If sourcing `nvm.sh` is too slow or causes issues in some commands, you can manually locate the node bin folder and prepend it to `PATH`:

1. Find installed Node versions under `$HOME/.nvm/versions/node/`.
2. Locate the default/latest bin folder, e.g. `$HOME/.nvm/versions/node/v20.11.0/bin` (or use wildcards/variables if scripting).
3. Prepend it to the PATH variable:

   ```bash
   export PATH="$HOME/.nvm/versions/node/$(ls -1 $HOME/.nvm/versions/node/ | tail -n 1)/bin:$PATH" && <command>
   ```
