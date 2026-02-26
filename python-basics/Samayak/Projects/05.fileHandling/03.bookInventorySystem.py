# Manage a library's book list

def add_book():
    with open ("books.txt", "a") as f:
        name = input("Enter name:\n")
        author = input("Author:\n")
        file.write(f"{name},{author}\n")

def view_books():
    with open("books.txt", "r") as file:
        print("\n--- Book List ---")
        print(file.read())

add_book()
view_books()