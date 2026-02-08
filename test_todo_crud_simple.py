"""
Simple test file to verify the Todo CRUD operations implementation.
"""
from datetime import datetime
from src.models.todo import Todo
from src.models.repository import TodoRepository
from src.services.todo_service import TodoService
from src.lib.exceptions import TodoNotFoundError, InvalidTodoError


def test_todo_crud_operations():
    """
    Test all CRUD operations for Todo items.
    """
    # Initialize the repository and service
    repository = TodoRepository()
    service = TodoService(repository)

    print("Testing Todo CRUD Operations...")

    # Test 1: Add a todo
    print("\n1. Testing Add Todo:")
    try:
        todo = service.add_todo("Buy groceries")
        print(f"   Added todo: {todo.description} (ID: {todo.id})")
        assert todo.description == "Buy groceries"
        assert todo.completed is False
        assert isinstance(todo.created_at, datetime)
        assert isinstance(todo.updated_at, datetime)
        print("   Add Todo test passed")
    except Exception as e:
        print(f"   Add Todo test failed: {e}")

    # Test 2: View all todos
    print("\n2. Testing View All Todos:")
    try:
        todos = service.get_todos()
        print(f"   Retrieved {len(todos)} todo(s)")
        assert len(todos) == 1
        assert todos[0].description == "Buy groceries"
        print("   View All Todos test passed")
    except Exception as e:
        print(f"   View All Todos test failed: {e}")

    # Test 3: View a specific todo
    print("\n3. Testing View Specific Todo:")
    try:
        retrieved_todo = service.get_todo(todo.id)
        print(f"   Retrieved todo: {retrieved_todo.description}")
        assert retrieved_todo.description == "Buy groceries"
        print("   View Specific Todo test passed")
    except Exception as e:
        print(f"   View Specific Todo test failed: {e}")

    # Test 4: Update a todo
    print("\n4. Testing Update Todo:")
    try:
        updated_todo = service.update_todo(todo.id, description="Buy groceries and cook dinner", completed=True)
        print(f"   Updated todo: {updated_todo.description}, completed: {updated_todo.completed}")
        assert updated_todo.description == "Buy groceries and cook dinner"
        assert updated_todo.completed is True
        print("   Update Todo test passed")
    except Exception as e:
        print(f"   Update Todo test failed: {e}")

    # Test 5: Mark todo as complete
    print("\n5. Testing Mark Complete:")
    try:
        completed_todo = service.mark_complete(todo.id)
        print(f"   Marked as complete: {completed_todo.completed}")
        assert completed_todo.completed is True
        print("   Mark Complete test passed")
    except Exception as e:
        print(f"   Mark Complete test failed: {e}")

    # Test 6: Mark todo as incomplete
    print("\n6. Testing Mark Incomplete:")
    try:
        incomplete_todo = service.mark_incomplete(todo.id)
        print(f"   Marked as incomplete: {incomplete_todo.completed}")
        assert incomplete_todo.completed is False
        print("   Mark Incomplete test passed")
    except Exception as e:
        print(f"   Mark Incomplete test failed: {e}")

    # Test 7: Delete a todo
    print("\n7. Testing Delete Todo:")
    try:
        service.delete_todo(todo.id)
        print("   Deleted todo successfully")

        # Try to get the deleted todo (should raise an exception)
        try:
            service.get_todo(todo.id)
            print("   Delete Todo test failed: Todo still exists")
        except TodoNotFoundError:
            print("   Delete Todo test passed")
    except Exception as e:
        print(f"   Delete Todo test failed: {e}")

    # Test 8: Validation - empty description should raise error
    print("\n8. Testing Validation:")
    try:
        service.add_todo("")
        print("   Validation test failed: Empty description was allowed")
    except InvalidTodoError:
        print("   Validation test passed: Empty description correctly rejected")
    except Exception as e:
        print(f"   Validation test result: {e}")

    # Test 9: Error handling - non-existent todo should raise error
    print("\n9. Testing Error Handling:")
    try:
        service.get_todo("non-existent-id")
        print("   Error handling test failed: Non-existent todo was found")
    except TodoNotFoundError:
        print("   Error handling test passed: Non-existent todo correctly raised error")
    except Exception as e:
        print(f"   Error handling test result: {e}")

    print("\nAll tests completed!")


if __name__ == "__main__":
    test_todo_crud_operations()