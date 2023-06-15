#Name: Azel (Axxl)
#Date: 2/5/23
#File Name: 3.03.py
#Description: Checks if the inputs are negative numbers

#Inputs
length = int(input("Please specify the length. -> "))
width = int(input("Please specify the width. -> "))

#If statement
if (length <= -1) and (width <= -1):
    print("Error! You must insert POSITIVE numbers. (Error, Cannot Calculate Negatives.)")
    print("<---- You're such a disapointment. ---->")
elif (length >1) and (width >1):
    area = length*width
    print("Area is equal to:", area)
    print("<--- Hey! ---->")