# SkyrimNG Companion Project State

Last documented: 2026-10-19
Status: Foundation organization. No implementation or tests verified.

## Intended v0.1
- Read-only MO2 instance/profile discovery.
- Parse `modlist.txt`, `plugins.txt`, available load order and mod metadata.
- Preserve separator ordering and enabled/disabled states.
- Produce deterministic, sanitized JSON snapshots and compare snapshots.
- Never modify MO2 files in the initial scanner.

## Longer-term
SQLite persistence, compatibility evidence/rules, xEdit/LOOT integrations, desktop dashboard, GitHub sync, optional native MO2 plugin, and AI-assisted analysis through supported interfaces.

## Open design questions
Profile and portable-instance discovery, file schemas, separator edge cases, database migrations, conflict evidence model, and safe GitHub sync.

## Next actions
1. Define scanner JSON schema and fixtures.
2. Implement profile parser and tests.
3. Validate against a real MO2 profile supplied by the user.
4. Define database schema after scan data is reliable.
