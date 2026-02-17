# 5.Write a program that checks if a given number is a prime number and prints "Prime" or "Not Prime."

num = int(input("Enter a number:\n"))

if num > 1:
    for i in range (2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(f"{num} is prime number")
else:
    print(f"{num} is not a prime number")


# from sympy import
# num1 = isprime(13)
# print(num1)