class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def show_task(self):
        print(f"Task: {self.title} - Completed: {self.completed}")

    def mark_complete(self):
        self.completed = True
    
    def rename(self, new_title):
        self.title = new_title

    def to_dict(self):
        return {
            "title": self.title,
            "completed": self.completed
        }
    
    @classmethod
    def from_dict(cls, task_dict):
        task = cls(task_dict["title"])
        task.completed = task_dict["completed"]
        return task


# my_task = Task("Learn Python")
# my_task.show_task()
# my_task.mark_complete()
# my_task.show_task()
# my_task.rename("Learn Python Programming")
# my_task.show_task()
# my_task.delete_task()