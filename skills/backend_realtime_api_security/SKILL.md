---
name: backend_realtime_api_security
description: WebSocket and gRPC security rules for transport, authentication, message validation, authorization, limits, and monitoring.
---

# Specialist Realtime API Security

## 1. Scope

Use this skill when implementing or reviewing WebSocket, Socket.IO, server-sent event alternatives, gRPC, streaming RPC, bidirectional APIs, realtime collaboration, notification channels, or service-to-service RPC.

## 2. Transport And Handshake

- Use TLS for production realtime traffic; use mTLS for service-to-service gRPC where trust boundaries require it.
- Validate WebSocket `Origin` headers and reject unexpected origins during handshake.
- Do not rely on cookies alone for WebSocket security; protect against cross-site WebSocket hijacking.
- Authenticate during connection establishment and revalidate when sessions expire, rotate, or are revoked.
- Disable gRPC reflection, debug endpoints, and broad service discovery in production unless protected.

## 3. Message Authorization

- Authorize each message or RPC method by actor, tenant, channel, resource, and operation.
- Do not assume an authenticated connection can perform every message type for its lifetime.
- Re-check authorization when subscribing to rooms, topics, streams, or object-specific channels.
- Prevent clients from choosing arbitrary server-side method names, topics, service names, or internal routes.
- Ensure disconnect, logout, role change, and account disablement terminate or downgrade active connections.

## 4. Validation And Limits

- Validate every inbound message against a schema, including type, size, nesting, enum values, and business rules.
- Set maximum message size, stream duration, queue depth, fanout, subscription count, and request rate.
- Apply timeouts and deadlines for gRPC calls, long-running streams, and backend work triggered by messages.
- Protect against replay, duplicate actions, ordering bugs, and client-controlled sequence numbers.
- Reject binary or compressed payloads unless decompression limits and content validation are explicit.

## 5. Error Handling And Observability

- Return minimal protocol errors; do not expose stack traces, internal service names, database errors, or policy details.
- Log connection lifecycle, auth failures, origin failures, rate limits, protocol errors, abnormal disconnects, and authorization denials.
- Avoid logging full message bodies, tokens, cookies, session IDs, PII, or secrets.
- Track per-user and per-tenant connection counts, message rates, dropped messages, and backpressure.
- Add tests for unauthorized subscription, cross-tenant channel access, CSWSH, oversized messages, replay, and stale session use.
