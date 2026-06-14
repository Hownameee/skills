---
name: backend_api_design
description: REST and HTTP API design rules for resource modeling, compatibility, security, and client ergonomics.
---

# Specialist API Design

## 1. Contract First

- Define or update the API contract before implementing endpoints.
- Use OpenAPI or an equivalent schema for request bodies, response bodies, error shapes, auth requirements, and status codes.
- Treat API docs as a product surface, not a post-implementation note.
- Preserve backwards compatibility unless the task explicitly authorizes a breaking change.

## 2. Resource Modeling

- Model stable business resources, not internal service methods.
- Use nouns for resource paths and HTTP methods for actions.
- Keep URLs normalized: no trailing slash variants, empty path segments, or action verbs when a resource model is possible.
- Use plural collection names consistently.
- Avoid deeply nested paths when a query parameter or top-level resource is clearer.

## 3. Requests And Responses

- Validate all input at the boundary.
- Return precise HTTP status codes and documented error payloads.
- Never expose stack traces, SQL errors, framework internals, or secrets in API responses.
- Use cursor pagination for large or mutable collections.
- Use idempotency keys for retryable unsafe operations such as payment, order, import, and provisioning flows.
- Document rate limits and return `429` with useful retry metadata when throttling.

## 4. API Security

- Enforce object-level authorization on every endpoint that accepts an object identifier.
- Enforce function-level authorization for admin, billing, export, moderation, and account-management actions.
- Prevent mass assignment by allowlisting writable fields.
- Apply response filtering so clients cannot infer or receive unauthorized object properties.
- Bound request size, page size, nested expansion, and expensive filters.
- Treat third-party API responses as untrusted input.

## 5. Versioning And Deprecation

- Prefer compatible additive changes over version forks.
- When deprecating, document replacement paths, sunset dates, and usage monitoring.
- Do not remove fields, change semantics, or alter error contracts without a migration plan.
