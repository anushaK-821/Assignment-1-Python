import os

FILE_NAME = "todo.txt"

def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task, status = line.strip().split("::")
                tasks.append({"task": task, "done": status == "done"})
    return tasks

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            status = "done" if task["done"] else "pending"
            file.write(f"{task['task']}::{status}\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    for idx, task in enumerate(tasks, 1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{idx}. {status} {task['task']}")

def todo_app():
    tasks = load_tasks()

    while True:
        print("-----------------------------------------------------")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Complete")
        print("5. Exit")
        print("-----------------------------------------------------")


        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            task_name = input("Enter new task: ")
            tasks.append({"task": task_name, "done": False})
            save_tasks(tasks)
            print("Task added.")
        elif choice == "3":
            show_tasks(tasks)
            index = int(input("Enter task number to remove: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                save_tasks(tasks)
                print(f"Removed: {removed['task']}")
            else:
                print("Invalid task number.")
        elif choice == "4":
            show_tasks(tasks)
            index = int(input("Enter task number to mark complete: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index]["done"] = True
                save_tasks(tasks)
                print("Task marked as complete.")
            else:
                print("Invalid task number.")
        elif choice == "5":
            print("Exiting To-Do App.")
            break
        else:
            print("Invalid choice. Please select between 1-5.")

todo_app()
