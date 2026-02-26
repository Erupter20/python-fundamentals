# 📝 To-Do List App (Without File Handling)
# Author: Piyush (Your Name)

tasks = []  # list to store tasks

while True:
    print("\n📝 To-Do List App")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':  # View Tasks
        if not tasks:
            print("📭 No tasks found!")
        else:
            print("\n📋 Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == '2':  # Add Task
        new_task = input("Enter new task: ")
        tasks.append(new_task)
        print("✅ Task added successfully!")

    elif choice == '3':  # Update Task
        if not tasks:
            print("📭 No tasks to update!")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            task_no = int(input("Enter task number to update: "))
            if 1 <= task_no <= len(tasks):
                new_task = input("Enter updated task: ")
                tasks[task_no - 1] = new_task
                print("✏️ Task updated successfully!")
            else:
                print("❌ Invalid task number!")

    elif choice == '4':  # Delete Task
        if not tasks:
            print("📭 No tasks to delete!")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            task_no = int(input("Enter task number to delete: "))
            if 1 <= task_no <= len(tasks):
                deleted = tasks.pop(task_no - 1)
                print(f"🗑️ Deleted task: {deleted}")
            else:
                print("❌ Invalid task number!")

    elif choice == '5':  # Exit
        print("👋 Thank you for using the To-Do List App!")
        break

    else:
        print("❌ Invalid choice! Please select between 1-5.")
