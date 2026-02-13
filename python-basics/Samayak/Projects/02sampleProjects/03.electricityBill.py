# Write a program to calculate the electricity bill based on units consumed.

units = int(input("Enter units consumed:\n"))

if units <= 100:
    bill = units *5
elif units <= 500:
    bill = units *10
else:
    bill = units * 20

print (f"total bill: {bill}")