# For_Loops_Activity_8.py
# @ Author: Norma Seym
# Date: December 2023
"""
Directions: Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
Note : Use 'continue' statement.
Expected Output : 0 1 2 4 5
"""

# Used a for loop as we are iterating through a range of numbers.

# Defines a range of numbers between 0 and 6.
output = range(0, 7)

# Creates a loop to iterate through `output`.
for x in output:
    # Sets conditions for when x is equal to numbers 3 or 6.
    if (x == 3) or (x == 6):
        """
        Uses the `continue` statement to stop the iteration at the above conditions and continue when the conditions are
        not met.
        """
        continue

    # Inline display of the numbers in the range defined in `output`.
    print(x, end=" ")
