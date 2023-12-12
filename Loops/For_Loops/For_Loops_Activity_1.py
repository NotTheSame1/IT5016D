# For_Loops_Activity_1.py
# @ Author: Norma Seym
# Date: December 2023

""" Directions: Write a Python program to find those numbers which are divisible by 7 and multiples of 5,
between 1500 and 2700 (both included)."""

# Iterates through the range of numbers 1500 to 2700
for number in range(1500, 2700):
    # Add conditions that check for numbers that are divisible by 7 and 5
    if (number % 7 == 0) and (number % 5 == 0):
        # Displays the numbers found in the iteration that meet the above conditions
        print(number)

        """ After checking the sample solution my code worked correctly, however the sample had additional code that 
        saved the numbers into a list, converted the result into a string and added a comma after each number. """
