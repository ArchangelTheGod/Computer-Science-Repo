#Name: Azel (Axxl)
#Date: 13/4/23
#File Name: pay_calc.py
#Description: Returns a calculated salary

#Inputs
hours = int(input("How many hours total did you work? ->"))
rate = float(input("What is your current rate of pay? ->"))
name = input("Please specify your name. ->")

#Calculations
net_pay = hours*rate
taxes = 0.1*net_pay
total_pay = round(net_pay - taxes,2)

#Print
print("*"*30)
print("Name:", name)
print("Hourly Rate:", net_pay)
print("Hours Worked:", hours)

#Footer
print("Net Pay\t\t", "Taxes\t\t", "Total Pay")
print(net_pay, "\t\t", taxes, "\t\t", total_pay)
print("*"*30)