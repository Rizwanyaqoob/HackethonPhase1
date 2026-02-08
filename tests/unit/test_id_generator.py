import pytest
from src.lib.id_generator import TodoIdGenerator


class TestTodoIdGenerator:
    """Unit tests for the TodoIdGenerator component."""

    def test_initial_id_generation(self):
        """Test that ID generator starts with the correct initial ID."""
        generator = TodoIdGenerator()

        first_id = generator.generate_id()
        assert first_id == 1

        second_id = generator.generate_id()
        assert second_id == 2

    def test_custom_initial_id(self):
        """Test ID generator with custom initial ID."""
        generator = TodoIdGenerator(initial_id=5)

        first_id = generator.generate_id()
        assert first_id == 5

        second_id = generator.generate_id()
        assert second_id == 6

    def test_unique_id_generation(self):
        """Test that generated IDs are unique."""
        generator = TodoIdGenerator()
        ids = set()

        for i in range(10):
            new_id = generator.generate_id()
            assert new_id not in ids
            ids.add(new_id)

        assert len(ids) == 10
        assert list(ids) == list(range(1, 11))

    def test_reset_functionality(self):
        """Test that the reset method works correctly."""
        generator = TodoIdGenerator()

        # Generate some IDs
        first_id = generator.generate_id()
        second_id = generator.generate_id()
        assert first_id == 1
        assert second_id == 2

        # Reset the generator
        generator.reset()

        # Generate IDs after reset
        reset_first_id = generator.generate_id()
        assert reset_first_id == 1

        reset_second_id = generator.generate_id()
        assert reset_second_id == 2