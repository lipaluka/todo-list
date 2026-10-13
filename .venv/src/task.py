from datetime import datetime


class Task:
    """Represents a single to-do item."""

    def __init__(
        self,
        task_id: int,
        title: str,
        is_done: bool = False,
        created_at: datetime | None = None,
    ) -> None:
        self._id = task_id
        self.title = title  # goes through the setter, so validation runs
        self._is_done = is_done
        self._created_at = created_at or datetime.now()

    # ---------- properties (controlled access to attributes) ----------

    @property
    def id(self) -> int:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        value = value.strip()
        if not value:
            raise ValueError("Title cannot be empty.")
        self._title = value

    @property
    def is_done(self) -> bool:
        return self._is_done

    @property
    def created_at(self) -> datetime:
        return self._created_at

    # ---------- behaviour ----------

    def mark_done(self) -> None:
        self._is_done = True

    def mark_undone(self) -> None:
        self._is_done = False

    # ---------- conversion to/from JSON-friendly dict ----------

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "title": self._title,
            "is_done": self._is_done,
            "created_at": self._created_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(
            task_id=data["id"],
            title=data["title"],
            is_done=data["is_done"],
            created_at=datetime.fromisoformat(data["created_at"]),
        )

    def __str__(self) -> str:
        status = "x" if self._is_done else " "
        return f"[{status}] {self._id}. {self._title}"