from src.app import TodoApp
from src.storage import JsonTaskStorage, StorageError
from src.task_manager import TaskManager


def main() -> None:
    storage = JsonTaskStorage("tasks.json")

    try:
        manager = TaskManager(storage.load())
    except StorageError as error:
        print(f"Error: {error}")
        return

    app = TodoApp(manager, storage)
    app.run()


if __name__ == "__main__":
    main()

