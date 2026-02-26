import random  # For random numbers

print("🎲 Dice Rolling Simulator")

while True:
    input("Press Enter to roll the dice...")  # Wait for user to press Enter
    dice = random.randint(1, 6)              # Random number between 1 and 6
    print(f"🎲 You rolled: {dice}\n")        # Show result
    
    choice = input("Do you want to roll again? (y/n): ").lower()
    if choice != 'y':
        print("👋 Thanks for playing!")
        break
