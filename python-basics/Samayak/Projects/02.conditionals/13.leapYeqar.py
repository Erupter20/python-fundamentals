# Write a Python program to check whether a year is a leap year or not.

year = int(input("Enter the year:\n"))

if (year % 4 == 0):
    print("leap year")
else:
    print("non-leap year")