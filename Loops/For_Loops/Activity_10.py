# Activity_10.py
# @ Author: Norma Seym
# Date: December 2023
"""
Directions: Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead
of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print
"FizzBuzz".
Sample Output :
fizzbuzz
1
2
fizz
4
buzz
"""

# Used a for loop as we are iterating through a range of numbers.

# Defines a range of numbers between 1 and 50.
output = range(1, 51)

# Creates a loop to iterate through `output`.
for x in output:
    # Sets condition for numbers divisible by both 3 and 5.
    if x % 15 == 0:
        # Displays specific message when this condition is met.
        print("FizzBuzz")

    # Sets condition for numbers divisible by 5.
    elif x % 5 == 0:
        # Displays specific message when this condition is met.
        print("Buzz")

    # Sets condition for numbers divisible by 3.
    elif x % 3 == 0:
        # Displays specific message when this condition is met.
        print("Fizz")

    # If none of the above conditions are met display the value of each number in `output`.
    else:
        print(x)
