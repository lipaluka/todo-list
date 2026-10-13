import pytest

from src.storage import JsonTaskStorage, StorageError
from src.task import Task


def test_save_and_load_round_trip(tmp_path):
    storage = JsonTaskStorage(tmp_path / "tasks.json")
    tasks = [Task(1, "Čaša vode"), Task(2, "Learn OOP", is_done=True)]

    storage.save(tasks)
    loaded = storage.load()

    assert [task.title for task in loaded] == ["Čaša vode", "Learn OOP"]
    assert loaded[1].is_done is True


def test_load_missing_file_returns_empty_list(tmp_path):
    storage = JsonTaskStorage(tmp_path / "missing.json")

    assert storage.load() == []


def test_load_corrupted_file_raises_storage_error(tmp_path):
    file_path = tmp_path / "tasks.json"
    file_path.write_text("this is not json", encoding="utf-8")

    with pytest.raises(StorageError):
        JsonTaskStorage(file_path).load()