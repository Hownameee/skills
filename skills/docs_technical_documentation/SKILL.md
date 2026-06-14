---
name: docs_technical_documentation
description: Technical documentation standards for README files, guides, API docs, and developer-facing instructions.
---

# Specialist Technical Documentation

## 1. Audience And Purpose

- Identify the reader: new contributor, operator, API consumer, end user, maintainer, or reviewer.
- Put the reader's task before internal implementation history.
- Start with prerequisites, expected outcome, and the shortest correct path.
- Use consistent terminology and avoid unexplained acronyms.

## 2. Structure

- Keep headings task-oriented and scannable.
- Put commands in copyable code blocks.
- Show expected output when it helps the reader verify progress.
- Separate conceptual explanation from step-by-step procedure.
- Keep troubleshooting close to the workflow it supports.

## 3. Accuracy

- Verify commands before publishing when the repository can run them.
- Do not document features, flags, or endpoints that are not present in the current code.
- Update docs in the same change that changes user-visible behavior, setup, configuration, or operations.
- Link to canonical internal or upstream docs instead of duplicating long reference material.

## 4. Style

- Use direct, active voice.
- Prefer short sentences and concrete nouns.
- Avoid marketing language in operational or developer docs.
- Use inclusive language and avoid jokes in error, incident, or security documentation.
- Keep examples realistic and safe to run.
