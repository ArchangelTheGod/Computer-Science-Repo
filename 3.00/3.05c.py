#Name: Azel (Axxl)
#Date: 24/5/23
#File Name: 3.05c.py
#Description: Calculates income tax on your salary.

#Inputs
salaryPrompt = int(input("Enter your salary. -> "))

#Constants
Percent1 = 0.25
Percent2 = 0.30
Percent3 = 0.35

#if/Elif
if salaryPrompt <= 6000:
    print("False")
    if (salaryPrompt > 6000) and (salaryPrompt < 20000):
        totalOutput = salaryPrompt*Percent1
        print(totalOutput)
    elif (salaryPrompt > 20000) and (salaryPrompt < 50000):
        totalOutput = salaryPrompt*Percent2
        print(totalOutput)
    elif (salaryPrompt > 50000) and (salaryPrompt <)