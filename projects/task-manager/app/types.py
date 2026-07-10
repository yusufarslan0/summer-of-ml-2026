from typing import TypedDict


class TaskData(TypedDict):
    id: int
    title: str
    completed: bool