# Quickstart Guide: Todo In-Memory Python Console Application

## Prerequisites
- Python 3.13+
- UV package manager

## Setup
1. Clone or create the project directory
2. Install dependencies: `uv sync` (or `uv pip install -r requirements.txt` if using requirements file)
3. Verify installation: `python -m src.cli.main --help`

## Basic Usage
- Add a task: `python -m src.cli.main add "My new task"`
- List all tasks: `python -m src.cli.main list`
- Mark task as complete: `python -m src.cli.main complete 1` (where 1 is the task ID)
- Mark task as incomplete: `python -m src.cli.main incomplete 1`
- Update a task: `python -m src.cli.main update 1 "Updated task description"`
- Delete a task: `python -m src.cli.main delete 1`

## Project Structure
```
src/
├── models/          # Task model and in-memory storage
├── services/        # Task management business logic
├── cli/             # Command-line interface
└── lib/             # Shared utilities
```

## Development
- Run tests: `pytest`
- Format code: `black .`
- Check types: `mypy src/`