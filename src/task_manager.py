from src.task import Task


class TaskNotFoundError(Exception):
    """Raised when a task with the given id does not exist."""


class TaskManager:
    """Manages a collection of tasks (add, find, complete, remove)."""

    def __init__(self, tasks: list[Task] | None = None) -> None:
        self._tasks: dict[int, Task] = {task.id: task for task in (tasks or [])}
        self._next_id = max(self._tasks, default=0) + 1

    def add_task(self, title: str) -> Task:
        task = Task(self._next_id, title)
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def get_task(self, task_id: int) -> Task:
        try:
            return self._tasks[task_id]
        except KeyError:
            raise TaskNotFoundError(f"Task with id {task_id} not found.") from None

    def complete_task(self, task_id: int) -> None:
        self.get_task(task_id).mark_done()

    def remove_task(self, task_id: int) -> None:
        self.get_task(task_id)  # raises TaskNotFoundError if it does not exist
        del self._tasks[task_id]

    def get_all(self, only_pending: bool = False) -> list[Task]:
        tasks = list(self._tasks.values())
        if only_pending:
            tasks = [task for task in tasks if not task.is_done]
        return tasks