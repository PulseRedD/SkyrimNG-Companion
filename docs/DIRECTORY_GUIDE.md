# SkyrimNG Companion Directory Guide

This repository owns the **software**, not modpack decisions or third-party mod assets.

| Path | Responsibility | Expected contents |
|---|---|---|
| `scanner/` | Read-only MO2 state discovery | Profile parsers, mod metadata parsing, deterministic snapshot generation |
| `database/` | Local persistence | SQLite schemas, migrations, repositories, audit records |
| `analysis/` | Compatibility reasoning | Snapshot diffs, dependency graph, patch invalidation, evidence-based rules |
| `integrations/` | External systems | LOOT/xEdit import, GitHub sync, future MO2 plugin adapters |
| `desktop/` | Local UI | PySide6 views, state management, review/approval interactions |
| `tests/` | Quality gates | Unit tests, fixtures, integration tests, regression coverage |
| `docs/` | Technical specifications | Architecture, directory guide, interfaces, security guidance |

**Boundary:** MO2 is authoritative for actual installation state; local SQLite tracks scans and tasks; GitHub contains reviewed, sanitized project knowledge. No runtime scanner implementation exists yet.
