---
name: backend_node_typescript_backend
description: Node.js and TypeScript backend standards for secure, reliable production services.
---

# Specialist Node.js & TypeScript Backend

## 1. Runtime And Project Structure

- Use TypeScript for production application code unless the project is intentionally JavaScript-only.
- Keep transport handlers thin; place business logic in services and persistence in repositories or data-access modules.
- Prefer explicit runtime configuration from environment variables with validation at startup.
- Use `npm ci`, `pnpm install --frozen-lockfile`, or equivalent lockfile-enforcing installs in CI.
- Do not mix package managers in one project.

## 2. Async And Reliability

- Never leave promises unhandled.
- Use request-scoped cancellation or timeout control for database calls, HTTP clients, queues, and long-running work.
- Do not block the event loop with CPU-heavy work, large synchronous file IO, or unbounded JSON processing.
- Add process-level handling for graceful shutdown, connection draining, and background worker stop signals.
- Bound concurrency for batch jobs and external API calls.

## 3. Security

- Validate all request inputs at the boundary with a schema library or framework validator.
- Configure HTTP timeouts, body size limits, upload limits, and rate limits.
- Do not run the inspector in production.
- Avoid `eval`, dynamic `Function`, shell string construction, and unsafe deserialization.
- Use constant-time comparison for secrets, tokens, and signatures where available.
- Treat npm packages as trusted code only after review; avoid packages with install scripts unless required.

## 4. API And Data

- Return structured errors with stable codes and safe messages.
- Avoid leaking stack traces or framework errors to clients.
- Use parameterized database queries or ORM query builders.
- Keep transactions short and scoped to the consistency boundary.
- Log request identifiers, actor identifiers, and domain event names without logging secrets or full sensitive payloads.

## 5. Testing

- Cover pure logic with fast isolated tests.
- Add integration tests for database queries, queues, external API adapters, and serialization contracts.
- Mock time, randomness, and external services explicitly.
- Do not make unit tests depend on network access, real cloud credentials, or wall-clock sleeps.
