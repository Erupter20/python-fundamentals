import random

print("Easy Password Generator")

length = int(input("Enter password length: "))

all_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"


password = ""
for i in range(length):
    password += random.choice(all_chars)

print("Your generated password is:", password)
