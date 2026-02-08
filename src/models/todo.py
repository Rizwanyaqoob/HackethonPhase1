from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from ..lib.constants import MAX_DESCRIPTION_LENGTH


@dataclass
class Todo:
    """
    Represents a todo item with description, completion status, and timestamps.
    """
    id: str
    description: str
    completed: bool
    created_at: datetime
    updated_at: datetime

    def __post_init__(self):
        """
        Validate the todo item after initialization.
        """
        if not self.description or not self.description.strip():
            raise ValueError("Description cannot be empty or contain only whitespace")
        if len(self.description) > MAX_DESCRIPTION_LENGTH:
            raise ValueError(f"Description must be less than {MAX_DESCRIPTION_LENGTH} characters")
        if self.created_at > datetime.now():
            raise ValueError("Created timestamp cannot be in the future")
        if self.updated_at < self.created_at:
            raise ValueError("Updated timestamp must be greater than or equal to created timestamp")

    def validate(self) -> bool:
        """
        Validate the todo item.

        Returns:
            True if the todo is valid, False otherwise
        """
        try:
            if not self.description or not self.description.strip():
                return False
            if len(self.description) > MAX_DESCRIPTION_LENGTH:
                return False
            if self.created_at > datetime.now():
                return False
            if self.updated_at < self.created_at:
                return False
            return True
        except:
            return False

    def update(self, description: str = None, completed: bool = None) -> None:
        """
        Update the todo item's description and/or completion status.

        Args:
            description: New description (optional)
            completed: New completion status (optional)
        """
        if description is not None:
            self.description = description
        if completed is not None:
            self.completed = completed
        self.updated_at = datetime.now()

    def mark_complete(self) -> None:
        """
        Mark the todo as complete.
        """
        self.completed = True
        self.updated_at = datetime.now()

    def mark_incomplete(self) -> None:
        """
        Mark the todo as incomplete.
        """
        self.completed = False
        self.updated_at = datetime.now()