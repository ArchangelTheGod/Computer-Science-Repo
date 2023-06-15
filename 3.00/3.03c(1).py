#Name: Azel (Axxl)
#Date: 2/5/23
#File Name: 3.03.py
#Description: Returns an error if number is a neg, or above 100.

#inputs
grade = int(input("Please enter your mark (in percentage) -> "))

#Constants
gradeA = 100
gradeB = 80
gradeC = 60
gradeD = 50
gradeF = 40

#If/Elifs
if (grade >100):
    print("Error! Input cannot be above 100!")
    print("<-- I've failed you. I'm sorry. -->")
elif (grade < -1):
    print("Error! Input cannot be less than -1!")
    print("<-- Whoops! Terminal Error -->")


#If/Elifs (1)
if (grade >90) or (grade == 100):
    print("Your grade is an A.")
elif (grade <90) and (grade >= gradeB):
    print("Your grade is a B")
elif (grade < gradeB) and (grade >= gradeC):
    print("Your grade is a C")
elif (grade < gradeC) and (grade >= gradeD):
    print("Your grade is a D")
elif (grade < gradeD) and (grade >= gradeF):
    print("You failed. You have an F")


#Output
print("<---- Hey! ---->")