# Write a program to make a 'guess the number game'

import random as r
number = r.randint(1,100)
guess = 0

print("welcome to guess the number")
print("try to guess")
 
while guess != number:
    guess = int (input("Enter Guess: "))

    if (guess != number):
        print("Guess Higher!")
    elif (guess > number):
        print(guess > number)
        print("Guess Lower!")
    else:
        print("You won!")