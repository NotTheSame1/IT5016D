# RichterScale.py
# @ Author: Norma Seym
# Date: 01, December 2023
"""
Description:
A program that reads a magnitude from the user and displays the appropriate
descriptor.

INFO: Magnitude Descriptor
< 1.9 Micro
2.0 - 2.9 Very minor
3.0 - 3.9 Minor
4.0 - 4.9 Light
5.0 - 5.9 Moderate
6.0 - 6.9 Strong
7.0 - 7.9 Major
8.0 - 9.9 Great
10.0 or more Meteoric
"""

# Gets user input to save into the variable and converts into float
magnitude = float(input("Hello, please enter the magnitude of the earthquake\n"))

# Uses input from `magnitude` to determine Richter Scale descriptor
if magnitude >= 10:
    print(f"A {magnitude} earthquake is measured as Meteoric in the Richter Scale.")
elif magnitude >= 8.0:
    print(f"A {magnitude} earthquake is measured as Great in the Richter Scale.")
elif magnitude >= 7.0:
    print(f"A {magnitude} earthquake is measured as Major in the Richter Scale.")
elif magnitude >= 6.0:
    print(f"A {magnitude} earthquake is measured as Strong in the Richter Scale.")
elif magnitude >= 5.0:
    print(f"A {magnitude} earthquake is measured as Moderate in the Richter Scale.")
elif magnitude >= 4.0:
    print(f"A {magnitude} earthquake is measured as Light in the Richter Scale.")
elif magnitude >= 3.0:
    print(f"A {magnitude} earthquake is measured as Minor in the Richter Scale.")
elif magnitude >= 2.0:
    print(f"A {magnitude} earthquake is measured as Very Minor in the Richter Scale.")
else:
    print(f"A {magnitude} earthquake is measured as Micro in the Richter Scale.")
