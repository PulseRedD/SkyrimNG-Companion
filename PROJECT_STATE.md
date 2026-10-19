# SkyrimNG Companion Project State

Last documented: 2026-10-19
Status: Scanner v0.1 proposed on feature branch; **not merged or validated on real MO2 data**.

## Proposed implementation
- Standard-library-only read-only MO2 profile parser in `scanner/mo2_snapshot.py`.
- Portable JSON report with modlist raw ordering, markers, plugin enablement and loadorder.
- Optional installed mod directory names, with no content scanning.
- Unit tests in `tests/test_mo2_snapshot.py`.

## Limitations
- No database, GUI, conflict analysis, metadata parsing, version tracking, or real MO2 validation yet.
- Separator detection is heuristic; modlist raw index is not calculated priority.
- PR approval required before changes are accepted into `development`.

## Next actions
1. Review and merge scanner PR if acceptable.
2. Run unit tests and validate against sanitized real MO2 profile files.
3. Refine separator and priority parsing based on evidence.
4. Design snapshot diff and SQLite persistence.
