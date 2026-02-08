"""
Console interface for the Todo application.
Implements the CLI menu system according to the console_ui_pattern.md specification.
"""
from typing import Optional
import sys
import os

# Add the project root directory to the Python path to handle imports correctly
# This allows the module to be run from any location
current_dir = os.path.dirname(os.path.abspath(__file__))  # src/cli/
parent_dir = os.path.dirname(current_dir)  # src/
project_root = os.path.dirname(parent_dir)  # project root

# Insert the project root at the beginning of sys.path to ensure proper imports
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Import using absolute paths from the project root
from src.services.todo_service import TodoService
from src.models.repository import TodoRepository
from src.lib.exceptions import TodoNotFoundError, InvalidTodoError
from src.lib.constants import MAX_DESCRIPTION_LENGTH


class TodoCLI:
    """
    Console interface for the Todo application.
    Implements a menu-driven system with numbered options for all CRUD operations.
    """

    def __init__(self):
        """Initialize the CLI with the Todo service."""
        self.repository = TodoRepository()
        self.service = TodoService(self.repository)
        self.running = True

    def display_menu(self):
        """Display the main menu with numbered options."""
        print("\n=== Todo Application ===")
        print("1. Add a new todo")
        print("2. View all todos")
        print("3. Update a todo")
        print("4. Delete a todo")
        print("5. Mark todo as complete/incomplete")
        print("6. Exit")
        print("========================")

    def get_menu_selection(self) -> int:
        """
        Get and validate user menu selection.

        Returns:
            int: Valid menu selection (1-6)
        """
        while True:
            try:
                selection = input("Please select an option (1-6): ").strip()
                if not selection.isdigit():
                    print("Error: Please enter a number between 1 and 6.")
                    continue

                selection_int = int(selection)
                if selection_int < 1 or selection_int > 6:
                    print("Error: Please enter a number between 1 and 6.")
                    continue

                return selection_int
            except (ValueError, EOFError):
                print("Error: Please enter a valid number between 1 and 6.")
                continue

    def handle_add_todo(self):
        """Handle adding a new todo."""
        try:
            description = input("Enter todo description: ").strip()

            # Validate description
            if not description:
                print("Error: Description cannot be empty.")
                return
            if len(description) > MAX_DESCRIPTION_LENGTH:
                print(f"Error: Description must be less than {MAX_DESCRIPTION_LENGTH} characters.")
                return

            # Add the todo
            todo = self.service.add_todo(description)
            print(f"Success: Added todo '{todo.description}' with ID: {todo.id}")

        except InvalidTodoError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def handle_view_todos(self):
        """Handle viewing all todos."""
        try:
            todos = self.service.get_todos()

            if not todos:
                print("No todos found.")
                return

            print("\n--- Todo List ---")
            for todo in todos:
                status = "Completed" if todo.completed else "Pending"
                print(f"[{todo.id}] - {todo.description} - {status}")
            print("-----------------")

        except Exception as e:
            print(f"Error viewing todos: {e}")

    def handle_update_todo(self):
        """Handle updating an existing todo."""
        try:
            # Get todo ID
            todo_id = input("Enter the ID of the todo to update: ").strip()

            # Validate ID exists
            try:
                existing_todo = self.service.get_todo(todo_id)
            except TodoNotFoundError:
                print(f"Error: Todo with ID '{todo_id}' not found.")
                return

            # Get new description (optional)
            new_description_input = input(f"Enter new description (leave blank to keep '{existing_todo.description}'): ").strip()
            new_description = new_description_input if new_description_input else None

            # Get new completion status (optional)
            completion_input = input(f"Update completion status? (y/n, leave blank to keep current status): ").strip().lower()
            new_completed = None
            if completion_input in ['y', 'yes']:
                current_status = "completed" if existing_todo.completed else "pending"
                target_status = input(f"Mark as (c)ompleted or (p)ending? (current: {current_status}): ").strip().lower()
                if target_status in ['c', 'completed']:
                    new_completed = True
                elif target_status in ['p', 'pending']:
                    new_completed = False
                else:
                    print("Invalid input. Completion status not changed.")
                    new_completed = None

            # Update the todo
            updated_todo = self.service.update_todo(
                todo_id,
                description=new_description,
                completed=new_completed
            )
            print(f"Success: Updated todo with ID: {updated_todo.id}")

        except InvalidTodoError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def handle_delete_todo(self):
        """Handle deleting a todo."""
        try:
            # Get todo ID
            todo_id = input("Enter the ID of the todo to delete: ").strip()

            # Validate ID exists
            try:
                existing_todo = self.service.get_todo(todo_id)
            except TodoNotFoundError:
                print(f"Error: Todo with ID '{todo_id}' not found.")
                return

            # Confirm deletion
            confirmation = input(f"Are you sure you want to delete '{existing_todo.description}'? (y/n): ").strip().lower()
            if confirmation not in ['y', 'yes']:
                print("Deletion cancelled.")
                return

            # Delete the todo
            self.service.delete_todo(todo_id)
            print(f"Success: Deleted todo with ID: {todo_id}")

        except TodoNotFoundError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def handle_mark_status(self):
        """Handle marking a todo as complete/incomplete."""
        try:
            # Get todo ID
            todo_id = input("Enter the ID of the todo to update status: ").strip()

            # Validate ID exists
            try:
                existing_todo = self.service.get_todo(todo_id)
            except TodoNotFoundError:
                print(f"Error: Todo with ID '{todo_id}' not found.")
                return

            # Get desired status
            current_status = "completed" if existing_todo.completed else "pending"
            target_status = input(f"Mark as (c)ompleted or (p)ending? (current: {current_status}): ").strip().lower()

            if target_status in ['c', 'completed']:
                updated_todo = self.service.mark_complete(todo_id)
                print(f"Success: Marked todo as completed - ID: {updated_todo.id}")
            elif target_status in ['p', 'pending']:
                updated_todo = self.service.mark_incomplete(todo_id)
                print(f"Success: Marked todo as pending - ID: {updated_todo.id}")
            else:
                print("Invalid input. Status not changed.")

        except TodoNotFoundError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def handle_exit(self):
        """Handle exiting the application."""
        print("Thank you for using the Todo Application. Goodbye!")
        self.running = False

    def run(self):
        """Run the main application loop."""
        print("Welcome to the Todo Application!")

        while self.running:
            self.display_menu()
            selection = self.get_menu_selection()

            if selection == 1:
                self.handle_add_todo()
            elif selection == 2:
                self.handle_view_todos()
            elif selection == 3:
                self.handle_update_todo()
            elif selection == 4:
                self.handle_delete_todo()
            elif selection == 5:
                self.handle_mark_status()
            elif selection == 6:
                self.handle_exit()


def main():
    """Main entry point for the CLI application."""
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()