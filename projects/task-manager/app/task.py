from app.types import TaskData


class Task:
    def __init__(self, id: int, title: str):
        self.id = id
        self.title = title
        self.completed = False

    def show_task(self) -> None:
        print(f"ID: {self.id}, Task: {self.title} - Completed: {self.completed}")

    def mark_complete(self) -> None:
        self.completed = True

    def rename(self, new_title: str) -> None:
        self.title = new_title

    def to_dict(self) -> TaskData:
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }
    
    @classmethod
    def from_dict(cls, task_dict: TaskData) -> Task:
        task = cls(id=task_dict["id"], title=task_dict["title"])
        task.completed = task_dict["completed"]
        return task