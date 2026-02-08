"""
Service layer for Todo CRUD operations.
Implements business logic and validation for todo operations.
"""
import uuid
from datetime import datetime
from typing import List
from ..models.todo import Todo
from ..models.repository import TodoRepository
from ..lib.exceptions import TodoNotFoundError, InvalidTodoError
from ..lib.validators import validate_description


class TodoService:
    """
    Service class for handling business logic for Todo operations.
    """
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def add_todo(self, description: str) -> Todo:
        """
        Create a new todo item.

        Args:
            description: The description of the todo item

        Returns:
            The created todo item

        Raises:
            InvalidTodoError: If the description is invalid
        """
        # Validate the description
        validate_description(description)

        # Generate unique ID
        todo_id = str(uuid.uuid4())

        # Create timestamps
        now = datetime.now()

        # Create the todo item
        todo = Todo(
            id=todo_id,
            description=description,
            completed=False,
            created_at=now,
            updated_at=now
        )

        # Store in repository
        return self.repository.create(todo)

    def get_todos(self) -> List[Todo]:
        """
        Retrieve all todo items.

        Returns:
            List of all todo items
        """
        return self.repository.get_all()

    def get_todo(self, todo_id: str) -> Todo:
        """
        Retrieve a specific todo item by ID.

        Args:
            todo_id: The ID of the todo item to retrieve

        Returns:
            The todo item

        Raises:
            TodoNotFoundError: If the todo item doesn't exist
        """
        todo = self.repository.get_by_id(todo_id)
        if todo is None:
            raise TodoNotFoundError(todo_id)
        return todo

    def update_todo(self, todo_id: str, description: str = None, completed: bool = None) -> Todo:
        """
        Update an existing todo item.

        Args:
            todo_id: The ID of the todo item to update
            description: The new description (optional)
            completed: The new completion status (optional)

        Returns:
            The updated todo item

        Raises:
            TodoNotFoundError: If the todo item doesn't exist
            InvalidTodoError: If the description is invalid
        """
        # Get the existing todo
        existing_todo = self.repository.get_by_id(todo_id)
        if existing_todo is None:
            raise TodoNotFoundError(todo_id)

        # Use existing values if not provided
        new_description = description if description is not None else existing_todo.description
        new_completed = completed if completed is not None else existing_todo.completed

        # Validate the new description if it's being updated
        if description is not None:
            validate_description(description)

        # Update the timestamps
        now = datetime.now()

        # Create updated todo
        updated_todo = Todo(
            id=existing_todo.id,
            description=new_description,
            completed=new_completed,
            created_at=existing_todo.created_at,
            updated_at=now
        )

        # Update in repository
        return self.repository.update(todo_id, updated_todo)

    def delete_todo(self, todo_id: str) -> bool:
        """
        Delete a todo item.

        Args:
            todo_id: The ID of the todo item to delete

        Returns:
            True if the item was deleted, False if it didn't exist

        Raises:
            TodoNotFoundError: If the todo item doesn't exist
        """
        deleted = self.repository.delete(todo_id)
        if not deleted:
            raise TodoNotFoundError(todo_id)
        return deleted

    def mark_complete(self, todo_id: str) -> Todo:
        """
        Mark a todo item as complete.

        Args:
            todo_id: The ID of the todo item to mark complete

        Returns:
            The updated todo item

        Raises:
            TodoNotFoundError: If the todo item doesn't exist
        """
        # Get the existing todo
        existing_todo = self.repository.get_by_id(todo_id)
        if existing_todo is None:
            raise TodoNotFoundError(todo_id)

        # Update the completion status and timestamp
        now = datetime.now()
        updated_todo = Todo(
            id=existing_todo.id,
            description=existing_todo.description,
            completed=True,
            created_at=existing_todo.created_at,
            updated_at=now
        )

        # Update in repository
        return self.repository.update(todo_id, updated_todo)

    def mark_incomplete(self, todo_id: str) -> Todo:
        """
        Mark a todo item as incomplete.

        Args:
            todo_id: The ID of the todo item to mark incomplete

        Returns:
            The updated todo item

        Raises:
            TodoNotFoundError: If the todo item doesn't exist
        """
        # Get the existing todo
        existing_todo = self.repository.get_by_id(todo_id)
        if existing_todo is None:
            raise TodoNotFoundError(todo_id)

        # Update the completion status and timestamp
        now = datetime.now()
        updated_todo = Todo(
            id=existing_todo.id,
            description=existing_todo.description,
            completed=False,
            created_at=existing_todo.created_at,
            updated_at=now
        )

        # Update in repository
        return self.repository.update(todo_id, updated_todo)