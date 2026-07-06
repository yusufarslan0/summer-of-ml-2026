from app.task import Task
import json
from pathlib import Path

DATA_FILE = Path("data/tasks.json")

def add_task(task):
    new_task = task.to_dict()
    existing_tasks = [t.to_dict() for t in load_tasks()]
    existing_tasks.append(new_task)
    with DATA_FILE.open("w", encoding="utf-8") as json_file:
        json.dump(existing_tasks, json_file, indent=4)

def load_tasks():
    try:
        with DATA_FILE.open("r", encoding="utf-8") as json_file:
            data = json.load(json_file)
        return [Task.from_dict(task_dict) for task_dict in data]
    except FileNotFoundError:
        return []
