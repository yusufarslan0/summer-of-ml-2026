from app.storage import load_tasks, save_tasks
from app.task import Task

def create_task(task_title: str) -> None:
	tasks = load_tasks()
	
    # Find the smallest available id
	id_list = [task_object.id for task_object in tasks]
	
	task_id = 1
	while (task_id in id_list):
		task_id += 1
		
    # Create and append the new task
	new_task = Task(id=task_id, title=task_title)
	tasks.append(new_task)
	save_tasks(tasks)

def delete_task(task_id: int) -> None:
	tasks = load_tasks()
	tasks = [task for task in tasks if task.id != task_id]
	save_tasks(tasks)
	print(f"Task deleted: {task_id}")

def complete_task(task_id: int) -> None:
	tasks = load_tasks()
	for task in tasks:
		if task.id == task_id:
			task.mark_complete()
	save_tasks(tasks)
	print(f"Task completed: {task_id}")