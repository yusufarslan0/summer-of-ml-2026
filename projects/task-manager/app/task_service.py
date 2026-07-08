from app.storage import load_tasks, save_tasks


def create_task(task):
	tasks = load_tasks()
	tasks.append(task)
	save_tasks(tasks)
