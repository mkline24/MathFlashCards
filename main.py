"""
This code will make flash cards for the user to practice math based on what settings they would like (difficulty, amount, and type of math)

Functions:

mx : will store how high the numbers should go

mn: will store how low the numbers should go

operator : will store whether they want to do addition, subtration, or multiplication

hwMany : will use this to determine how many problems to give
"""

import random


operator = input("What would you like to practice?(+, -, *) ")
hwMany = int(input("How many would you like to practice? "))
mx = int(input("Set the max (enter any whole number): " ))
mn = int(input("Set the Minimum (enter any whole number): "))
print(" ")

if operator == "+":
  for i in range (hwMany):
    a1 = random.randint(mn,mx) #this is "a1" for add 1 and is the first random number be added
    a2 = random.randint(mn,mx) #this is "a2" for add 2 and is the second random number to be added
    prob = int(input((str(a1) + " + " + str(a2) + " = ")))
    if prob == a1 + a2:
      print("Correct!")
      print(" ")
    else:
      print("Incorrect. The correct answer was " + str(a1 + a2) + ".")
      print(" ")


elif  operator == "-":
  for i in range (hwMany):
    a1 = random.randint(mn,mx) #this is "a1" for add 1 and is the first random number be added
    a2 = random.randint(mn,mx) #this is "a2" for add 2 and is the second random number to be added
    prob = int(input((str(a1) + " - " + str(a2) + " = ")))
    if prob == a1 - a2:
      print("Correct! ")
      print(" ")
    else:
      print("Incorrect. The correct answer was " + str(a1 - a2) + ". ")
      print(" ")



elif  operator == "*":
  for i in range (hwMany):
    a1 = random.randint(mn,mx) #this is "a1" for add 1 and is the first random number be added
    a2 = random.randint(mn,mx) #this is "a2" for add 2 and is the second random number to be added
    prob = int(input((str(a1) + " * " + str(a2) + " = ")))
    if prob == a1 * a2:
      print("Correct!")
      print(" ")
    else:
      print("Incorrect. The correct answer was " + str(a1 * a2) + ".")
      print(" ")