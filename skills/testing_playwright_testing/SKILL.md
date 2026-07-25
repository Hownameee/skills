---
name: testing_playwright_testing
description: "Create, review, or debug Playwright API tests using the repository's existing Playwright configuration, built-in request fixture, and test conventions. Use when an existing Playwright suite must verify HTTP/API behavior. Do not use for browser UI tests or to add Playwright, schema libraries, or plugins unless the user explicitly requests that change."
---

# Specialist Playwright API Testing

## 1. Scope And Modes

Use this skill for:

- **Create:** Add focused API tests to an existing Playwright suite.
- **Review:** Find correctness, isolation, coverage, and reliability defects.
- **Debug:** Reproduce and classify a failing API test before changing it.

Route browser interaction and visual/end-to-end UI testing to the frontend testing skill. Do not replace the project's established API-test framework merely because Playwright is available.

## 2. Preflight Discovery

Before editing tests:

1. Inspect package manifests, lockfiles, Playwright version, configuration, projects, fixtures, and current API tests.
2. Identify JavaScript versus TypeScript, module system, test location, naming, and repository test command.
3. Resolve `baseURL`, authentication, headers, web-server lifecycle, timeouts, retries, parallelism, and target environment.
4. Read the API contract and implementation or existing integration tests for the behavior under test.
5. Identify data ownership, cleanup APIs, rate limits, tenant boundaries, and whether tests may run concurrently.

Use the repository's existing package manager and dependencies. Never install a plugin, Zod, or another production/test dependency without explicit approval.

## 3. Request Client Selection

- Prefer Playwright's built-in `request` fixture for ordinary isolated API tests.
- The built-in `request` fixture provides an isolated `APIRequestContext` for each test and Playwright manages its teardown.
- Use `playwright.request.newContext()` or an imported `request.newContext()` only when a separately configured context or explicit lifecycle is required; always dispose it in teardown.
- A manual context retains response bodies until the response or context is disposed. Dispose large responses after use in a long-lived context.
- Reuse a repository fixture when it already provides authentication, tenant selection, tracing, or cleanup.
- Use a schema validator only when it is already part of the project or the user approved adding it.
- Do not import undocumented fixtures such as `api` unless the repository defines them.

Keep credentials in approved environment or fixture configuration. Never hardcode tokens, cookies, private URLs, or production accounts.

## 4. Test Design Workflow

### Step 1: Define The Contract Under Test

For each case, identify:

- Method, path, authentication, and authorization role.
- Request headers, path/query values, and body.
- Expected status, content type, headers, and body.
- State change and observable side effects.
- Retry, idempotency, pagination, or eventual-consistency behavior.

Test public behavior rather than internal function calls.

### Step 2: Build A Risk-Based Matrix

Cover applicable cases:

| Class | Examples |
| --- | --- |
| Success | Valid create, read, update, delete |
| Validation | Missing, malformed, boundary, unknown field |
| Authentication | Missing, expired, malformed credential |
| Authorization | Wrong role, tenant, or object owner |
| Conflict | Duplicate, stale version, invalid state |
| Protocol | Content type, redirects, caching, status, headers |
| Resilience | Timeout, retry, idempotency, rate limit |
| Collection | Empty, page boundary, stable order, invalid cursor |

Do not multiply cases that exercise the same behavior without additional risk coverage.

### Step 3: Isolate Data

- Create unique test data; include worker identity or a generated identifier when tests run in parallel.
- Do not rely on execution order, shared mutable fixtures, or production-like seed records unless the suite guarantees them.
- Create prerequisites through stable APIs or existing fixtures.
- Track created identifiers and clean them in `finally` or fixture teardown.
- Make cleanup narrowly scoped and verify it when deletion matters.
- Never use arbitrary sleeps. Poll an observable condition with a bounded timeout for eventual consistency.

### Step 4: Assert Precisely

- Assert the exact documented status rather than only `response.ok()`.
- Check relevant content type and protocol headers before parsing.
- Assert required response fields, types, values, and absence of sensitive fields.
- Validate a schema at runtime when the project already uses a schema library.
- Assert side effects through a public read path when that behavior is part of the contract.
- Include enough response context in failures without logging credentials or private payloads.

## 5. Valid Built-In Fixture Example

Adapt names, fields, status codes, and cleanup behavior to the actual contract:

```typescript
import { randomUUID } from 'node:crypto';
import { test, expect } from '@playwright/test';

test('creates and returns a user', async ({ request }, testInfo) => {
  const email = `pw-${testInfo.parallelIndex}-${randomUUID()}@example.test`;
  let userId: string | undefined;

  try {
    const response = await request.post('/api/users', {
      data: { name: 'Playwright Test', email },
    });

    const contentType = response.headers()['content-type']?.toLowerCase() ?? '';
    const body: unknown = contentType.includes('application/json')
      ? await response.json()
      : undefined;

    // Capture cleanup identity before assertions so a contract failure does
    // not leave a successfully created resource behind.
    if (typeof body === 'object' && body !== null && !Array.isArray(body)) {
      const record = body as Record<string, unknown>;
      if (typeof record.id === 'string') userId = record.id;
    }

    expect(response.status()).toBe(201);
    expect(contentType).toContain('application/json');
    expect(body).toEqual(expect.objectContaining({
      id: expect.any(String),
      email,
    }));
  } finally {
    if (userId) {
      const cleanup = await request.delete(`/api/users/${userId}`);
      expect(cleanup.status(), 'test-created user cleanup failed').toBe(204);
    }
  }
});
```

Do not copy this example blindly. If the API returns numeric identifiers, requires a tenant header, or uses a different deletion contract, follow the real schema.

## 6. Debugging Workflow

1. Run the narrowest failing test with the repository's configured command.
2. Capture the assertion, status, safe response metadata, and relevant server logs.
3. Classify the failure as product behavior, contract drift, environment/configuration, test data, timing, authentication, or test defect.
4. Reproduce without retries before changing the test.
5. Fix the owning layer; do not weaken an assertion merely to make CI green.

Use retries to expose flakiness in CI policy, not to hide deterministic defects.

## 7. Safety And Edge Cases

- Default to local, test, or explicitly approved staging environments.
- Never point destructive API tests at production.
- Do not start external services, modify shared environments, or create billable resources without authorization.
- Redact authorization headers, cookies, secrets, and sensitive response fields from traces and reports.
- Consider redirect behavior, compressed/empty bodies, invalid JSON, large payloads, rate limits, clock skew, asynchronous completion, duplicate cleanup, partial setup failure, and cross-tenant access.

Stop when the target environment, destructive scope, authentication source, or cleanup ownership is unresolved.

## 8. Verification Checklist

- Run the repository's formatter/linter/typecheck for the changed test when available.
- Run the narrowest affected Playwright test, then the relevant project or suite.
- Confirm the test passes without relying on retries.
- Confirm parallel execution does not collide when the suite supports it.
- Verify setup and cleanup leave no shared state.
- Review traces, reports, and failure output for secrets or private data.
- Confirm no dependencies or configuration were changed unintentionally.

If execution is unavailable, report the exact command and missing environment or dependency.

## 9. Output Contract

Return tests or review findings, behavior covered, environment assumptions, commands run, failures classified, cleanup behavior, skipped validation, and residual coverage risk.
