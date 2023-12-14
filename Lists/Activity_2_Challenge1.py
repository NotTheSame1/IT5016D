# Activity_15.py
# @ Author: Norma Seym
# Date: December 2023
"""
Directions: Write a program that displays the first 2 lists. The user must be prompted and given a choice to see either
the sum or the average of the combined lists. Assume that the user enters valid integers only.
"""
list_1 = [23, 66, 23, 12]
list_2 = [1, 19, 4, 8]
sum_list = sum(list_1) + sum(list_2)

print("List 1:", list_1, "\nList 2:", list_2)

option = input("Display the (S)um or (A)verage of the combined lists? ")
if option.upper() == "S":
    print(sum_list)

else:
    len_list = len(list_1) + len(list_2)
    avg_list = sum_list / len_list
    print(avg_list)
