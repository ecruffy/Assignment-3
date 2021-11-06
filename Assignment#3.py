def getTotalMoney():
    spendableMoney = int(input("How much money do you wish to spend?: "))
    return spendableMoney

def getAppleQty():
    qtyOfApples= int(input("How much does an apple cost?: "))
    return qtyOfApples

def getApplesAfford(totalMoneySpendableF, appleCostF):
    getAppleAmount= (totalMoneySpendableF) // (appleCostF)
    return getAppleAmount

def getChange(totalMoneySpendableF, appleCostF):
    amountOfChange= (totalMoneySpendableF) % (appleCostF)
    return amountOfChange

def DisplayOutput(GetQuantityYouCanBuyF, GetTotalChangeF):
    print(f"You can buy {applesYouCanBuy} apples and your change is {change} pesos")

totalMoneySpendable = getTotalMoney()
appleCost = getAppleQty()

applesYouCanBuy = getApplesAfford(totalMoneySpendable, appleCost)
change = getChange(totalMoneySpendable, appleCost)

DisplayOutput(applesYouCanBuy, change)