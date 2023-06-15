#Name: Azel (Axxl)
#Date: 16/5/23
#File Name: 3.04b.py
#Description: I HAVE NO IDEA :)

#Imports
import random

#Randomizer
randmark = random.randrange(100)

#If/Elifs
if (randmark >= 100) or (randmark <= 49):
    False
    print("False")
elif (randmark > 50) and (randmark < 101): 
    print("You Passed!")
    print(randmark)
elif (randmark == 100) and (randmark > 50):
    print("You Passed!")
    print(randmark)
elif (randmark > 30) and (randmark < 50):
    print("You Failed!")
    print(randmark)

#Output
print("<--- Hey! --->")