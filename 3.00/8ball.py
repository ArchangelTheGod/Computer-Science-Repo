#8ball by Quad9 God

#Imports
import random
run = True
while run:
    #Input
    print("Enter *TERMINATE* to exit.")
    prompt = input("\nWhat would you like to ask me? -> ")

    #Loop
    if prompt.lower() == "terminate":
        break
    
    #Randomizer
    promptRand = random.randrange(15) + 1

    #If/Elif
    if (promptRand == 1):
        print("\nFocus a bit harder. And try again.")
    elif (promptRand == 2):
        print("\nIt is not for certain.")
    elif (promptRand == 3):
        print("\nThere is a possibility... It isn't impossible though.")
    elif (promptRand == 4):
        print("\nYes.")
    elif (promptRand == 5):
        print("\nNo.")
    elif (promptRand == 6):
        print("\nImpossible!")
    elif (promptRand == 7):
        print("\nVery Likely...")
    elif (promptRand == 8):
        print("\nUnfortunately, No...")
    elif (promptRand == 9):
        print("\nFortunately, No")
    elif (promptRand == 10):
        print("\nUnfortunately, Yes...")
    elif (promptRand == 11):
        print("\nFortunately, Yes")
    elif (promptRand == 12):
        print("8ball Doesn't want to answer your question. Try Again.")
    elif (promptRand == 13):
        # print("You have frustrated 8ball. Process is being terminated.")
        # break
        print("FR?")
    elif (promptRand == 14):
        # print("8ball.exe has stopped working. Process is being terminated.")
        # break
        print("Slayyyyyy Queen")
    elif (promptRand == 15):
        # print("8ball doesn't want to talk/answer you. Process is being terminated.")
        #break
        print("no stupid")