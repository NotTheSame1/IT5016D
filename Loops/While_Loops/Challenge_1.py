# Challenge_1.py
# @ Author: Norma Seym
# Date: December 2023

"""
Directions: Write a program with a while loop that prints 1 through to n in square brackets.
"""

# Converts user input to integer and assigns that value to the variable
number = int(input("Enter a number:\n"))
# Sets variable to zero to start the while loop
count = 0
# While loop to keep the program running while the value of `count` is less than `number`
while count < number:
    """The program starts counting from 1 through to the value of `number` and displays each number
    inside of square brackets [ ]"""
    print(
        f"[{count + 1}]", end=" "
    )  # Used end parameter to keep message inline instead of the default newline
    # Tells the program that inside of this loop we want the variable `count` to increase by 1 in each iteration
    count += 1

"""
Test case assertion 1:
`number` = 6, prints [1] [2] [3] [4] [5] [6] 

Test case assertion 2:
`number` = 3, prints [1] [2] [3]  
"""
