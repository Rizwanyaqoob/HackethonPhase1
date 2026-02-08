# Implementation Plan: Architecture Fixes for Todo Application

**Feature**: Architecture Fixes for Todo Application
**Branch**: 5-arch-fix
**Created**: 2025-12-31
**Status**: In Progress

## Technical Context

**Architecture Pattern**: Clean, consistent architecture with single source of truth
**Canonical Implementation**: UUID-based Todo system (Todo model, TodoService, TodoRepository)
**Technology Stack**: Python 3.13+ with standard library only
**Constraints**:
- Remove duplicate implementations (Task, TodoList, TaskService)
- Fix timestamp update bug where updated_at field doesn't refresh
- Eliminate manual path manipulation in imports
- Consolidate validation logic to single location
- Extract hardcoded values to constants
- Add missing exception definitions
- Add missing type annotations
- Maintain constitutional compliance (Python 3.13+, in-memory only, no global state)

**Unknowns**:
- Specific locations of all duplicate files to be removed
- Exact implementation details for missing methods in Todo class
- All hardcoded values that need to be extracted to constants

## Constitution Check

**Constitution Alignment**:
- [x] Python version 3.13+ compliance
- [x] In-memory data only (no files/database)
- [x] No global mutable state (after fixes)
- [x] All functions have type hints (will be added)
- [x] Single responsibility principle
- [x] Clear naming conventions
- [x] Console-only interface (no GUI/web as specified)

**Gates**:
- [x] No persistence - data stored only in memory
- [x] Type hints required for all functions (will be added)
- [x] Functions have single responsibility
- [x] Clear naming for variables and functions

**Post-Design Compliance**:
- [x] Architecture follows single source of truth principle
- [x] Proper module imports without manual path manipulation
- [x] Validation centralized to prevent redundancy
- [x] Type hints included in all specifications

## Phase 0: Research & Unknown Resolution

### Research Tasks

1. **Duplicate Implementation Research**
   - Identify all locations of Task, TodoList, and TaskService implementations
   - Determine which files need to be removed vs. which contain unique functionality
   - Map dependencies between duplicate implementations

2. **Missing Methods Research**
   - Identify which methods (validate, update, mark_complete, mark_incomplete) need to be added to Todo class
   - Determine proper method signatures and return types
   - Research best practices for implementing these methods in dataclasses

3. **Hardcoded Values Research**
   - Scan all files for hardcoded numeric/string literals
   - Identify values that should be constants vs. acceptable inline literals
   - Determine appropriate constant naming and organization

### Completed Research
- Research document created at `specs/5-arch-fix/research.md`
- All unknowns resolved with data-driven decisions

## Phase 1: Design & Contracts

### Data Model: Todo Entity (Canonical Implementation)

- **Todo Entity Structure**:
  - id: str (UUID)
  - description: str (task description)
  - completed: bool (completion status)
  - created_at: datetime (timestamp)
  - updated_at: datetime (timestamp)

- **Methods to Add**:
  - validate(): Validates the todo item
  - update(description: str = None, completed: bool = None): Updates the todo
  - mark_complete(): Marks the todo as complete
  - mark_incomplete(): Marks the todo as incomplete

- **Validation Rules**:
  - Description cannot be empty or whitespace only
  - Description must be less than 1000 characters (or constant-defined limit)
  - Timestamp validation rules

### Business Logic Contracts

1. **Todo Validation Contract**
   - Input: Todo instance
   - Output: Validation result or error
   - Error: InvalidTodoError if validation fails

2. **Todo Update Contract**
   - Input: Todo instance, optional description, optional completed status
   - Output: Updated Todo instance
   - Validation: Description validation if provided
   - Error: InvalidTodoError if validation fails

3. **Todo Status Update Contracts**
   - Input: Todo instance
   - Output: Updated Todo instance with new status
   - Error: None

### Implementation Architecture

- **Models**: Canonical Todo model with all required methods
- **Services**: TodoService with consolidated logic
- **Lib**: Constants module, exceptions, validators

### Completed Artifacts
- Data model defined in `specs/5-arch-fix/data-model.md`
- Quickstart guide created at `specs/5-arch-fix/quickstart.md`

## Phase 2: Implementation Plan

### Step 1: Architectural Cleanup
- Identify and remove duplicate files (Task, TodoList, TaskService)
- Select UUID-based Todo system as the canonical implementation
- Ensure all references point to the canonical implementation

### Step 2: Bug Fixes
- Fix timestamp update bug in appropriate methods
- Ensure updated_at is properly refreshed when state changes
- Verify all state-changing operations update timestamps correctly

### Step 3: Import Structure Fix
- Remove manual sys.path manipulation
- Implement proper package imports using Python module structure
- Test import functionality from different execution contexts

### Step 4: Validation Consolidation
- Move validation logic to Todo model's __post_init__ method
- Remove redundant validation from service layer
- Ensure validation is centralized and not duplicated

### Step 5: Constants Extraction
- Create constants module with named constants
- Replace hardcoded values with constants
- Update all references to use constants instead of literals

### Step 6: Missing Definitions
- Add DuplicateTodoError to exceptions module
- Implement missing methods in Todo class
- Update method signatures with proper return types

### Step 7: Type Annotations
- Add missing return type annotations
- Ensure all functions have proper type hints
- Verify type consistency across the codebase

## Success Criteria

- Duplicate implementations resolved with single canonical implementation
- All critical bugs fixed (timestamp update, import issues)
- Validation logic consolidated with no redundancy
- Hardcoded values extracted to constants module
- Missing exception definitions added
- Missing methods implemented in Todo class
- All type annotations present and correct
- Constitutional compliance maintained
- All existing functionality preserved
- Code quality improved according to review recommendations