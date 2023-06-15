#Name: Azel (Axxl)  
#Date: 11/4/23
#File name: 2.05b_simple_repot_card.py
#Description: Returns a "repot card" 

#Inputs
mathGrade = float(input("Specify Math Grade ->"))
englishGrade = float(input("Specify English Grade ->"))
computerscGrade = float(input("Specify Computer Science Grade ->"))
classAverage = float(input("Specify Your Class Average ->"))
schoolname = input("Specify Your School ->")
country = input("Specify Your Country ->")
province = input("Specify Your Province (Optional) ->")
state = input("Specify Your State (Optional) ->")
residence = input("Specify Your Place of Residence->")
name = input("Specify Name ->")
middleName = input("Specify Middle Name (Optional!) ->")
surname = input("Specify Surname ->")



#Headers
print("Student Repot".center(100))
print(schoolname.center(100))

#Body
print("Current Marks for", name, middleName, surname, "are\n")
print("Math Average\t\t\t\t\t\t", mathGrade) 
print("English Average\t\t\t\t\t\t", englishGrade)
print("Computer Science Average\t\t\t\t", computerscGrade, "\n\n\n")

#Footer
print("Country:", country)
print("Province:",  province)
print("State:", state)
print("Residence:", residence, "\n\n")


print("All 'Repot Cards' are to be returned to point of origin.")
print("Principal's Signature: David Ragoonath\n")
print("Date: 31/12/2002".center(100))