#Name: Azel (Axxl)
#Date: 18/4/23
#File name: 2.07cc.py
#Description: Returns a receipt.

#Input
itemQuant = str(input("Please enter the amount of product you are purchasing. ->"))
itemPrice =  float(input("Please enter the item's price. -->"))

#Constants
hst = .13

#Calculations
subtotal = itemQuant*itemPrice
hst = round(0.13*subtotal, 2) 
total = subtotal+hst

#Outputs
print("<-- Item -->")
print(subtotal)