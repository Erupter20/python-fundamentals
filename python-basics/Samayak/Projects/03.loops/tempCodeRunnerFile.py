# Project: Simple Bank Management System
'''
Goal:
Create a program that allows users to:
•Create an account
•Deposit money
•Withdraw money
•Check balance
•Exit the system

'''

print("----- Welcome To Bank 🔯 ----- ")

accounts = {}
deposit = None
withdraw = None

# Menu load:
while True:
    print("1.Create an account")
    print("2.Deposit money")
    print("3.Withdraw money")
    print("4.Check balance")
    print("5.Exit the system")
    print("  \n")
    choice = int(input("select an option(1/2/3/4/5):\n"))

    if choice == 1:
        user_id = input("Enter User ID:\n")
        user_passwd = input("Enter a password\n")
        confirm_password = input("re-enter the password:\n")
        if user_passwd == confirm_password:
            print("proceed")
        else:
            print("invalid password, try again\n")
    
    if choice == 2:
        deposit == int(input("Enter amount to deposit:\n"))
        balance = balance + deposit
        print(f"{deposit} deposited\n Balance = {balance}")

    if choice == 3:
        withdraw == int(input("Enter amount to withdraw:\n"))
        balance = balance + withdraw
        print(f"{withdraw} withdrawed\n Balance = {balance}")

    if choice == 4:
        print(f"balance:{balance}")

    if choice == 5:
        print("Thanks for using this service\n BYE!")
