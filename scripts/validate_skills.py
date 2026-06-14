#!/usr/bin/env python3
"""Validate this repository's Codex-compatible skill package layout."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9_][a-z0-9_-]*$")
ALLOWED_ROOT_MARKDOWN = {"README.md", "AGENTS.md"}


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str | None]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, "missing opening YAML frontmatter delimiter"

    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, "missing closing YAML frontmatter delimiter"

    data: dict[str, str] = {}
    for lineno, raw in enumerate(text[4:end].splitlines(), start=2):
        if not raw.strip():
            continue
        if ":" not in raw:
            return {}, f"invalid frontmatter line {lineno}: {raw!r}"
        key, value = raw.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if not key:
            return {}, f"empty frontmatter key on line {lineno}"
        data[key] = value
    return data, None


def main() -> int:
    errors: list[str] = []

    if not SKILLS_DIR.is_dir():
        errors.append("missing skills/ directory")
    else:
        root_skill_files = sorted(ROOT.glob("*.md"))
        root_skill_files = [p for p in root_skill_files if p.name not in ALLOWED_ROOT_MARKDOWN]
        for path in root_skill_files:
            errors.append(f"root-level skill markdown is not allowed: {path.name}")

        seen: dict[str, Path] = {}
        skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
        if not skill_files:
            errors.append("no skills found under skills/<name>/SKILL.md")

        for path in skill_files:
            folder_name = path.parent.name
            data, err = parse_frontmatter(path)
            if err:
                errors.append(f"{path.relative_to(ROOT)}: {err}")
                continue

            name = data.get("name")
            description = data.get("description")
            if not name:
                errors.append(f"{path.relative_to(ROOT)}: missing name")
            elif name != folder_name:
                errors.append(
                    f"{path.relative_to(ROOT)}: name {name!r} does not match folder {folder_name!r}"
                )
            elif not NAME_RE.match(name):
                errors.append(f"{path.relative_to(ROOT)}: invalid skill name {name!r}")
            elif name in seen:
                errors.append(
                    f"{path.relative_to(ROOT)}: duplicate skill name {name!r}; first seen at {seen[name].relative_to(ROOT)}"
                )
            else:
                seen[name] = path

            if not description:
                errors.append(f"{path.relative_to(ROOT)}: missing description")

        extra_skill_files = sorted(
            p for p in SKILLS_DIR.rglob("SKILL.md") if p.parent.parent != SKILLS_DIR
        )
        for path in extra_skill_files:
            errors.append(f"nested skill package is not allowed: {path.relative_to(ROOT)}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"OK: validated {len(list(SKILLS_DIR.glob('*/SKILL.md')))} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
