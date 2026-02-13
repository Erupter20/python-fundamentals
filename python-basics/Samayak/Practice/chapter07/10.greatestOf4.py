#10.write a program to find greatest of faur number entered by the user.

num1 = int(input("Enter first number:\n"))
num2 = int(input("Enter second number:\n"))
num3 = int(input("Enter third number:\n"))
num4 = int(input("Enter fourth number:\n"))

if (num1 > num2 and num1 > num3 and num1 > num4):
    print(f"{num1} is largest")
elif (num2> num1 and num2 > num3 and num2> num4):
    print(f"{num2} is largest")
elif ( num3> num1 and num3 > num2 and num3 > num4):
    print(f"{num3} is largest")
else:
    print(f"{num4} is largest")