---
name: testing_frontend_testing
description: Frontend testing rules for Cypress, Playwright, Vitest, Testing Library, selectors, isolation, secrets, and reliable UI tests.
---

# Specialist Frontend Testing

## 1. Scope

Use this skill when writing or reviewing frontend unit, component, integration, or end-to-end tests using Cypress, Playwright, Vitest, Testing Library, or similar browser-focused test tools.

## 2. Test Intent

- Test user-observable behavior before implementation details.
- Choose the smallest test type that proves the behavior: unit, component, integration, API, or end-to-end.
- Keep end-to-end tests for critical workflows, routing, auth, browser integration, and regressions that lower-level tests cannot prove.
- Avoid snapshot-only tests for behavior that needs explicit assertions.
- Make failure messages point to the broken user outcome.

## 3. Selectors And Interactions

- Prefer accessible role, label, text, and user-facing queries when they express the behavior under test.
- Use stable `data-*` test selectors when text or roles are not the intent of the test.
- Do not bind tests to generated classes, styling selectors, brittle DOM depth, or framework internals.
- Use real user interactions where practical instead of directly mutating component state.
- Avoid arbitrary sleeps; wait on observable UI state, network events, or framework-supported retry behavior.

## 4. Isolation And State

- Keep tests independent and safe to run in any order.
- Reset database, storage, cookies, local state, feature flags, and mocked services intentionally.
- Programmatically create authenticated state when UI login is not the behavior under test.
- Avoid testing third-party sites directly; mock, contract-test, or use controlled test tenants.
- Keep clocks, network mocks, and service workers scoped to each test.

## 5. Secrets And Test Data

- Never hardcode passwords, tokens, API keys, or private test data in specs.
- Keep sensitive values in CI secret stores or environment mechanisms that do not expose them to browser context.
- Use synthetic users and fixtures with clear ownership and cleanup.
- Redact videos, screenshots, traces, logs, and reports when they can contain sensitive data.
- Do not commit generated artifacts that include cookies, storage state, traces, or credentials.

## 6. CI Reliability

- Run critical tests in CI with deterministic browser, viewport, locale, timezone, and network assumptions.
- Quarantine flaky tests only with an owner and repair plan.
- Keep retries limited and visible; retries should not hide deterministic bugs.
- Capture artifacts that help debugging without leaking secrets.
- Track test duration and split suites by risk and runtime.
