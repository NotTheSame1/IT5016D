# ParkingMeter.py
# @ Author: Norma Seym
# Date: 27, November 2023
"""
Description: Write a simple program that does the following:
    - Displays a message on the screen saying: "Kia Ora, this is a parking meter"
    - Creates and sets the value for variable ParkTime = 4 hours
    - Creates and sets values for variables: rate and cost
    - Calculates the parking charges for ParkTime using an If statement
    - Displays appropriate message showing the calculated charge.
    - Extend the program further by having the user enter the number of hours that they wish to park.
    - Create 2 more test case assertions to the one already shown, and use them to test your work.

INFO: This parking meter charges $4 per hour for the first 3 hours and then $2 per hour thereafter.
"""

print("Kia Ora, this is a parking meter")
print("Park Time:\n $4/hr for the first 3 hours\n $2/hr for each additional hour")

# return input as an integer
park_time = (int(input("How many hours will you be parking for? ")))
print("Park time is ", park_time, " hours.")
rate = 4
cost = rate * park_time

# Calculate cost for every hour over 3 hours
if park_time > 3:
    cost = rate * 3
    # Drop rate by $2
    rate -= 2
    # Get remainder of hours
    park_time -= 3
    # Add to the current cost
    cost += rate * park_time
    print("The cost for parking is $" + str(cost))
# Calculation for cost 0-3 hours
else:
    cost = rate * park_time
    print("The cost of the parking is $" + str(cost))

"""
Test case assertion 1:
If parking hours is 4, the parking cost should be $14
If parking hours is 1, the parking cost should be $4
If parking hours is 3, the parking cost should be $12
"""