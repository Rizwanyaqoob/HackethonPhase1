<!-- Sync Impact Report:
     Version change: N/A → 1.0.0
     Added sections: All principles and sections based on user requirements
     Templates requiring updates: N/A (new constitution)
     Follow-up TODOs: None
-->
# Todo In-Memory Python Console App Constitution

## Core Principles

### No Manual Coding
No manual coding by the human. All code must be generated via Claude Code.

### Spec-Driven Development
Follow spec-driven development strictly: sp.specify → sp.plan → sp.tasks → sp.implementation

### Python 3.13+ and UV
Python version must be 3.13+ and use UV as the package manager.

### In-Memory Data Only
In-memory data only. No files, no database, no persistence. No global mutable state.

### Code Quality Standards
All functions must have type hints, single responsibility, and clear naming. Console application only. No GUI, no web.

### Feature Completeness
Implement exactly these features: Add task, View tasks, Update task, Delete task, Mark task complete/incomplete.

## Project Structure Requirements
Clean project structure required: /src, /specs, /specs/history. All specs must be saved and versioned in /specs/history.

## Development Guidelines
If requirements are unclear, ask before implementing. Prefer clarity over cleverness. No abstractions without reason.

## Governance
All implementations must comply with these 13 non-negotiable rules. Violations require immediate correction.

**Version**: 1.0.0 | **Ratified**: 2025-12-30 | **Last Amended**: 2025-12-30