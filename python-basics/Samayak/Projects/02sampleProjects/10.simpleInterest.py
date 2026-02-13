# Write a Python program to calculate simple interest.

p = int(input("enter principle amount:\n"))
r = int(input("enter rate of interest\n"))
t = float(input("enter time duration:\n"))

interest = (p*r*t) /1000

print (f"Simple Interest: INR {interest}")