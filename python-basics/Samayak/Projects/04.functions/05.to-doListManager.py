# Create a small task management system where the user can add, view and delete tasks - using user - defined functions.

# Simple to-do list manager:

# Global list to store tasks:

tasks = []

# function to add tasks:
def add_tasks():
    tasks.append(task)
    print(f"Task:'{task} added successfully!'")
# Function to view all tasks:
def view_tasks():
    if len(tasks) == 0:
        print("no tasks avaliable.")
    else:
        print("-----Your Tasks----")
        for i, task in enumerate(tasks, start =1):
            print(f"{i}: {task}")
            print("-"*8)

#function to delete a task:

def view_task():
    if len(tasks)==0:
        print("No tasks available\n")
    else:
        print("\n-----Your Tasks-----\n")
        for i,task in enumerate(tasks, start=1):
            print(f"{i}, {task}"
            )
            print("-"*8)

#function to delete task

def delete_task(task_number):
    if 0 < task_number <=len(tasks):
        removed  =tasks.pop(task_number - 1)
        print("Task removed successfully!")
    else:
        print("Task not found!")

# Code:

while True:
    print("\n-----To do menu-----")
    print("1.Add Task")
    print("2.View Task")
    print("3.Remove Task")
    print("4.Exit")

    choice = int(input("Enter your choice(1-4):\n"))

    if choice == 1:
        task = input("Enter new task:\n")
        add_tasks()

    elif choice == 2:
        view_tasks()

    elif choice == 3:
        view_tasks()
        num = int(input("Enter a task to delete:\n"))
        delete_task(num)

    elif choice == 4:
        print("Thank you for using the To do manager!\n")

    else:
        print("Invalid input, try again!\n")
