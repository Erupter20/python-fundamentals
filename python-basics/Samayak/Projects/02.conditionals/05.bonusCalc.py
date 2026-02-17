# 5.Write a Python program to calculate employee bonus based on experience and salary.

salary = int(input("Enter salary:\n"))
experience = int(input("Enter experience:\n"))

if experience >= 3:
    bonus = salary * 10
elif experience >=5:
    bonus = salary * 15
else: 
    bonus = salary * 15
    
print(f"your bonus is {bonus}")