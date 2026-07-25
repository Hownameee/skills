---
name: devops_env_setup
description: "Diagnose and load the repository-selected Node.js runtime and package manager in non-interactive shells. Use when node, npm, npx, yarn, pnpm, Corepack, or Node-based Git hooks are unavailable or use the wrong version; do not install runtimes, change global defaults, or bypass hooks without explicit approval."
---

# Node.js Environment Setup

## Scope And Boundaries

- Use this skill only to make an existing repository-selected runtime available to the current shell.
- Prefer the runtime manager, version file, and package manager already selected by the repository.
- Do not install Node.js, a runtime manager, Corepack, or a package manager; download a runtime; change a global default; edit shell startup files; or bypass Git hooks without explicit user approval.
- Do not use this skill when Node.js is already available at the required version and the command is failing for an application, dependency, or test reason.

## Preflight

Before changing `PATH` or loading a manager:

1. Capture the original error and distinguish `command not found`, wrong version, package-manager mismatch, missing dependency, and hook failure.
2. Inspect repository guidance and the nearest relevant files:
   - `.nvmrc`, `.node-version`, `.tool-versions`, and `mise.toml`
   - `package.json` fields such as `engines`, `packageManager`, and Volta configuration
   - `package-lock.json`, `npm-shrinkwrap.json`, `pnpm-lock.yaml`, `yarn.lock`, and manager configuration files
   - `.husky/`, `core.hooksPath`, and package scripts when Git hooks are involved
3. Check the current shell without mutating it:

   ```bash
   command -v node
   command -v npm
   node --version
   npm --version
   ```

4. Detect existing managers with `command -v volta`, `command -v fnm`, `command -v asdf`, `command -v mise`, and a check for an existing NVM loader. Do not assume that NVM is installed.
5. Stop and report a conflict when version files disagree or the requested runtime is not installed. Do not silently select the lexicographically latest directory.

## Manager Selection

Use the strongest repository signal in this order:

1. A manager-specific project configuration, such as Volta configuration or `mise.toml`.
2. A project version file supported by an already-installed manager.
3. The package manager declared by `packageManager`.
4. Existing repository documentation.

When multiple installed managers can satisfy the same version, use the one explicitly configured by the repository. Do not initialize every manager in one shell.

### NVM

Load NVM from its configured directory or the conventional per-user directory without hardcoding a username:

```bash
export NVM_DIR="${NVM_DIR:-"$HOME/.nvm"}"
[ -s "$NVM_DIR/nvm.sh" ] || { echo "nvm.sh not found at $NVM_DIR" >&2; exit 1; }
. "$NVM_DIR/nvm.sh"
nvm use
<actual-command>
```

`nvm use` must resolve a repository version or an already-selected version. Do not replace it with directory globbing, `ls | tail`, or an implicit "latest" version.

### Other Managers

- With Volta, use its existing shim or `volta run -- <actual-command>` when the project declares a Volta toolchain.
- With fnm, initialize fnm for the current shell using the command recommended for that shell, then select the repository version.
- With asdf or mise, use the repository version through `asdf exec <actual-command>` or `mise exec -- <actual-command>`.
- Use Corepack only when it is already available and the repository declares a compatible `packageManager`. Do not activate a different package manager than the lockfile implies.

Use the shell syntax appropriate to the active platform. Do not copy Bash initialization into PowerShell, cmd.exe, or another incompatible shell.

## Git Hooks

- Inspect hook ownership before committing: `.husky/`, `git config --get core.hooksPath`, and relevant package scripts.
- Run `git commit` from the same initialized environment used to verify Node.js and the package manager.
- Never use `--no-verify`, delete a hook, edit a hook to suppress a failure, or replace the repository's runtime version merely to make a commit pass.
- If the hook fails after the runtime is available, preserve its exit code and diagnose the hook or project failure instead of treating it as an environment problem.

## Failure Handling

- **Runtime absent:** report the required version and detected managers; request approval before installation.
- **Wrong runtime:** show the expected and actual versions and select only an already-installed compatible version.
- **Package-manager mismatch:** follow the declared manager and lockfile; do not regenerate a lockfile with another manager.
- **Shim or PATH conflict:** report `command -v` results and load only the selected manager for the current command.
- **Container or CI failure:** fix the container image or workflow setup rather than relying on a developer's personal shell initialization.

## Post-Execution Checklist

- `command -v node` and `node --version` match the repository requirement.
- The selected package-manager executable and version match `packageManager`, the lockfile, and repository documentation.
- The original command ran exactly once in the corrected environment and its exit status was preserved.
- Git hooks ran normally when applicable.
- No runtime, global default, startup file, lockfile, or dependency was changed unless the task explicitly required and authorized it.
- Report the manager and version used, the command outcome, and any unresolved setup requirement.
