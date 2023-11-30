# WhatColorIsTheSquare.py
# @ Author: Norma Seym
# Date: 29, November 2023

"""
Description:
A program that reads Chess board position coordinates from the user
and lets the user know if the square is either black or white.
The program may assume that a valid position will always be entered.
It does not need to perform any error checking.
"""

# Saves user input into this variable
column_choice = input("Enter the letter of the column\n")

# Saves user input into this variable and converts type from string to integer
row_choice = int(input("Enter the number of the row\n"))

# Sets a list that will be checked later in an if statement
column = ["a", "c", "e"]

# Checks if the user input from `column_choice is not in `column` then
# assigns it the value of 1 or the value of 2 if `column` is present in
# `column_choice`
if column_choice.lower() not in column:
    column_choice = 1
else:
    column_choice = 2

# Adds the value of `row_choice` and the new value of `column_choice`
coordinate = row_choice + column_choice

# Checks if the sum of `coordinate` is an odd or even number
if coordinate % 2 == 0:
    # Print if sum is an odd number
    print("The square is white")
else:
    # Print if sum is an even number
    print("The square is black")

"""
Test case assertion 1:
If a coordinate is equal to an odd number the square should be black.
If the coordinate is an even number the square should be white

Test case assertion 2:
column a row 1 should be a black square

Test case assertion 3:
column a row 2 should be a white square

Test case assertion 4:
column b row 1 should be a white square

Test case assertion 5:
column b row 2 should be a black square
"""
