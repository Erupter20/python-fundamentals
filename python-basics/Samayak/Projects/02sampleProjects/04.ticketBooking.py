# Write a program for a movie ticket system where ticket price changes based on age and time.

import time #datetime

age = int(input("Enter your age :\n"))
time = time.time()
if time > 1100 and age >=35: # module doesn't work?
    print("price is INR 300")
else:
    print("price is INR 250")