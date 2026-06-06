---
description: Code quality and strict commenting standards across all file types.
---

# Code Quality & Documentation Standards

## 1. Commenting Rules (Strict)

- **Focus on Business Logic (The "Why"):** Comments must only explain the underlying **business logic** or the high-level system execution flow. Why does this exist?
- **Do NOT explain the code (The "What" & "How"):** Never write comments explaining what a function does or how the syntax works. Let the code explain itself. If the user needs an explanation, write it in the chatbot chatbox, not in the source file.
- **Keep it concise:** Comments should be as short as possible, ideally restricted to a **single line**.
- **No decorative noise:** STRICTLY AVOID decorative symbols or separator blocks in comments (e.g., `// ============`, `/* ### */`, `# --------`).
- **Self-documenting code:** Use clear, descriptive variable and function names. If code requires a comment to explain its mechanics, refactor the code instead.

## 2. Function Size & Single Responsibility

- **Keep it small:** A function should not exceed 30 lines of code. If it is longer, you MUST break it down into smaller, descriptive sub-functions.
- **Single Responsibility Principle (SRP):** A function should do exactly one thing and do it well.
- **Intention vs. Implementation:** The function's name should describe *what* it does, while the body handles *how* it does it.

## 3. Error Handling (Fail Fast)

- **Never swallow errors:** Empty `catch` blocks or simply ignoring errors are strictly forbidden. The `catch (e)` block must always log the error with proper context or re-throw it.
- **Provide Context:** When throwing or logging an error, include meaningful information (e.g., what failed, the parameters used, and why).
- **Fail Fast:** Validate inputs and throw errors as early as possible to prevent confusing side effects later in the execution flow.
- **Avoid returning Null for errors:** Do not return `null` to indicate a failure; throw a proper exception instead so the caller is forced to handle it.

## 4. Naming Conventions

- **Reveal Intent:** Variable and function names must be self-explanatory (why it exists, what it does).
- **No abbreviations:** Do NOT use single-letter variables (`a`, `b`, `x`, `y`) except for standard loop indices (`i`, `j`). Use `daysSinceLastUpdate` instead of `d`.
- **Consistency:** Use a consistent vocabulary across the codebase (e.g., do not mix `fetchUser`, `getUser`, and `retrieveUser`).
- **No Magic Numbers/Strings:** Do not hardcode numbers or strings directly into the logic. Extract them into clearly named constants (e.g., `MAX_RETRIES = 3`, `SECONDS_IN_A_DAY = 86400`).

## 5. DRY (Don't Repeat Yourself)

- **Single Source of Truth:** Do not duplicate code. If the same logic or magic number is used in multiple places, extract it into a reusable utility function (`utils`) or a constant.
- **Maintainability:** If a business rule changes, you should only have to update it in exactly one file.
- **Avoid over-engineering:** Only extract logic if it represents the same *knowledge* or business rule. If two pieces of code just happen to look similar by coincidence but serve completely different domains, do not force them into a single abstraction.

## 6. Security Standards

- **Secure Defaults:** Always use the most secure method available by default.
- **Prevent Injections:** NEVER concatenate strings to build database queries or system commands. ALWAYS use parameterized queries or prepared statements to prevent SQL/Command injection.
- **Sanitize Output:** Always encode/escape user input before rendering it in the UI to prevent XSS (Cross-Site Scripting).
