# Data Model: CLI Components

**Feature**: CLI Integration for Todo App
**Date**: 2025-12-31
**Status**: Complete

## CLI Menu Structure

### Main Menu Options

- **Option 1**: "Add a new todo"
  - Action: Prompt for todo description and create new todo
  - Input: Todo description string
  - Output: Confirmation message or error

- **Option 2**: "View all todos"
  - Action: Display all todos with status and details
  - Input: None
  - Output: Formatted list of todos

- **Option 3**: "Update a todo"
  - Action: Prompt for todo ID and new details, update existing todo
  - Input: Todo ID, new description, completion status
  - Output: Confirmation message or error

- **Option 4**: "Delete a todo"
  - Action: Prompt for todo ID and confirm deletion
  - Input: Todo ID
  - Output: Confirmation message or error

- **Option 5**: "Mark todo as complete/incomplete"
  - Action: Prompt for todo ID and completion status
  - Input: Todo ID, completion status (complete/incomplete)
  - Output: Confirmation message or error

- **Option 6**: "Exit"
  - Action: Close the application
  - Input: None
  - Output: Exit message

### Input Validation Rules

1. **Menu Selection Validation**:
   - Must be a number between 1 and 6
   - Non-numeric input should show error and re-prompt
   - Out-of-range numbers should show error and re-prompt

2. **Todo ID Validation**:
   - Must be a valid UUID string format
   - Must exist in the system
   - Invalid format should show error and re-prompt
   - Non-existent ID should show error and re-prompt

3. **Description Validation**:
   - Cannot be empty or contain only whitespace
   - Must be less than 1000 characters
   - Empty input should show error and re-prompt

4. **Confirmation Validation**:
   - For delete operations, require explicit confirmation
   - Accept 'y', 'yes', 'n', 'no' (case-insensitive)
   - Invalid input should show error and re-prompt

### Output Formatting Rules

1. **Todo List Display**:
   - Format: "[ID] - [Description] - [Status]"
   - Status: "Completed" or "Pending"
   - Empty list: "No todos found"

2. **Status Indicators**:
   - Use consistent format for completion status
   - Visual indicators for completed vs pending items
   - Clear differentiation in display

3. **Error Messages**:
   - Clear, descriptive error messages
   - Instructions for correction
   - Return to appropriate menu after error

4. **Success Messages**:
   - Confirmation of completed actions
   - Brief summary of changes made
   - Return to main menu after success

### Navigation Flow

- **Main Loop**: Display menu, get selection, process action, return to menu
- **Operation Flow**: Prompt for input → Validate → Process → Confirm → Return to menu
- **Error Flow**: Show error → Return to appropriate prompt or menu
- **Exit Flow**: Clean shutdown with optional confirmation

### Business Logic Integration Points

- **TodoService**: Interface with existing business logic
- **Repository**: Through existing service layer
- **Exception Handling**: Convert business exceptions to user-friendly messages
- **Data Flow**: CLI input → Service → Repository → Service → CLI output