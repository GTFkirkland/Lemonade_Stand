import inventory
import pricing
import recipes
import introStory
import customer_function
import dayMenu
money = 200 #starting money
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

money = dayMenu.startDay(money)
money = dayMenu.startDay(money)












