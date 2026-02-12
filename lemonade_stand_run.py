import inventory
import pricing
import recipes
money = 200 #starting money(temp)
price = 1
#folder- cd ./Lemonade_Stand
#inventory functions
    #Use money = buyIngre(money) to buy ingredients
    #Use showStat(money) to show inventory and money
#recipe
    #use recipe = changeRecipe(recipe)
#pricing
    #use price = changePrice(price)

price = pricing.changePrice(price)
recipe = recipes.changeRecipe(recipes.recipe)
money = inventory.buyIngre(money)
money = inventory.buyIngre(money)
money = inventory.buyIngre(money)
money = inventory.buyIngre(money)
inventory.showStat(money)
