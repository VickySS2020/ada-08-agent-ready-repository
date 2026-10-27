# Implicit Knowledge Found

## IK-01
What:
Any CLI argument added to the program should have it's instructions added inside README.md

How was it discovered:
Missing 'Sort By Name/Email' instructions in **How to execute** section inside `README.md`.

Should this remain implicit?
NO

Where should it become explicit?
AGENTS.md / scripts/verify_repo.sh

## IK-02
What:
If more tests are added, they should be included in the appropriate documentation (`traceability.md` and `README.md`).

How was it discovered:
The agent made no changes to these files, even though it added new automatic tests.

Risk:
This could affect the traceability of the tests.

Remediation:
AGENTS.md / scripts/verify_repo.sh
