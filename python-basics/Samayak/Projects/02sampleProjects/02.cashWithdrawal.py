# Write a program to simulate an ATM machine. Ask user for PIN and withdrawal amount.

pin = 0000
balance = 1000

user_pin = int(input("Enter pin:\n"))

if pin == user_pin:
    amount = int(input("Enter withdrawal amount:\n"))
    if amount <= balance:
        balance -=amount
        print("Successful Transaction")
    else:
        print("Amount exceeds balance")
else:
    print("Invalid credentials")