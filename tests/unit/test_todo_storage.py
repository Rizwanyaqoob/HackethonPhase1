import pytest
from datetime import datetime
from src.models.todo import Todo
from src.models.todo_storage import TodoStorage
from src.lib.id_generator import TodoIdGenerator
from src.lib.exceptions import TodoNotFoundError, DuplicateTodoError, InvalidTodoError


class TestTodoStorage:
    """Unit tests for the TodoStorage entity."""

    def test_add_todo_with_valid_todo(self):
        """Test adding a valid todo to storage."""
        storage = TodoStorage()
        todo = Todo(id=1, title="Test task")

        added_todo = storage.add_todo(todo)

        assert added_todo.id == 1
        assert added_todo.title == "Test task"
        assert storage.get_todo(1) is not None

    def test_add_todo_without_id_assigns_generated_id(self):
        """Test that todos without IDs get assigned generated IDs."""
        id_generator = TodoIdGenerator()
        storage = TodoStorage(id_generator=id_generator)

        # Create a todo with ID 0 (which should trigger ID generation)
        todo = Todo(id=0, title="Test task")

        added_todo = storage.add_todo(todo)

        assert added_todo.id == 1  # First generated ID
        assert storage.get_todo(1) is not None

    def test_add_todo_with_duplicate_id_raises_error(self):
        """Test that adding a todo with duplicate ID raises an error."""
        storage = TodoStorage()
        todo1 = Todo(id=1, title="First task")
        todo2 = Todo(id=1, title="Second task")

        storage.add_todo(todo1)

        with pytest.raises(DuplicateTodoError, match="Todo with ID 1 already exists"):
            storage.add_todo(todo2)

    def test_add_invalid_todo_raises_error(self):
        """Test that adding an invalid todo raises an error."""
        storage = TodoStorage()

        # Create a valid todo first, then manipulate its attributes to make it invalid for testing
        valid_todo = Todo(id=1, title="Valid task")
        # Directly manipulate the title to make it invalid (for testing purposes only)
        valid_todo.title = ""

        with pytest.raises(InvalidTodoError, match="Invalid todo item"):
            storage.add_todo(valid_todo)

    def test_get_todo_returns_correct_todo(self):
        """Test that get_todo returns the correct todo."""
        storage = TodoStorage()
        todo = Todo(id=1, title="Test task")
        storage.add_todo(todo)

        retrieved_todo = storage.get_todo(1)

        assert retrieved_todo is not None
        assert retrieved_todo.id == 1
        assert retrieved_todo.title == "Test task"

    def test_get_nonexistent_todo_returns_none(self):
        """Test that get_todo returns None for nonexistent todo."""
        storage = TodoStorage()

        retrieved_todo = storage.get_todo(999)

        assert retrieved_todo is None

    def test_update_todo_updates_attributes(self):
        """Test updating a todo's attributes."""
        storage = TodoStorage()
        todo = Todo(id=1, title="Original task", description="Original description")
        storage.add_todo(todo)

        updated_todo = storage.update_todo(1, title="Updated task", description="Updated description", completed=True)

        assert updated_todo.title == "Updated task"
        assert updated_todo.description == "Updated description"
        assert updated_todo.completed is True

    def test_update_nonexistent_todo_raises_error(self):
        """Test that updating a nonexistent todo raises an error."""
        storage = TodoStorage()

        with pytest.raises(TodoNotFoundError, match="Todo with ID 999 not found"):
            storage.update_todo(999, title="Updated task")

    def test_update_todo_with_invalid_data_raises_error(self):
        """Test that updating a todo with invalid data raises an error."""
        storage = TodoStorage()
        todo = Todo(id=1, title="Original task")
        storage.add_todo(todo)

        with pytest.raises(InvalidTodoError, match="Invalid todo after update"):
            storage.update_todo(1, title="")  # Empty title should be invalid

    def test_delete_todo_removes_from_storage(self):
        """Test that deleting a todo removes it from storage."""
        storage = TodoStorage()
        todo = Todo(id=1, title="Test task")
        storage.add_todo(todo)

        result = storage.delete_todo(1)

        assert result is True
        assert storage.get_todo(1) is None

    def test_delete_nonexistent_todo_raises_error(self):
        """Test that deleting a nonexistent todo raises an error."""
        storage = TodoStorage()

        with pytest.raises(TodoNotFoundError, match="Todo with ID 999 not found"):
            storage.delete_todo(999)

    def test_list_todos_returns_all_todos(self):
        """Test that list_todos returns all todos when no filter is applied."""
        storage = TodoStorage()
        todo1 = Todo(id=1, title="Task 1")
        todo2 = Todo(id=2, title="Task 2")
        storage.add_todo(todo1)
        storage.add_todo(todo2)

        todos = storage.list_todos()

        assert len(todos) == 2
        assert {todo.id for todo in todos} == {1, 2}

    def test_list_todos_with_completed_filter(self):
        """Test that list_todos filters by completion status."""
        storage = TodoStorage()
        todo1 = Todo(id=1, title="Completed task", completed=True)
        todo2 = Todo(id=2, title="Pending task", completed=False)
        storage.add_todo(todo1)
        storage.add_todo(todo2)

        completed_todos = storage.list_todos(completed=True)
        assert len(completed_todos) == 1
        assert completed_todos[0].id == 1

        pending_todos = storage.list_todos(completed=False)
        assert len(pending_todos) == 1
        assert pending_todos[0].id == 2

        all_todos = storage.list_todos(completed=None)
        assert len(all_todos) == 2

    def test_mark_complete_updates_status(self):
        """Test marking a todo as complete."""
        storage = TodoStorage()
        todo = Todo(id=1, title="Test task", completed=False)
        storage.add_todo(todo)

        marked_todo = storage.mark_complete(1)

        assert marked_todo.completed is True

    def test_mark_complete_nonexistent_todo_raises_error(self):
        """Test that marking a nonexistent todo as complete raises an error."""
        storage = TodoStorage()

        with pytest.raises(TodoNotFoundError, match="Todo with ID 999 not found"):
            storage.mark_complete(999)

    def test_mark_incomplete_updates_status(self):
        """Test marking a todo as incomplete."""
        storage = TodoStorage()
        todo = Todo(id=1, title="Test task", completed=True)
        storage.add_todo(todo)

        marked_todo = storage.mark_incomplete(1)

        assert marked_todo.completed is False

    def test_mark_incomplete_nonexistent_todo_raises_error(self):
        """Test that marking a nonexistent todo as incomplete raises an error."""
        storage = TodoStorage()

        with pytest.raises(TodoNotFoundError, match="Todo with ID 999 not found"):
            storage.mark_incomplete(999)