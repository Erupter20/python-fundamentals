# 08. Write a Python program that calculates the final bill after discount.

amount = int(input("Enter Amount:\n"))

if amount < 1000:
    final_amount = amount
elif amount <= 2000:
    final_amount = amount - 300
elif 3000 > amount > 2000:
    final_amount = amount - 600
else:
    final_amount = amount - 2000

discount = amount - final_amount

print(f"Final Discount:{discount} ")
print(f"Final Amount: {final_amount}")