'''
Project: Student Grade Management System
Goal:
Create a program that:
•Takes details of multiple students (name, marks).
•Calculates their average.
•Decides their grade.
•Displays a full report.
'''

# print("Student Grade Management System")

# students = [] # empty list

# while True:
#     name = input("Enter your name/stop:\n")
#     if name.lower() =='stop':
#         break

#     total_marks = 0
#     subjects = int(input("Enter number of subjects:\n"))
    
#     int(input("Enter marks:\n"))
#     marks = int(input("Enter marks:\n"))
#     total_marks += marks

#     avg = total_marks / subjects

#     # grade calc
#     if avg>=90:
#         grade = 'A+'
#     elif avg>=75:
#         grade = 'A'
#     elif avg>=60:
#         grade = 'B'
#     elif avg >= 40:
#         grade = 'C'
#     else:
#         grade = 'F'

# students.append({"Name": name, "Average": avg, "Grade": grade})

# # Printing the list
# print(students)

print("Student Grade Management System")
students = [] # list to store student data
while True:
    name = input("\nEnter student name (or 'stop' to finish): ")
    if name.lower() == 'stop':
        break
total_marks = 0
subjects = int(input("Enter number of subjects: "))
for i in range(subjects):
    marks = float(input(f"Enter marks for subject {i+1}: "))    
    total_marks += marks
    avg = total_marks / subjects
# Grade calculation
if avg >= 90:
    grade = 'A+'
elif avg >= 75:
    grade = 'A'
elif avg >= 60:
    grade = 'B'
elif avg >= 40:
    grade = 'C'
else:
    grade = 'F'
    students.append({"Name": name, "Average": avg, "Grade": grade})