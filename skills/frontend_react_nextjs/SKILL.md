---
name: frontend_react_nextjs
description: Next.js 14 App Router, React, and TypeScript development standards.
---

# Specialist React & Next.js 14

## 1. Core Principles

- **TypeScript First:** Use TypeScript for all code. Prefer `interfaces` over `types`. Avoid `enums`, use maps instead.
- **Functional Paradigm:** Use functional, declarative programming. Avoid classes. Use the "function" keyword for pure functions.
- **Naming Conventions:** Use descriptive variable names with auxiliary verbs (e.g., `isLoading`, `hasError`). Use lowercase with dashes for directories (e.g., `components/auth-wizard`).
- **RORO Pattern:** Use the Receive an Object, Return an Object pattern for complex functions.

## 2. Component Architecture

- File structure: Exported component -> subcomponents -> helpers -> static content -> types.
- Favor named exports for components.
- Minimize `'use client'`, `useEffect`, and `useState`. Heavily favor React Server Components (RSC).
- Wrap client components in `Suspense` with a proper fallback.
- Use `Shadcn UI`, `Radix`, and `Tailwind CSS` for styling. Use mobile-first responsive design.

## 3. Next.js App Router Rules

- Rely on Next.js App Router for state changes and routing.
- **Server Actions:** Use `next-safe-action` for all server actions. Implement type-safe actions with `Zod` schema validation.
- Model expected errors as return values in Server Actions rather than throwing `try/catch`. Use `useActionState` to manage errors.
- Use error boundaries (`error.tsx`, `global-error.tsx`) for unexpected errors.

## 4. Control Flow & Error Handling

- Handle errors and edge cases at the very beginning of functions (Guard Clauses).
- Use early returns to avoid deeply nested if-statements.
- Place the "happy path" at the very end of the function.
- Omit curly braces for simple single-line conditional statements.
