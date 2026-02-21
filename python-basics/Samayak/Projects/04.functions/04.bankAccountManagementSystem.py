# create a simple program to deposit, withdraw and check balance using functions

balance = 0

# function to deposit money

def deposit(amount):
    global balance
    balance += amount
    print(f"${amount} deposited succesfully")

# withdraw

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -=amount
        print(f"{amount} withdrawn successfully!")
    else:
        print("Insufficent balance!")

# function to check balance:
def check_balance():
    print(f"Current Balance:${balance}\n")

# Main Program:

while True:
    print("\n-----Bank Menu-----")
    print("1.Deposit Money")
    print("2.Withdraw Money")
    print("3.Check Balance")
    print("4.Exit")

    choice = int(input("Enter your choice (1-4):\n"))

    if choice == 1:
        amt = int(input("Enter the amount to deposit:\n"))
        deposit(amt)
    elif choice == 2:
        amt = int(input("Enter the amount to withdraw:\n"))
        withdraw(amt)
    elif choice == 3:
        check_balance()
    elif choice == 4:
        print("Thank you for using the bank\n")
        break
    else:
        print("Invalid choice! Try again")