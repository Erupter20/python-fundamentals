# 🎲 Guess the Number Game
# Author: Piyush (Your Name)

import random

# Step 1: Computer chooses a random number between 1 and 100
secret_number = random.randint(1, 100)

print("🎯 Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 100.")
print("Can you guess it? 🤔")

# Step 2: Initialize attempt counter
attempts = 0

# Step 3: Loop until the user guesses correctly
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    # Step 4: Check conditions
    if guess < secret_number:
        print("Too low! Try again ⬆️")
    elif guess > secret_number:
        print("Too high! Try again ⬇️")
    else:
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
        break
