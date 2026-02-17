'''
Create a program that simulates ATM functions:
•Check balance
•Deposit money
•Withdraw money
•Exit the system
'''

print("Welcome to ATM\n")
balance = 0
deposit = 0


while True:
    print("\n -----Menu----- \n 1.Check Balance\n 2.Deposit Money\n 3.Withdraw Money\n 4. Exit")
    choice = int(input("Enter your choice (1-4):\n"))

    # 1. Check balance:
    if choice == 1:
        print(f"Your current balance is {balance}\n")

    elif choice == 2:
        deposit = int(input("Enter the amount to deposit\n"))
        balance += deposit 
        print(f"New balance: {balance}")
    
    elif choice == 3:
        withdraw = int(input("Enter the amount to withdraw:\n"))
        if withdraw > balance:
            print("Insufficent balance")
        else:
            balance -= withdraw
            print(f"New balance: {balance}")
    
    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid input! Try again.")