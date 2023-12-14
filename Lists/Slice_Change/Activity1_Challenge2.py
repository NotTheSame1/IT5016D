# Activity1_Challenge2.py
# @ Author: Norma Seym
# Date: December 2023
"""
Directions:
- Create a stored list with an even number of elements. The list must have no fewer than 6 elements.
- Write a program that returns the first half of all the elements of any list containing an even number of elements.
"""
my_list = [1, 4, 8, 9, 22, 27]

# Determine how many items are in the list
list_length = len(my_list)
# Determine which numbers are the first half of the list
first_half = int(list_length / 2)
# Displays first half of list items
print(my_list[0:first_half])
