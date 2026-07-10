def get_valid_task_title() -> str:
    while True:
        task_title = input("Enter task title: ").strip()
        if not task_title:
            print("Task title cannot be empty.")
        else:
            return task_title

def get_valid_task_id(prompt: str = "Enter task ID: ") -> int:
    while True:
        try:
            task_id = int(input(prompt))

            if task_id <= 0:
                print("Invalid input. Please enter a positive integer.")
                continue
           
            return task_id

        except ValueError:
            print("Invalid input. Please enter a valid integer.")
