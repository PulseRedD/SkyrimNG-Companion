# MO2 Scanner v0.1

Read-only profile inventory prototype. Requires Python 3.10+; no external packages.

## Run

From repository root:

```powershell
python -m scanner.mo2_snapshot --profile "D:\\Modding\\MO2\\profiles\\Default" --output "snapshot.json"
python -m unittest discover -s tests -v
```

Optional: `--mods-dir "D:\\Modding\\MO2\\mods"` records **directory names only**, not metadata or file contents. Without `--output`, JSON is printed to stdout.

## Current contract

The report contains schema version, profile name, ordered `modlist.txt` entries with original indices and marker, `plugins.txt` entries with enabled markers, `loadorder.txt` entries, optional installed mod directory names, and explicit warnings.

No absolute source paths are included in the JSON. The scanner does not edit MO2 data, calculate actual priority, identify overwrite winners, or determine whether patches are needed.

## Important caveats

- Separator detection based on `_separator` is a heuristic and needs testing against your MO2 setup.
- An asterisk in `modlist.txt` is preserved as unknown enabled state, not guessed.
- Missing optional profile files produce empty arrays; missing `modlist.txt` is an error.
- Do not share snapshots publicly before reviewing mod names and any personally identifying labels.
- The CLI refuses an output path within the selected profile folder. Keep output outside all MO2-managed directories.
- This prototype needs real MO2 fixtures and further validation before being trusted for Wabbajack or patch decisions.
