#Name: Azel (Axxl)
#Date: 1/5/23
#File Name: totalTaxes.py
#Description: I DUNNO :)

#Inputs
price = float(input("Please enter the price of the meal. -> "))

#Constants
hst = 0.13


#If/Else
if price > 4.00:
    totalTaxes = price + hst

else:
    noTax = price
    print("$", noTax)

#Outputs
print("Total Taxes", "$", totalTaxes)
print("<---- NO! ---->")