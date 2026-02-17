# 3. Check Prime: Create a function named is_prime that checks if a number is prime and returns True or False.

def isPrime(n1):
    if n1 > 1:
        for i in range(2, n1):
            if n1 % i == 0:
                return False
            else:
                return True
    else:
        return False

num1 = int(input("Enter a number to check:\n"))
checkPrime = print(isPrime(num1))