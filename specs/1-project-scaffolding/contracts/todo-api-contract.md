# API Contract: Todo Console Application

## Overview
This contract defines the interface for the Todo In-Memory Python Console Application. Since this is a console application, the "API" refers to the internal function interfaces and CLI commands.

## CLI Commands

### Add Task
- **Command**: `python todo.py add "Task description"`
- **Input**: Task title as string argument
- **Output**: Success message with task ID or error message
- **Error cases**:
  - Empty task title → Returns error message

### List Tasks
- **Command**: `python todo.py list`
- **Input**: None
- **Output**: Formatted list of all tasks with their completion status
- **Error cases**: None

### Update Task
- **Command**: `python todo.py update <task_id> "New task description"`
- **Input**: Task ID and new title
- **Output**: Success message or error message
- **Error cases**:
  - Invalid task ID → Returns error message
  - Empty new title → Returns error message

### Delete Task
- **Command**: `python todo.py delete <task_id>`
- **Input**: Task ID
- **Output**: Success message or error message
- **Error cases**:
  - Invalid task ID → Returns error message

### Mark Task Complete
- **Command**: `python todo.py complete <task_id>`
- **Input**: Task ID
- **Output**: Success message or error message
- **Error cases**:
  - Invalid task ID → Returns error message

### Mark Task Incomplete
- **Command**: `python todo.py incomplete <task_id>`
- **Input**: Task ID
- **Output**: Success message or error message
- **Error cases**:
  - Invalid task ID → Returns error message

## Internal Function Interfaces

### Task Management Service
```python
def add_task(title: str) -> dict:
    """Add a new task and return its details"""

def list_tasks(completed: Optional[bool] = None) -> List[dict]:
    """List tasks, optionally filtered by completion status"""

def update_task(task_id: int, title: str = None, completed: bool = None) -> dict:
    """Update task details and return updated task"""

def delete_task(task_id: int) -> bool:
    """Delete a task by ID, return success status"""

def mark_complete(task_id: int) -> dict:
    """Mark a task as complete and return updated task"""

def mark_incomplete(task_id: int) -> dict:
    """Mark a task as incomplete and return updated task"""
```