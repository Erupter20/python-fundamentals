# ✊✋✌️ Rock, Paper, Scissors Game
# Author: Piyush (Your Name)

import random

choices = ["rock", "paper", "scissors"]

print("🎮 Welcome to Rock, Paper, Scissors!")
print("Type 'exit' to quit the game anytime.\n")

while True:
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice == "exit":
        print("👋 Thanks for playing! Goodbye!")
        break

    if user_choice not in choices:
        print("❌ Invalid choice! Try again.\n")
        continue

    computer_choice = random.choice(choices)
    print(f"💻 Computer chose: {computer_choice}")

    # Check winner
    if user_choice == computer_choice:
        print("😐 It's a tie!\n")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("🎉 You win!\n")
    else:
        print("😞 You lose!\n")
