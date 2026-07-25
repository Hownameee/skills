#!/usr/bin/env python3
"""Install or re-install repository skills to global (~/.gemini/config, ~/.agents, ~/.codex) and local roots."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
AGENTS_MD = ROOT / "AGENTS.md"

HOME = Path.home()
TARGETS = [
    HOME / ".gemini" / "config" / "skills",
    HOME / ".agents" / "skills",
    HOME / ".codex" / "skills",
]

AGENTS_MD_TARGETS = [
    HOME / ".gemini" / "config" / "AGENTS.md",
    HOME / ".agents" / "AGENTS.md",
    HOME / ".codex" / "AGENTS.md",
]


def validate() -> bool:
    """Run validation before installing."""
    import validate_skills
    return validate_skills.main() == 0


def sync_skills_dir(source_dir: Path, target_dir: Path) -> int:
    try:
        target_dir.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"Warning: Could not create/access directory {target_dir}: {e}")
        return 0

    valid_skill_names = {p.name for p in source_dir.iterdir() if p.is_dir()}

    copied_count = 0
    for skill_path in sorted(source_dir.iterdir()):
        if not skill_path.is_dir():
            continue
        dest_path = target_dir / skill_path.name
        try:
            if dest_path.exists():
                shutil.rmtree(dest_path)
            shutil.copytree(skill_path, dest_path)
            copied_count += 1
        except Exception as e:
            print(f"Warning: Failed to copy {skill_path.name} to {dest_path}: {e}")

    # Prune obsolete skills (ignore hidden folders like .system)
    try:
        for existing in target_dir.iterdir():
            if existing.is_dir() and not existing.name.startswith("."):
                if existing.name not in valid_skill_names:
                    print(f"  Removing obsolete skill: {existing.name} from {target_dir}")
                    shutil.rmtree(existing, ignore_errors=True)
    except Exception as e:
        print(f"Warning: Could not prune obsolete skills in {target_dir}: {e}")

    return copied_count


def install_agents_md():
    if not AGENTS_MD.exists():
        return
    for target in AGENTS_MD_TARGETS:
        try:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(AGENTS_MD, target)
            print(f"Updated {target}")
        except Exception as e:
            print(f"Warning: Could not copy AGENTS.md to {target}: {e}")


def main() -> int:
    sys.path.insert(0, str(ROOT / "scripts"))
    print("Validating skills before installation...")
    if not validate():
        print("ERROR: Skill validation failed. Aborting installation.", file=sys.stderr)
        return 1

    print("\nInstalling skills to target directories...")
    for target in TARGETS:
        count = sync_skills_dir(SKILLS_DIR, target)
        print(f"Successfully installed {count} skills to {target}")

    install_agents_md()

    # Set up workspace local links/copies in .agents and .codex
    workspace_agents_skills = ROOT / ".agents" / "skills"
    workspace_codex_skills = ROOT / ".codex" / "skills"
    sync_skills_dir(SKILLS_DIR, workspace_agents_skills)
    sync_skills_dir(SKILLS_DIR, workspace_codex_skills)

    if AGENTS_MD.exists():
        try:
            shutil.copy2(AGENTS_MD, ROOT / ".agents" / "AGENTS.md")
            shutil.copy2(AGENTS_MD, ROOT / ".codex" / "AGENTS.md")
        except Exception as e:
            print(f"Warning: Could not copy AGENTS.md to local target: {e}")

    print("\nSkill installation complete!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
