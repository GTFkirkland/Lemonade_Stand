import inventory
import pricing
import recipes
import introStory
import customer_function
money = 200 #starting money(temp)
price = 1 #starting price
#folder- cd ./Lemonade_Stand
#inventory functions
    #Use money = buyIngre(money) to buy ingredients
    #Use showStat(money) to show inventory and money
#recipe
    #use recipe = changeRecipe(recipe)
#pricing
    #use price = changePrice(price)
#debugging:
# price = pricing.changePrice(price)
# recipe = recipes.changeRecipe(recipes.recipe)
# money = inventory.buyIngre(money)
# money = inventory.buyIngre(money)
# money = inventory.buyIngre(money)
# money = inventory.buyIngre(money)
# inventory.showStat(money)

introStory.startGame(1)
#GAME
print("Welcome to, TACO BEELL ON WHEEL")
print("This is NOT a trademark violation *tacobell please don't sue us*")

inventory.ingredients = {"shells": 20,
                "meat": 20,
                "cheese": 20,
                "hotSauce": 20}

recipe = recipes.changeRecipe(recipes.recipe)
price = pricing.changePrice(price)

inventory.showStat(money)

money += customer_function.runCustomers(recipe, price, inventory.ingredients)
print(f"Total money: ${money}")
inventory.showStat(money)





