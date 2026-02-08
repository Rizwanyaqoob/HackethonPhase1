# Quickstart: Todo Domain Model

## Overview

The Todo Domain Model provides a complete in-memory storage solution for managing Todo items. This model includes entities for Todo items, storage management, and ID generation.

## Core Components

### Todo Entity

The `Todo` entity represents a single task with the following attributes:

- `id`: Unique integer identifier (auto-generated)
- `title`: String representing the task description (required)
- `description`: Optional string with additional task details
- `created_at`: Datetime when the task was created
- `completed`: Boolean indicating completion status (default: False)
- `updated_at`: Datetime when the task was last modified

### TodoStorage Entity

The `TodoStorage` entity manages all Todo items in memory:

- `todos`: Dictionary mapping IDs to Todo objects for O(1) lookup
- `next_id`: Counter for generating unique IDs

### TodoIdGenerator Component

The `TodoIdGenerator` component provides unique ID generation:

- `current_id`: Current ID value for generation
- `generate_id()`: Returns next unique integer ID
- `reset()`: Resets the ID generator

## Usage Examples

### Creating a Todo

```python
from datetime import datetime
from src.models.todo import Todo

todo = Todo(
    id=1,
    title="Complete project",
    description="Finish the todo application",
    created_at=datetime.now(),
    completed=False
)
```

### Using TodoStorage

```python
from src.models.todo_storage import TodoStorage

storage = TodoStorage()

# Add a new todo
new_todo = storage.add_todo(todo)

# Retrieve a todo by ID
retrieved_todo = storage.get_todo(1)

# Update a todo
updated_todo = storage.update_todo(1, title="Updated title")

# Mark as complete
completed_todo = storage.mark_complete(1)

# List all todos
all_todos = storage.list_todos()

# List only completed todos
completed_todos = storage.list_todos(completed=True)

# Delete a todo
success = storage.delete_todo(1)
```

### Using TodoIdGenerator

```python
from src.lib.id_generator import TodoIdGenerator

id_generator = TodoIdGenerator()
new_id = id_generator.generate_id()  # Returns unique integer ID
```

## Validation Rules

- Todo title must not be empty or None
- ID must be unique within the application
- Completed status must be a boolean value

## State Transitions

- **Created**: When task is added (completed=False)
- **Updated**: When task details are changed
- **Completed**: When task is marked as complete (completed=True)
- **Reopened**: When completed task is marked as incomplete (completed=False)