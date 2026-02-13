#to use the function: money = inventory(x,x,money)
from recipes import recipe
ingredients = {"shells": 0,
                "meat": 0,
                "cheese": 0,
                "hotSauce": 0}
def buyIngre(money):
    print("~~~~~~~~~SHOP~~~~~~~~~~~")
    item = input("What do you want to buy?(shells(1)/meat(2)/cheese(3)/hotSauce(4))\n")
    if item == "shells" or item == "meat" or item == "cheese" or item == "hotSauce" or item == "1" or item == "2" or item == "3" or item == "4":
        amount = int(input("How many of this item?\n"))
        return inventory(item, amount, money)
    else:
        print("That is not an option, this is a taco truck...")
        buyIngre(money)

def inventory(item, amount, money):
    global ingredients
    if item == "shells" or item == "1":
        if money >= amount * .40:
            ingredients["shells"] += amount
            money -= amount * .40
        else:
            print("You're too poor to afford this.")
    elif item == "meat" or item == "2":
        if money >= amount * .70:
            ingredients["meat"] += amount
            money -= amount * .70
        else:
            print("You're to poor to afford this.")
    elif item == "cheese" or item == "3":
        if money >= amount * .55:
            ingredients["cheese"] += amount
            money -= amount * .55
        else:
            print("You're to poor to afford this.")
    else:
        if money >= amount * .35:
            ingredients["hotSauce"] += amount
            money -= amount * .35
        else:
            print("You're to poor to afford this.")
    return money

def maxTacos(list):
    copyList = list
    global recipe
    tacosMade = 0
    for i in range(0, list["shells"]):
        copyList["shells"] -= 1
        copyList["meat"] -= recipe["meat"]
        copyList["cheese"] -= recipe["cheese"]
        copyList["hotSauce"] -= recipe["hotSauce"]
        if copyList["shells"] >= 0 and copyList["meat"] >= 0 and copyList["cheese"] >= 0 and copyList["hotSauce"] >= 0:
            tacosMade +=1
        else:
            break
    return tacosMade


def showStat(money):
    global ingredients
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    print("$$$:", money)
    print("Shells:", ingredients["shells"])
    print("Meat:", ingredients["meat"])
    print("Cheese:", ingredients["cheese"])
    print("Hot Sauce:", ingredients["hotSauce"])
    print(f"Total tacos: {maxTacos(ingredients)}")