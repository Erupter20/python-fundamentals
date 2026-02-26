# Concept: Store and view daily tasks using file handling.
def add_task():
    with open("todo.txt", "a") as file:
        task = input("Enter new task: ")
        file.write(task + "\n")
def view_tasks():
    with open("todo.txt", "r") as file:
        print("\n--- To-Do List ---")
        print(file.read())
add_task()
view_tasks()