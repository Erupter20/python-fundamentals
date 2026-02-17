# Write a Python program that calculates a student’s grade based on marks.


grade = int(input("Enter marks:\n"))
if grade>=90:
    print("A")
elif 80<= grade < 90:
    print("B")
elif 70<= grade < 80:
    print("C")
elif 60<= grade < 70:
    print("D")
elif 50<=grade < 60:
    print("F")