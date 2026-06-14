---
name: backend_graphql_security
description: GraphQL API security rules for schema design, resolver authorization, query limits, and production configuration.
---

# Specialist GraphQL Security

## 1. Scope

Use this skill when implementing, reviewing, or testing GraphQL schemas, resolvers, clients, gateways, or GraphQL-backed API features.

## 2. Schema And Input Design

- Model input with explicit schema types, enums, custom scalars, and mutation input objects.
- Validate all resolver arguments with allowlists and domain constraints before using them in database, HTTP, filesystem, shell, or search calls.
- Do not pass user-controlled identifiers into downstream URLs, query builders, shell commands, or file paths without strict normalization and authorization.
- Keep public schema fields intentionally minimal; do not expose internal IDs, admin-only fields, or convenience traversal paths without a use case.
- Prefer opaque pagination cursors over raw offsets or database identifiers.

## 3. Resolver Authorization

- Enforce authorization in resolvers or shared policy layers, not only at the UI or route boundary.
- Check object-level access for every node returned from a query, including nested fields loaded through relationships.
- Treat mutations as privileged state changes: validate actor, target object, tenant, role, and state transition.
- Avoid resolver shortcuts that bypass service-layer authorization used by REST or internal APIs.
- Add regression tests for IDOR, cross-tenant access, admin-only fields, and unauthorized nested traversal.

## 4. Availability Controls

- Set depth, breadth, result count, and timeout limits for all public GraphQL operations.
- Require pagination on list fields and cap `first`, `last`, `limit`, or equivalent arguments.
- Use query cost or complexity analysis when the graph has expensive nested relationships.
- Apply rate limits by actor and source, and protect batching endpoints from brute-force or credential stuffing patterns.
- Use server-side batching and caching to reduce duplicate backend calls, but never cache across tenants or authorization contexts.

## 5. Production Configuration

- Disable or restrict introspection and GraphiQL-style explorers in production unless explicitly required and protected.
- Return stable, minimal errors to clients; log detailed resolver errors server-side with request correlation.
- Do not expose stack traces, SQL fragments, internal service names, or authorization policy details in GraphQL responses.
- Review third-party GraphQL plugins for default introspection, upload, tracing, and federation behavior.
- Verify changes with security tests that include malicious depth, excessive limits, invalid IDs, and unauthorized nested fields.
