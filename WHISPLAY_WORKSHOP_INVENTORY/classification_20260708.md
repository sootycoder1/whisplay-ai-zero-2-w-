# WHISPLAY WORKSHOP CLASSIFICATION — 2026-07-08

Status: DRAFT
Rule: No files are deleted by this classification.
Rule: No broad git add . is allowed.
Rule: Every untracked file must be reviewed before keep/archive/ignore/delete.

## 1. Keep / Possible Git Review

These appear to be meaningful stage files, candidates, locked files, or tests.
They may belong in Git after review.

## 2. Tests / Possible Git Review

These are test files and may belong with their stages after review.

## 3. Archive / Do Not Git Yet

These look like backups, baselines, old candidate branches, or recovery references.
Preserve before deleting.

## 4. Ignore / Junk Review

These appear to be accidental command-name files or editor temporary files.
Do not delete until archived or confirmed.

## 5. Next Safe Action

Create an archive of all currently untracked files before any cleanup.
Then review what should be added to Git in small stage groups.
