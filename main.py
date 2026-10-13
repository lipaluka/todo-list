from src.storage import JsonTaskStorage
from src.task_manager import TaskManager


def main() -> None:
    storage = JsonTaskStorage("tasks.json")
    manager = TaskManager(storage.load())
    print(f"Loaded {len(manager.get_all())} task(s) from file.\n")

    manager.add_task("Čaša vode")  # test for Croatian characters
    manager.complete_task(1)

    for task in manager.get_all():
        print(task)

    storage.save(manager.get_all())


if __name__ == "__main__":
    main()