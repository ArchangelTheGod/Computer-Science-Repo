#Name: Azel (Axxl)
#Date: 18/5/2023
#File Name: 3.04e.py
#Description: Guessing game

#Imports
import random

#Imputs
guess = int(input("Guess a number between 0 & 1000! -> "))

#Randomizer
rand = random.randrange(1000)

#If/Elif
if (guess <= 100) and (guess >= 0):
    print("Generated Number:")
    print(rand)
elif (guess >= 9999) or (guess < 999999999999999):
    print("False")