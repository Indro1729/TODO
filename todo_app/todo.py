import json
import os

# ---- Task Class ----
class Task:
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed

    def mark_completed(self):
        self.completed = True


# ---- File Handling ----
def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)


def load_tasks():
    if not os.path.exists("tasks.json"):
        return []

    with open("tasks.json", "r") as f:
        data = json.load(f)
        return [Task(**task) for task in data]


# ---- Application Functions ----
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter description: ")
    category = input("Enter category (Work / Personal / Urgent): ")

    tasks.append(Task(title, description, category))
    print("Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return

    print("\n------ TASK LIST ------")
    for i, task in enumerate(tasks):
        status = "✔ Completed" if task.completed else "✘ Not Completed"
        print(f"{i+1}. {task.title} ({task.category}) - {status}")
        print(f"   Description: {task.description}")
    print("------------------------\n")


def mark_task_completed(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        num = int(input("Enter task number to mark as completed: "))
        tasks[num - 1].mark_completed()
        print("Task marked as completed!")
    except:
        print("Invalid selection.")


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num - 1)
        print("Task deleted successfully!")
    except:
        print("Invalid selection.")


# ---- Main Program ----
def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting program.")
            break
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
