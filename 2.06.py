#Name: Azel (Axxl)
#Date: 12/4/23
#File Name: 2.06.py
#Description: Returns a custom receipt with user-controlled outputs

#Inputs
item = input("Enter Item Names ->")
prices = float(input("Enter Item Price(s) ->"))
quant = int(input("Enter Item Quantity(ies) ->"))

#Calculations
subtotal = quant*prices
hst = round(0.13*subtotal, 2) 
total = subtotal+hst

#Outputs
print("Receipt".center(100))
print("="*100)
print("Description", "\t\t", "QTY", "\t\t", "Price", "\t\t", "Subtotal")
print(item, "\t\t", quant, "\t\t", prices, "\t\t", subtotal, "\n")
print("HST:", "\t\t", hst)
print("="*100)
print("Total:", "\t\t", total)