import pytest

from src.task import Task
from src.task_manager import TaskManager, TaskNotFoundError


@pytest.fixture
def manager() -> TaskManager:
    return TaskManager()


def test_add_task_assigns_incrementing_ids(manager):
    first = manager.add_task("First")
    second = manager.add_task("Second")

    assert (first.id, second.id) == (1, 2)


def test_get_unknown_task_raises_error(manager):
    with pytest.raises(TaskNotFoundError):
        manager.get_task(99)


def test_complete_task(manager):
    task = manager.add_task("Write tests")

    manager.complete_task(task.id)

    assert manager.get_task(task.id).is_done is True


def test_remove_task(manager):
    task = manager.add_task("Temporary")

    manager.remove_task(task.id)

    assert manager.get_all() == []


def test_remove_unknown_task_raises_error(manager):
    with pytest.raises(TaskNotFoundError):
        manager.remove_task(99)


def test_get_all_only_pending(manager):
    done = manager.add_task("Done task")
    manager.add_task("Pending task")
    manager.complete_task(done.id)

    pending = manager.get_all(only_pending=True)

    assert [task.title for task in pending] == ["Pending task"]


def test_next_id_continues_after_loaded_tasks():
    manager = TaskManager([Task(7, "Old task")])

    new_task = manager.add_task("New task")

    assert new_task.id == 8