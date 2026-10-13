import pytest

from src.task import Task


def test_new_task_is_not_done():
    task = Task(1, "Buy milk")

    assert task.is_done is False


def test_title_is_stripped():
    task = Task(1, "  Buy milk  ")

    assert task.title == "Buy milk"


def test_empty_title_raises_error():
    with pytest.raises(ValueError):
        Task(1, "   ")


def test_mark_done_and_undone():
    task = Task(1, "Buy milk")

    task.mark_done()
    assert task.is_done is True

    task.mark_undone()
    assert task.is_done is False


def test_id_is_read_only():
    task = Task(1, "Buy milk")

    with pytest.raises(AttributeError):
        task.id = 2


def test_to_dict_and_from_dict_round_trip():
    original = Task(5, "Čaša vode", is_done=True)

    restored = Task.from_dict(original.to_dict())

    assert restored.id == original.id
    assert restored.title == original.title
    assert restored.is_done == original.is_done
    assert restored.created_at == original.created_at