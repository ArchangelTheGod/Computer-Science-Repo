#Name: Archangel (Azel)
#Date: 13/6/23
#File Name: 4.03.py
#Description: Uses tkinter.

#Imports
from tkinter import *

#Constants
window = Tk()
lbl = Label(window, text="You've got a virus", font=("Times New Roman", 100))
img1 = PhotoImage(file='./IMG/Reverse-Flash.png')

#Listeners
# def clicked():    
#     res = "Welcome to " + txt.get()
#     lbl.configure(text = res)
# def addMe():
#     global counter 
#     counter += int(txt.get())
#     lbl.configure(text = counter)

#Window Structuring
window.title("Ransomware Attack!")
#Labels
lbl.grid()
#Buttons
    # btn = Button(window, text="Pay Ransom", bg="Green", fg="White", command=clicked)
btn = Button(window, text="Pay Ransom", bg="Green", fg="White")
btn.grid(column=1, row=0)
#Text Inputs
# txt = Entry(window,width=10)
# txt.grid(row=1, column=1)
#Images
image = Label(window, image= img1)
image.grid(row= 1, column= 2)

#MISC
# txt.focus()
counter = 0
window.mainloop()