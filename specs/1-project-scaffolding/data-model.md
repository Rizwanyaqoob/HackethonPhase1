# Data Model: Todo In-Memory Python Console Application

## Task Entity

**Name**: Task
**Fields**:
- id: int (unique identifier, auto-generated)
- title: str (required, the task description)
- completed: bool (default: False, indicates completion status)
- created_at: datetime (timestamp when task was created)
- updated_at: datetime (timestamp when task was last modified)

**Validation Rules**:
- title must not be empty or None
- id must be unique within the application
- completed must be a boolean value

**State Transitions**:
- Created: When task is added (completed=False)
- Updated: When task details are changed
- Completed: When task is marked as complete (completed=True)
- Reopened: When completed task is marked as incomplete (completed=False)

## In-Memory Storage

**Name**: TodoList
**Fields**:
- tasks: List[Task] (collection of all tasks in memory)
- next_id: int (counter for generating unique IDs)

**Operations**:
- add_task(title: str) -> Task
- get_task(task_id: int) -> Task
- update_task(task_id: int, title: str = None, completed: bool = None) -> Task
- delete_task(task_id: int) -> bool
- list_tasks(completed: Optional[bool] = None) -> List[Task]
- mark_complete(task_id: int) -> Task
- mark_incomplete(task_id: int) -> Task