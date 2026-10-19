"""Read-only Mod Organizer 2 profile snapshot. Python 3.10+; standard library only."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def _lines(path: Path) -> list[str]:
    if not path.is_file():
        return []
    # MO2 profile files may use UTF-8 BOM; preserve meaningful order.
    return path.read_text(encoding="utf-8-sig", errors="replace").splitlines()


def scan_profile(profile: Path, mods_dir: Path | None = None) -> dict:
    """Return a portable inventory without writing to MO2 or scanning mod contents.

    MO2 modlist.txt is generally bottom-to-top priority; we preserve raw line
    indices rather than pretending that index is a computed overwrite priority.
    """
    profile = profile.expanduser().resolve()
    if not (profile / "modlist.txt").is_file():
        raise FileNotFoundError(f"Missing MO2 profile modlist.txt in {profile}")

    mods = []
    for index, raw in enumerate(_lines(profile / "modlist.txt")):
        if not raw or raw.startswith("#"):
            continue
        prefix = raw[0]
        if prefix not in ("+", "-", "*"):
            continue
        name = raw[1:]
        if not name:
            continue
        # '*' denotes a foreign/managed entry in some MO2 versions; do not
        # infer its enabled state. Separators commonly use _separator suffix.
        is_separator = name.lower().endswith("_separator")
        mods.append({
            "name": name,
            "raw_index": index,
            "marker": prefix,
            "enabled": True if prefix == "+" else False if prefix == "-" else None,
            "is_separator": is_separator,
        })

    def plugins(filename: str) -> list[dict]:
        result = []
        for index, raw in enumerate(_lines(profile / filename)):
            raw = raw.strip()
            if not raw or raw.startswith("#"):
                continue
            # plugins.txt uses '*' for enabled plugins. loadorder.txt is an
            # ordering list; enabled is unknown there.
            enabled = raw.startswith("*") if filename == "plugins.txt" else None
            name = raw[1:] if raw.startswith("*") else raw
            result.append({"name": name, "index": index, "enabled": enabled})
        return result

    installed = []
    if mods_dir is not None:
        directory = mods_dir.expanduser().resolve()
        if not directory.is_dir():
            raise NotADirectoryError(directory)
        installed = sorted(p.name for p in directory.iterdir() if p.is_dir())

    return {
        "schema_version": 1,
        "source": "mo2-profile",
        "profile_name": profile.name,
        "mods": mods,
        "plugins": plugins("plugins.txt"),
        "loadorder": plugins("loadorder.txt"),
        "installed_directory_names": installed,
        "warnings": [
            "Modlist raw_index preserves source file order, not calculated MO2 priority.",
            "Separator identification by _separator suffix is heuristic.",
            "File conflicts, plugin records, mod versions, and metadata are not analyzed.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Read-only SkyrimNG MO2 profile snapshot")
    parser.add_argument("--profile", type=Path, required=True, help="MO2 profiles/<name> directory")
    parser.add_argument("--mods-dir", type=Path, help="Optional MO2 mods directory (names only)")
    parser.add_argument("--output", type=Path, help="Write JSON outside MO2; stdout by default")
    args = parser.parse_args()
    snapshot = scan_profile(args.profile, args.mods_dir)
    encoded = json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        output = args.output.expanduser().resolve()
        if output.is_relative_to(args.profile.expanduser().resolve()):
            parser.error("Refusing to write a report inside the MO2 profile directory")
        output.write_text(encoded, encoding="utf-8")
        print(f"Snapshot written: {output}")
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
