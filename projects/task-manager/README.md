# CLI Task Manager

A simple command-line task manager built with Python.

This project allows users to create, view, complete, and delete tasks. Tasks are stored in a JSON file, so data persists between program runs.

## Features

- View all tasks
- Add new tasks
- Mark tasks as completed
- Delete tasks
- Automatic task ID assignment
- Persistent storage using JSON
- Input validation
- Object-oriented design
- Type hints with `TypedDict`

## Project Structure

```
.
├── app/
│   ├── menu.py
│   ├── storage.py
│   ├── task.py
│   ├── task_service.py
│   ├── types.py
│   └── validators.py
├── data/
│   └── tasks.json
├── main.py
└── README.md
```

## Technologies

- Python 3
- JSON
- Object-Oriented Programming (OOP)
- Type Hints
- TypedDict

## How to Run

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd task-manager
```

Run the application:

```bash
python main.py
```

## Example

```
1. View Tasks
2. Add Task
3. Delete Task
4. Complete Task
5. Exit

Enter your choice: 2

Enter task title: Finish Python project
```

## What I Learned

Through this project I practiced:

- Object-oriented programming
- Working with JSON files
- File I/O
- Modular project organization
- Type hints and `TypedDict`
- Input validation
- Basic software architecture