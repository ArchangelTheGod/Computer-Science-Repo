#Name: Azel (Axxl)
#Date: 2/5/23
#File Name: 3.03.py
#Description: Converts percentage marks to a Grade.

#inputs
grade = int(input("Please enter your mark (in percentage) -> "))

#Constants
gradeA = 100
gradeB = 80
gradeC = 60
gradeD = 50
gradeF = 40


#If/Elifs
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