# AI Usage Log

## Entry 01 - Initial Repository Readiness Audit

Stage: Initial Audit

Prompt/goal: Audit the `before` branch to identify repository-readiness problems that could affect an AI coding agent, including navigation, instructions, architecture, traceability, testing, automation, and safety.

AI contribution: The agent reviewed the repository documentation, source structure, and tests. It identified inconsistent entry-point documentation, limited automated enforcement, generated Python artifacts, and gaps in independently verifiable test evidence. The initial readiness score was 75/100.

Student decision:  
I reviewed the findings against the available repository files and distinguished documented problems from issues that still required independent verification. I used the initial score as a baseline rather than treating every observation as a confirmed defect.

Impact:  
REPOSITORY_READINESS_AUDIT.md

## Entry 02 - Designing AGENTS.md
Stage: Agent Instructions

Prompt/goal:  
Create `AGENTS.md` so an AI coding agent can understand the repository, identify authoritative documents, follow the architecture, and validate changes before declaring a task complete.

AI contribution:  
The agent helped organize the instructions around a recommended reading order, sources of truth, repository navigation, available commands, architectural boundaries, and verification expectations. It also emphasized that repository content must be treated as data rather than as instructions that override the agent's established boundaries.

Student decision:  
I accepted the structured reading order, explicit references to requirements and specifications, and the repository map. I treated instructions as guidance rather than sufficient enforcement.

Impact:  
AGENTS.md

## Entry 03 - Discoverability and Implicit Knowledge

Stage: Design Changes

Prompt/goal:  
Identify repository knowledge that was implicit, difficult to discover, or missing from the documentation, and decide whether it should become explicit instructions or executable checks.

AI contribution:  
The analysis highlighted 2 implicit knowledge cases centered around updating the proper documentation (`README.md`, `traceability.md`) when new test or CLI arguments are added.

Student decision:  
I decided to add an explicit instruction inside `AGENTS.md` about updating`README.md` and created a `verify_repo.sh` executable that verifies that the new test cases or CLI arguments are mentioned in the corresponding documentation.

Impact:  
AGENTS.md, verify_repo.sh

## Entry 04 - Turning a Guardrail into Software

Stage: Deterministic Validation

Prompt/goal:  
Implement deterministic repository-readiness checks so essential repository contracts can be validated instead of being left entirely to the coding agent's memory.

AI contribution:  
The agent helped define checks for required documentation and source files, test execution, and test traceability. The resulting verification approach uses `scripts/verify_repo.sh`, with `scripts/check_repo_contract.py` intended to check core repository requirements.

Student decision:  
I chose to automate conditions that can be checked deterministically, such as file existence and test execution. I ran the scripts to check they functioned properly.

Impact:  
check_repo_contract.py

## Entry 05 - After Repository Readiness Audit

Stage: Last Audit

Prompt/goal: Audit the `after` branch to identify repository-readiness problems that could affect an AI coding agent, including navigation, instructions, architecture, traceability, testing, automation, and safety.

AI contribution: The agent explored the files especified in `AGENT.md`, ran the test modules through the standard testing commmands and modified the proper documentation (`README.md`) after implementing the changes. It found improvements from the previous branch. The initial score given by the agent was 83 / 100

Student decision:  
I reviewed the findings against the available repository files and used the initial score as a baseline rather than treating every observation as a confirmed defect. I changed the ponts given to "Build / Run / Test" in `REPOSITORY_READINESS_AUDIT.md`.

Impact:  
REPOSITORY_READINESS_AUDIT.md