#Name: Azel (Axxl)
#Date: 2/5/23
#File Name: 3.02b.py
#Description: Something about Baskin Robins :)

#Inputs
cones = float(input("How many cones did you sell in a week? -> "))
salary = float(input("Please enter your salary. ->"))

#Constants
bonus = 10.00
bonusperCone = 00.10
bonusperCone2 = 00.25
#----------------------
cones100 = 100
cones250 = 250

#Elifs
if cones > cones100:
    total1 = round(bonusperCone * cones, 2)
    print("Total bonus:", "$", total1)
elif cones == cones250:
    total2 = round(bonusperCone * cones, 2)
    print("Total bonus:", "$", total2)
elif cones > 250:
    total3 = round(bonusperCone2 * cones, 2)
    print("Total bonus:", "$", total3)
elif cones < 100:
    print("So sorry there bud, no bonus for your lazy ass")
elif cones == 100:
    print("So sorry there bud, no bonus for your lazy ass")

if cones > cones100:
    total11 = salary + total1
    print(total11)
elif cones == cones250:
    total22 = salary + total2
    print(total22)
elif cones > 250:
    total33 = salary + cones250
    print(total33)
elif cones < 100:
    salary + 0
elif cones == 100:
    salary + 0


#Outputs
print("<-- HI -->")