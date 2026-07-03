import json

def save_tasks(tasks):
    data = [task.to_dict() for task in tasks]
    with open(".//data/tasks.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
