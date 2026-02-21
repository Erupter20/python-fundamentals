# Calculate and display a student's marks based on their marks using a function

# function to calculate marks:
def calc_grade(marks):
    if marks>=90:
        return "A"
    elif 80<= marks < 90:
        return "B"
    elif 70<= marks < 80:
        return "C"
    elif 60<= marks < 70:
        return "D"
    elif 50<= marks < 60:
        return "F"

# Function to display result
def show_result(name, marks):
    result = calc_grade(marks)
    print("-----Result-----")
    print(f"Student Name:{name}\n")
    print(f"Marks:{marks}\n")
    print(f"Grade:{result}\n")


student_name = input("Enter your name\n")
student_marks = int(input("Enter obtained marks:\n"))

show_result(student_name,student_marks)