#Name: Azel (Axxl)
#Date: 18/5/2023
#File Name: 3.04d.py
#Description: Generates a die

#Imports
import random

#Randomizer
death = random.randrange(6) + 1

#If/Elif
if (death == 1):
    print("-----------")
    print("|         |")
    print("|    o    |")
    print("|         |")
    print("-----------")
    print("You rolled 1")
elif (death == 2):
    print("-----------")
    print("|         |")
    print("|  o   o  |")
    print("|         |")
    print("-----------")
    print("You rolled 2")
elif (death == 3):
    print("-----------")
    print("|         |")
    print("|  o o o  |")
    print("|         |")
    print("-----------")
    print("You rolled 3")
elif (death == 4):
    print("-----------")
    print("|  o   o  |")
    print("|         |")
    print("|  o   o  |")
    print("-----------")
    print("You rolled 4")
elif (death == 5):
    print("-----------")
    print("|  o   o  |")
    print("|    o    |")
    print("|  o   o  |")
    print("-----------")
    print("You rolled 5")
elif (death == 6):
    print("-----------")
    print("|  o   o  |")
    print("|  o   o  |")
    print("|  o   o  |")
    print("-----------")
    print("You rolled 6")