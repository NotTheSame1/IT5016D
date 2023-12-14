# Activity2_Challenge2.py
# @ Author: Norma Seym
# Date: December 2023
"""
Info: A known Maori proverb translated to English states:
'As man disappears from sight, the land remains.'
Parts of this proverb are written in the list shown.

Directions:
Write a program that requests input from the user, then inserts it into the list.
Afterward, the program must join all the strings then output them to the screen.
Assume that the user types in the correct input.
"""
print(
    "A known Maori proverb translated to English states: "
    "'As man disappears from sight, the land remains.'\n"
)
proverb_part_list = ["As a man disappears ", " the ", "land remains."]

# Requests input from the user.
missing_proverb = input(
    "The following list is missing part of the proverb. Type in the missing words as shown above to complete the "
    "proverb.\n"
    '["As a man disappears ", " the ", "land remains."]\n'
)
# Takes user input and inserts as 2nd item in `proverb_part_list`.
proverb_part_list.insert(1, missing_proverb)
# Joins and displays items from the new list as a string.
print("".join(proverb_part_list))
