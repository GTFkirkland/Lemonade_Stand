import inventory
import pricing
from recipes import recipe, changeRecipe
import customer_function
from gameRun import health
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
1) Purchase Ingredients
2) Change taco price
3) Change taco recipe
4) Display inventory and money""")
        menuChoice = input("5) Start day\n")
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
    global health
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
    elif day == 2: #day 2 special thing
        print(f"When day {day} rolls around you know it's time to pay your taxes...")
        print(f"-$5(Independant)")
        check = input("(click enter to continue)")
        check = input("When you wake up you spot a chicken crossing the road...")
        if tires == "y":
            chicken = input("RuN iT oVeR?(y/n)")
            if chicken != "n":
                chicken = "y"
                for i in range(5):
                    check = input("...")
                check = input("While viewing the chicken's final moments you spot something green in its mouth.")
                check = input('Inside you find a $25 bill and think, "How did that get there?" +$25')
                money += 25
        else:
            print("The chicken makes it to the other side...")
    elif day == 3: #day 3 special thing
        check = input("The day's begining greets you with an offer...")
        brakes = input("You can buy truck brakes for $25, do you?(y/n)\n")
        if not brakes == "n":
            brakes = "y"
            print("You purchased brakes... -$25")
            money -= 25
    elif day == 4: #day 4 special thing
        print(f"When day {day} rolls around you know it's time to pay your taxes...")
        print(f"-$5(Independant)")
        check = input("(click enter to continue)")
        if tires == "y":
            print("You have recieved an offer to cater a wedding.(click enter to continue)")
            print("While driving there you cross a bridge and hear a weird creek.")
            if brakes == "y":
                print("You made it out alive. (+$50)")
            else:
                health = -1
    elif day == 5: #day 5 special thing
        insur = input("You can purchase insurance for $45, do you?(y/n)\n")
        if not insur == "n":
            insur = "y"
            print("You purchased insurance")
            money -= 45
    elif day == 6: #day 6 special thing
        print(f"When day {day} rolls around you know it's time to pay your taxes...")
        print(f"-$5(Independant)")
        check = input("(click enter to continue)")
        if insur == "y":
            print("While driving to get more groceries you spot a car driving right at you.")
            print("...")
            print("...")
            print("...")
            print("...")
            if insur == "y":
                print("You made it out alive and insurance is going to pay for the damage.")
            else:
                print("You must pay for the damges. (-$30)")
                health -= 1
                money -= 30
    elif day == 7: #day 7 special thing
        None
    else:
        if day % 2 == 0:
            print(f"When day {day} rolls around you know it's time to pay your taxes...")
            print(f"-${round(day*(money/100),2)}(Dependant)")
            print(f"-$5(Independant)")
            check = input("(click enter to continue)")
            money -= round(day*(money/100),2)
    
    #THE ACTUAL DAY
    day += 1
    if health > 0:
        return menu(money)
    else:
        return money
    
