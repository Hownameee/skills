---
name: testing_test_strategy
description: "Choose test levels and coverage for a feature, regression, or reliability risk. Use when planning tests, finding coverage gaps, or deciding between unit, integration, contract, and end-to-end checks. For implementation or runner configuration, follow repository conventions and a matching framework skill when available."
---

# Specialist Test Strategy

## 1. Test Purpose

- Start by naming the risk the test reduces.
- Prefer many fast deterministic tests and fewer expensive end-to-end tests.
- Do not add tests that only assert implementation details without protecting behavior.
- Keep tests independent so they can run in any order and in parallel.
- Inspect existing coverage and repository test commands before proposing additions. Select the smallest set that covers the identified risks; do not add redundant tests or expand into unrelated suites.

## 2. Test Levels

- Use small tests for pure logic, validation, serialization, and edge cases.
- Use medium integration tests for database queries, filesystem behavior, queues, caches, framework wiring, and service adapters.
- Use large end-to-end tests for critical user journeys and cross-service contracts.
- Use contract tests when a service boundary is more stable than either implementation.

## 3. Test Quality

- Avoid sleeps; wait on observable conditions with bounded timeouts.
- Avoid real network, real cloud credentials, and shared mutable environments in unit tests.
- Make fixtures minimal and named after the business scenario they represent.
- Assert outputs, state changes, emitted events, and security denials that matter to users.
- Add regression tests for bugs before or alongside the fix when feasible.

## 4. Flakiness

- Treat flaky tests as product defects in the delivery system.
- Quarantine only with an owner, issue, and removal condition.
- Investigate nondeterministic time, order, random data, external services, and leaked state first.
- Do not loosen assertions until the original behavioral requirement is understood.

## 5. Result And Verification

Return the material risks, existing coverage, missing scenarios, suitable test levels, and the narrowest relevant commands. For a planning request, stop at an actionable coverage plan; for implementation, run the affected checks and broaden only for shared behavior, failures, or required repository gates.
