# 6. Write a Python function that takes a tuple and an element as input and checks if the element exists in the tuple.

mytuple = (1,2,3,45,54)


# how will we add a user input? its immutable

element = int(input("Enter an element:\n"))
print(element in mytuple)