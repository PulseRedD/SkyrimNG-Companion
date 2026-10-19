# Contribution and Change-Control Policy

## Absolute rule: no direct changes to `main`

**All changes must be committed on a non-main branch and proposed through a pull request. Zero exceptions.** Applies to code, docs, generated files, AI agents, and urgent fixes. Never self-merge without explicit project-owner approval. Never rewrite `main` history.

## Workflow
1. Read `PROJECT_STATE.md`, architecture docs, and relevant source/tests.
2. Create a narrowly scoped branch from `main`.
3. Commit with specific intent (`docs(scanner): define read-only MO2 profile inputs`).
4. Open a PR documenting scope, affected modules, verification, migration risks, and follow-up tasks.
5. Wait for review. Do not merge without explicit owner approval.

## AI safety constraints
- Never replace whole modules or directory trees without comparing current code and obtaining approval for major rewrites.
- Prefer minimal diffs; preserve existing behavior and tests.
- Do not execute destructive file operations or write to MO2 profiles during initial scanner development.
- Do not force-push, delete branches containing unmerged work, or alter protection rules without approval.

## Enforcement
Configure a GitHub ruleset or branch protection requiring PRs on `main`, review approval where supported, and blocking force pushes/deletions and bypass. Verify settings separately: this document is policy, not technical enforcement.
