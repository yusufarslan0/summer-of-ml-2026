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
    
    def delete_task(self):
        del self


# my_task = Task("Learn Python")
# my_task.show_task()
# my_task.mark_complete()
# my_task.show_task()
# my_task.rename("Learn Python Programming")
# my_task.show_task()
# my_task.delete_task()