---
name: testing_test_strategy
description: Test strategy rules for unit, integration, end-to-end, contract, and regression coverage.
---

# Specialist Test Strategy

## 1. Test Purpose

- Start by naming the risk the test reduces.
- Prefer many fast deterministic tests and fewer expensive end-to-end tests.
- Do not add tests that only assert implementation details without protecting behavior.
- Keep tests independent so they can run in any order and in parallel.

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
