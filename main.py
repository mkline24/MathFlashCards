"""
This code will make flash cards for the user to practice math based on what settings they would like (difficulty, amount, and type of math)

Functions:

level : will store the difficulty level that is entered

operator : will store whether they want to do addition, subtration, or multiplication

hwMany : will use this to determine how many problems to give
"""

import random

level = input("What difficulty would you like?(easy, med, hard)" )
operator = input("What type of math would you like to practice?(+,-,*) ")
hwMany = int(input("How many would you like to practice? "))


