"""
In-memory repository for Todo items using dictionary storage.
"""
from typing import Dict, List, Optional
from ..models.todo import Todo
from ..lib.exceptions import TodoNotFoundError


class TodoRepository:
    """
    Repository class for handling in-memory storage of Todo items.
    Uses a dictionary for O(1) lookup performance by ID.
    """
    def __init__(self) -> None:
        self._storage: Dict[str, Todo] = {}

    def create(self, todo: Todo) -> Todo:
        """
        Create a new todo item in the repository.

        Args:
            todo: The todo item to create

        Returns:
            The created todo item
        """
        self._storage[todo.id] = todo
        return todo

    def get_all(self) -> List[Todo]:
        """
        Retrieve all todo items from the repository.

        Returns:
            List of all todo items
        """
        return list(self._storage.values())

    def get_by_id(self, todo_id: str) -> Optional[Todo]:
        """
        Retrieve a todo item by its ID.

        Args:
            todo_id: The ID of the todo item to retrieve

        Returns:
            The todo item if found, None otherwise
        """
        return self._storage.get(todo_id)

    def update(self, todo_id: str, updated_todo: Todo) -> Todo:
        """
        Update an existing todo item in the repository.

        Args:
            todo_id: The ID of the todo item to update
            updated_todo: The updated todo item

        Returns:
            The updated todo item

        Raises:
            TodoNotFoundError: If the todo item doesn't exist
        """
        if todo_id not in self._storage:
            raise TodoNotFoundError(todo_id)

        self._storage[todo_id] = updated_todo
        return updated_todo

    def delete(self, todo_id: str) -> bool:
        """
        Delete a todo item from the repository.

        Args:
            todo_id: The ID of the todo item to delete

        Returns:
            True if the item was deleted, False if it didn't exist
        """
        if todo_id in self._storage:
            del self._storage[todo_id]
            return True
        return False