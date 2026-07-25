---
name: devops_agy_cli
description: "Inspect and administer the Antigravity agy CLI, including version and help output, models, agents, projects, plugins, updates, headless modes, permissions, and troubleshooting. Use for ordinary CLI management; use gemini_subagent for RAM-backed ephemeral or parallel worker orchestration."
---

# Antigravity CLI Operations

## Scope And Boundary

Use this skill to inspect, configure, update, and troubleshoot the `agy` executable and its normal persistent environment.

Use [`gemini_subagent`](../gemini_subagent/SKILL.md) when the primary goal is process-level context isolation, a temporary `HOME`, best-effort cleanup, or parallel worker fan-out. Do not duplicate that orchestration here.

## Operating Modes

| Mode | Examples | Authority |
| --- | --- | --- |
| Inspection | Version, help, models, agents, plugin list | May run when relevant; disclose cache refreshes |
| Headless prompt | `-p`, model, agent, project, mode, sandbox, timeout | Must match task and permission scope |
| Local configuration | Settings, shell integration, plugin enable/disable | Requires explicit request when state changes |
| Installation or update | `agy install`, `agy update`, plugin import/install/uninstall | Requires explicit approval |

Never treat permission to inspect the CLI as permission to update it, install plugins, change settings, create projects, or run an autonomous task.

## Preflight

1. Inspect the installed binary and current syntax before composing commands:

```bash
command -v agy
agy --version
agy --help
```

2. Identify the current working directory, intended project, requested agent/model, execution mode, timeout, and whether tools or file edits are allowed.
3. Read current CLI output instead of relying on remembered flags or model names; the CLI changes independently of this repository.
4. Do not override `HOME` for ordinary inventory. A fresh home can have empty model, agent, project, and plugin metadata.
5. Treat `~/.gemini/antigravity-cli/` as persistent user state. Do not delete, replace, migrate, or copy its conversations, settings, or credentials without explicit authorization.

## Read-Only Inventory

```bash
agy models

agy agents

agy plugin list
```

An empty list is not proof that no models or agents exist. Check whether `HOME` was overridden, onboarding is incomplete, the project is unresolved, authentication is unavailable, or metadata refresh failed.

`agy changelog` may refresh persistent cache data. Run it only when release information is needed and cache writes are acceptable.

## Headless Prompt Execution

Use the least-privileged mode that satisfies the task:

```bash
agy --mode plan --sandbox --print-timeout 2m \
  -p "Start with AGY_OK, then answer concisely without tools or file changes."
```

Place every flag before `-p`; the validated CLI treats the next argument after `-p` as the prompt. It does not accept a missing `-p` argument from stdin. Recheck this behavior after upgrading `agy`.

For a multiline prompt, author it in a private temporary file, then expand it as the final argument. This reduces shell-quoting mistakes but does not hide the prompt from process listings or remove argument-size limits:

```bash
umask 077
PROMPT_FILE=""

cleanup_prompt() {
  case "${PROMPT_FILE:-}" in
    /tmp/agy-prompt.*)
      rm -f -- "$PROMPT_FILE"
      ;;
  esac
}

trap cleanup_prompt EXIT
trap 'exit 129' HUP
trap 'exit 130' INT
trap 'exit 143' TERM

PROMPT_FILE="$(mktemp /tmp/agy-prompt.XXXXXX)" || {
  printf 'failed to create prompt file\n' >&2
  exit 1
}

cat > "$PROMPT_FILE" <<'EOF'
Analyze the supplied evidence.
Return findings, confidence, and validation limits.
Do not modify files or external state.
EOF

agy --mode plan --sandbox --print-timeout 2m \
  -p "$(< "$PROMPT_FILE")"
```

Use `--model` only after `agy models` confirms the exact identifier in the relevant environment. If exact model selection matters, inspect stderr or the CLI log and fail when the CLI reports a fallback.

Do not accept exit status alone as proof of task success. Headless mode can soft-deny a required tool and still exit 0. Require an output marker or another task-specific result check, then reject missing, denied, refused, or empty results.

## Projects And Workspace Scope

- Use the current directory only when it is the intended trusted workspace.
- Use `--project <id>` only for a confirmed existing project.
- `--new-project` creates persistent state and requires an explicit request.
- Add directories with repeatable `--add-dir <path>` only after resolving the exact paths and confirming their read/write scope.
- For autonomous edits, prefer a disposable worktree or copy and verify the diff afterward.

## Permissions And Sandbox

- `--mode plan` changes agent behavior; it is not a security boundary.
- `--sandbox` enables terminal restrictions; verify that the installed platform supports them.
- Fine-grained permission rules should grant only the required files, commands, URLs, or MCP tools.
- `--dangerously-skip-permissions` auto-approves every tool permission request. Use it only after separate explicit approval, inside a disposable environment without production credentials or sensitive mounts.
- A headless permission denial is a signal to narrow the task or add one scoped rule, not to default to blanket approval.

## Plugins, Installation, And Updates

- `agy plugin list` and `agy plugin validate <path>` are inspection operations.
- `plugin import`, `install`, `uninstall`, `enable`, and `disable` change persistent state. Confirm the exact plugin and requested action first.
- Inspect third-party plugin source, provenance, requested capabilities, and bundled skills or MCP servers before installation.
- `agy install` can change environment paths or shell configuration.
- `agy update` changes the executable. Run it only when requested, after recording the current version and reviewing the available release information.
- Never claim an update or plugin action succeeded until the resulting version or plugin state is verified.

## Troubleshooting

| Symptom | Check | Response |
| --- | --- | --- |
| `agy` not found | `command -v agy`, shell `PATH` | Report the expected path; do not install without approval |
| Empty models or agents | `HOME`, onboarding, auth, project metadata | Restore the intended persistent environment or initialize explicitly |
| Localhost socket denied | Outer sandbox or container network policy | Request bounded authorization; do not disable unrelated protections |
| Non-zero print result | Exit status, stderr, `--log-file` output | Classify auth, model, server, permission, or transport failure |
| Model fallback | `agy models`, stderr, CLI log | Omit the model or fail closed when an exact model is required |
| Tool denied in print mode | Fine-grained permission and task scope | Add one scoped rule or reduce the task |
| Exit 0 but no usable answer | Output marker and denial text | Treat the task as failed; do not publish the result |
| Persistent state unexpected | `~/.gemini/antigravity-cli/`, project selection | Stop and identify the writer before cleanup |

## Verification Checklist

- The binary path, version, and current help were recorded.
- The command used the intended project, agent, model, mode, sandbox, and timeout.
- Flags appeared before `-p`, with exactly one prompt argument.
- Tool permissions matched the user's authority.
- State-changing plugin, install, update, or project operations were explicitly authorized.
- Exit status, stdout, stderr, and relevant log output were checked.
- A task-specific output marker or equivalent semantic result check passed.
- Requested model selection and resulting persistent state were verified.
- Any skipped execution, model fallback, sandbox limitation, or residual state was reported.

## Output Contract

Report the binary version, command purpose, project/workspace, execution and permission modes, exit status, relevant output, persistent changes, and validation limits. Redact credentials, account data, private prompts, and sensitive paths.

## Trigger Examples

Should trigger:

- "List the models and agents available in my `agy` installation."
- "Diagnose why `agy -p` exits without output."
- "Review this Antigravity plugin before installing it."
- "Update the Antigravity CLI and verify the installed version."

Should not trigger:

- "Run three isolated `agy` code-review workers in parallel." Use `gemini_subagent`.
- "Keep this sub-agent's conversation database in `/dev/shm`." Use `gemini_subagent`.
- "Use the Gemini API directly from this service." Use the applicable API-development workflow.

Should trigger but pause for approval:

- "Install this third-party `agy` plugin and update the CLI." Confirm both state-changing actions, inspect the plugin, and record the current version first.
