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
    while menuChoice != "5":
        print("""What would you like to select?
~Purchase ingredients~ 1
~Change taco price~ 2
~Change taco recipe~ 3
~Display inventory and money~ 4""")
        menuChoice = input("~Start day~ 5\n")
        if menuChoice == "1":
            money = inventory.buyIngre(money, 1)
        elif menuChoice == "2":
            price = pricing.changePrice(price)
        elif menuChoice == "3":
            recipe = changeRecipe(recipe)
        elif menuChoice == "5":
            money += customer_function.runCustomers(recipe, price, inventory.ingredients)
        elif menuChoice == "4":
            inventory.showStat(money)
        else:
            print("That is NOT an option, try again...")
    return money

def startDay(money):
    global tires
    global day
    print(f"~~~~~~~~~~~~~~~~~~~~~~~DAY {day}~~~~~~~~~~~~~~~~~~~~~~~~")
    # inventory.ingredients = {"shells": 50, #STARTING INVENTORY FOR TESTING
    #             "meat": 50,
    #             "cheese": 50,
    #             "hotSauce": 50}
    #special things
    if day == 1: #day 1 special thing
        print("While looking online you find an amazing deal, and have to make a choice...")
        tires = input("Do you repair the 3 missing tires on the taco truck for $50?(y/n)\n")
        if not tires == "n":
            tires = "y"
            print("You repaired the tires on the truck... -$50")
            money -= 50
    if day == 2: #day 2 special thing
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
    if day == None: #more special things later, idk
        None
    
    #THE ACTUAL DAY
    day += 1
    return menu(money)
    
