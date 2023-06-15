#Name: Azel (Axxl)
#Date: 30/5/23
#File Name: 3.06.py
#Description: Dice game 

#Welcome
print("Welcome")
print("\t\tInstructions\t\t")
print("\t\tGuess the number that is rolled\t\t")
print("\t\tSee if your're correct\t\t")

#Imports
import random

#Confirm?
confirm = input("\nAre you ready? [Y/N] -> ")

if confirm.lower() == "y":
    print("Okay!")
    confirmed = "true"
elif confirm.lower() == "n":
    +
    print("false.")

#Confirmed
if confirmed == "true":
    startRand = random.randrange(5) + 1
    ask = input("Guess a number from 1-6 -> ")
    if (startRand == 1):  
        print("-----------")
        print("|         |")
        print("|    o    |")
        print("|         |")
        print("-----------")
    elif (startRand == 2):
        print("-----------")
        print("|         |")
        print("|  o   o  |")
        print("|         |")
        print("-----------")
    elif (startRand == 3):
        print("-----------")
        print("|         |")
        print("|  o o o  |")
        print("|         |")
        print("-----------")
    elif (startRand == 4):
        print("-----------")
        print("|  o   o  |")
        print("|         |")
        print("|  o   o  |")
        print("-----------")
    elif (startRand == 5):
        print("-----------")
        print("|  o   o  |")
        print("|    o    |")
        print("|  o   o  |")
        print("-----------")
    elif (startRand == 6):
        print("-----------")
        print("|  o   o  |")
        print("|  o   o  |")
        print("|  o   o  |")
        print("-----------")
#If
if (startRand == ask):
    print("You got it correct")
    if (ask > startRand) or (ask < startRand):
        print("WRONG LOL")


#Output
print("I rolled:", startRand)
print("You guessed:", ask)
