# HackethonPhase1 - Todo In-Memory Python Console Application

A simple command-line todo application that stores tasks in memory only. No files, no database, no persistence - all data is lost when the application closes.

## Features

- Add new tasks
- View all tasks
- Update task descriptions
- Delete tasks
- Mark tasks as complete/incomplete

## Prerequisites

- Python 3.13+
- UV package manager

## Setup

1. Clone or download the repository
2. Install dependencies using UV:
   ```bash
   uv sync
   ```
   Or install directly with pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Adding a Task
```bash
python -m src.cli.main add "My new task"
```

### Listing Tasks
```bash
python -m src.cli.main list
```
To list only completed tasks:
```bash
python -m src.cli.main list --completed true
```

To list only incomplete tasks:
```bash
python -m src.cli.main list --completed false
```

### Updating a Task
```bash
python -m src.cli.main update 1 "Updated task description"
```

### Deleting a Task
```bash
python -m src.cli.main delete 1
```

### Marking a Task as Complete
```bash
python -m src.cli.main complete 1
```

### Marking a Task as Incomplete
```bash
python -m src.cli.main incomplete 1
```

## Project Structure

```
src/
├── models/          # Data models (Task, TodoList)
├── services/        # Business logic (TaskService)
├── cli/             # Command-line interface
└── lib/             # Utility functions
```

## Development

- Run tests: `pytest`
- Format code: `black .`
- Check types: `mypy src/`

## License

This project is licensed under the terms specified in the project documentation.
