"""4. Write a program that calculates a grade based on the following
conditions:
•Score ≥ 90: Grade A
•80 ≤ Score < 90: Grade B
•70 ≤ Score < 80: Grade C
•60 ≤ Score < 70: Grade D
•Score < 60: Grade F"""

grade = 60
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