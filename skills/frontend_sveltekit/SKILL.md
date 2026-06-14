---
name: frontend_sveltekit
description: SvelteKit rules for load functions, form actions, server-only code, routing, progressive enhancement, security, and deployment.
---

# Specialist SvelteKit

## 1. Scope

Use this skill when building or reviewing SvelteKit routes, layouts, load functions, form actions, endpoints, server-only modules, stores, progressive enhancement, or deployment adapters.

## 2. Routing And Data Loading

- Keep route ownership clear: `+page`, `+layout`, `+server`, and endpoint files should each have a narrow reason to exist.
- Use server load functions for private data, secrets, cookies, and trusted backend calls.
- Use universal load only for data that is safe to serialize to the client.
- Avoid duplicating fetches across layouts, pages, and components.
- Return typed, minimal data from load functions rather than entire backend objects.

## 3. Forms And Mutations

- Prefer form actions for server-side mutations and progressive enhancement when the workflow fits HTML forms.
- Validate all form data on the server, including fields that are hidden or client-validated.
- Model expected validation failures as user-visible form errors.
- Use redirects after successful state-changing form submissions when that prevents duplicate posts.
- Add idempotency or duplicate-submit protection for payments, emails, webhooks, and external side effects.

## 4. Server And Client Boundaries

- Keep secrets, private environment variables, database clients, and privileged SDKs in server-only modules.
- Do not import server-only modules into client-reachable code.
- Treat anything returned from load functions or embedded in page data as client-visible.
- Be explicit about cookie flags, path, SameSite, secure, and HTTP-only behavior.
- Review adapter-specific deployment behavior for edge runtimes, Node APIs, file access, and environment variables.

## 5. Security

- Authorize every server action and endpoint by actor, tenant, resource, and state transition.
- Do not trust route params or form values for ownership.
- Sanitize rich HTML and avoid unsafe rendering of user-controlled markup.
- Keep CSRF, CORS, cookie auth, and origin checks aligned with the deployment model.
- Avoid leaking stack traces, secrets, or internal data through error pages and action responses.

## 6. Testing And Operations

- Test load functions, actions, redirects, cookies, auth failures, and progressive enhancement paths.
- Add end-to-end tests for navigation, form validation, offline or JavaScript-disabled behavior where relevant.
- Monitor server errors, failed actions, auth denials, and adapter-specific runtime failures.
- Keep dependencies and adapters current.
- Verify production build output for accidental client exposure of private modules or environment variables.
