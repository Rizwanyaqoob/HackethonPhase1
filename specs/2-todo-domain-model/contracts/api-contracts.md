# API Contracts: Todo Domain Model

## Todo Entity Contract

### Todo Creation Contract

**Request:**
- **Type**: Object Creation
- **Required Fields**:
  - `title`: string (non-empty)
- **Optional Fields**:
  - `description`: string
  - `completed`: boolean (default: false)

**Response:**
- **Type**: Todo object
- **Fields**:
  - `id`: integer (auto-generated, unique)
  - `title`: string
  - `description`: string (nullable)
  - `created_at`: datetime (ISO 8601 format)
  - `completed`: boolean
  - `updated_at`: datetime (ISO 8601 format, same as created_at for new items)

**Validation:**
- `title` must not be empty or None
- `completed` must be boolean if provided
- `id` must be unique across all todos

### Todo Update Contract

**Request:**
- **Type**: Object Update
- **Parameters**:
  - `todo_id`: integer (required, existing todo ID)
- **Optional Fields** (at least one required):
  - `title`: string (non-empty)
  - `description`: string
  - `completed`: boolean

**Response:**
- **Type**: Todo object or null
- **Success**: Returns updated Todo object
- **Failure**: Returns null if todo_id doesn't exist

**Validation:**
- `todo_id` must exist in storage
- If `title` is provided, it must not be empty or None
- `completed` must be boolean if provided

## TodoStorage API Contracts

### Add Todo Contract

**Method**: `add_todo(todo: Todo) -> Todo`
**Precondition**: Todo object has valid fields
**Postcondition**: Todo is stored with unique ID
**Return**: The stored Todo object with assigned ID

### Get Todo Contract

**Method**: `get_todo(todo_id: int) -> Optional[Todo]`
**Precondition**: todo_id is a valid integer
**Postcondition**: None
**Return**: Todo object if found, None otherwise

### Update Todo Contract

**Method**: `update_todo(todo_id: int, title: str = None, description: str = None, completed: bool = None) -> Optional[Todo]`
**Precondition**: todo_id exists in storage
**Postcondition**: Todo is updated if found
**Return**: Updated Todo object if found, None otherwise

### Delete Todo Contract

**Method**: `delete_todo(todo_id: int) -> bool`
**Precondition**: todo_id exists in storage
**Postcondition**: Todo is removed from storage
**Return**: True if deletion successful, False otherwise

### List Todos Contract

**Method**: `list_todos(completed: Optional[bool] = None) -> List[Todo]`
**Precondition**: None
**Postcondition**: None
**Return**: List of Todo objects
  - If `completed` is None: returns all todos
  - If `completed` is True: returns only completed todos
  - If `completed` is False: returns only pending todos

### Mark Complete Contract

**Method**: `mark_complete(todo_id: int) -> Optional[Todo]`
**Precondition**: todo_id exists in storage
**Postcondition**: Todo's completed status is set to True
**Return**: Updated Todo object if found, None otherwise

### Mark Incomplete Contract

**Method**: `mark_incomplete(todo_id: int) -> Optional[Todo]`
**Precondition**: todo_id exists in storage
**Postcondition**: Todo's completed status is set to False
**Return**: Updated Todo object if found, None otherwise

## TodoIdGenerator Contract

### Generate ID Contract

**Method**: `generate_id() -> int`
**Precondition**: None
**Postcondition**: Internal counter is incremented
**Return**: Next unique integer ID

### Reset Contract

**Method**: `reset() -> None`
**Precondition**: None
**Postcondition**: Internal counter is reset to initial value
**Return**: None