import inventory
import pricing
import recipes
import introStory
import customer_function
import dayMenu
money = 200 #starting money
health = 1 #yes, you can die now
#folder- cd ./Lemonade_Stand
#inventory functions
    #Use money = buyIngre(money, 1) to buy ingredients
    #Use showStat(money) to show inventory and money
#recipe
    #use recipe = changeRecipe(recipe)
#pricing
    #use price = changePrice(price)
#customer I think
    #money += customer_function.runCustomers(recipe, price, inventory.ingredients)
#debugging:
# price = pricing.changePrice(price)
# recipe = recipes.changeRecipe(recipes.recipe)
# money = inventory.buyIngre(money)
# money = inventory.buyIngre(money)
# money = inventory.buyIngre(money)
# money = inventory.buyIngre(money)
# inventory.showStat(money)
# inventory.ingredients = {"shells": 20,
#                 "meat": 20,
#                 "cheese": 20,
#                 "hotSauce": 20}

# recipe = recipes.changeRecipe(recipes.recipe)
# price = pricing.changePrice(price)

# inventory.showStat(money)

# money += customer_function.runCustomers(recipe, price, inventory.ingredients)
# print(f"Total money: ${money}")
# inventory.showStat(money)

check = input("Game - Do you understand that if I ask you a question and you don't answer (y/n)✅❌, I will AUTOMATICALY input y✅?\n")
check = input("READ GAME BACKGROUND?📙\n")
if check == "no" or check == "No" or check == "n" or check == "N":
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    introStory.startGame(2)
else:
    introStory.startGame(1)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#GAME
print("Welcome to, TACO BEELL ON WHEEL™ 🌮🔔🛞")

while health != -999:
    #day run
    data = dayMenu.startDay(money, health)
    health = data[1]
    money = data[0]
    #stuff
    if money < 5 and (inventory.ingredients["shells"] < 1 or inventory.ingredients["meat"] < 1 or inventory.ingredients["cheese"] < 1):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(" When the day ends you feel you don't have the funds to keep going...💀💰")
        print("                           GAME OVER")
        break
    elif health == 0:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(" You feel the handcuffs latching around you wrists and will soon know what a dirty prison cell smells like...💀👮")
        print("                                               GAME OVER")
        break
    elif health == -1:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(" In the air, above a seemingly endless void, you know that you'll go down in flames...💀🔥")
        print("                                      GAME OVER")
        break
    end = "n"
    if dayMenu.getDay() == 7:
        check = input("You have reached the end of your week of business🏢, remember! if you go bankrupt from now on you will STILL lose!❌")
        end = input("Do you wish to press on? (y/n)")
    elif dayMenu.getDay() > 7:
        check = input("Remember, if you go bankrupt you WILL lose.❌")
        end = input("Do you still wish to continue your campaign in the business world?🏢 (y/n)")
    
    if end != "n":
        end = "y"
    if end == "y":
        health = -999
    else:
        continue

    
else:
    if (money-200) < 1000:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f" You pack up your things and exit the truck feeling proud that you lasted {dayMenu.getDay()} days long!🕛")
    elif (money-200) < 3500:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f" You leave your truck knowing how much of a successful business person you are! You lasted {dayMenu.getDay()} days long!🕛")
    elif (money-200) >= 3500:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f" You leave your business in the dust after making all of your money back and then some! You lasted {dayMenu.getDay()} days long!🕛")
    print(f"You sold {customer_function.gethsTacos()} tacos!🌮")
    print(f"You made ${money-200} profit after starting your business!💵")
    












