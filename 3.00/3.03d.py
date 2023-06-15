#Name: Azel (Axxl)
#Date: 9/5/23
#File Name: 3.03d.py
#Description: Checks if you qualify for a certain level of boxing.

#Inputz
name = str(input("Please enter your name. -> "))
userWeight = float(input("Please enter your weight (Kg). ->"))


#Constants
hW = 90.72
cW = 79.4
lW = 76.2
sM = 72.6
mW = 69.9

#If/elifs
if hW <= userWeight:
    print("true1")
    class1 = "HeavyWeight"
    print("You qualify for HeavyWeight.\n")
    print("Name:", name)
    print("Weight:", userWeight)
    print("Class:", class1)
elif (userWeight < cW) and (userWeight >= hW):
    class2 = "Cruiserweight"
    print("You qualify for Cruiserwight.\n")
    print("Name:", name)
    print("Weight:", userWeight)
    print("Class:", class2)
elif (userWeight < lW) and (userWeight >= cW):
    class3 = "Light Heavyweight"
    print("You qualify for Light Heavyweight.\n")
    print("Name:", name)
    print("Weight:", userWeight)
    print("Class:", class3)
elif (userWeight < sM) and (userWeight >= lW):
    class4 = "Super MiddleWeight"
    print("You qualify for Super Middleweight.\n")
    print("Name:", name)
    print("Weight:", userWeight)
    print("Class:", class4)
elif (userWeight < mW) and (userWeight >= sM):
    class5 = "Middle Weight"
    print("You qualify for Middleweight.\n")
    print("Name:", name)
    print("Weight:", userWeight)
    print("Class:", class5)

#Output
print("<-- NO!!! DON'T!!! -->")