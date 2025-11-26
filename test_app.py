import unittest
from app import TodoList 

class TestTodoList(unittest.TestCase):
    """Tests for the TodoList class."""

    def setUp(self):
        """Set up a new, empty TodoList before each test method."""
        self.todo = TodoList()

    def test_add_task(self):
        """Test adding a single task."""
        result = self.todo.add_task("Buy groceries")
        self.assertEqual(result, "Task added: 'Buy groceries'")
        self.assertEqual(len(self.todo.tasks), 1)
        # Check task details: (description, completed=False)
        self.assertEqual(self.todo.tasks[0], ("Buy groceries", False))

    def test_add_empty_task(self):
        """Test adding an empty task description."""
        result = self.todo.add_task("")
        self.assertEqual(result, "Error: Task description cannot be empty.")
        self.assertEqual(len(self.todo.tasks), 0)

    def test_view_tasks_empty(self):
        """Test viewing tasks when the list is empty."""
        output = self.todo.view_tasks()
        self.assertEqual(output, ["Your todo list is empty!"])

    def test_view_tasks_with_items(self):
        """Test viewing tasks with a mix of completed and uncompleted items."""
        self.todo.add_task("Walk the dog")
        self.todo.add_task("Finish report")
        self.todo.complete_task(1) # Complete the first task

        output = self.todo.view_tasks()
        expected = [
            "1. [x] Walk the dog",
            "2. [ ] Finish report"
        ]
        self.assertEqual(output, expected)

    def test_remove_task_valid(self):
        """Test removing a task by a valid index."""
        self.todo.add_task("Task 1")
        self.todo.add_task("Task 2")
        self.todo.add_task("Task 3")

        result = self.todo.remove_task(2) # Remove the second task
        self.assertEqual(result, "Task removed: 'Task 2'")
        self.assertEqual(len(self.todo.tasks), 2)
        # Check that the remaining tasks are correct
        self.assertEqual(self.todo.tasks[0][0], "Task 1")
        self.assertEqual(self.todo.tasks[1][0], "Task 3")

    def test_remove_task_invalid_index(self):
        """Test removing a task with an index that is out of bounds."""
        self.todo.add_task("Only task")
        result_high = self.todo.remove_task(5)
        result_low = self.todo.remove_task(0)
        
        self.assertEqual(result_high, "Error: Invalid task number.")
        self.assertEqual(result_low, "Error: Invalid task number.")
        self.assertEqual(len(self.todo.tasks), 1)

    def test_complete_task_valid(self):
        """Test marking a task as complete."""
        self.todo.add_task("Uncompleted task")
        self.todo.add_task("Another task")

        result = self.todo.complete_task(1)
        self.assertEqual(result, "Task marked as complete: 'Uncompleted task'")
        # Check status in the internal list
        self.assertEqual(self.todo.tasks[0], ("Uncompleted task", True))
        self.assertEqual(self.todo.tasks[1], ("Another task", False))

    def test_complete_task_invalid_input(self):
        """Test completing a task with non-integer input."""
        self.todo.add_task("Task to complete")
        result = self.todo.complete_task("one")
        self.assertEqual(result, "Error: Task number must be an integer.")
        
if __name__ == '__main__':
    unittest.main()