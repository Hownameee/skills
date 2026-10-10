#!/usr/bin/env python3
"""Install repository skills globally while preserving unrelated packages."""

from __future__ import annotations

import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
AGENTS_MD = ROOT / "AGENTS.md"

HOME = Path.home()
TARGETS = [
    HOME / ".gemini" / "config" / "skills",
    HOME / ".codex" / "skills",
]

AGENTS_MD_TARGETS = [
    HOME / ".gemini" / "config" / "AGENTS.md",
    HOME / ".codex" / "AGENTS.md",
]


def validate() -> bool:
    """Run validation before installing."""
    import validate_skills
    return validate_skills.main() == 0


def sync_skills_dir(source_dir: Path, target_dir: Path) -> int:
    target_dir.mkdir(parents=True, exist_ok=True)
    copied_count = 0
    for entrypoint in sorted(source_dir.glob("*/SKILL.md")):
        skill_path = entrypoint.parent
        dest_path = target_dir / skill_path.name
        if dest_path.is_symlink() or (dest_path.exists() and not dest_path.is_dir()):
            raise OSError(f"Refusing to replace non-directory or symlink: {dest_path}")
        # Finish copying before replacing an installed package, so a failed
        # read or copy leaves the working installation intact.
        with tempfile.TemporaryDirectory(prefix=".skill-install-", dir=target_dir) as tmp:
            staged = Path(tmp) / "package"
            shutil.copytree(skill_path, staged)
            if dest_path.exists():
                shutil.rmtree(dest_path)
            staged.rename(dest_path)
            copied_count += 1

    return copied_count


def install_agents_md():
    if not AGENTS_MD.exists():
        return
    for target in AGENTS_MD_TARGETS:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(AGENTS_MD, target)
        print(f"Updated {target}")


def main() -> int:
    sys.path.insert(0, str(ROOT / "scripts"))
    print("Validating skills before installation...")
    if not validate():
        print("ERROR: Skill validation failed. Aborting installation.", file=sys.stderr)
        return 1

    print("\nInstalling skills to target directories...")
    try:
        for target in TARGETS:
            count = sync_skills_dir(SKILLS_DIR, target)
            print(f"Successfully installed {count} skills to {target}")
        install_agents_md()
    except OSError as error:
        print(f"ERROR: Installation incomplete: {error}", file=sys.stderr)
        return 1

    print("\nSkill installation complete!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
