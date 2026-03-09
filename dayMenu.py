import inventory
import pricing
from recipes import recipe, changeRecipe
import customer_function
import minigame
#This is the day menu for TACO BEELL ON WHEEL
day = 1
price = 1 #starting price
evades = 0
def evade(type):
    global evades
    if type == 0:
        evades += 1
        return minigame.minigame()
    else:
        print("Hmm... but no one likes paying taxes! Will you pay yours?")
        evasion = input("Commit tax evasion? (y/n)")
        if evasion != "n":
            evasion = "y"
            evades += 1
            return minigame.minigame()
        else:
            print("What a good Samaritan you are!")
            return 3


def getDay():
    global day
    return day

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

tires = "n"
brakes = "n"
wedding = "n"
insur = "n"
def startDay(money, health):
    global tires
    global day
    global brakes
    global wedding
    global evades
    global insur
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
        else:
            print("The deal has been left in the dust")
    
    elif day == 2: #day 2 special thing
        print(f"When day {day} rolls around you know it's time to pay your taxes...")
        #tax things
        taxes = evade(1)
        if taxes == 3:
            print(f"-$2(Independant)")
            money -= 2
        else:
            health = taxes
        if health == 1:
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
                    print("You have a good heart... not what I would've done though")
            else:
                print("The chicken makes it to the other side...")
    
    
    elif day == 3: #day 3 special thing
        check = input("The day's begining greets you with an offer...")
        brakes = input("You can buy truck brakes for $25, do you?(y/n)\n")
        if not brakes == "n":
            brakes = "y"
            print("You purchased brakes... -$25")
            money -= 25
        else:
            print("The brakes are bought shortly after by someone else and you feel as though you didn't make the right decision")
    
    
    elif day == 4: #day 4 special thing
        print(f"When day {day} rolls around you know it's time to pay your taxes...")
        
        #tax things
        taxes = evade(1)
        if taxes == 3:
            print(f"-$2(Independant)")
            money -= 2
        else:
            health = taxes
        
        if health == 1:
            check = input("(click enter to continue)")
            if tires == "y":
                check = input("Your day starts off with an offer to cater a wedding for $50 (click enter to continue)")
                wedding = input("Do you accept the offer? (y/n)")
                if wedding != "n":
                    wedding = "y"
                #start
                if wedding == "y":
                    check = input("On your way over to the wedding rain starts to fall...")
                    check = input("Halfway to the celebration you approach a sketchy bridge...")
                    check = input("While driving over, the water on the road causes you to lose control of the wheel...")
                    if brakes == "y":
                        check = input("You use you truck's natural functions to regain contorl.")
                        check = input("After arriving to the wedding you learn that you must sell your tacos for free...")
                        check = input("Even so, you still made $50 for showing up. +$50")
                        money += 50
                    else:
                        check = input("with no way to slow down you fly through the guard rail.")
                        health = -1
                else:
                    print("I guess you don't like big parties...")

    
    
    elif day == 5: #day 5 special thing
        insur = input("You can purchase insurance for $25, do you?(y/n)\n")
        if insur != "n":
            insur = "y"
            print("You purchased insurance. -$25")
            money -= 25
        else:
            print("Maybe you prefer being cheap...")
    
    
    elif day == 6: #day 6 special thing
        print(f"When day {day} rolls around you know it's time to pay your taxes...")
        
        #tax things
        taxes = evade(1)
        if taxes == 3:
            print(f"-$2(Independant)")
            money -= 2
        else:
            health = taxes
        
        if health == 1:
            check = input("(click enter to continue)")
            if insur == "y":
                check = input("In the morning you drive to a new spot to get a different customer base.")
                check = input("On the way, a kid on a bike crashes into you, smashing one of your front headlights.")
                if insur == "y":
                    print("Thanks to the insurance you bought, you don't have to pay for the damages.")
                else:
                    print("Sadly, you must pay $35 to fix your headlight. -$35)")
                    money -= 35
    
    
    elif day == 7: #day 7 special thing
        if evades == 0:
            check = input("The cops are tired of waiting for you to evade your taxes.")
            check = input("They're right outside your truck, FLEE!")
            check = input("*Loading...")
        else:
            check = input("It's your last day and the police are suspicious of your business...")
            check = input("They're right outside your truck, RUN!")
            check = input("*Loading...")
        health = evade(0)
    else:
        if day % 2 == 0:
            print(f"When day {day} rolls around you know it's time to pay your taxes...")
            #tax things
            taxes = evade(1)
            if taxes == 3:
                print(f"-${round(day*(money/100),2)}(Dependant)")
                print(f"-$2(Independant)")
                money -= round(day*(money/100),2)+2
            else:
                health = taxes
            
            check = input("(click enter to continue)")
    
    #THE ACTUAL DAY
    day += 1
    if health > 0:
        data = [menu(money), health]
        return data
    else:
        data = [money, health]
        return data
    
