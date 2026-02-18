# 6Find minimum: write a fuction and find the minimum of 2 number.

def min_of_2(a,b): #since min() is already is pre-defined function in python
    return min(a,b)

n1 = int(input("Enter first number:\n"))
n2 = int(input("Enter second number:\n"))

print(f"the minimum among these is {min_of_2(n1, n2)}")