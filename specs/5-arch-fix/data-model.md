# Data Model: Todo Entity (Canonical Implementation)

**Feature**: Architecture Fixes for Todo Application
**Date**: 2025-12-31
**Status**: Complete

## Todo Entity Structure

### Fields

- **id**: `str`
  - Type: String
  - Description: Unique identifier for the todo item (UUID)
  - Constraints: Required, must be unique
  - Generation: Auto-generated using UUID4

- **description**: `str`
  - Type: String
  - Description: Description of the task to be completed
  - Constraints: Required, cannot be empty or whitespace only
  - Validation: Must be less than MAX_DESCRIPTION_LENGTH characters

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

### Constants

- **MAX_DESCRIPTION_LENGTH**: `int`
  - Value: 1000
  - Description: Maximum allowed length for todo description

### Methods to Add

- **validate()**: `None`
  - Purpose: Validates the todo item according to business rules
  - Input: None (validates current instance)
  - Output: None
  - Error: Raises InvalidTodoError if validation fails

- **update()**: `None`
  - Purpose: Updates the todo item's description and/or completion status
  - Input: description (str, optional), completed (bool, optional)
  - Output: None
  - Side Effect: Updates updated_at timestamp

- **mark_complete()**: `None`
  - Purpose: Marks the todo as complete
  - Input: None
  - Output: None
  - Side Effect: Sets completed = True, updates updated_at timestamp

- **mark_incomplete()**: `None`
  - Purpose: Marks the todo as incomplete
  - Input: None
  - Output: None
  - Side Effect: Sets completed = False, updates updated_at timestamp

### Validation Rules

1. **Description Validation**:
   - Cannot be empty or contain only whitespace
   - Must be less than MAX_DESCRIPTION_LENGTH characters
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
- **Update**: `updated_at = current_time`

### Business Rules

1. A todo item cannot be created without a description
2. The completion status can be changed at any time
3. All timestamps are stored in UTC
4. The `updated_at` field is automatically updated whenever the todo is modified
5. Description validation occurs during instantiation and updates