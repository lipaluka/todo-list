import json
from abc import ABC, abstractmethod
from pathlib import Path

from src.task import Task


class StorageError(Exception):
    """Raised when tasks cannot be saved to or loaded from storage."""


class TaskStorage(ABC):
    """Interface: any class that can save and load tasks must follow it."""

    @abstractmethod
    def save(self, tasks: list[Task]) -> None:
        """Persist the given tasks."""

    @abstractmethod
    def load(self) -> list[Task]:
        """Return all persisted tasks."""


class JsonTaskStorage(TaskStorage):
    """Stores tasks in a JSON file."""

    def __init__(self, file_path: str | Path = "tasks.json") -> None:
        self._file_path = Path(file_path)

    def save(self, tasks: list[Task]) -> None:
        data = [task.to_dict() for task in tasks]
        try:
            with self._file_path.open("w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
        except OSError as error:
            raise StorageError(f"Could not save tasks: {error}") from error

    def load(self) -> list[Task]:
        if not self._file_path.exists():
            return []
        try:
            with self._file_path.open("r", encoding="utf-8") as file:
                data = json.load(file)
            return [Task.from_dict(item) for item in data]
        except (OSError, ValueError, KeyError, TypeError) as error:
            raise StorageError(f"Could not load tasks: {error}") from error