---
id: 1
title: Create Constitution For Todo App
stage: constitution
date: 2025-12-30
surface: agent
model: Claude Sonnet 4.5
feature: none
branch: master
user: user
command: sp.constitution
labels: [constitution, todo-app, setup]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

```text
You are operating under a strict Constitution for Phase I of the project:
"Todo In-Memory Python Console App".

Non-Negotiable Rules:
1. No manual coding by the human. All code must be generated via Claude Code.
2. Follow spec-driven development strictly:
   sp.specify → sp.plan → sp.tasks → sp.implementation
3. Python version must be 3.13+
4. Use UV as the package manager.
5. In-memory data only. No files, no database, no persistence.
6. No global mutable state.
7. All functions must have:
   - Type hints
   - Single responsibility
   - Clear naming
8. Console application only. No GUI, no web.
9. Implement exactly these features:
   - Add task
   - View tasks
   - Update task
   - Delete task
   - Mark task complete / incomplete
10. Clean project structure required:
    - /src
    - /specs
    - /specs/history
11. All specs must be saved and versioned in /specs/history.
12. If requirements are unclear, ask before implementing.
13. Prefer clarity over cleverness. No abstractions without reason.

Violat
```

## Response snapshot

The constitution for the "Todo In-Memory Python Console App" has been successfully updated with version 1.0.0. The new constitution incorporates all 13 non-negotiable rules provided in the user input and establishes clear principles for the project.

**Summary:**
- **New Version**: 1.0.0 (initial version)
- **Version Bump Rationale**: Initial creation of the constitution based on project requirements
- **Files Updated**: `.specify/memory/constitution.md`
- **Suggested Commit Message**: `docs: create constitution for Todo In-Memory Python Console App v1.0.0`

The constitution now contains 6 core principles and 2 additional sections that reflect the project's requirements:
1. No Manual Coding - All code must be generated via Claude Code
2. Spec-Driven Development - Following the sp.specify → sp.plan → sp.tasks → sp.implementation workflow
3. Python 3.13+ and UV - Using specific Python version and UV package manager
4. In-Memory Data Only - No files, databases, or persistence; no global mutable state
5. Code Quality Standards - Functions must have type hints, single responsibility, and clear naming
6. Feature Completeness - Implementing specific features: Add, View, Update, Delete, Mark Complete/Incomplete tasks
7. Project Structure Requirements - Clean structure with /src, /specs, /specs/history
8. Development Guidelines - Ask before implementing if unclear, prefer clarity over cleverness

All placeholders have been replaced with specific values derived from the user's requirements, and the constitution is ready for use in the spec-driven development process.

## Outcome

- ✅ Impact: Created initial project constitution with 13 non-negotiable rules
- 🧪 Tests: none
- 📁 Files: Updated .specify/memory/constitution.md with complete constitution
- 🔁 Next prompts: Proceed with sp.specify to create feature specification
- 🧠 Reflection: Constitution successfully captures all required project constraints

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Begin feature specification with sp.specify