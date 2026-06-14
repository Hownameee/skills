---
name: backend_go_best_practices
description: Go development standards for idiomatic packages, error handling, concurrency, and testing.
---

# Specialist Go Best Practices

## 1. Package Design

- Keep packages small, cohesive, and named for what they provide.
- Avoid package names like `utils`, `common`, or `helpers` unless the existing project already uses them.
- Expose only the API that callers need; keep implementation details unexported.
- Put interfaces at the consumer boundary, not automatically beside implementations.
- Prefer simple functions and structs over premature framework abstractions.

## 2. Error Handling

- Return errors explicitly and handle them at the call site.
- Wrap errors with operation context using `%w` when callers may inspect the cause.
- Do not panic for expected runtime failures.
- Keep error messages lowercase and without trailing punctuation unless the project differs.
- Check cleanup errors when cleanup can affect data integrity.

## 3. Concurrency

- Use goroutines only when there is a clear ownership, cancellation, and synchronization model.
- Pass `context.Context` as the first parameter for request-scoped work.
- Respect context cancellation in IO, database, queue, and long-running loops.
- Close channels only from the sender side.
- Avoid shared mutable state; protect it with synchronization or channel ownership.

## 4. Testing

- Prefer table-driven tests for input/output variations.
- Use `t.Helper()` in test helpers.
- Run race-sensitive code with `go test -race` when feasible.
- Keep unit tests independent, deterministic, and free of network dependencies.
- Use integration tests for real database, filesystem, or external service behavior.

## 5. Formatting And Tooling

- Run `gofmt` or `go fmt` on all edited Go files.
- Use `go test ./...` for broad verification unless the repo has a narrower documented command.
- Use `go vet` or the project lint target when changing exported APIs, concurrency, or unsafe code.
