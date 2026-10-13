# To-do List (Python, OOP)

Command-line to-do list application written in Python with a focus on clean
object-oriented design. Tasks are stored in a JSON file, so they persist
between runs.

## Features

- Add, complete and remove tasks
- Show all tasks or only pending ones
- Persistent storage in `tasks.json`
- Input validation and clear error messages
- Unit tests with `pytest`

## Project structure

```
todo-list/
├── src/
│   ├── task.py          # Task entity (validation, serialization)
│   ├── task_manager.py  # Business logic for managing tasks
│   ├── storage.py       # TaskStorage interface + JSON implementation
│   └── app.py           # Command-line interface
├── tests/               # pytest unit tests
├── main.py              # Entry point
└── requirements.txt
```

## Design notes

- **Single responsibility:** each class has one job (entity, logic, storage, UI).
- **Encapsulation:** private attributes and read-only properties in `Task`.
- **Abstraction and polymorphism:** `TaskStorage` is an abstract interface, so
  the JSON storage can be replaced (e.g. with SQLite) without changing other code.
- **Dependency injection:** `TodoApp` receives its manager and storage
  through the constructor.
- **Custom exceptions:** `TaskNotFoundError` and `StorageError`.

## Getting started

```bash
git clone https://github.com/lipaluka/todo-list.git
cd todo-list
python -m venv .venv
.venv\Scripts\Activate.ps1        # Windows (PowerShell)
# source .venv/bin/activate       # macOS / Linux
pip install -r requirements.txt
python main.py
```

## Running tests

```bash
pytest -v
```

## Possible improvements

- SQLite storage implementation
- Due dates and priorities
- Web interface (FastAPI)