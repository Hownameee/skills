---
name: security_oauth_oidc_security
description: OAuth 2.0 and OpenID Connect security rules for flows, clients, tokens, redirect URIs, scopes, and session binding.
---

# Specialist OAuth & OIDC Security

## 1. Scope

Use this skill when implementing or reviewing OAuth 2.0, OAuth 2.1-style flows, OpenID Connect, social login, API authorization, token exchange, service integrations, or identity-provider configuration.

## 2. Flow Selection

- Use Authorization Code with PKCE for browser, native, SPA, desktop, and other public clients.
- Do not use the implicit grant for new code; migrate existing `response_type=token` flows.
- Use client credentials only for machine-to-machine use cases, never for user delegation.
- Use device authorization only when the device genuinely cannot support a browser-based redirect.
- Keep identity authentication decisions separate from API authorization decisions.

## 3. Redirects, State, And Nonce

- Register exact redirect URIs; avoid wildcards, open redirects, and environment-sharing redirect endpoints.
- Generate high-entropy `state` per authorization request and bind it to the browser session.
- Use OIDC `nonce` when processing ID tokens and bind it to the transaction that initiated login.
- Validate issuer, audience, expiration, signature, algorithm, and key ID for every token.
- Reject authorization responses that do not match the initiating client, redirect URI, state, nonce, and PKCE verifier.

## 4. Tokens And Scopes

- Request the minimum scopes needed and separate read, write, admin, and offline access.
- Store refresh tokens only in server-side or platform-protected storage appropriate to the client type.
- Prefer short-lived access tokens and rotate refresh tokens where the provider supports it.
- Do not put access tokens in URLs, logs, analytics, crash reports, local storage, or referrer-leaking contexts.
- Use sender-constrained tokens, mTLS, DPoP, or workload identity where token theft risk is material.

## 5. Client And Provider Configuration

- Treat public clients as unable to keep secrets; do not ship client secrets in frontend or mobile code.
- Enforce PKCE at the authorization server when supported.
- Disable unused grant types, response types, redirect URIs, and legacy compatibility settings.
- Verify provider-specific defaults for consent, refresh token lifetime, token audience, and group or role claims.
- Test logout, account switching, expired sessions, revoked consent, rotated keys, and replayed authorization codes.

## 6. Failure Handling

- Fail closed on token validation, issuer mismatch, missing state, PKCE mismatch, or unknown signing keys.
- Use generic user-facing auth errors while logging structured server-side diagnostics.
- Do not auto-link accounts solely by unverified email address.
- Protect callback endpoints with CSRF and replay defenses.
- Add integration tests for redirect tampering, state replay, token audience confusion, and stale JWKS cache behavior.
