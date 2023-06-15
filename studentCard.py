#Start
print("Please enter your information to continue...")

#logging
f = open("studentCard.txt", "a")

#Names
name = input("Enter your Name -> ")
surname = input("Enter your Surname -> ")

#Address
address = input("Enter your Address -> ")

#Orginization
org = input("Enter your Current Employer -> ")

#Logging2
f.write(name)
f.write("\n")
f.write("\n")
f.write(surname)
f.write("\n")
f.write("\n")
f.write(address)
f.write("\n")
f.write("\n")
f.write(org)
f.close()

#print
print("Your info:")
print("")
print("Name:", name, surname)
print("")
print("Address:", address)
print("")
print("Your Specified Orginization:", org)
print("☺Ä☻☻☻☻☻☻☻☻☻▬☺☺♂☺♥♥♥!♥♥♥♥!!♥♥♥♥♥♥♥♥♥!")