# SoundLevels.py
# @ Author: Norma Seym
# Date: 04, December 2023

"""
Description:
A program that reads a sound level in decibels from the user and displays
a message advising the noise level is similar to a specific item.

- If the user enters a decibel level that matches one of the noises in the table,
then the program should display a message containing only that noise.
- If the user enters a number of decibels between the noises listed, then the
program should display a message indicating which noises the level is between.
- Ensure that the program also generates reasonable output for a value smaller
than the quietest noise in the table, and for a value larger than the loudest
noise in the table.

Info:
Noise Decibel level (dB)
Jackhammer 130
Petrol lawnmower 106
Alarm clock 70
Quiet room 40
"""

decibel_input = int(input("Please enter a decibel value:\n"))

if decibel_input == 130:
    print(f"A decibel level of {decibel_input} is the same as a jackhammer")
elif decibel_input == 106:
    print(f"A decibel level of {decibel_input} is the same as a petrol lawnmower")
elif decibel_input == 70:
    print(f"A decibel level of {decibel_input} is the same as an alarm clock")
elif decibel_input == 40:
    print(f"A decibel level of {decibel_input} is the same as a quiet room")
elif decibel_input <= 129 or decibel_input > 106:
    print(
        f"A decibel level of {decibel_input} is between a jackhammer and a Petrol lawnmower"
    )
