from src.storage import StorageError, TaskStorage
from src.task import Task
from src.task_manager import TaskManager, TaskNotFoundError


class TodoApp:
    """Command-line interface that connects the user, the manager and the storage."""

    MENU = (
        "\n=== To-do list ===\n"
        "1. Show all tasks\n"
        "2. Show pending tasks\n"
        "3. Add task\n"
        "4. Complete task\n"
        "5. Remove task\n"
        "0. Exit"
    )

    def __init__(self, manager: TaskManager, storage: TaskStorage) -> None:
        self._manager = manager
        self._storage = storage
        self._actions = {
            "1": self._show_all,
            "2": self._show_pending,
            "3": self._add_task,
            "4": self._complete_task,
            "5": self._remove_task,
        }

    def run(self) -> None:
        while True:
            print(self.MENU)
            choice = input("Choose an option: ").strip()

            if choice == "0":
                print("Goodbye!")
                break

            action = self._actions.get(choice)
            if action is None:
                print("Invalid option, try again.")
                continue

            try:
                action()
            except (TaskNotFoundError, ValueError, StorageError) as error:
                print(f"Error: {error}")

    # ---------- menu actions ----------

    def _show_all(self) -> None:
        self._print_tasks(self._manager.get_all())

    def _show_pending(self) -> None:
        self._print_tasks(self._manager.get_all(only_pending=True))

    def _add_task(self) -> None:
        title = input("Task title: ")
        task = self._manager.add_task(title)
        self._save()
        print(f"Added: {task}")

    def _complete_task(self) -> None:
        task_id = self._read_task_id()
        self._manager.complete_task(task_id)
        self._save()
        print("Task marked as done.")

    def _remove_task(self) -> None:
        task_id = self._read_task_id()
        self._manager.remove_task(task_id)
        self._save()
        print("Task removed.")

    # ---------- helpers ----------

    def _save(self) -> None:
        self._storage.save(self._manager.get_all())

    @staticmethod
    def _read_task_id() -> int:
        raw = input("Task id: ").strip()
        if not raw.isdigit():
            raise ValueError("Id must be a positive whole number.")
        return int(raw)

    @staticmethod
    def _print_tasks(tasks: list[Task]) -> None:
        if not tasks:
            print("No tasks.")
            return
        for task in tasks:
            print(task)