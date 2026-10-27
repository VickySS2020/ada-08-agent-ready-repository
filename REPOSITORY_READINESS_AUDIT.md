# Repository Readiness Audit

## BEFORE

| Dimension | Score 0–5 | Weighted | Evidence | Main Gap |
|---|---:|---:|---|---|
| Entry Point & Navigation | 4 | 12/15 | README.md describe el propósito, la instalación, los comandos de búsqueda y las pruebas. | El README presenta una discrepancia entre dos comandos de ejecución que referencian módulos distintos: "src.cli" en los ejemplos del README y "customer_search" en otra documentación. |
| Agent Instructions | 5 | 15/15 | AGENTS.md define reglas, documentos de referencia, validación y Definition of Done. | No se observa una carencia crítica en las instrucciones principales. |
| Build / Run / Test | 4 | 12/15 | El README documenta python -m src.cli --name Alice y pytest -v. | No se encontraron comandos reproducibles para instalar y validar el programa. |
| Architecture Boundaries | 4 | 8/10 | ARCHITECTURE.md separa CLI, servicio y almacenamiento, con responsabilidades e interfaces. | Las capas de la arquitectura están bien organizadas. |
| Requirements & Traceability | 4 | 8/10 | REQUIREMENTS.md, SPEC.md, TASKS.md y traceability.md relacionan requisitos, tareas, archivos y pruebas. | Persisten preguntas abiertas en los documentos de requisitos y se debe verificar que las referencias y estados de cobertura sigan correspondiendo a las pruebas reales. |
| Automation & Guardrails | 1 | 2/10 | AGENTS.md exige ejecutar pruebas y no debilitar los tests. | No se observó CI ni automatización visible que imponga estas reglas. Además, el árbol incluye archivos compilados __pycache__. |
| Testability & Evidence | 4 | 12/15 | El repositorio contiene tests/test_cli.py, test_service.py, test_storage.py, test_validation.py y test_setup.py. También documenta evidencia en agent-report.md. | El reporte documenta pruebas ejecutadas, pero los resultados de cada una no fueron anotados. |
| Safety & Permissions | 3 | 6/10 | SPEC.md limita el alcance y excluye modificaciones de datos y llamadas externas; AGENTS.md restringe cambios innecesarios. | No se observó un .gitignore en el árbol inspeccionado y hay archivos .pyc versionados. Tampoco se encontró evidencia visible de controles automatizados de seguridad. |

TOTAL BEFORE: 75 / 100

Top 3 friction points:
1. Lack of verifiable automation. The instructions state that tests must be run, but no continuous integration workflow was identified that performs this automatically with every change.
2. Repository hygiene. Compiled files—specifically `__pycache__` and `.pyc` files—were found under version control. Should update or review the `.gitignore` file to prevent the inclusion of generated artifacts that are dependent on the local environment.
3. Independent verification and document consistency. The repository includes documentation and test reports; however, it is still necessary to run `pytest -v`, verify the startup commands, and cross-reference the results with the traceability matrix.
