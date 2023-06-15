#Name: Azel (Axxl)
#Date: 23/5/23
#File Name: 3.05a.py
#Description: ORDER LE PIZZA 

#Inputs
#Pizza size menu
print("\t\tPizza Size\n\t1. Large\t-\t$7.00\n\t2. Medium\t-\t$6.00\n\t3. Small\t-\t$5.00")
pizzaSize = str(input("Specify the size of the pizza. -> "))
toppingsNum = int(input("Specify amount of toppings. -> "))

#Constants
largePizza = 7.00
mediumPizza = 6.00
smallPizza = 5.00

#If/Elifs
if pizzaSize.lower() == "large":
    largeToppings = 1.25
    if (toppingsNum == 1):
        # wwwwsssrdfdt5hug6ytfrd5yh5u67kjo9i8juh5ytgfrdeft5ghhhhhhhhht
        total = toppingsNum*largeToppings+largePizza
        print(total)
    elif (toppingsNum == 2):
        largeToppings = 1.15
        total = toppingsNum*largeToppings+largePizza
        print(total)
    elif (toppingsNum >= 3):
        largeToppings = 1.00
        total = toppingsNum*largeToppings+largePizza
        print(total)

if pizzaSize.lower() == "medium":
    mediumToppings = 1.00
    if (toppingsNum == 1):
        total = toppingsNum*mediumToppings+mediumPizza
        print(total)
    elif (toppingsNum == 2):
        mediumToppings = 0.90
        total = toppingsNum*mediumToppings+mediumPizza
        print(total)
    elif (toppingsNum >= 3):
        mediumToppings = 0.80
        total = toppingsNum*mediumToppings+mediumPizza
        print(total)

if pizzaSize.lower() == "small":
    smallToppings = 0.75
    if (toppingsNum == 1):
        total = toppingsNum*smallToppings+smallPizza
        print(total)
    elif (toppingsNum == 2):
        smallToppings = 0.70
        total = toppingsNum*smallToppings+smallPizza
        print(total)
    elif (toppingsNum >= 3):
        smallToppings = 0.65
        total = toppingsNum*smallToppings+smallPizza
        print(total)

#Output
print("<--- No. --->")