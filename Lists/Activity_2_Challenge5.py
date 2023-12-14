# Activity_2_Challenge5.py
# @ Author: Norma Seym
# Date: December 2023
"""
Directions: Write a program that outputs every odd valued index item from list_1
"""

list_1 = [23, 66, 23, 12]

# iterates through the list
for x in list_1:
    # Checks if list item is not an even number
    if x % 2 != 0:
        # Displays items in list that are of odd value
        print(x, end=", ")

"""
Test case assertion 1:
Items displayed should be 23, 23

Test case assertion 2:
Temporarily changed items in list_1 to `list_1 = [1, 5, 23, 12]`
Items displayed should be 1, 5, 23,
"""
