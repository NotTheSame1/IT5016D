# Activity_3.py
# @ Author: Norma Seym
# Date: December 2023

"""
Directions:  Write a Python program to guess a number between 1 and 9.
Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is
correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.
"""
# As it is not known how many times we need the loop to iterate a while loop will need to be used.

# Imports the built-in `random` module.
import random

# Generates a random integer between 1 and 9
i = random.randint(1, 9)

# Defines a variable to later be redefined inside the while loop.
guess = 0

# Sets a condition for the loop to continue to run while `guess` is not equal to `i`.
while i != guess:
    # Redefines `guess` inside of this loop and converts string to integer.
    guess = int(
        input(
            "***** Guess the number game *****\n\n" "Enter a number between 1 and 9:\n"
        )
    )
    # Stops the program from running once the user guesses correctly.
    if guess == i:
        print("Well guessed!")
