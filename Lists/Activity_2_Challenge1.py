# Activity_15.py
# @ Author: Norma Seym
# Date: December 2023
"""
Directions: Write a program that displays the first 2 lists. The user must be prompted and given a choice to see either
the sum or the average of the combined lists. Assume that the user enters valid integers only.
"""
list_1 = [23, 66, 23, 12]
list_2 = [1, 19, 4, 8]
# Uses built-in sum() function to get the sum of the combined lists.
sum_list = sum(list_1) + sum(list_2)

# Displays both lists.
print("List 1:", list_1, "\nList 2:", list_2)

# Prompts the user to choose to see either the sum or the average of the lists and saves into `option`.
option = input("Display the (S)um or (A)verage of the combined lists? ")

# Checks if `option` is "S".
if option.upper() == "S":
    # Displays the sum of the combined lists.
    print(f"The sum of the items on the lists is {sum_list}")

# If the option is not "S"
else:
    # Adds the length of the combined lists.
    len_list = len(list_1) + len(list_2)
    # Calculated the average of the combined lists.
    avg_list = sum_list / len_list
    # Displays the average of the combined lists.
    print(f"The average of the items on the list is {avg_list}")

"""
Test case assertion 1:
`option` is "S", result is sum = 156

Test case assertion 2:
`option` is "A", result is average = 19.5
"""
