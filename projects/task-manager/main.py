from app.storage import load_tasks
from app.task_service import complete_task, create_task, delete_task
from app.menu import show_menu
from app.validators import *


while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Viewing tasks...")
        tasks = load_tasks()
        for task in tasks:
            task.show_task()
    elif choice == "2":
<<<<<<< HEAD
        task_title = input("Enter task title: ")
        create_task(task_title)
    elif choice == "3":
        task_id = int(input("Enter task ID to delete: "))
        delete_task(task_id)
    elif choice == "4":
        task_id = int(input("Enter task ID to complete: "))
=======
        task_title = get_valid_task_title()
        create_task(task_title)
    elif choice == "3":
        task_id = get_valid_task_id("Enter task ID to delete: ")
        delete_task(task_id)
    elif choice == "4":
        task_id = get_valid_task_id("Enter task ID to complete: ")
>>>>>>> 4998ddc (feat: implement task operations and add type hints)
        complete_task(task_id)
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")