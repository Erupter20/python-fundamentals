# Make a small program that calculates a customer’s total bill — including tax — using user-defined functions.

# Function to calculate total amount:

def calculate_total(price, quantity, tax_rate):
    subTotal = price * quantity
    tax = subTotal * tax_rate/100
    total = subTotal + tax
    return total

# function to display bill:
def bill(itemName, price, quantity, tax_rate):
    total = calculate_total(price, quantity, tax_rate)
    print("------BILL------")
    print(f"item: ${itemName}")
    print(f"Price per item : ${price}")
    print(f"Quantity: {quantity}")
    print(f"tax rate: {tax_rate}%")
    print("-" * 8)
    print(f"Total amount: ${total:2f}")
    print("-" * 8)

# calling the functions

item = input("Enter item name:\n")
price = float(input("Enter the price per item:\n"))
quantity = int(input("Enter the number of items:\n"))
tax_rate = float(input("Enter tax rate:\n"))

bill(item, price,quantity ,tax_rate)