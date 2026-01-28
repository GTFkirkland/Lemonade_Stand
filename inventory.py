#to use the function: money = inventory(x,x,money)
money = 100
shells = 0
meat = 0
cheese = 0
hotSauce = 0

def buyIngre(money):
    item = input("What do you want to buy?(shells/meat/cheese/hot sauce)\n")
    amount = int(input("How many of this item?\n"))
    return inventory(item, amount, money)

def inventory(item, amount, money):
    global shells
    global meat
    global cheese
    global hotSauce
    if item == "shells":
        if money >= amount * .10:
            shells += amount
            money -= amount * .10
        else:
            print("You're too poor to afford this.")
    elif item == "meat":
        if money >= amount * .30:
            meat += amount
            money -= amount * .30
        else:
            print("You're to poor to afford this.")
    elif item == "cheese":
        if money >= amount * .20:
            cheese += amount
            money -= amount * .20
        else:
            print("You're to poor to afford this.")
    else:
        if money >= amount * .15:
            hotSauce += amount
            money -= amount * .15
        else:
            print("You're to poor to afford this.")
    return money

def showStat(money):
    global shells
    global meat
    global cheese
    global hotSauce
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    print("$$$:", money)
    print("Shells:", shells)
    print("Meat:", meat)
    print("Cheese:", cheese)
    print("Hot Sauce:", hotSauce)

money = buyIngre(money)
showStat(money)
