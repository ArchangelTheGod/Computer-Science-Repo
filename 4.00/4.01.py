#Name: Archangel (Azel)
#Date: 9/6/23
#File Name: 4.01.py
#Description: I literally have no fucking idea :)

#Input
temperature = float(input("What is the temperature of the substance, child? -> "))

#Loop/If/Elif
loop = True
while loop:
    if (temperature > 102.5):
        toomuch = True
        print("Turn down the thermostat, wait 5 minutes, and check the temperature again.")
    elif (temperature < 102.5):
        good = True
        print("Temperature is at a reasonable rate.")

        if toomuch == True:
            print("Terminating process")
            break

if good == True:
    print("restarting...")