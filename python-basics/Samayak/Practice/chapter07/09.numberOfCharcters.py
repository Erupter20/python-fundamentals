# 9.write a program to find whether a given username cantains less then 10 characters or not

name = input("Enter your name:\n")
length = len(name)

if(length> 10):
    print("Too many charcters")
else:
    print("Acceptable length")