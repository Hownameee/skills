---
name: backend_api_design
description: "Design or review REST and HTTP API contracts for resources, methods, errors, pagination, compatibility, security, and client ergonomics. Use when creating or changing an HTTP/JSON API or its OpenAPI contract. Do not use for GraphQL schemas, WebSocket/gRPC protocols, or language-specific implementation details."
---

# Specialist REST API Design

## 1. Scope And Modes

Use this skill in one of three modes:

- **Design:** Produce a new API contract from confirmed requirements.
- **Change:** Extend an existing contract while protecting current clients.
- **Review:** Identify contract defects and recommend precise corrections without changing code unless requested.

For GraphQL, WebSocket, gRPC, or handler implementation, use a matching protocol or language skill when available. Otherwise follow the repository's established implementation and testing conventions; do not assume this checkout contains those skills.

## 2. Preflight Discovery

Before proposing endpoints:

1. Read the current OpenAPI or equivalent schema, routes, handlers, authorization policy, and contract tests.
2. Identify consumers, supported versions, compatibility promises, authentication method, rate limits, and deployment constraints.
3. Confirm the business resources, caller goals, authorization subjects, tenant boundaries, expected cardinality, and retry behavior.
4. Separate verified facts, assumptions, and unresolved choices. Ask only when a missing choice materially changes the public contract.
5. Check repository conventions for naming, error envelopes, pagination, timestamps, identifiers, and deprecation.

Do not invent consumers, fields, permissions, service limits, or compatibility guarantees.

## 3. Contract Workflow

### Step 1: Model Resources And Operations

- Model stable business resources rather than service methods or database tables.
- Prefer plural noun paths and HTTP methods: `GET /orders/{order_id}`.
- Use action subresources only when an operation cannot be represented as resource state, for example `POST /orders/{order_id}/cancellations`.
- Keep nesting shallow. Use a top-level resource or filter when ownership is not the only access path.
- Define identifier format and normalization. Never expose sequential internal identifiers when that creates an enumeration risk.

For each operation, record:

| Field | Required decision |
| --- | --- |
| Purpose | Caller goal and business outcome |
| Request | Path, query, headers, body, limits |
| Response | Status, headers, body schema |
| Authorization | Subject, action, object, tenant |
| Errors | Stable code and retry semantics |
| Compatibility | Existing clients and migration |
| Operations | Rate limit, timeout, observability |

### Step 2: Select HTTP Semantics

- `GET` and `HEAD` must be safe; `PUT` and `DELETE` must be idempotent.
- Use `201 Created` with `Location` for synchronous resource creation.
- Use `202 Accepted` plus an operation-status resource for asynchronous work.
- Use `204 No Content` only when no response representation is useful.
- Distinguish `400` malformed input, `401` missing/invalid authentication, `403` denied authorization, `404` hidden or absent resources, `409` state conflict, `412` failed precondition, `422` semantically invalid input, and `429` throttling.
- Document redirect behavior, content types, cache headers, and retry metadata when applicable.

Do not return `200` for every outcome or encode failures only inside a success body.

### Step 3: Define Input And Output Contracts

- Validate type, format, range, length, enum, cross-field rules, and unknown fields at the boundary.
- Allowlist writable fields to prevent mass assignment.
- Use one documented timestamp format and timezone convention.
- Define optional, nullable, absent, and defaulted fields separately.
- Keep error responses stable and machine-readable. Include a stable application code, human-safe detail, request correlation identifier, and field errors when applicable.
- Never expose stack traces, SQL errors, framework internals, credentials, or private upstream payloads.

Example error shape:

```json
{
  "code": "order_state_conflict",
  "message": "The order cannot be cancelled in its current state.",
  "request_id": "req_01J...",
  "errors": [{"path": "status", "reason": "must_be_pending"}]
}
```

### Step 4: Bound Collections

- Bound page size, filters, sort fields, expansions, search expressions, and response size.
- Prefer cursor pagination for large or changing collections.
- Use a deterministic order with a unique tie-breaker.
- Bind cursors to the effective filter, sort, tenant, and authorization context; make them opaque and tamper-resistant.
- Document first, next, empty, deleted-between-pages, and invalid/expired cursor behavior.
- Reject unsupported or excessively expensive filters instead of silently ignoring them.

### Step 5: Handle Retries, Concurrency, And Caching

- Require idempotency keys for retryable non-idempotent operations such as payments, imports, orders, and provisioning.
- Define key scope, retention, request fingerprinting, replay response, in-flight behavior, and conflicting reuse.
- Use entity versions, `ETag`/`If-Match`, or an equivalent precondition for lost-update risks.
- Define cacheability, `Cache-Control`, validators, invalidation, and authorization-aware cache keys.
- For asynchronous operations, expose state, progress when reliable, terminal errors, cancellation rules, retention, and polling guidance.

### Step 6: Apply Security And Abuse Controls

- Enforce object-level and function-level authorization server-side on every operation.
- Apply tenant constraints in the data-access path, not only in request filters.
- Filter response fields according to caller permissions.
- Bound request bodies, uploads, batch sizes, expansions, and execution time.
- Validate filenames and media types; scan or isolate untrusted uploads as required by the system threat model.
- Authenticate webhooks, prevent replay, define delivery identifiers, and document retry ordering and deduplication.
- Treat third-party responses and callback URLs as untrusted input.

### Step 7: Preserve Compatibility

- Prefer additive optional changes.
- Treat required fields, removed fields, narrower enums, changed defaults, status changes, error-code changes, and semantic changes as potentially breaking.
- When deprecating, define replacement, notice mechanism, telemetry, migration window, sunset date, and removal owner.
- Do not create a new version until compatibility cannot be preserved safely.

## 4. Edge Cases And Fail-Fast Rules

Explicitly decide behavior for empty collections, duplicates, partial batch failure, stale writes, deleted resources, repeated retries, upstream timeouts, ambiguous dates, unknown enum values, long-running work, and cross-tenant identifiers.

Stop and escalate when authorization ownership, destructive semantics, externally relied-on behavior, or a breaking-change migration is unresolved.

## 5. Verification Checklist

- Validate the contract with the repository's existing OpenAPI/schema command.
- Inspect the generated or rendered contract diff for accidental breaking changes.
- Run existing contract and handler tests.
- Test success, malformed input, authentication failure, authorization failure, absent object, state conflict, rate limit, retry, and pagination boundaries.
- Confirm examples conform to the schema and documented status codes match runtime behavior.
- Confirm logs and error payloads do not expose secrets or private data.

If a command cannot be run, name the missing dependency or environment and the exact repository command to run later.

## 6. Output Contract

For design or change work, return:

1. Confirmed requirements and assumptions.
2. Endpoint/operation table.
3. Request, response, error, authorization, and compatibility decisions.
4. OpenAPI or equivalent contract changes.
5. Migration/deprecation plan when needed.
6. Validation performed and residual risks.

For review work, report findings by severity with operation, evidence, client impact, and a concrete correction.
