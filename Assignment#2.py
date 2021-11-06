print("The apple = 20 pesos orange = 25 pesos")

appleCost = 20
orangeCost = 25

def getTotalApple():
    orderedApples= int(input("How many apples do you want to buy?: "))
    return orderedApples

def getTotalOrange():
    orderedOranges= int(input("How many oranges do you want to buy?: "))
    return orderedOranges

def getTotalCost(appleCostF, orangeCostF, appleQty, orangeQty):
    totalCost= (appleQty*appleCostF) + (orangeQty*orangeCostF)
    return totalCost

def DisplayOutput(AmountFunc):
    print(f"The total amount is {amount}.")

applesOrdered =  getTotalApple()
orangesOrdered = getTotalOrange()

amount = getTotalCost (appleCost, orangeCost, applesOrdered, orangesOrdered)

DisplayOutput(amount)