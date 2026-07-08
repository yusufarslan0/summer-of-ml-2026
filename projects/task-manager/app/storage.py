import json
from pathlib import Path

from app.task import Task

DATA_FILE = Path("data/tasks.json")

def load_tasks():
    try:
        with DATA_FILE.open("r", encoding="utf-8") as json_file:
            data = json.load(json_file)
        return [Task.from_dict(task_dict) for task_dict in data]
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []


def save_tasks(tasks):
    task_data = [task.to_dict() for task in tasks]
    with DATA_FILE.open("w", encoding="utf-8") as json_file:
        json.dump(task_data, json_file, indent=4)
