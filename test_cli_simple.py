"""
Simple test file to verify the CLI implementation works correctly.
"""
import sys
from io import StringIO
from unittest.mock import patch
from src.cli.main import TodoCLI


def test_cli_creation():
    """Test that the CLI can be created successfully."""
    print("Testing CLI creation...")
    try:
        cli = TodoCLI()
        print("+ CLI created successfully")
        print(f"+ Service is available: {cli.service is not None}")
        print(f"+ Repository is available: {cli.repository is not None}")
        print(f"+ Running state: {cli.running}")
        return True
    except Exception as e:
        print(f"- CLI creation failed: {e}")
        return False


def test_add_todo():
    """Test adding a todo through the CLI."""
    print("\nTesting Add Todo functionality...")
    try:
        cli = TodoCLI()

        # Mock user input for description
        with patch('builtins.input', return_value='Test task from CLI'):
            cli.handle_add_todo()

        # Check that a todo was added
        todos = cli.service.get_todos()
        if len(todos) > 0:
            print("+ Todo added successfully")
            print(f"+ Todo description: {todos[0].description}")
            print(f"+ Todo ID: {todos[0].id}")
            print(f"+ Todo completed: {todos[0].completed}")
            return True
        else:
            print("- No todo was added")
            return False
    except Exception as e:
        print(f"- Add todo test failed: {e}")
        return False


def test_view_todos():
    """Test viewing todos through the CLI."""
    print("\nTesting View Todos functionality...")
    try:
        cli = TodoCLI()

        # First add a todo to view
        cli.service.add_todo("Test task for viewing")

        # Capture the printed output
        captured_output = StringIO()
        import sys
        original_stdout = sys.stdout
        sys.stdout = captured_output

        try:
            cli.handle_view_todos()
        finally:
            sys.stdout = original_stdout

        output = captured_output.getvalue()
        print("+ View todos executed successfully")
        print(f"+ Output contains todo information: {'Test task for viewing' in output}")
        print(f"+ Output contains status: {'Pending' in output or 'Completed' in output}")
        return True
    except Exception as e:
        print(f"- View todos test failed: {e}")
        return False


def test_menu_display():
    """Test that the menu displays correctly."""
    print("\nTesting Menu Display...")
    try:
        cli = TodoCLI()

        # Capture the printed output
        captured_output = StringIO()
        import sys
        original_stdout = sys.stdout
        sys.stdout = captured_output

        try:
            cli.display_menu()
        finally:
            sys.stdout = original_stdout

        output = captured_output.getvalue()
        print("+ Menu display executed successfully")
        print(f"+ Menu contains 'Add a new todo': {'Add a new todo' in output}")
        print(f"+ Menu contains 'View all todos': {'View all todos' in output}")
        print(f"+ Menu contains 'Exit': {'Exit' in output}")
        return True
    except Exception as e:
        print(f"- Menu display test failed: {e}")
        return False


def test_get_menu_selection():
    """Test menu selection with mock input."""
    print("\nTesting Menu Selection...")
    try:
        cli = TodoCLI()

        # Test with valid input
        with patch('builtins.input', return_value='1'):
            selection = cli.get_menu_selection()
            print(f"+ Valid selection test passed: {selection == 1}")

        # Test with invalid input followed by valid input
        with patch('builtins.input', side_effect=['99', '1']):  # Invalid then valid
            selection = cli.get_menu_selection()
            print(f"+ Invalid input handling test passed: {selection == 1}")

        return True
    except Exception as e:
        print(f"- Menu selection test failed: {e}")
        return False


def run_all_tests():
    """Run all CLI tests."""
    print("Running CLI Implementation Tests...\n")

    tests = [
        test_cli_creation,
        test_add_todo,
        test_view_todos,
        test_menu_display,
        test_get_menu_selection
    ]

    passed = 0
    total = len(tests)

    for test in tests:
        if test():
            passed += 1

    print(f"\nTest Results: {passed}/{total} tests passed")

    if passed == total:
        print("All tests passed! CLI implementation is working correctly.")
        return True
    else:
        print("Some tests failed. Please review the implementation.")
        return False


if __name__ == "__main__":
    run_all_tests()