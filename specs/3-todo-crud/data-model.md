# Data Model: Todo Entity

**Feature**: Todo CRUD Operations
**Date**: 2025-12-31
**Status**: Complete

## Todo Entity

### Fields

- **id**: `str`
  - Type: String
  - Description: Unique identifier for the todo item
  - Constraints: Required, must be unique
  - Generation: Auto-generated using UUID

- **description**: `str`
  - Type: String
  - Description: Description of the task to be completed
  - Constraints: Required, cannot be empty or whitespace only

- **completed**: `bool`
  - Type: Boolean
  - Description: Completion status of the todo item
  - Default: False
  - Constraints: Required

- **created_at**: `datetime`
  - Type: DateTime
  - Description: Timestamp when the todo was created
  - Constraints: Required, auto-generated
  - Format: ISO 8601

- **updated_at**: `datetime`
  - Type: DateTime
  - Description: Timestamp when the todo was last updated
  - Constraints: Required, auto-generated
  - Format: ISO 8601

### Validation Rules

1. **Description Validation**:
   - Cannot be empty or contain only whitespace
   - Must be less than 1000 characters
   - Required field

2. **ID Validation**:
   - Must be unique within the system
   - Auto-generated using UUID4
   - Required field

3. **Status Validation**:
   - Must be a boolean value (True/False)
   - Default value is False (incomplete)

4. **Timestamp Validation**:
   - Must be valid datetime objects
   - `created_at` cannot be in the future
   - `updated_at` must be >= `created_at`

### State Transitions

- **New Todo**: `completed = False` (default)
- **Mark Complete**: `completed = True`
- **Mark Incomplete**: `completed = False`

### Relationships

- No relationships with other entities in this domain

### Business Rules

1. A todo item cannot be created without a description
2. The completion status can be changed at any time
3. All timestamps are stored in UTC
4. The `updated_at` field is automatically updated whenever the todo is modified