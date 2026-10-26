# Task Under Test
Change ID: CR-01

## Goal
Implement an optional `--sort` CLI argument that allows users to sort matching customer records alphabetically by name or email. The supported values will be `name` and `email`. Sorting must be case-insensitive and must not change the existing search behavior, validation, or output format.

## Requirements Covered
- FR-04
- FR-06
- AC-04

## Verification
- Verify that `--sort name` displays matching customers in alphabetical order by name, ignoring differences in letter case.
- Verify that `--sort email` displays matching customers in alphabetical order by email, ignoring differences in letter case.
- Verify that sorting does not change which customers match the search query.
- Verify that the output table retains the ID, Name, and Email columns.
- Verify that searches without `--sort` continue to work as before.
- Add automated tests using `pytest` to validate both sorting options and confirm that existing search functionality remains unchanged.
- Verify that the implementation uses only Python standard libraries and remains compatible with Python 3.11+.

## Constraints
- Use `REQUIREMENTS.md` and `SPEC.md` as the source of truth.
- Keep changes scoped to this task.
- Do not redefine requirements in this file.
- The application must only use Python standard libraries, with no external third-party production packages or external APIs.
- Automated tests must be implemented and executable using `pytest`.
- Implementation must be compatible with Python 3.11+.