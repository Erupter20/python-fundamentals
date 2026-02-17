'''
Create a program that:
•Adds new books
•Displays all books
•Allows borrowing and returning of books
•Works in a continuous menu using loops
'''

print("*****Welcome to library Management System*****\n")

library = []

while True:
    print("\n***** MENU*****")
    print("1.Add Book\n2.View Inventory\n3.Borrow Book\n4.Return Book\n5.Exit")

    choice = input("Enter choice (1-5):\n")

    # Adding a new book
    if choice == "1":
        title = input("enter book's title:\n")
        author = input("Enter book's author\n")
        library.append({"Title":title, "Author":author,"Available":True})
# Show Inventory
    elif choice == "2":
        if len(library) == 0:
            print("No books in library yet!")
        else:
            print("\n Available books\n:")
            print("-" * 40)
            for i , book in enumerate(library, start=1):
                status = "Available" if book["Available"] else "Borrowed"
                print(f"{i}.{book['Title']} b {book['Author']} - {status}")

# Borrow a book:
    elif choice == "3":
        title = input("Enter the title of the book to be borrowed:\n")
        found = False
        for book in library:
            if book["Title"].lower() == title.lower():
                found = True
                if book["Available"] :
                    book ["Available"] = False
                    print(f"You bowrrowed '{book['Title']}'.")
                else:
                    print("Sorry book is not available")
                    break
        if not found:
            print("Book not found!")
            break

    elif choice =="4":
        title = input("enter a book to return:")
        found = False
        for book in library:
            if book["Title"].lower() == title.lower():
                found = True
                if not book["Available"]:
                    book["Available"] = True
                    print(f"'{book['Title']}' returned successfully!") # not working
            else:
                print("The book wasn't borrowed!")
            break
        if not found:
            print("Book not found")

#Exit
    elif choice == "5":
        print("Thanks for using the system!")
        break
    else:
        print("Invalid choice! try again")