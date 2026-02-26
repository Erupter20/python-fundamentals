import random

print("🔐 Easy Password Generator")

# Ask user for password length
length = int(input("Enter password length: "))

# All possible characters
all_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

# Generate password
password = ""
for i in range(length):
    password += random.choice(all_chars)

# Show password
print("Your generated password is:", password)
