## Changes Made

### Improvement I-01
Category: Context

Problem: The README does not document every CLI argument, as shown by the missing instructions for sorting customers by name or email.

Change: Added an instruction to AGENTS.md requiring every new CLI argument to be documented in the README.md, including its purpose, accepted values, and usage examples.

Evidence: AGENTS.md contains the documentation rule, and README.md includes the --sort name and --sort email examples.

### Improvement I-02
Category: CI Check

Problem: New automated tests can be added without updating traceability.md and README.md, leaving test coverage and documentation out of sync.

Change: Updated AGENTS.md to require agents to review and update the relevant documentation whenever they add or modify tests. Added a repository check in scripts/verify_repo.sh to detect missing test references in the traceability documentation.

Evidence: AGENTS.md defines the documentation requirement, and scripts/verify_repo.sh checks test references in docs/traceability.md.

### Improvement I-03
Category: Test

Problem: There is no automated verification that new CLI arguments are documented in the README.

Change: Added a repository test that checks whether supported CLI arguments, including --sort, are mentioned in the README.

Evidence: The repository check reports a failure when a supported CLI argument is missing from the documentation.

### Improvement I-04
Category: Executable Knowledge

Problem: Contributors may not know which command to run to verify repository consistency after making changes.

Change: Added a standard verification command to AGENTS.md to run scripts/verify_repo.sh. The script checks for documentation consistency and test references.

Evidence: AGENTS.md documents the command, and scripts/verify_repo.sh provides a reproducible verification procedure.
