# Challenge_3.py
# @ Author: Norma Seym
# Date: December 2023

# Write a program that prints multiples of p from 10 until the value of q (inclusive).

# Converts user input to integer and assigns that value to the variable
p = int(input("Please enter an increment:\n"))
q = int(input("Please enter an ending number:\n"))
# Sets values to 10 as we are wanting to print multiples from 10 of `p`
counter = 10
# Equation that takes the value of p and increments this by 10
starting_number = p + counter
# Run the program until `counter` reaches `q`
while counter < q:
    # After the equation from `starting_number` has run, display inline each multiple of `p` from 10 separated by a ","
    print(starting_number, end=", ")
    """ After the equation from `starting_number` has completed, and we have that sum, re-define `starting_number` 
    to a new equation that takes the original value/sum of `starting_number and increase by the value of `p` """
    starting_number = starting_number + p
    """ Re-define `counter` so that at each iteration `counter` increases by the value of `p` and saves the value as the
     new value of `counter`"""
    counter += p

"""
Test case assertion 1: 
p = 3, q = 17, result = multiples of 3 from 10 (13, 16, 19,)
Iteration 1, `counter` = 10: run `starting_number` equation `p` + `counter` = `starting_number` is 13 
Iteration 2, new `counter` = 13: `starting_number` is 13. Run equation `starting_number` + `p` = `starting_number` is 16 
Iteration 3, new `counter` = 16: `starting_number` is 16. Run equation `starting_number` + `p` = `starting_number` is 16
Program stops running as next iteration the `counter` will be greater than the value of `q` 

Test case assertion 2: 
p = 6, q = 30, result = multiples of 6 from 10 (16, 22, 28, 34,)
"""
