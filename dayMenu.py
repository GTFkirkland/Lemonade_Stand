import inventory
import pricing
from recipes import recipe, changeRecipe
import customer_function
#This is the day menu for TACO BEELL ON WHEEL
day = 1
price = 1 #starting price
def menu(money):
    global price
    global recipe
    print("~~~~~~~~~~MENU~~~~~~~~~~")
    menuChoice = ""
    while menuChoice != "4":
        print("""What would you like to select?
~Purchase ingrediants~1
~Change taco price~2
~Change taco recipe~3""")
        menuChoice = input("~Start day~4\n")
        if menuChoice == "1":
            inventory.buyIngre(money, 1)
        elif menuChoice == "2":
            price = pricing.changePrice(price)
        elif menuChoice == "3":
            recipe = changeRecipe(recipe)
        elif menuChoice == "4":
            money += customer_function.runCustomers(recipe, price, inventory.ingredients)
        else:
            print("That is NOT an option, try again...")

def startDay(money):
    global day
    print(f"~~~~~~~~~~~~~~~~~~~~~~~DAY {day}~~~~~~~~~~~~~~~~~~~~~~~~")
    #special things
    #day 1 special thiong
    if day == 1:
        tires = input("Do you repair the 3 missing tires on the taco truck for $50?(y/n)")
        if tires != "n":
            tires = "y"
            print("You repaired the tires on the truck... -$50")
            money -= 50
    #day 2 special thiong
    elif day == 2:
        check = input("When you wake up you spot a chicken crossing the road...")
        if tires == "y":
            chicken = input("RuN iT oVeR?(y/n)")
            if chicken != "n":
                chicken = "y"
                for i in range(5):
                    check = input("...")
                check = input("You... you just killed the chicken")
                check = input("HOW COULD YOU!? +$25")
                money += 25
        else:
            print("The chicken makes it to the other side...")
    #more special thiongs later, idk
    elif day == None:
        None
    
    #THE ACTUAL DAY
    menu(money)
    day+=1
    
