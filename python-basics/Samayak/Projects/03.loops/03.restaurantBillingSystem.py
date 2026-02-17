'''
Goal:
Create a program that:
•Shows a food menu
•Lets customers order multiple items
•Calculates total bill with tax
•Prints a final receipt
'''

print("Welcome To Restaurant\n")

menu ={
    "Burger" : 8,
    "Pizza" : 10,
    "Cake" : 15,
    "done" : 0
}
bill = 0
total = 0

order = {} # store update items

while True:
    print("\n------Menu------")
    for item,price in menu.items():
        print(f"{item}: ${price}")

    choice = input("Enter an item to order.:\n").capitalize()
    if choice.lower() == "done":
        break
    elif choice in menu:
        quantity = int(input("Enter no of items:\n"))
        if choice in order:
            order[choice] = +quantity
        else:
            order[choice] = quantity
        print(f"{choice} added to your order\n")
    else:
        print("Invalid choice\n")

# calculating bill
print("\n Order Summary:")
print ("-" * 30)
total = 0
for item, quantity in order.items():
    price = menu[item] * quantity
    total += price
    print(f"price = {item} * {quantity}")
    total += price
    
tax = total * 0.05
grandTotal = total + tax
print(f"Subtotal: ${total}")
print(f"GST (5%): ${tax:.2f}")
print(f"Total Bill:${grandTotal:.2f}")
print("-" * 30)
print("Thank you! Visit again!")