#!/usr/bin/env python3
"""
Example usage of the Todo domain and in-memory store.
This demonstrates the implemented functionality without CLI or I/O.
"""

from src.models.todo import Todo
from src.models.todo_storage import TodoStorage
from src.lib.id_generator import TodoIdGenerator


def example_usage():
    """Example demonstrating the Todo domain functionality."""
    # Create a storage instance with a custom ID generator
    id_generator = TodoIdGenerator(initial_id=100)
    storage = TodoStorage(id_generator=id_generator)

    # Create some todos
    todo1 = Todo(id=0, title="Implement domain model", description="Create the core Todo entities")
    todo2 = Todo(id=0, title="Write tests", description="Create comprehensive test suite")

    # Add todos to storage (IDs will be auto-generated)
    stored_todo1 = storage.add_todo(todo1)
    stored_todo2 = storage.add_todo(todo2)

    # Retrieve a todo
    retrieved_todo = storage.get_todo(stored_todo1.id)

    # Update a todo
    updated_todo = storage.update_todo(
        stored_todo1.id,
        title="Implement domain model - COMPLETED",
        completed=True
    )

    # Mark a todo as complete
    completed_todo = storage.mark_complete(stored_todo2.id)

    # List all todos
    all_todos = storage.list_todos()

    # List only completed todos
    completed_todos = storage.list_todos(completed=True)

    # List only pending todos
    pending_todos = storage.list_todos(completed=False)

    # Return example results to demonstrate functionality
    return {
        'stored_todo1_id': stored_todo1.id,
        'stored_todo2_id': stored_todo2.id,
        'retrieved_title': retrieved_todo.title,
        'updated_title': updated_todo.title,
        'completed_todo_id': completed_todo.id,
        'all_todos_count': len(all_todos),
        'completed_count': len(completed_todos),
        'pending_count': len(pending_todos),
    }


if __name__ == "__main__":
    results = example_usage()
    print("Example completed successfully. Results:")
    for key, value in results.items():
        print(f"  {key}: {value}")