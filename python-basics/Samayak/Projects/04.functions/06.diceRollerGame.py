# Simulate rolling a dice — the user can roll multiple times — using functions.
import random 
import time

# fuction to roll the dice:

def rollDice():
    return random.randint(1,6)

#Function to play game:
def _game():
    print("-----Welcome To Dice Game-----\n")
    while True:
        choice = input("Press 'r' to roll or 'q' to quit\n")

        if choice == 'r':
          number = rollDice()
          print("You rolled ", number)
        
        elif choice == 'q':
            print("Thanks for playing!")
        
        else:
            print("Invalid choice. Try again!\n")
    
# main program:
_game()