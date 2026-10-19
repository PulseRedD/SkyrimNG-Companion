# Architecture

## Components
1. `scanner/`: read-only local MO2 inventory and profile parser.
2. `database/`: versioned SQLite schema and migrations.
3. `analysis/`: dependency graph, compatibility rules, and patch invalidation.
4. `integrations/`: external-tool report import and GitHub synchronization.
5. `desktop/`: future local Qt dashboard.
6. `tests/`: fixtures, parser tests, and regression checks.

## Safety
No auto-reordering, plugin edits, or file deletion in early releases. Sanitize paths and secrets before syncing. Never infer that an asset overwrite or plugin override is automatically a bug.

## Boundaries
MO2 remains authoritative for installed state; SQLite for local scan history; GitHub for curated portable project knowledge. AI reads evidence through an explicitly supported connection or user-supplied reports.
