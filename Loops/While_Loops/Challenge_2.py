# Challenge_2.py
# @ Author: Norma Seym
# Date: December 2023

"""
Directions: Write a program with a while loop that computes the sum of the first n positive integers.
"""

# Converts user input to integer and assigns that value to the variable
number = int(input("Please enter a number:\n"))
# Sets `count` to zero to start the while loop
count = 0
"""
Sets `total` to zero so that the program can start adding at each iteration from zero until it reaches the value of 
`number`
ex: `number` + 0 = total, new `total` +1, new `total` +2...etc
"""
total = 0
# Run the program until `count` reaches `number`
while count <= number:
    """Defines a variable `total` with the equation telling the program that at each iteration take the total and add
    that to the value of `count`"""
    total = total + count
    # Tells the program that inside of this loop we want the variable `count` to increase by 1 at each iteration
    count += 1
""" Displays the value that was entered for`number` and what the sum of `total` was after all the iterations done by the 
end of the program"""
print(f"n= {number} total= {total}")

"""
Test case assertion 1:
`number` = 6, prints n= 6 total= 21
Iteration 1: (number) 6 + (count) 0 = (new total) 6
Iteration 2: (number is new total) 6 + (count) 1 = (total) 7
Iteration 3: (number is new total) 7 + (count) 2 = (total) 9
Iteration 4: (number is new total) 9 + (count) 3 = (total) 12
Iteration 5: (number is new total) 12 + (count) 4 = (total) 16
Iteration 6: (number is new total) 16 + (count) 5 = (total) 21
Stops at 6 iterations as the while loop declares the program can only run until the number of iterations `count`
is less than or equal to the value of `number`

Test case assertion 2:
`number` = 3, prints n= 3 total= 6
"""
