# Implementation Tasks: Todo Domain Model

**Feature**: 2-todo-domain-model | **Date**: 2025-12-31 | **Spec**: [link to spec](specs/2-todo-domain-model/spec.md)

## Overview

Implementation of the Todo domain model with in-memory storage strategy. This includes defining the Todo entity with proper attributes and data types, implementing an in-memory storage mechanism for managing Todo items, creating an ID generation system for unique identification, and establishing status tracking for completed vs pending tasks.

## Dependencies

- User Story 3 (ID Strategy) depends on User Story 1 (Todo Data Structure)
- User Story 2 (In-Memory Storage) depends on User Story 1 (Todo Data Structure)
- User Story 4 (Status Handling) depends on User Story 1 (Todo Data Structure)

## Parallel Execution Opportunities

- ID Generator implementation can run in parallel with storage implementation
- Unit tests can be developed in parallel with implementation tasks

## Implementation Strategy

- **MVP Scope**: Implement User Story 1 (Todo Data Structure) first with minimal functionality
- **Incremental Delivery**: Each user story builds upon the previous one
- **Independent Testing**: Each user story can be tested independently

---

## Phase 1: Setup

- [ ] T001 Create project structure per implementation plan: src/models/, src/services/, src/lib/, tests/unit/, tests/integration/
- [ ] T002 Set up Python 3.13+ project with proper type hints configuration
- [ ] T003 Create initial directory structure for models, services, and utilities

## Phase 2: Foundational Components

- [ ] T004 [P] Create base requirements file with dependencies
- [ ] T005 [P] Set up testing framework (pytest) configuration

## Phase 3: User Story 1 - Todo Data Structure (Priority: P1)

**Goal**: Define the core Todo entity with proper attributes and data types to represent tasks in the system.

**Independent Test**: Can be fully tested by creating Todo entities with different attributes and verifying they maintain their properties correctly.

- [ ] T006 [P] [US1] Define Todo type with type hints in src/models/todo.py
- [ ] T007 [P] [US1] Implement Todo entity with id, title, description, creation timestamp, and status fields
- [ ] T008 [P] [US1] Add validation to ensure title is not empty or None
- [ ] T009 [P] [US1] Implement datetime handling for created_at and updated_at fields
- [ ] T010 [P] [US1] Add default value for completed field (False)
- [ ] T011 [P] [US1] Create Todo data validation methods
- [ ] T012 [P] [US1] Add string representation method for Todo entity

## Phase 4: User Story 3 - ID Strategy (Priority: P3)

**Goal**: Implement a unique ID generation strategy for Todo items to ensure each item can be uniquely identified.

**Independent Test**: Can be tested by creating multiple Todo items and verifying each has a unique identifier.

- [ ] T013 [P] [US3] Create TodoIdGenerator component in src/lib/id_generator.py
- [ ] T014 [P] [US3] Implement generate_id() method that returns unique integer IDs
- [ ] T015 [P] [US3] Implement reset() method to reset the ID generator
- [ ] T016 [P] [US3] Add current_id field to track the current ID value
- [ ] T017 [P] [US3] Ensure ID generation is thread-safe if needed
- [ ] T018 [P] [US3] Test ID uniqueness across multiple generations

## Phase 5: User Story 2 - In-Memory Storage Mechanism (Priority: P2)

**Goal**: Implement an in-memory storage system that can hold multiple Todo items without persistence.

**Independent Test**: Can be tested by adding, retrieving, updating, and deleting Todo items in the storage system.

- [ ] T019 [P] [US2] Define TodoStorage entity in src/models/todo_storage.py
- [ ] T020 [P] [US2] Implement todos dictionary field with ID as key and Todo as value
- [ ] T021 [P] [US2] Implement next_id field to track the next available ID
- [ ] T022 [P] [US2] Implement add_todo(todo: Todo) -> Todo method
- [ ] T023 [P] [US2] Implement get_todo(todo_id: int) -> Optional[Todo] method
- [ ] T024 [P] [US2] Implement update_todo(todo_id: int, title: str = None, description: str = None, completed: bool = None) -> Optional[Todo] method
- [ ] T025 [P] [US2] Implement delete_todo(todo_id: int) -> bool method
- [ ] T026 [P] [US2] Implement list_todos(completed: Optional[bool] = None) -> List[Todo] method
- [ ] T027 [P] [US2] Implement mark_complete(todo_id: int) -> Optional[Todo] method
- [ ] T028 [P] [US2] Implement mark_incomplete(todo_id: int) -> Optional[Todo] method
- [ ] T029 [P] [US2] Add integration with TodoIdGenerator for new Todo items

## Phase 6: User Story 4 - Status Handling (Priority: P4)

**Goal**: Implement status management for Todo items to track completion state.

**Independent Test**: Can be tested by changing status of Todo items and verifying the status changes are properly maintained.

- [ ] T030 [P] [US4] Enhance Todo entity to properly handle status transitions
- [ ] T031 [P] [US4] Implement status validation to ensure only boolean values
- [ ] T032 [P] [US4] Add state transition tracking for Created, Updated, Completed, Reopened
- [ ] T033 [P] [US4] Update updated_at timestamp when status changes
- [ ] T034 [P] [US4] Ensure status methods properly update the Todo's completed field

## Phase 7: Validation and Error Handling

**Goal**: Add validation and error handling to ensure robust operation.

- [ ] T035 [P] Add validation to prevent duplicate IDs in storage
- [ ] T036 [P] Implement proper error handling for missing todo IDs
- [ ] T037 [P] Add validation for required fields during Todo creation
- [ ] T038 [P] Implement error messages for invalid operations
- [ ] T039 [P] Add input validation for all public methods
- [ ] T040 [P] Create custom exceptions for domain-specific errors

## Phase 8: Unit Testing

**Goal**: Create comprehensive unit tests for all components.

- [ ] T041 [P] Create unit tests for Todo entity in tests/unit/test_todo.py
- [ ] T042 [P] Create unit tests for TodoIdGenerator in tests/unit/test_id_generator.py
- [ ] T043 [P] Create unit tests for TodoStorage in tests/unit/test_todo_storage.py
- [ ] T044 [P] Test all validation rules and error conditions
- [ ] T045 [P] Test all state transitions and status handling
- [ ] T046 [P] Test edge cases and boundary conditions

## Phase 9: Integration Testing

**Goal**: Create integration tests to verify components work together.

- [ ] T047 [P] Create integration tests for TodoStorage operations
- [ ] T048 [P] Test the integration between Todo, TodoStorage, and TodoIdGenerator
- [ ] T049 [P] Test full CRUD operations with all components
- [ ] T050 [P] Test performance with multiple Todo items

## Phase 10: Polish & Cross-Cutting Concerns

**Goal**: Final implementation touches and documentation.

- [ ] T051 [P] Add comprehensive docstrings to all classes and methods
- [ ] T052 [P] Review and optimize performance of operations
- [ ] T053 [P] Ensure all type hints are properly implemented
- [ ] T054 [P] Run all tests and verify they pass
- [ ] T055 [P] Update project documentation
- [ ] T056 [P] Save final spec to /specs/history directory