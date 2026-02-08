from typing import Dict, List, Optional
from datetime import datetime
from .todo import Todo
from ..lib.id_generator import TodoIdGenerator
from ..lib.exceptions import TodoNotFoundError, DuplicateTodoError, InvalidTodoError


class TodoStorage:
    """
    In-memory storage mechanism that manages multiple Todo items.
    """

    def __init__(self, id_generator: Optional[TodoIdGenerator] = None):
        """
        Initialize the Todo storage.

        Args:
            id_generator: ID generator instance (optional, creates default if None)
        """
        self.todos: Dict[str, Todo] = {}  # Changed from int to str for UUID
        self.id_generator = id_generator or TodoIdGenerator()

    def add_todo(self, todo: Todo) -> Todo:
        """
        Add a new todo to the storage.

        Args:
            todo: The todo item to add

        Returns:
            The added todo item

        Raises:
            DuplicateTodoError: If a todo with the same ID already exists
            InvalidTodoError: If the todo is invalid
        """
        # Validate the todo before adding
        if not todo.validate():
            raise InvalidTodoError(f"Invalid todo item: {todo.description}")

        # If the todo doesn't have an ID, assign one using the generator
        if not todo.id or todo.id is None:
            todo.id = self.id_generator.generate_id()
        elif todo.id in self.todos:
            raise DuplicateTodoError(f"Todo with ID {todo.id} already exists")

        self.todos[todo.id] = todo
        return todo

    def get_todo(self, todo_id: str) -> Optional[Todo]:
        """
        Retrieve a todo by its ID.

        Args:
            todo_id: The ID of the todo to retrieve

        Returns:
            The todo if found, None otherwise
        """
        return self.todos.get(todo_id)

    def update_todo(
        self,
        todo_id: str,
        title: Optional[str] = None,
        description: Optional[str] = None,
        completed: Optional[bool] = None
    ) -> Optional[Todo]:
        """
        Update a todo's attributes.

        Args:
            todo_id: The ID of the todo to update
            title: New title (optional)
            description: New description (optional)
            completed: New completion status (optional)

        Returns:
            The updated todo if found, None otherwise

        Raises:
            TodoNotFoundError: If the todo with the given ID is not found
            InvalidTodoError: If the update results in an invalid todo
        """
        if todo_id not in self.todos:
            raise TodoNotFoundError(f"Todo with ID {todo_id} not found")

        todo = self.todos[todo_id]

        # Handle potential ValueError from Todo.update and convert to InvalidTodoError
        try:
            # Use description parameter instead of title (as Todo model uses description)
            todo.update(description=description, completed=completed)
        except ValueError as e:
            raise InvalidTodoError("Invalid todo after update")

        # Validate the updated todo
        if not todo.validate():
            raise InvalidTodoError(f"Invalid todo after update: {todo.description}")

        return todo

    def delete_todo(self, todo_id: str) -> bool:
        """
        Delete a todo by its ID.

        Args:
            todo_id: The ID of the todo to delete

        Returns:
            True if the todo was deleted, False if it didn't exist

        Raises:
            TodoNotFoundError: If the todo with the given ID is not found
        """
        if todo_id not in self.todos:
            raise TodoNotFoundError(f"Todo with ID {todo_id} not found")

        del self.todos[todo_id]
        return True

    def list_todos(self, completed: Optional[bool] = None) -> List[Todo]:
        """
        List all todos, optionally filtered by completion status.

        Args:
            completed: Filter by completion status (True=completed, False=not completed, None=all)

        Returns:
            List of todos matching the filter
        """
        if completed is None:
            return list(self.todos.values())

        return [todo for todo in self.todos.values() if todo.completed == completed]

    def mark_complete(self, todo_id: str) -> Optional[Todo]:
        """
        Mark a todo as complete.

        Args:
            todo_id: The ID of the todo to mark as complete

        Returns:
            The updated todo if found, None otherwise

        Raises:
            TodoNotFoundError: If the todo with the given ID is not found
        """
        if todo_id not in self.todos:
            raise TodoNotFoundError(f"Todo with ID {todo_id} not found")

        todo = self.todos[todo_id]
        todo.mark_complete()
        return todo

    def mark_incomplete(self, todo_id: str) -> Optional[Todo]:
        """
        Mark a todo as incomplete.

        Args:
            todo_id: The ID of the todo to mark as incomplete

        Returns:
            The updated todo if found, None otherwise

        Raises:
            TodoNotFoundError: If the todo with the given ID is not found
        """
        if todo_id not in self.todos:
            raise TodoNotFoundError(f"Todo with ID {todo_id} not found")

        todo = self.todos[todo_id]
        todo.mark_incomplete()
        return todo