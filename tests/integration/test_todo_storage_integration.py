import pytest
from src.models.todo import Todo
from src.models.todo_storage import TodoStorage
from src.lib.id_generator import TodoIdGenerator
from src.lib.exceptions import TodoNotFoundError, DuplicateTodoError, InvalidTodoError


class TestTodoStorageIntegration:
    """Integration tests for TodoStorage operations."""

    def test_full_crud_operations_with_all_components(self):
        """Test full CRUD operations integrating Todo, TodoStorage, and TodoIdGenerator."""
        # Setup with custom ID generator
        id_generator = TodoIdGenerator(initial_id=100)
        storage = TodoStorage(id_generator=id_generator)

        # Create a todo
        original_todo = Todo(id=0, title="Integration test task", description="Test description")
        created_todo = storage.add_todo(original_todo)

        # Verify the todo was created with a generated ID
        assert created_todo.id == 100
        assert created_todo.title == "Integration test task"
        assert created_todo.description == "Test description"
        assert created_todo.completed is False

        # Read the todo
        retrieved_todo = storage.get_todo(100)
        assert retrieved_todo is not None
        assert retrieved_todo.id == 100
        assert retrieved_todo.title == "Integration test task"

        # Update the todo
        updated_todo = storage.update_todo(100, title="Updated integration task", completed=True)
        assert updated_todo.title == "Updated integration task"
        assert updated_todo.completed is True

        # Verify the update by reading again
        verified_todo = storage.get_todo(100)
        assert verified_todo.title == "Updated integration task"
        assert verified_todo.completed is True

        # Delete the todo
        delete_result = storage.delete_todo(100)
        assert delete_result is True

        # Verify the todo was deleted
        deleted_todo = storage.get_todo(100)
        assert deleted_todo is None

    def test_integration_with_multiple_todos(self):
        """Test integration with multiple todos in storage."""
        storage = TodoStorage()

        # Add multiple todos
        todo1 = Todo(id=0, title="First task")
        todo2 = Todo(id=0, title="Second task")
        todo3 = Todo(id=0, title="Third task", completed=True)

        created1 = storage.add_todo(todo1)
        created2 = storage.add_todo(todo2)
        created3 = storage.add_todo(todo3)

        # Verify they all have unique IDs
        assert created1.id != created2.id
        assert created2.id != created3.id
        assert created1.id != created3.id

        # Verify all todos are stored
        all_todos = storage.list_todos()
        assert len(all_todos) == 3

        # Verify filtering by completion status works
        completed_todos = storage.list_todos(completed=True)
        assert len(completed_todos) == 1
        assert completed_todos[0].id == created3.id

        pending_todos = storage.list_todos(completed=False)
        assert len(pending_todos) == 2

    def test_integration_of_status_operations(self):
        """Test integration of status operations."""
        storage = TodoStorage()
        todo = Todo(id=0, title="Status test task", completed=False)
        created_todo = storage.add_todo(todo)

        # Mark as complete
        completed_todo = storage.mark_complete(created_todo.id)
        assert completed_todo.completed is True

        # Verify the change is persistent
        retrieved_todo = storage.get_todo(created_todo.id)
        assert retrieved_todo.completed is True

        # Mark as incomplete
        incomplete_todo = storage.mark_incomplete(created_todo.id)
        assert incomplete_todo.completed is False

        # Verify the change is persistent
        final_todo = storage.get_todo(created_todo.id)
        assert final_todo.completed is False

    def test_error_handling_integration(self):
        """Test error handling across components."""
        storage = TodoStorage()

        # Try to get a non-existent todo
        nonexistent_todo = storage.get_todo(999)
        assert nonexistent_todo is None

        # Try to update a non-existent todo (should raise exception)
        with pytest.raises(TodoNotFoundError):
            storage.update_todo(999, title="Updated task")

        # Try to delete a non-existent todo (should raise exception)
        with pytest.raises(TodoNotFoundError):
            storage.delete_todo(999)

        # Try to mark complete a non-existent todo (should raise exception)
        with pytest.raises(TodoNotFoundError):
            storage.mark_complete(999)

        # Try to add a duplicate todo (should raise exception)
        valid_todo = Todo(id=1, title="Valid task")
        storage.add_todo(valid_todo)

        duplicate_todo = Todo(id=1, title="Duplicate task")
        with pytest.raises(DuplicateTodoError):
            storage.add_todo(duplicate_todo)

        # Try to add an invalid todo (should raise exception)
        invalid_todo = Todo(id=2, title="Valid task")  # Create valid todo first
        invalid_todo.title = ""  # Then make it invalid
        with pytest.raises(InvalidTodoError):
            storage.add_todo(invalid_todo)

    def test_id_generator_integration(self):
        """Test integration with ID generator."""
        id_generator = TodoIdGenerator(initial_id=500)
        storage = TodoStorage(id_generator=id_generator)

        # Add multiple todos and verify they get sequential IDs
        todo1 = Todo(id=0, title="First task")
        todo2 = Todo(id=0, title="Second task")
        todo3 = Todo(id=0, title="Third task")

        created1 = storage.add_todo(todo1)
        created2 = storage.add_todo(todo2)
        created3 = storage.add_todo(todo3)

        assert created1.id == 500
        assert created2.id == 501
        assert created3.id == 502