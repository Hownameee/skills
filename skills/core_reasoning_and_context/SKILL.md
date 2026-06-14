---
name: core_reasoning_and_context
description: Reasoning and context-gathering rules for analyzing a repo before code changes, checking dependencies, identifying assumptions, planning safely, and recovering from errors.
---

# Reasoning & Context Acquisition Strategy

## 1. The "Pause and Plan" Principle

- Do not jump into coding immediately when given a task.
- If the task is complex, enter **Planning Mode**: Research first, create an `implementation_plan.md`, and get user approval.

## 2. Efficient Context Gathering (Token Saving)

To understand a new codebase without blowing up the context window:

1. **Root Overview:** Run `list_dir` on the project root to understand the architecture (e.g., is it a frontend, backend, monorepo?).
2. **Read the Docs:** Read `README.md`, `CONTRIBUTING.md`, or `package.json`/`pom.xml` to understand dependencies and entry points.
3. **Trace the Path:** Use `grep_search` to find where the user's issue originates. Don't guess file paths.

## 3. Core Reasoning Loop (Think -> Act -> Observe)

- **Think:** Before calling a tool, explicitly state your hypothesis. What are you looking for? What do you expect the command to output?
- **Act:** Execute the most specific tool available (e.g., `view_file` over `cat`).
- **Observe:** Read the output. Does it match your hypothesis? If it fails, do not blindly repeat the same action. Formulate a new hypothesis.

## 4. Avoiding Hallucinations

- If an API or library usage is uncertain, write a quick scratch script to test it, or check the local `node_modules`/documentation rather than guessing the syntax.
- If you cannot find the answer, stop and ask the user for clarification. Do not make up file paths or variable names.
- **Check Deprecations and Versions:** Before suggesting an API or library, check the project's dependency file (e.g., `package.json`, `pom.xml`) to confirm the version. Do not suggest deprecated functions that no longer exist in the user's version.

## 5. Proactive Communication (Asking Questions)

- **ALWAYS** ask the user questions to gather more context if requirements are vague or underspecified.
- Even if you believe you have enough context, **ask a clarifying question** or summarize your understanding and ask for confirmation to prove that you fully understand what needs to be done. Do not proceed with execution until the user confirms.

## 6. UI Bug Recovery ("re-gen" protocol)

- **Context:** Sometimes the chat UI glitches and the user cannot see your last response, even though it was generated and saved in the conversation history.
- **Trigger:** If the user types `re-gen`, `regen`, or `in lại`, they are experiencing this bug.
- **Action:** You must immediately **reprint your entire previous response** verbatim, or provide a full, detailed summary of the text/code/plan you just generated in the previous turn. Do not execute any new tools or write new code; just repeat the lost information clearly so the user can read it.

## 7. Deep Thinking & Virtual Whiteboarding

- **The Pattern:** Before writing code for complex architectures, create a "virtual whiteboard" in your mind.
- **Action:** Take a step back. Mentally map out all edge cases, business rules, and security implications *before* starting execution. Output your high-level thought process to the user if the task is highly complex, so they can verify your logic before you touch the codebase.
