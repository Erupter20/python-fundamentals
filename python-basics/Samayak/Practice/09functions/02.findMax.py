# Find Maximum: Write a function named find_max that takes 4 user enter numbers and returns the largest number in the list.

def max_of_four(n1,n2,n3,n4): # can't name it max since there already exists a predefined max function
    return max(n1,n2,n3,n4)
        
num1 = int(input("Enter first number:\n"))
num2 = int(input("Enter second number:\n"))
num3 = int(input("Enter third number:\n"))
num4 = int(input("Enter fourth number:\n"))

largest_number = max_of_four(num1, num2, num3 ,num4)

print(f"the largest among 4 is {largest_number}")