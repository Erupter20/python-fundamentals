# Basic Contact Book

contacts = []  # Empty list to store contacts

while True:
    print("\n📇 Contact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts.append({"name": name, "phone": phone})  # Store as dictionary
        print(f"✅ Contact {name} added.")

    elif choice == "2":
        print("\n📋 All Contacts:")
        if not contacts:
            print("No contacts found.")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")

    elif choice == "3":
        search = input("Enter name to search: ")
        found = False
        for contact in contacts:
            if contact['name'].lower() == search.lower():
                print(f"Name: {contact['name']}, Phone: {contact['phone']}")
                found = True
                break
        if not found:
            print("❌ Contact not found.")

    elif choice == "4":
        print("👋 Exiting Contact Book.")
        break

    else:
        print("❌ Invalid choice. Please try again.")
