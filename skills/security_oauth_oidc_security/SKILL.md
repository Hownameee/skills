---
name: security_oauth_oidc_security
description: "Design, implement, review, and test OAuth 2.0 and OpenID Connect clients, authorization servers, resource servers, and provider configuration. Use for login, API authorization, token exchange, service identity, or account linking; do not change production identity-provider settings, rotate secrets, revoke tokens, or migrate flows without explicit authorization."
---

# OAuth 2.0 And OpenID Connect Security

## Scope And Boundaries

- Determine whether the component is an OAuth client, authorization server, OpenID Provider, resource server, gateway, broker, or relying party.
- Keep authentication, delegated authorization, API authorization, application session, and account linking as separate decisions.
- Treat identity-provider dashboards, client registrations, redirect URIs, secrets, signing keys, consent, scopes, roles, and production sessions as high-risk state.
- Ask before changing production provider or client configuration, rotating a secret or key, revoking grants or sessions, changing redirect or logout URIs, or migrating a live flow.

## Preflight

Before implementation or review, record:

1. Client type and ability to protect credentials.
2. User-agent and platform: server-rendered web, SPA, native, desktop, CLI, device, or machine workload.
3. Trusted issuer, discovery document, authorization/token/JWKS/user-info/introspection/revocation endpoints, and supported algorithms.
4. Client IDs, environment-specific redirect and post-logout URIs, response mode, and authentication method.
5. Requested scopes, API audiences/resources, roles or claims, offline access, and consent behavior.
6. Token format and validation owner, application-session storage, cookie policy, refresh-token storage, and logout behavior.
7. Tenant selection, account-linking policy, provider-specific requirements, proxy or load-balancer effects, and rollback.

Do not infer security behavior from provider marketing or SDK defaults. Verify configured and runtime behavior.

## Flow Selection

- Use Authorization Code with PKCE for public browser, native, desktop, and SPA clients. Confidential web clients should also use PKCE when supported.
- Prefer a backend-for-frontend and protected HTTP-only application session for browser applications when architecture permits. If a SPA handles tokens, minimize lifetime and persistent browser storage.
- Use client credentials only for a workload acting as itself, never to represent a user.
- Use device authorization only for devices that genuinely cannot complete a normal browser redirect. Bind the device flow to clear user verification and rate limits.
- Use token exchange only with explicit subject, actor, audience, scope, and delegation policy.
- Do not introduce implicit or resource-owner-password grants. Treat migration from a legacy flow as a separately planned compatibility and session change.

## Authorization Transaction

- Register exact redirect URIs by environment. Avoid wildcards, substring matching, open-redirect chains, and shared development/production callbacks.
- Generate high-entropy `state`, PKCE verifier/challenge, and OIDC `nonce` per transaction; bind them to the initiating browser session, client, issuer, and redirect URI.
- Store concurrent login transactions keyed by `state`; a single global session slot breaks multi-tab and retry behavior.
- Validate error responses with the same transaction binding as successful responses.
- Reject mismatched state, issuer, client, redirect URI, nonce, PKCE verifier, or replayed authorization code.
- Protect against authorization-server mix-up by binding the transaction to the expected issuer and validating the returned issuer where supported.
- For native apps, use an external user agent and platform-appropriate claimed HTTPS, app/universal links, loopback redirects, or collision-resistant custom schemes.

## Token Validation And Use

- Use ID tokens only to authenticate the client session; do not present them to APIs as access tokens.
- Resource servers must validate access tokens according to the issuer's defined profile. Introspect opaque tokens when required; do not assume every token-shaped string is a locally verifiable JWT.
- For ID tokens, enforce an algorithm allowlist and validate signature, exact issuer, audience, authorized party when applicable, expiration, not-before and issued-at bounds, nonce, and transaction context.
- Fetch discovery and JWKS only from the configured trusted issuer over TLS. Do not follow token-controlled key URLs.
- On an unknown key ID, perform a bounded JWKS refresh and fail closed. Prevent attacker-driven refresh storms and retain valid cached keys during normal rotation.
- Apply small, documented clock skew; do not disable lifetime validation.
- Request the minimum scopes and audience. Separate read, write, admin, and offline access.
- Keep public clients free of embedded secrets. Use an appropriate confidential-client authentication method for server clients.

## Token And Session Protection

- Keep access and refresh tokens out of URLs, logs, analytics, crash reports, referrers, source code, and broadly readable browser storage.
- Store refresh tokens server-side or in platform-protected storage appropriate to the client. Rotate refresh tokens and detect reuse when supported.
- Use short-lived access tokens. Consider mTLS, DPoP, or workload identity when bearer-token theft risk warrants sender constraint.
- For cookie sessions, use `Secure`, `HttpOnly`, a flow-compatible `SameSite` policy, CSRF protection, rotation after login, bounded lifetime, and server-side invalidation where required.
- Treat logout from the local application, provider session termination, token revocation, and federated logout as different operations. Do not claim one guarantees the others.

## Identity And Account Linking

- Do not authorize APIs from display claims or group names without a server-controlled mapping and current policy.
- Do not link accounts solely by an email claim, even when verified, unless the provider, tenant, reauthentication, and anti-takeover policy make the link explicit.
- Require step-up authentication for sensitive linking, recovery, privilege, payment, or security-setting changes.
- Define behavior for account switching, tenant switching, consent denial, revoked consent, disabled users, changed email, and deleted upstream accounts.

## Failure Handling And Observability

- Fail closed on validation, transaction, issuer, key, audience, nonce, PKCE, or replay failures.
- Return generic user-facing errors and log structured diagnostic codes, correlation IDs, issuer, client, and safe failure reason.
- Never log tokens, authorization codes, verifiers, client secrets, cookies, or full sensitive claims.
- Rate-limit authorization starts, callbacks, device polling, token exchange, introspection, and recovery paths as appropriate.

## Test Matrix

Include successful and failing integration tests for:

- redirect URI tampering, open-redirect chaining, state/nonce/code replay, and PKCE mismatch;
- issuer mix-up, wrong audience, missing or wrong `azp`, disallowed algorithm, expired/not-yet-valid tokens, unknown keys, and key rotation;
- multi-tab login, callback retries, account switching, tenant switching, consent denial, revoked grants, and logout;
- refresh rotation and reuse, token substitution, ID-token misuse, and scope or audience escalation;
- proxy-host and scheme handling, native redirect collision, cookie/CSRF behavior, and account-link takeover attempts.

Use synthetic clients, users, and tokens outside production. Never weaken validation to make a test fixture pass.

## Completion Checklist

- Client type, flow, issuer, endpoints, redirect URIs, scopes, audiences, token owner, session storage, and account-linking policy are explicit.
- Transaction values are unique, session-bound, single-use, and replay-protected.
- Token signature, issuer, audience, authorized party, lifetime, nonce, algorithm, and key rotation are validated as applicable.
- Tokens, cookies, logs, errors, refresh behavior, logout, and provider failure are covered.
- Negative tests exercise tampering, replay, mix-up, substitution, rotation, and account-linking abuse.
- Production provider, secret, key, grant, redirect, role, and session changes had explicit authorization and a rollback plan.
