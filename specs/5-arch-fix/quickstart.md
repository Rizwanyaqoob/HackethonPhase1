# Quickstart Guide: Architecture Fixes for Todo Application

**Feature**: Architecture Fixes for Todo Application
**Date**: 2025-12-31

## Overview

This guide provides instructions for implementing the architecture fixes to bring the Todo application into constitutional compliance. The fixes address code duplication, bug fixes, and code quality improvements as identified by the python_code_reviewer.

## Architecture

The implementation follows a clean architecture pattern with:

- **Models**: Canonical UUID-based Todo model as the single source of truth
- **Services**: TodoService with consolidated business logic
- **Lib**: Shared utilities, constants, and exceptions

## Implementation Steps

### Step 1: Architectural Cleanup

1. Remove duplicate implementations:
   - Delete `src/models/task.py`
   - Delete `src/models/todo_list.py`
   - Delete `src/services/task_service.py`

2. Ensure all references point to canonical implementation:
   - Update any imports that referenced the duplicate files
   - Verify TodoService is used consistently throughout the application

### Step 2: Bug Fixes

1. Fix timestamp update bug in appropriate methods:
   - Locate the bug where `task.updated_at = task.updated_at` doesn't update the timestamp
   - Change to `task.updated_at = datetime.now()` or equivalent
   - Verify all state-changing methods update timestamps correctly

### Step 3: Import Structure Fix

1. Remove manual path manipulation:
   - Remove manual `sys.path.insert()` calls
   - Update imports to use proper Python package structure
   - Test import functionality from different execution contexts

### Step 4: Validation Consolidation

1. Centralize validation logic:
   - Move validation logic to Todo model's `__post_init__` method
   - Remove redundant validation from service layer
   - Ensure validation is centralized and not duplicated

### Step 5: Constants Extraction

1. Create constants module:
   - Create `src/lib/constants.py`
   - Define `MAX_DESCRIPTION_LENGTH = 1000` and other hardcoded values
   - Replace inline literals with named constants

### Step 6: Missing Definitions

1. Add missing exception:
   - Add `DuplicateTodoError` to `src/lib/exceptions.py`
   - Follow same pattern as other custom exceptions

2. Implement missing methods in Todo class:
   - Add `validate()` method
   - Add `update()` method
   - Add `mark_complete()` method
   - Add `mark_incomplete()` method

### Step 7: Type Annotations

1. Add missing type annotations:
   - Add return type annotations to all functions
   - Ensure all functions have proper type hints
   - Verify type consistency across the codebase

## Key Implementation Notes

- All functions must have type hints
- Each function should have a single responsibility
- Use proper error handling with custom exceptions
- Follow the data model specifications exactly
- Ensure constitutional compliance (Python 3.13+, in-memory only, no global state)
- No external dependencies beyond Python standard library
- Maintain all existing functionality while making improvements

## Testing Strategy

- Unit tests for all new and modified methods
- Integration tests to verify import structure fixes
- Validation tests to ensure centralized validation works
- Regression tests to ensure existing functionality remains intact
- Error handling tests for new exception types

## Success Criteria

- All duplicate implementations removed
- All critical bugs fixed (timestamp update, import issues)
- Validation logic consolidated with no redundancy
- Hardcoded values extracted to constants module
- Missing exception definitions added
- Missing methods implemented in Todo class
- All type annotations present and correct
- Constitutional compliance maintained
- All existing functionality preserved
- Code quality improved according to review recommendations