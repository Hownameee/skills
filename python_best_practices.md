---
description: Python development standards focusing on project structure, typing, and testing.
---

# Specialist Python Best Practices

## 1. Project Structure & Architecture

- Maintain clear separation: source code, tests, docs, and config.
- Modular design: separate files for models, services, controllers, and utilities.

## 2. Configuration & Management

- Dependency management: Use `uv` (<https://github.com/astral-sh/uv>) and virtual environments.
- Configuration: Use environment variables for all environment-specific configs.
- Code style: Strictly enforce formatting and linting using `Ruff`.

## 3. Code Quality & Typing

- **100% Type Hinting:** ALWAYS add typing annotations to each function or class. Include explicit return types (including `None` where appropriate).
- **Documentation:** Use PEP 257 docstring conventions for all functions and classes. Update existing docstrings when modifying code. Preserve any existing inline comments.
- **Fail Fast:** Implement robust error handling and logging, explicitly capturing context.

## 4. Testing Standards

- **Framework:** ONLY use `pytest` or `pytest` plugins. Do not use `unittest`.
- **Location:** Place all tests under the `./tests` directory. Add `__init__.py` where necessary.
- **Typing in Tests:** All test functions must have typing annotations and docstrings.
- **Mocking:** Be sure to import types for fixtures if `TYPE_CHECKING` (e.g., `CaptureFixture`, `FixtureRequest`, `MonkeyPatch`, `MockerFixture`).
