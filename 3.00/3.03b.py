#Name: Azel (Axxl)
#Date: 2/5/23
#File Name: 3.03.py
#Description: Checks if you're eligible for a discount.

#Inputs
age = int(input("Please enter your age. -> "))

#If/Elif
if (age >=65) and (age <12):
    print("Congratulations! You're eligible to recieve the discount!")
elif (age <65) and (age >12):
    print("So sorry there bud, you sadly don't qualify for the discount :( ")
