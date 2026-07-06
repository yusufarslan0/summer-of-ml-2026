from app.task import Task
from app.storage import load_tasks, add_task
from app.menu import show_menu


while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        task_title = input("Enter task title: ")
        task = Task(task_title)
        add_task(task)
    elif choice == "2":
        print("Viewing tasks...")
        tasks = load_tasks()
        for task in tasks:
            task.show_task()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")