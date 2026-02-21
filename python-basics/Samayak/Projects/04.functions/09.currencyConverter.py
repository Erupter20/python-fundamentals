# Convert money from Indian Rupees (INR) to other currencies using functions.

# Function for converter:

def convert_currency(amount, currency):
    if currency == "USD":
        return amount/83.2 

    elif currency == "EUR":
        return amount/90.5

    elif currency == "GBP":
        return amount/105.3

    elif currency == "JPY":
        return amount * 1.79

    else:
        return None

# Function to display result

def show_result(amount, currency):
    converted = convert_currency(amount, currency)
    if converted is not None:
        print(f"INR {amount}  = {converted} {currency}")
    else:
        print("Not available!")

# Main program
print("-----Currency Calculator-----")

amount = float(input("Enter the amount in INR:\n"))
print("Available currencies: USD, EUR, GBP, JPY:\n")
currency = input("Enter the currency to convert into:\n").upper()

show_result(amount, currency)