from business_manager import *


def upgrade_menu():
    while True:
        print("\n====== PROPERTY UPGRADES ======")
        print("1. Add Upgrade")
        print("2. View Upgrades")
        print("3. Back")

        choice = input("Choose option: ")

        if choice == "1":
            add_upgrade()

        elif choice == "2":
            view_upgrades()

        elif choice == "3":
            break

        else:
            print("Invalid option.")


def menu():
    while True:
        print("\n=================================")
        print("       GTA BUSINESS TERMINAL")
        print("=================================")
        print("1. Record Property Purchase")
        print("2. View Properties")
        print("3. Total Investment")
        print("4. Delete Property")
        print("5. Manage Upgrades")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            record_transaction()

        elif choice == "2":
            view_properties()

        elif choice == "3":
            total_spending()

        elif choice == "4":
            delete_property()

        elif choice == "5":
            upgrade_menu()

        elif choice == "6":
            print("Exiting terminal...")
            break

        else:
            print("Invalid choice.")


menu()