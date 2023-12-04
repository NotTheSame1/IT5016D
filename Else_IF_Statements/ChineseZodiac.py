# ChineseZodiac.py
# @ Author: Norma Seym
# Date: 04, December 2023

"""
Description:
a program that reads a year from the user and displays the animal associated
with that year.

Info:
The Chinese zodiac assigns animals to years in a 12-year cycle.
Divide your year of birth by 12 and read about the remainder. If the number of
the year can be divided with no remainder, take the remainder as zero. Each
remainder corresponds to an animal sign.
0: Monkey
1: Rooster
2: Dog
3: Pig
4: Rat
5: Ox
6: Tiger
7: Hare
8: Dragon
9: Snake
10: Horse
11:Sheep
"""

# Returns input as integer
year = int(input("What year were you born? "))

# Calculates remainder of input and 12 and assigns zodiac animal based
# on the value of the remainder
if year % 12 == 0:
    print("Your Chinese Zodiac is a Monkey")
elif year % 12 == 1:
    print("Your Chinese Zodiac is a Rooster")
elif year % 12 == 2:
    print("Your Chinese Zodiac is a Dog")
elif year % 12 == 3:
    print("Your Chinese Zodiac is a Pig")
elif year % 12 == 4:
    print("Your Chinese Zodiac is a Rat")
elif year % 12 == 5:
    print("Your Chinese Zodiac is a Ox")
elif year % 12 == 6:
    print("Your Chinese Zodiac is a Tiger")
elif year % 12 == 7:
    print("Your Chinese Zodiac is a Hare")
elif year % 12 == 8:
    print("Your Chinese Zodiac is a Dragon")
elif year % 12 == 9:
    print("Your Chinese Zodiac is a Snake")
elif year % 12 == 10:
    print("Your Chinese Zodiac is a Horse")
elif year % 12 == 11:
    print("Your Chinese Zodiac is a Sheep")
else:
    print("Incorrect data entered")


"""
Test case assertion 1:
If year is 1986, the zodiac animal should be a Tiger

Test case assertion 2:
If year is 2011, the zodiac animal should be a Hare

Reference: TravelChinaGuide.com (2023), Chinese Zodiac Calculator. What is My 
Chinese Zodiac?. How to Calculate Your Chinese zodiac sign mathematically?.
https://www.travelchinaguide.com/intro/social_customs/zodiac/calculator.htm
"""
