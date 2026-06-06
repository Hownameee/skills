---
description: Optimal rules for reading and modifying files efficiently (saving tokens and avoiding errors).
---

# File Operations Rules (Read & Modify)

## 1. Context Acquisition (Reading)

- **Do NOT read entire files blindly.** This wastes tokens and dilutes the context window.
- Use `grep_search` to find specific functions, classes, or variables.
- Use `list_dir` to understand the folder structure before diving into specific files.
- If a file is large, only read the relevant chunks using `StartLine` and `EndLine` parameters in your `view_file` tool.

## 2. File Modification (Transparent & Verifiable)

- **ALWAYS use native replacement tools** (like `replace_file_content` or `multi_replace_file_content`). These tools generate a visual Diff block in the UI, allowing the user to clearly review the changes and choose to "Accept" or "Reject".
- **NEVER use silent background scripts** (like `sed`, `awk`, `echo`, or custom Python scripts) to modify source code. Script-based modifications are invisible to the user and very difficult to validate.
- **AVOID complete rewrites.** Do not use tools that rewrite the entire file unless creating a new file from scratch.
- When using replacement tools, provide the **exact, literal `TargetContent`** including exact indentation and whitespace.
- If making multiple scattered changes, use multiple ReplacementChunks in a single call instead of editing line-by-line sequentially.
- **Preserve Existing Formatting:** Strictly respect the file's original formatting. Do not arbitrarily change indentations (tabs vs. spaces), quote styles (single vs. double), or line endings if they are not part of the required logic change.

## 3. Verification (Lint, Build, & Run)

- **ALWAYS verify your changes immediately.** Never assume a change worked without executing validation steps.
- **Lint & Check:** Run linters or syntax checkers to ensure no syntax errors were introduced (e.g., `npm run lint`, `python -m py_compile file.py`).
- **Build & Compile:** If the project requires compilation, build it to catch compilation errors (e.g., `npm run build`, `mvn compile`, `cargo check`).
- **Run & Test:** If possible, execute the code or run unit tests to guarantee the logic is correct and bug-free (e.g., `npm start`, `pytest`, `mvn test`).
- Ensure that every code modification is meaningful and does not cause bugs.
