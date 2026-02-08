# Data Model: Todo Domain Model

## Todo Entity

**Name**: Todo
**Fields**:
- id: int (unique identifier, auto-generated)
- title: str (required, the task description)
- description: str (optional, additional details about the task)
- created_at: datetime (timestamp when task was created)
- completed: bool (default: False, indicates completion status)
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

## TodoStorage Entity

**Name**: TodoStorage
**Fields**:
- todos: Dict[int, Todo] (dictionary of all todos with ID as key)
- next_id: int (counter for generating unique IDs)

**Operations**:
- add_todo(todo: Todo) -> Todo
- get_todo(todo_id: int) -> Optional[Todo]
- update_todo(todo_id: int, title: str = None, description: str = None, completed: bool = None) -> Optional[Todo]
- delete_todo(todo_id: int) -> bool
- list_todos(completed: Optional[bool] = None) -> List[Todo]
- mark_complete(todo_id: int) -> Optional[Todo]
- mark_incomplete(todo_id: int) -> Optional[Todo]

## TodoIdGenerator Component

**Name**: TodoIdGenerator
**Fields**:
- current_id: int (the current ID value for generation)

**Operations**:
- generate_id() -> int
- reset() -> None