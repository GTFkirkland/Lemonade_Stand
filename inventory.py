#to use the function: money = inventory(x,x,money)
from recipes import recipe
ingredients = {"shells": 0,
                "meat": 0,
                "cheese": 0,
                "hotSauce": 0}
def buyIngre(money,type):
    if type == 1:
        print("~~~~~~~~~SHOP~~~~~~~~~~~")
    else:
        None
    item = input("What do you want to buy?(shells(1)/meat(2)/cheese(3)/hotSauce(4))\n")
    if item == "shells" or item == "meat" or item == "cheese" or item == "hotSauce" or item == "1" or item == "2" or item == "3" or item == "4":
        amount=10000000000000000000000
        while not amount >= 0 and not amount <= 1000000:
            try:
                amount = int(input("How many of this item?\n"))
            except:
                print("Add a realistic integer number") 
        money = inventory(item, amount, money)
        check = input("Purchase more ingredients?\n")
        if check == "no" or check == "No" or check == "n" or check == "N":
            print("~~~~~~~~~~MENU~~~~~~~~~~")
            return money
        else:
            return buyIngre(money, 2)
    else:
        print("I don't think people want to eat that in their tacos...")
        return buyIngre(money, 2)

def inventory(item, amount, money):
    global ingredients
    if item == "shells" or item == "1":
        if money >= round(amount * .40,2):
            check = input(f"This will cost ${round(amount * .40,2)}, continue?\n")
            if check == "yes" or check == "Yes" or check == "y" or check == "Y":
                ingredients["shells"] += amount
                money -= round(amount * .40,2)
                print(f"-${round(amount * .40,2)}")
            else:
                None
        else:
            print("You're too poor to afford this.")
            check = input("Go into debt?")
            if check == "no" or check == "No" or check == "n" or check == "N":
                None
            else:
                print("CHEATER!!!")
                print("-$1")
                money -= 1
    elif item == "meat" or item == "2":
        if money >= round(amount * .70,2):
            check = input(f"This will cost ${round(amount * .70,2)}, continue?\n")
            if check == "yes" or check == "Yes" or check == "y" or check == "Y":
                ingredients["meat"] += amount
                money -= round(amount * .70,2)
                print(f"-${round(amount * .70,2)}")
            else:
                None
        else:
            print("You're too poor to afford this.")
            check = input("Go into debt?")
            if check == "no" or check == "No" or check == "n" or check == "N":
                None
            else:
                print("CHEATER!!!")
                print("-$1")
                money -= 1
    elif item == "cheese" or item == "3":
        if money >= round(amount * .55,2):
            check = input(f"This will cost ${round(amount * .55,2)}, continue?\n")
            if check == "yes" or check == "Yes" or check == "y" or check == "Y":
                ingredients["cheese"] += amount
                money -= round(amount * .55,2)
                print(f"-${round(amount * .55,2)}")
            else:
                None
        else:
            print("You're too poor to afford this.")
            check = input("Go into debt?")
            if check == "no" or check == "No" or check == "n" or check == "N":
                None
            else:
                print("CHEATER!!!")
                print("-$1")
                money -= 1
    else:
        if money >= round(amount * .35,2):
            check = input(f"This will cost ${round(amount * .35,2)}, continue?\n")
            if check == "yes" or check == "Yes" or check == "y" or check == "Y":
                ingredients["hotSauce"] += amount
                money -= round(amount * .35,2)
                print(f"-${round(amount * .35,2)}")
            else:
                None
        else:
            print("You're too poor to afford this.")
            check = input("Go into debt?")
            if check == "no" or check == "No" or check == "n" or check == "N":
                None
            else:
                print("CHEATER!!!")
                print("-$1")
                money -= 1
    return money

def maxTacos(list):
    copyList = {"shells": list["shells"], "meat": list["meat"], "cheese": list["cheese"], "hotSauce": list["hotSauce"]}
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
    print("~~~~~~~~~~~INVENTORY~~~~~~~~~~~~")
    print("$$$:", money)
    print("Shells:", ingredients["shells"])
    print("Meat:", ingredients["meat"])
    print("Cheese:", ingredients["cheese"])
    print("Hot Sauce:", ingredients["hotSauce"])
    check = input(f"Total tacos: {maxTacos(ingredients)} (press enter to continue)")
    print("~~~~~~~~~~MENU~~~~~~~~~~")