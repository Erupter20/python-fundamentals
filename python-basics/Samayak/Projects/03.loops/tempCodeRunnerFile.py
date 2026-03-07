# # Project: Simple Bank Management System
# '''
# Goal:
# Create a program that allows users to:
# •Create an account
# •Deposit money
# •Withdraw money
# •Check balance
# •Exit the system

# '''

# print("----- 🔯 Welcome To Bank 🔯 ----- ")

# accounts = {}


# # Menu load:
# while True:
#     print("1.Create an account")
#     print("2.Deposit money")
#     print("3.Withdraw money")
#     print("4.Check balance")
#     print("5.Exit the system")
#     print("  \n")
    
#     choice = int(input("Enter your choice:\n"))
#     if choice == "1":
#         name = input("Enter your name:\n")
#        [acc_no] = int(input("Enter your account number:\n"))
#         print("Account created successfully!")

#     # depositing money
#     elif choice == "2":
#         acc_no  = int(input("Enter account number:\n"))
#         if acc_no in accounts:
#             amount = int(input("Enter the amount to deposit:\n"))
#             accounts[acc_no]["Balance"] += amount
#             print(f"{amount} deposited successfully")
#         else:
#             print("Account nnot found!")

#     # Withdrawing money  
#     elif choice == "3":
#         acc_no = int(input("Enter account number:\n"))
#         if acc_no in accounts:
#             amount = int(input("Enter the amount to withdraw:\n"))
#             if amount < accounts:
#                 [acc_no]["Balance"] -= amount
#                 print("Withdrawal succesful!")
#             else:
#                 print("Insufficient balance!")
#         else:
#             print("Account not found!")

#     # Checking Balance
#     elif choice == "4":
#      acc_no = input("Enter account number: ")
#         if acc_no in accounts:
#             print(f"Name: {accounts[acc_no]['Name']}")
#             print(f"Balance: ₹{accounts[acc_no]['Balance']}")
#         else:
#             print("Account not found!")
#     elif choice == "5":
#         print("Thank you for using our bank system!")
#         break
#     else:
#         print("Invalid choice! Try again.")


print("🔯Welcome to Simple Bank Management System🔯")

accounts = {}  # Dictionary to store account details

while True:
    print("\n------ MENU ------")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    i   f choice == "1":
        name = input("Enter your name: ")
        acc_no = input("Enter account number: ")
        accounts[acc_no] = {"Name": name, "Balance": 0}
        print("\nAccount created successfully!")

    elif choice == "2":
        acc_no = input("Enter account number: ")
        if acc_no in accounts:
            amount = float(input("Enter amount to deposit: "))
            accounts[acc_no]["Balance"] += amount
            print("\nAmount deposited successfully!")
        else:
            print("\nAccount not found!")

    elif choice == "3":
        acc_no = input("Enter account number: ")
        if acc_no in accounts:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= accounts[acc_no]["Balance"]:
                accounts[acc_no]["Balance"] -= amount
                print("\nWithdrawal successful!")
            else:
                print("\nInsufficient balance!")
        else:
            print("\nAccount not found!")

    elif choice == "4":
        acc_no = input("Enter account number: ")
        if acc_no in accounts:
            print(f"Name: {accounts[acc_no]['Name']}")
            print(f"Balance: ₹{accounts[acc_no]['Balance']}")
        else:
            print("\nAccount not found!")

    elif choice == "5":
        print("\nThank you for using our bank system!")
        break

    else:
        print("\nInvalid choice! Try again.")
