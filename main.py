from src.task_manager import TaskManager, TaskNotFoundError


def main() -> None:
    manager = TaskManager()
    manager.add_task("Buy milk")
    manager.add_task("Learn Python OOP")
    manager.add_task("Push project to GitHub")

    manager.complete_task(2)

    print("All tasks:")
    for task in manager.get_all():
        print(task)

    print("\nPending tasks:")
    for task in manager.get_all(only_pending=True):
        print(task)

    manager.remove_task(1)

    try:
        manager.remove_task(99)
    except TaskNotFoundError as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()