# Activity_2_Challenge5.py
# @ Author: Norma Seym
# Date: December 2023
"""
Directions: Write a program that outputs every odd valued index item from list_1
"""

list_1 = [23, 66, 23, 12]

for x in list_1:
    if x % 2 != 0:
        print(x, end=",")
