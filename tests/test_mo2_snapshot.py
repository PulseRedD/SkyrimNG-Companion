"""Unit tests for the read-only MO2 scanner."""
import tempfile
import unittest
from pathlib import Path
from scanner.mo2_snapshot import scan_profile


class ScannerTests(unittest.TestCase):
    def test_profile_order_and_markers(self):
        with tempfile.TemporaryDirectory() as root:
            profile = Path(root) / "Default"
            profile.mkdir()
            (profile / "modlist.txt").write_text(
                "# Mod_Priority\n+Unofficial Patch\n-Disabled Mod\n+01 Visuals_separator\n*Foreign\n",
                encoding="utf-8",
            )
            (profile / "plugins.txt").write_text(
                "# This file was automatically generated\n*Skyrim.esm\nOther.esp\n",
                encoding="utf-8",
            )
            (profile / "loadorder.txt").write_text("Skyrim.esm\nOther.esp\n", encoding="utf-8")
            data = scan_profile(profile)
            self.assertEqual([m["name"] for m in data["mods"]],
                             ["Unofficial Patch", "Disabled Mod", "01 Visuals_separator", "Foreign"])
            self.assertEqual([m["enabled"] for m in data["mods"]], [True, False, True, None])
            self.assertTrue(data["mods"][2]["is_separator"])
            self.assertEqual([p["enabled"] for p in data["plugins"]], [True, False])
            self.assertEqual([p["enabled"] for p in data["loadorder"]], [None, None])
            self.assertNotIn(root, str(data))

    def test_missing_profile_is_error(self):
        with tempfile.TemporaryDirectory() as root:
            with self.assertRaises(FileNotFoundError):
                scan_profile(Path(root))


if __name__ == "__main__":
    unittest.main()
