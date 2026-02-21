    '''Create a simple Student Management System that allows:
    •Adding new students
    •Viewing all student records
    •Searching a student by roll number
    •Deleting a student record
    '''

    # Student management System
    students = []

    # Function to add a new student

    def add_student():
        roll_no = int(input("Enter your roll number:\n"))
        name = input("Enter your name\n")
        course = input("Enter Course:\n")
        marks = int(input("Enter your marks:\n"))

        student = {
            "Roll No" : roll_no,
            "Name" : name,
            "Course": course,
            "Marks" : marks
        }

        students.append(student)
        print(f"Student {name} added successfully!")

    # to view all students:
    def view_students():
        if len(students) == 0:
            print("No students found!")
        else:
            print("\n-----Student Records-----")
            for s in students:
                print(f"Roll No: {s['Roll No']}, Name : {s['Name']}, Course : {s['Course']}, Marks: {s['Marks']
                }")

    # Function to search student by roll number:

    def search_student():
        roll = int(input("Enter Roll Number to search:\n"))
        found = False
        for s in students:
            if s["Roll No"] == roll:
                print("\n -----Student Found-----")
                print(f"\nRoll No: {s['Roll No']}")
                print(f"Name: {s['Name']}")
                print(f"Course: {s['Course']}")
                print(f"Marks: {s['Marks']}")
                print("---------------------------")
                found = True
                break
        if not found:
            print("Student not found!")
    # Function to delete student 
    # Function to delete student record
    def delete_student():
        roll = int(input("Enter Roll Number to search:\n"))
        for s in students:
            if s["Roll No"] == roll:
                students.remove(s)
                print(f"Student with Roll No {roll} deleted successfully!")
                return
        print("Student not found!")
        
    # Main program menu
    def main_menu():
        while True:
            print("\n===== STUDENT MANAGEMENT SYSTEM =====")
            print("1. Add Student")
            print("2. View All Students")
            print("3. Search Student")
            print("4. Delete Student")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")
            if choice == "1":
                add_student()
            elif choice == "2":
                view_students()
            elif choice == "3":
                search_student()
            elif choice == "4":
                delete_student()
            elif choice == "5":
                print("Thank you for using Student Management System!")
                break
            else:
                print("Invalid choice! Try again.")
    # Start program
    main_menu()