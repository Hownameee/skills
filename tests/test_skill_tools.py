"""Repository package and installation regressions; never use global targets."""

from contextlib import redirect_stderr, redirect_stdout
import io
import re
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import install_skills
import validate_skills


class SkillToolsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "skills"
        self.source.mkdir()
        self.target = self.root / "installed"
        self.target.mkdir()
        self.make_skill(self.source / "example", "current")

    def make_skill(self, path, body="example"):
        path.mkdir(parents=True, exist_ok=True)
        (path / "SKILL.md").write_text(
            f"---\nname: {path.name}\ndescription: Example skill\n---\n{body}\n"
        )

    def validate(self):
        with patch.object(validate_skills, "ROOT", self.root), patch.object(
            validate_skills, "SKILLS_DIR", self.source
        ), redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            return validate_skills.main()

    def test_preserves_independently_installed_and_system_skills(self):
        self.make_skill(self.target / "independent", "keep")
        self.make_skill(self.target / ".system" / "builtin", "keep")
        before = {
            p.relative_to(self.target): p.read_bytes()
            for p in self.target.rglob("*") if p.is_file()
        }
        self.assertEqual(install_skills.sync_skills_dir(self.source, self.target), 1)
        for path, content in before.items():
            self.assertEqual((self.target / path).read_bytes(), content)

    def test_replaces_managed_package_and_copies_support_files(self):
        old = self.target / "example"
        self.make_skill(old, "old")
        (old / "obsolete.txt").write_text("stale")
        (self.source / "example" / "LICENSE").write_text("notice")
        install_skills.sync_skills_dir(self.source, self.target)
        self.assertFalse((old / "obsolete.txt").exists())
        self.assertEqual((old / "LICENSE").read_text(), "notice")
        self.assertEqual((old / "SKILL.md").read_bytes(), (self.source / "example" / "SKILL.md").read_bytes())

    def test_workspace_snapshots_validate_but_are_not_installed(self):
        self.make_skill(self.source / "example-workspace" / "skill-snapshot")
        self.assertEqual(self.validate(), 0)
        self.assertEqual(install_skills.sync_skills_dir(self.source, self.target), 1)
        self.assertFalse((self.target / "example-workspace").exists())

    def test_new_skill_workspace_is_not_installed(self):
        workspace = self.source / "example-workspace"
        workspace.mkdir()
        (workspace / "results.json").write_text("{}")
        self.assertEqual(self.validate(), 0)
        self.assertEqual(install_skills.sync_skills_dir(self.source, self.target), 1)
        self.assertFalse((self.target / "example-workspace").exists())

    def test_nested_skill_inside_package_is_rejected(self):
        self.make_skill(self.source / "example" / "nested")
        self.assertEqual(self.validate(), 1)

    def test_missing_entrypoint_outside_workspace_is_rejected(self):
        (self.source / "broken").mkdir()
        self.assertEqual(self.validate(), 1)

    def test_copy_failure_preserves_existing_package(self):
        self.make_skill(self.target / "example", "old")
        old = (self.target / "example" / "SKILL.md").read_bytes()
        with patch.object(install_skills.shutil, "copytree", side_effect=OSError("copy failed")):
            with self.assertRaises(OSError):
                install_skills.sync_skills_dir(self.source, self.target)
        self.assertEqual((self.target / "example" / "SKILL.md").read_bytes(), old)
        self.assertFalse(list(self.target.glob(".skill-install-*")))

    def test_symlink_destination_is_not_followed_or_replaced(self):
        outside = self.root / "outside"
        self.make_skill(outside, "keep")
        (self.target / "example").symlink_to(outside, target_is_directory=True)
        before = (outside / "SKILL.md").read_bytes()
        with self.assertRaises(OSError):
            install_skills.sync_skills_dir(self.source, self.target)
        self.assertEqual((outside / "SKILL.md").read_bytes(), before)
        self.assertTrue((self.target / "example").is_symlink())

    def test_install_failure_returns_nonzero_without_success_message(self):
        out, err = io.StringIO(), io.StringIO()
        with patch.object(install_skills, "validate", return_value=True), patch.object(
            install_skills, "TARGETS", [self.target]
        ), patch.object(install_skills, "SKILLS_DIR", self.source), patch.object(
            install_skills, "sync_skills_dir", side_effect=OSError("denied")
        ), redirect_stdout(out), redirect_stderr(err):
            self.assertEqual(install_skills.main(), 1)
        self.assertIn("Installation incomplete", err.getvalue())
        self.assertNotIn("Skill installation complete!", out.getvalue())

    def test_instruction_copy_failure_returns_nonzero(self):
        guide = self.root / "AGENTS.md"
        guide.write_text("test guide")
        out, err = io.StringIO(), io.StringIO()
        with patch.object(install_skills, "validate", return_value=True), patch.object(
            install_skills, "TARGETS", []
        ), patch.object(install_skills, "AGENTS_MD", guide), patch.object(
            install_skills, "AGENTS_MD_TARGETS", [self.target / "AGENTS.md"]
        ), patch.object(install_skills.shutil, "copy2", side_effect=OSError("denied")), redirect_stdout(out), redirect_stderr(err):
            self.assertEqual(install_skills.main(), 1)
        self.assertNotIn("Skill installation complete!", out.getvalue())


class SkillCatalogTests(unittest.TestCase):
    def test_trigger_matrix_covers_current_packages(self):
        root = Path(__file__).resolve().parents[1]
        packages = {p.parent.name for p in (root / "skills").glob("*/SKILL.md")}
        matrix = (root / "docs" / "skill_trigger_tests.md").read_text()
        listed = re.findall(r"^\| `([^`]+)` \|", matrix, re.MULTILINE)
        self.assertEqual(len(listed), len(set(listed)), "Duplicate trigger rows")
        self.assertEqual(packages, set(listed))


if __name__ == "__main__":
    unittest.main()
