#to use the function: money = inventory(x,x,money)
ingredients = {"shells": 0,
                "meat": 0,
                "cheese": 0,
                "hotSauce": 0}
def buyIngre(money):
    print("~~~~~~~~~SHOP~~~~~~~~~~~")
    item = input("What do you want to buy?(shells/meat/cheese/hotSauce)\n")
    if item == "shells" or item == "meat" or item == "cheese" or item == "hotSauce":
        amount = int(input("How many of this item?\n"))
        return inventory(item, amount, money)
    else:
        print("That is not an option, this is a taco truck...")
        buyIngre(money)

def inventory(item, amount, money):
    global ingredients
    if item == "shells":
        if money >= amount * .20:
            ingredients["shells"] += amount
            money -= amount * .20
        else:
            print("You're too poor to afford this.")
    elif item == "meat":
        if money >= amount * .50:
            ingredients["meat"] += amount
            money -= amount * .50
        else:
            print("You're to poor to afford this.")
    elif item == "cheese":
        if money >= amount * .40:
            ingredients["cheese"] += amount
            money -= amount * .40
        else:
            print("You're to poor to afford this.")
    else:
        if money >= amount * .25:
            ingredients["hotSauce"] += amount
            money -= amount * .25
        else:
            print("You're to poor to afford this.")
    return money

def showStat(money):
    global ingredients
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    print("$$$:", money)
    print("Shells:", ingredients["shells"])
    print("Meat:", ingredients["meat"])
    print("Cheese:", ingredients["cheese"])
    print("Hot Sauce:", ingredients["hotSauce"])
