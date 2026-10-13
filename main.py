from src.task import Task


def main() -> None:
    task = Task(1, "  Learn Python OOP  ")
    print(task)
    task.mark_done()
    print(task)
    print(task.to_dict())

    try:
        task.title = "   "
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()