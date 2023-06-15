#Name: Azel (Axxl)
#Date: 2/5/23
#File Name: 3.02.py
#Description: Feeds Pacman till he dies.

#Input
askPellets = int(input("Please specify the amount of pellets you wish to feed Pacman with. -> "))

#Constants
pellet100 = 100
pellet101 = 101
pellet150 = 150

#Elifs
if askPellets < pellet100:
    print("Still Hungry Bud.")
elif askPellets == pellet100:
    print("Still Hungry Bud.")
elif askPellets == pellet101:
    print("Thanks bud.")
elif askPellets == pellet150:
    print("Thanks bud.")
elif askPellets > pellet150:
    print("'Pacman is now full.'")
elif askPellets == pellet150:
    print("'Pacman is now full.'")
# elif askPellets > 9999:
#     print("STOPPP!!!!")
# elif askPellets == 9999:
#     print("STOPPP!!!!")    
# elif askPellets > 99999:
#     print("YOU CAN STOP NOW, YOU KNOW.")
# elif askPellets == 99999:
#     print("YOU CAN STOP NOW, YOU KNOW.")

#Output
print("<-- Oh, Hey There! -->")