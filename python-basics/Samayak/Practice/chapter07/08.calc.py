# 8.Write a program that takes two numbers and an operator (+, -, *, /) and performs the operation, printing the result. Handle division by zero by printing "Error: Division by zero."

num1 = 2
num2 = 3

op = input("Enter an operator:\n")

if op == "+":
    print(num1+num2)
elif op =="-":
    print(num1-num2)
elif op =="*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("Invalid input")