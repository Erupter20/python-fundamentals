# 1. Student Record Management System
# Concept: Store, read, and update student details using a text file.

def add_students():
    with open("students.txt","a") as file:
        name = input("Enter Student name:\n")
        roll = int(input("Enter roll number:\n"))
        file.write(f"{roll} : {name}")
        print("Student added successfully!\n")

def view_students():
    with open("students.txt", "r") as file:
        print("-----Student List-----\n")
        print(file.read())

add_students()
view_students()