# Activity_15.py
# @ Author: Norma Seym
# Date: December 2023
"""
Directions: Write a Python program to check the validity of passwords input by users.
Validation :
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
"""
# Imports built-in `re` module to use regular expression to be able to use .search() method.
import re

# Stores user input to be used during validation.
password = input("Enter a password:\n ")

# Sets variable to a boolean to be used to start the while loop
valid = True

# Starts while loop and iterates through each condition until the result is true.
while valid:
    # Checks that `password` greater than 6 characters and less than 16 characters.
    if (len(password) < 6) or (len(password) > 16):
        # If condition is True move onto the next condition
        break

    # Sets condition to False, searches for lowercase letters in `password` and return boolean True if found
    elif not re.search("[a-z]", password):
        # If condition is True move onto the next condition
        break

    # Sets condition to false, searches for uppercase letters in `password` and return boolean True if found
    elif not re.search("[A-Z]", password):
        # If condition is True move onto the next condition
        break

    # Sets condition to false, searches for numbers in `password` and return boolean True if found
    elif not re.search("[0-9]", password):
        break

    # Sets condition to false, searches for special characters in `password` and return boolean True if found
    elif not re.search("[!-=]", password):
        # If condition is True move onto the next condition
        break

    # If all conditions are true, redefine `valid` to be false and exit the loop.
    else:
        # Displays a message to confirm if the password is valid.
        print("Thank you. Password is valid")
        valid = False
        break


# If any of the conditions fail in the while loop, `valid` remains True and the following code block will execute.

# Display a message advising the password is not valid if `valid` remains True.
if valid:
    print("Not a valid password")
