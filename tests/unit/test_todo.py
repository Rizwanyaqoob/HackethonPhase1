import pytest
from datetime import datetime
from src.models.todo import Todo


class TestTodo:
    """Unit tests for the Todo entity."""

    def test_todo_creation_with_valid_data(self):
        """Test creating a Todo with valid data."""
        todo = Todo(id=1, title="Test task", description="Test description")

        assert todo.id == 1
        assert todo.title == "Test task"
        assert todo.description == "Test description"
        assert todo.completed is False
        assert isinstance(todo.created_at, datetime)
        assert isinstance(todo.updated_at, datetime)

    def test_todo_creation_with_completed_true(self):
        """Test creating a Todo with completed status."""
        todo = Todo(id=1, title="Test task", completed=True)

        assert todo.completed is True

    def test_todo_creation_with_empty_title_raises_error(self):
        """Test that creating a Todo with empty title raises an error."""
        with pytest.raises(ValueError, match="Title must not be empty or None"):
            Todo(id=1, title="")

    def test_todo_creation_with_none_title_raises_error(self):
        """Test that creating a Todo with None title raises an error."""
        with pytest.raises(ValueError, match="Title must not be empty or None"):
            Todo(id=1, title=None)

    def test_todo_creation_with_whitespace_title_raises_error(self):
        """Test that creating a Todo with whitespace-only title raises an error."""
        with pytest.raises(ValueError, match="Title must not be empty or None"):
            Todo(id=1, title="   ")

    def test_todo_update_method(self):
        """Test updating a Todo's attributes."""
        todo = Todo(id=1, title="Original task", description="Original description")

        original_updated_at = todo.updated_at
        todo.update(title="Updated task", description="Updated description", completed=True)

        assert todo.title == "Updated task"
        assert todo.description == "Updated description"
        assert todo.completed is True
        assert todo.updated_at > original_updated_at

    def test_todo_update_with_invalid_title_raises_error(self):
        """Test that updating a Todo with invalid title raises an error."""
        todo = Todo(id=1, title="Original task")

        with pytest.raises(ValueError, match="Title must not be empty or None"):
            todo.update(title="")

    def test_todo_update_with_invalid_completed_type_raises_error(self):
        """Test that updating a Todo with invalid completed type raises an error."""
        todo = Todo(id=1, title="Original task")

        with pytest.raises(ValueError, match="Completed must be a boolean value"):
            todo.update(completed="invalid")

    def test_todo_validate_method(self):
        """Test the validate method."""
        todo = Todo(id=1, title="Test task")

        assert todo.validate() is True

        # Test with empty title
        todo.title = ""
        assert todo.validate() is False

        # Test with non-boolean completed
        todo.title = "Valid title"
        # We can't directly set completed to non-boolean due to validation in update method
        # So we'll test by directly setting the attribute (not recommended in real code)
        todo.completed = "invalid"
        assert todo.validate() is False

    def test_todo_string_representation(self):
        """Test the string representation of a Todo."""
        todo = Todo(id=1, title="Test task", completed=False)

        str_repr = str(todo)
        assert "Todo(id=1, title='Test task', status=Pending)" in str_repr

        todo.completed = True
        str_repr = str(todo)
        assert "Todo(id=1, title='Test task', status=Completed)" in str_repr

    def test_todo_repr_method(self):
        """Test the detailed string representation of a Todo."""
        todo = Todo(id=1, title="Test task", description="Test description")

        repr_str = repr(todo)
        assert "Todo(id=1, title='Test task'" in repr_str
        assert "description='Test description'" in repr_str

    def test_mark_complete_method(self):
        """Test marking a todo as complete."""
        todo = Todo(id=1, title="Test task", completed=False)
        original_updated_at = todo.updated_at

        todo.mark_complete()

        assert todo.completed is True
        assert todo.updated_at > original_updated_at

    def test_mark_incomplete_method(self):
        """Test marking a todo as incomplete."""
        todo = Todo(id=1, title="Test task", completed=True)
        original_updated_at = todo.updated_at

        todo.mark_incomplete()

        assert todo.completed is False
        assert todo.updated_at > original_updated_at