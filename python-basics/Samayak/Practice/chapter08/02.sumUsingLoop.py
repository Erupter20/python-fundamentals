# 2. Sum of Numbers: Write a program that calculates the sum of all numbers from 1 to 100.

n = 100
total_sum = 0

for i in range(1,101):
    total_sum  += i

print(f"Total sum is {total_sum}")
