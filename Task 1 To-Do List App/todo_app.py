import os
import json

# File to store tasks persistently
TASK_FILE = "tasks.json"

# Load tasks from file or initialize an empty list
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return []

# Save current tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks found!\n")
    else:
        print("\n📝 To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["completed"] else "❌"
            print(f"{i}. {task['task']} [{status}]")
        print()

# Add a new task
def add_task(tasks):
    task_desc = input("Enter task description: ").strip()
    if task_desc:
        tasks.append({"task": task_desc, "completed": False})
        save_tasks(tasks)
        print("✅ Task added successfully!")
    else:
        print("⚠️ Task description cannot be empty.")

# Mark a task as complete
def complete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            save_tasks(tasks)
            print("✅ Task marked as complete!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"🗑️ Task '{removed['task']}' deleted.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Main menu
def main():
    tasks = load_tasks()
    while True:
        print("\n====== TO-DO LIST MENU ======")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Exiting... Have a productive day!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
