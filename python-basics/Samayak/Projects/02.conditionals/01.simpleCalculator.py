# Write a Python program that performs addition, subtraction, multiplication, or division based on user choice.
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