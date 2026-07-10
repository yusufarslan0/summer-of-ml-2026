from app.storage import load_tasks
from app.task_service import complete_task, create_task, delete_task
from app.menu import show_menu


while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Viewing tasks...")
        tasks = load_tasks()
        for task in tasks:
            task.show_task()
    elif choice == "2":
        task_title = input("Enter task title: ")
        create_task(task_title)
    elif choice == "3":
        task_id = int(input("Enter task ID to delete: "))
        delete_task(task_id)
    elif choice == "4":
        task_id = int(input("Enter task ID to complete: "))
        complete_task(task_id)
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")