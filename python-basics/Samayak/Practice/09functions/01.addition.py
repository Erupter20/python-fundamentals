# 1. Basic Addition Function: Write a function named add_numbers that takes two numbers as parameters and returns their sum.

def sum(a,b):
    return a+b

a = int(input("enter first number:\n"))
b = int(input("enter second number:\n"))

print(f"sum of these numbers is {sum(a,b)}")