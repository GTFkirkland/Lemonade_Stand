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

check = input("Game - Do you understand that if I ask you a question and you don't answer (y/n), I will AUTOMATICALY input y?\n")
check = input("READ GAME BACKGROUND?\n")
if check == "no" or check == "No" or check == "n" or check == "N":
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    introStory.startGame(2)
else:
    introStory.startGame(1)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#GAME
print("Welcome to, TACO BEELL ON WHEEL™ 🌮🌮🌮")

while True:
    
    data = dayMenu.startDay(money, health)
    health = data[1]
    money = data[0]
    
    if money < 5 and (inventory["shells"] < 1 or inventory["meat"] < 1 or inventory["cheese"] < 1):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(" When the day ends you feel you don't have the funds to keep going...")
        print("                           GAME OVER")
        break
    elif health == 0:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(" You feel the handcuffs latching around you wrists and will soon know what a dirty prison cell smells like...")
        print("                                               GAME OVER")
    elif health == -1:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(" Your precious taco truck flies off the bridge and you know, that you'll go down in flames...")
        print("                                        GAME OVER")
    elif health == -999:
        print("Whatever win is")
    












