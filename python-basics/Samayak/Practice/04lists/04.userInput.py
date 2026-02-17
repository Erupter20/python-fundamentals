# 04. Write a program that asks the user to enter 5 numbers and stores them in a list. Print the list in Accending order.


num1 = int(input("Enter first number:\n"))
num2 = int(input("Enter second number:\n"))
num3 = int(input("Enter third number:\n"))
num4 = int(input("Enter fourth number:\n"))
num5 = int(input("Enter fifth number:\n"))
newList = [num1, num2, num3, num4, num5]
newListSorted= sorted(newList)
print(newListSorted)