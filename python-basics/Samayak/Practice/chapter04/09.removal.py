# 9. Ask the user to enter a list of 5 items. Then, ask them to enter one item to remove. Remove that item from the list if it exists and display the updated list.

num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
num3 = int(input("enter third number:"))
num4 = int(input("enter fourth number:"))
num5 = int(input("enter fifth number:"))

list = [num1, num2,num3, num4, num5]

toRemove = int(input("enter the number to remove"))

list.remove(f"toRemove")

print(list)