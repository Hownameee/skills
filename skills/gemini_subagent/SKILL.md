---
name: gemini_subagent
description: "Run isolated, ephemeral Antigravity CLI (agy) workers for bounded analysis or parallel subtasks while keeping conversation state out of the orchestrator's home. Use for process-level context isolation and fan-out; use devops_agy_cli for installation, discovery, updates, plugins, or ordinary interactive CLI administration."
---

# Ephemeral Antigravity Sub-Agents

## Scope And Boundary

Use this skill to delegate a bounded task to one or more short-lived `agy` processes. Each worker receives an isolated home directory, prompt, output files, and exit status. This reduces orchestrator context growth; it does not reduce model context within the worker.

Use `devops_agy_cli` for CLI installation, version checks, model or agent discovery, plugin management, updates, and ordinary interactive sessions.

Do not delegate when the task is trivial, requires unresolved user decisions, or cannot be safely bounded. Never broaden the orchestrator's authority: a sub-agent may perform only actions already authorized for the parent task.

## Guarantees And Limits

- On Linux, `/dev/shm` is normally a RAM-backed `tmpfs`; verify it on the current host. Falling back to `/tmp` loses the RAM-backed guarantee.
- Overriding `HOME`, `TMPDIR`, and XDG directories keeps most CLI state beneath the worker root. It does not contain the working directory, OS keyring, network activity, telemetry, system logs, or paths that `agy` accesses explicitly.
- Cleanup traps are best-effort. They run on normal exit and handled signals, but not on `SIGKILL`, power loss, kernel failure, or host termination.
- The installed `agy 1.1.7` requires prompt text as the value of `-p`. Reading a prompt from a file avoids shell-authoring mistakes, but the expanded prompt is still an argument: it may be visible in process listings, is subject to `ARG_MAX`, and loses trailing newlines.
- An empty ephemeral home may have no local model catalog. Do not claim a requested model was used unless resolution is verified in that same environment.
- RAM-backed state can improve local metadata I/O, but model latency and tool execution usually dominate. Measure before claiming a performance gain.

## Preflight

1. Confirm the CLI and current flags:

```bash
command -v agy
agy --version
agy --help
```

2. Define one concrete task, required inputs, allowed directories, expected output, timeout, and success criteria per worker.
3. Separate read-only analysis from edits, external writes, production access, credentials, billing, and destructive work.
4. Use a disposable working tree or copy whenever unintended writes would be unacceptable. Plan mode expresses intent; it is not a write barrier, and an isolated `HOME` alone does not protect the source repository.
5. Keep secrets and private data out of prompts because print-mode prompts are passed through process arguments.
6. Omit `--model` by default. If an exact model is required, verify it with the same ephemeral home and fail when the CLI reports a fallback.
7. Stop if `/dev/shm` or `/tmp` cannot create a private directory, the task needs interactive clarification, or the permission boundary is unresolved.

## Permission Profiles

| Task | Default flags | Requirements |
| --- | --- | --- |
| Explanation or review without tools | `--mode plan --sandbox` | Disposable working directory; no permission bypass |
| Repository analysis | `--mode plan --sandbox --add-dir <validated-path>` | Narrowly scoped directory, required fine-grained read/command rules, and a disposable or read-only copy when writes are unacceptable |
| Edits | `--mode accept-edits --sandbox` | Explicit edit authorization and disposable worktree or copy |
| Automatic tool approval | `--dangerously-skip-permissions` | Separate explicit approval, disposable environment, no production credentials, and documented reason |

Never make `--dangerously-skip-permissions` the default. It auto-approves every tool permission request.

## Single-Worker Pattern

This Bash pattern keeps state and captured output under one validated root. All `agy` flags precede `-p` because `-p` consumes its next argument as the prompt.

```bash
set -u
umask 077

RUN_ROOT=""

cleanup() {
  case "${RUN_ROOT:-}" in
    /dev/shm/agy-subagent.*|/tmp/agy-subagent.*)
      rm -rf -- "$RUN_ROOT"
      ;;
  esac
}

trap cleanup EXIT
trap 'exit 129' HUP
trap 'exit 130' INT
trap 'exit 143' TERM

if [ -d /dev/shm ] && [ -w /dev/shm ]; then
  RUN_ROOT="$(mktemp -d /dev/shm/agy-subagent.XXXXXX)" || {
    printf 'failed to create /dev/shm worker directory\n' >&2
    exit 1
  }
  STORAGE_KIND="tmpfs-candidate"
else
  RUN_ROOT="$(mktemp -d /tmp/agy-subagent.XXXXXX)" || {
    printf 'failed to create /tmp worker directory\n' >&2
    exit 1
  }
  STORAGE_KIND="filesystem-unknown"
fi

mkdir -p \
  "$RUN_ROOT/home" "$RUN_ROOT/tmp" "$RUN_ROOT/work" "$RUN_ROOT/io" \
  "$RUN_ROOT/xdg-config" "$RUN_ROOT/xdg-data" \
  "$RUN_ROOT/xdg-state" "$RUN_ROOT/xdg-cache"

PROMPT_FILE="$RUN_ROOT/io/prompt.txt"
STDOUT_FILE="$RUN_ROOT/io/stdout.txt"
STDERR_FILE="$RUN_ROOT/io/stderr.txt"
EXPECTED_MARKER="WORKER_OK:single"

cat > "$PROMPT_FILE" <<'EOF'
Put WORKER_OK:single on the first output line.
Return a concise, evidence-backed answer to this bounded task.
Do not call tools or modify files. State any missing evidence.
EOF

(
  cd "$RUN_ROOT/work" || exit 70
  exec env \
    HOME="$RUN_ROOT/home" \
    TMPDIR="$RUN_ROOT/tmp" \
    XDG_CONFIG_HOME="$RUN_ROOT/xdg-config" \
    XDG_DATA_HOME="$RUN_ROOT/xdg-data" \
    XDG_STATE_HOME="$RUN_ROOT/xdg-state" \
    XDG_CACHE_HOME="$RUN_ROOT/xdg-cache" \
    agy --mode plan --sandbox --print-timeout 2m \
      -p "$(< "$PROMPT_FILE")"
) > "$STDOUT_FILE" 2> "$STDERR_FILE"
WORKER_STATUS=$?

if [ "$WORKER_STATUS" -eq 0 ]; then
  FIRST_LINE="$(sed -n '1p' "$STDOUT_FILE")"
  if [ "$FIRST_LINE" != "$EXPECTED_MARKER" ]; then
    printf 'worker output contract missing: %s\n' "$EXPECTED_MARKER" >&2
    WORKER_STATUS=65
  fi
fi

cat "$STDOUT_FILE"
if [ -s "$STDERR_FILE" ]; then
  cat "$STDERR_FILE" >&2
fi

printf 'agy worker status=%s storage=%s\n' "$WORKER_STATUS" "$STORAGE_KIND" >&2
exit "$WORKER_STATUS"
```

Add `--add-dir "$TARGET_DIR"` only after resolving and validating the exact directory. Add `--model "$MODEL"` only after the same isolated environment lists or otherwise confirms that model.

## Parallel Fan-Out Pattern

Use one coordinator root, one directory per worker, unique outputs, and individual waits:

```bash
set -u
umask 077

RUN_ROOT=""
PIDS=()
NAMES=(security quality)

cleanup() {
  case "${RUN_ROOT:-}" in
    /dev/shm/agy-fanout.*|/tmp/agy-fanout.*)
      rm -rf -- "$RUN_ROOT"
      ;;
  esac
}

terminate() {
  code="$1"
  trap - HUP INT TERM
  for pid in "${PIDS[@]}"; do
    kill "$pid" 2>/dev/null || true
  done
  for pid in "${PIDS[@]}"; do
    wait "$pid" 2>/dev/null || true
  done
  exit "$code"
}

trap cleanup EXIT
trap 'terminate 129' HUP
trap 'terminate 130' INT
trap 'terminate 143' TERM

if [ -d /dev/shm ] && [ -w /dev/shm ]; then
  RUN_ROOT="$(mktemp -d /dev/shm/agy-fanout.XXXXXX)" || {
    printf 'failed to create /dev/shm coordinator directory\n' >&2
    exit 1
  }
else
  RUN_ROOT="$(mktemp -d /tmp/agy-fanout.XXXXXX)" || {
    printf 'failed to create /tmp coordinator directory\n' >&2
    exit 1
  }
fi

for name in "${NAMES[@]}"; do
  mkdir -p \
    "$RUN_ROOT/$name/home" "$RUN_ROOT/$name/tmp" \
    "$RUN_ROOT/$name/work" \
    "$RUN_ROOT/$name/xdg/config" "$RUN_ROOT/$name/xdg/data" \
    "$RUN_ROOT/$name/xdg/state" "$RUN_ROOT/$name/xdg/cache"
done

cat > "$RUN_ROOT/security/prompt.txt" <<'EOF'
Put WORKER_OK:security on the first output line.
Review this supplied statement without calling tools:
"The service stores authentication tokens in application logs."
Return the concrete security concern and one mitigation.
EOF

cat > "$RUN_ROOT/quality/prompt.txt" <<'EOF'
Put WORKER_OK:quality on the first output line.
Review this supplied requirement without calling tools:
"The pipeline should usually finish quickly and handle bad data."
Return the ambiguities that must be made testable.
EOF

run_worker() {
  name="$1"
  worker="$RUN_ROOT/$name"
  cd "$worker/work" || exit 70
  exec env \
    HOME="$worker/home" \
    TMPDIR="$worker/tmp" \
    XDG_CONFIG_HOME="$worker/xdg/config" \
    XDG_DATA_HOME="$worker/xdg/data" \
    XDG_STATE_HOME="$worker/xdg/state" \
    XDG_CACHE_HOME="$worker/xdg/cache" \
    agy --mode plan --sandbox --print-timeout 2m \
      -p "$(< "$worker/prompt.txt")"
}

for name in "${NAMES[@]}"; do
  run_worker "$name" \
    > "$RUN_ROOT/$name/stdout.txt" \
    2> "$RUN_ROOT/$name/stderr.txt" &
  PIDS+=("$!")
done

OVERALL_STATUS=0
STATUSES=()
for index in "${!PIDS[@]}"; do
  status=0
  wait "${PIDS[$index]}" || status=$?
  name="${NAMES[$index]}"
  if [ "$status" -eq 0 ]; then
    first_line="$(sed -n '1p' "$RUN_ROOT/$name/stdout.txt")"
    if [ "$first_line" != "WORKER_OK:$name" ]; then
      printf 'worker %s output contract missing\n' "$name" >&2
      status=65
    fi
  fi
  STATUSES[$index]="$status"
  if [ "$status" -ne 0 ]; then
    OVERALL_STATUS=1
  fi
done

for index in "${!NAMES[@]}"; do
  name="${NAMES[$index]}"
  printf '=== %s status=%s ===\n' "$name" "${STATUSES[$index]}"
  cat "$RUN_ROOT/$name/stdout.txt"
  if [ -s "$RUN_ROOT/$name/stderr.txt" ]; then
    cat "$RUN_ROOT/$name/stderr.txt" >&2
  fi
done

exit "$OVERALL_STATUS"
```

Do not use `wait "$PID1" "$PID2"` as the only check: Bash reports the status of the last PID and can hide an earlier worker failure.

## Failure Handling

- **No output or non-zero exit:** preserve the worker status and stderr; inspect the temporary CLI log before cleanup when diagnosis is required.
- **Permission request in print mode:** add a narrowly scoped permission or reduce the task. Do not automatically add the dangerous bypass.
- **Exit 0 with a denial, refusal, or empty answer:** require a per-worker completion marker and treat a missing marker as failure.
- **Model fallback or empty model list:** omit the hardcoded model or initialize and verify model metadata in the same isolated home.
- **Outer sandbox blocks a localhost socket:** request authorization for that bounded execution; do not disable unrelated host protections.
- **Prompt near argument limits:** split the task or shorten the prompt. A temporary file does not remove the CLI's argument-size limit.
- **Interrupted fan-out:** terminate known worker PIDs, wait for them, then clean the coordinator root.

## Verification Checklist

- Every worker has a unique home, work directory, prompt, stdout, stderr, and PID.
- All flags appear before `-p`, and the prompt is the single value after `-p`.
- The real `~/.gemini` tree is unchanged when ephemeral execution was intended.
- No coordinator directory or fixed worker result file remains after normal exit.
- Every PID was waited separately and every non-zero status is reported.
- Every successful result begins with its expected completion marker; exit status alone is not accepted as proof of success.
- No tool permission exceeded the parent task's authorization.
- The reported model was verified rather than inferred from the requested flag.
- Any `/tmp` fallback, cache activity, or cleanup limitation is disclosed.

## Output Contract

Return the worker result plus its exit status, task boundary, permission mode, storage type, model-verification status, cleanup result, and any stderr or residual-state caveat. Do not claim zero overhead, zero disk I/O, guaranteed cleanup, or exact model use without direct evidence.

## Trigger Examples

Should trigger:

- "Delegate these three independent code reviews to isolated `agy` workers."
- "Run this large analysis in an ephemeral Antigravity sub-agent."
- "Fan out these bounded research tasks without filling the main context."

Should not trigger:

- "List my Antigravity models and plugins." Use `devops_agy_cli`.
- "Update the `agy` binary." Use `devops_agy_cli`.
- "Run this one short shell command locally." Use the applicable shell or domain workflow.

Should trigger but pause for approval:

- "Run four workers with `--dangerously-skip-permissions` against production." Require separate approval and a safer disposable boundary before execution.
