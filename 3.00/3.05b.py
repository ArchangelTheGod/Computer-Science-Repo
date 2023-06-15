#Name: Azel (Axxl)
#Date: 24/5/23
#File Name: 3.05b.py
#Description: Converts mark to letter form.

#Loop
run = True
while run:

    #Inputs
    print("<<ENTER *999* TO TERMINATE>>")
    prompt = int(input("Enter your mark. -> "))

    #Abort
    if prompt == 999:
        print("Terminating...")
        print("Process Terminated")
        break
    
    #If/Elif
    if prompt == 100:
        print("A+")
        if (prompt >95) and (prompt <100):
            print("A")
        elif (prompt >90) and (prompt <95):
            print("A-")
    elif (prompt >85) and (prompt <90):
        print("B+")
        if (prompt >80) and (prompt <85):
            print("B")
        elif (prompt <85) and (prompt >80):
            print("B-")
    elif (prompt >75) and (prompt <80):
        print("C+")
        if (prompt >70) and (prompt <75):
            print("C")
        elif (prompt <75) and (prompt >70):
            print("C-")
    elif (prompt >65) and (prompt <70):
        print("D+")
        if (prompt >60) and (prompt <65):
            print("D")
        elif (prompt <65) and (prompt >60):
            print("D-")
    elif (prompt >55) and (prompt <60):
        print("F+")
        if (prompt >50) and (prompt <55):
            print("F")
        elif (prompt <55) and (prompt >50):
            print("F-")
    elif (prompt <50):
        print("R")