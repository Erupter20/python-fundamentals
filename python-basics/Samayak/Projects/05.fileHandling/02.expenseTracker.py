# Save daily expenses and calculate total from a file:

def add_expense():
    with open("expenses.txt") as file:
        item=input("Enter item:\n")
        amount= int(input("Enter amount:\n"))
        file.write(f"{item} : {amount}\n")

def total_expense():
    total = 0
    with open("expenses.txt", "r") as f:
        for line in f:
            total += float(line.strip().split()(",")[1])
        print(f"Total Expense: {total}" )

add_expense()
total_expense()