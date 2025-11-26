import sys

class TodoList:
    """A simple command-line Todo List manager."""
    def __init__(self):
        # The list stores tuples of (task_description, is_completed)
        self.tasks = []

    def add_task(self, task_desc):
        """Adds a new task to the list (initially not completed)."""
        if not task_desc:
            return "Error: Task description cannot be empty."
        self.tasks.append((task_desc, False))
        return f"Task added: '{task_desc}'"

    def view_tasks(self):
        """Returns a list of strings representing the current tasks."""
        if not self.tasks:
            return ["Your todo list is empty!"]

        output = []
        for i, (desc, completed) in enumerate(self.tasks):
            status = "[x]" if completed else "[ ]"
            output.append(f"{i+1}. {status} {desc}")
        return output

    def remove_task(self, task_index):
        """Removes a task by its 1-based index."""
        try:
            index = int(task_index) - 1
            if 0 <= index < len(self.tasks):
                removed_task = self.tasks.pop(index)[0]
                return f"Task removed: '{removed_task}'"
            else:
                return "Error: Invalid task number."
        except ValueError:
            return "Error: Task number must be an integer."

    def complete_task(self, task_index):
        """Marks a task as completed by its 1-based index."""
        try:
            index = int(task_index) - 1
            if 0 <= index < len(self.tasks):
                desc, _ = self.tasks[index]
                self.tasks[index] = (desc, True) # Update task status
                return f"Task marked as complete: '{desc}'"
            else:
                return "Error: Invalid task number."
        except ValueError:
            return "Error: Task number must be an integer."


def main(args):
    """Parses command line arguments and runs the todo app."""
    todo_list = TodoList()

    # Simple load/save logic could go here, but omitted for simplicity

    if len(args) < 2:
        print("Usage: python todo_cli.py <command> [arguments]")
        print("Commands: add <task_description>, view, remove <task_number>, complete <task_number>")
        return

    command = args[1]
    result = None

    if command == "add" and len(args) > 2:
        task_desc = " ".join(args[2:])
        result = todo_list.add_task(task_desc)
    elif command == "view":
        results = todo_list.view_tasks()
        print("\n*** TODO LIST ***")
        for line in results:
            print(line)
        print("*****************\n")
        return
    elif command == "remove" and len(args) == 3:
        result = todo_list.remove_task(args[2])
    elif command == "complete" and len(args) == 3:
        result = todo_list.complete_task(args[2])
    else:
        result = f"Error: Unknown command or incorrect arguments for '{command}'."

    if result:
        print(result)

if __name__ == "__main__":
    # The main function is executed when the script is run directly
    # sys.argv is the list of command-line arguments
    # [0] is the script name itself ('todo_cli.py')
    main(sys.argv)