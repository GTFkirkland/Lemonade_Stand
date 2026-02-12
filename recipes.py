recipe = {"meat": 1,
          "cheese": 1,
          "hotSauce": 0}

def changeRecipe(recipe):
    print("~~~~~~~~~~~RECIPE~~~~~~~~~~~")
    #meat
    recipe["meat"] = int(input("How much meat do you want in your tacos? (1-3)\n"))
    while not recipe["meat"] > 0 or not recipe["meat"] <= 3:
        try:
            recipe["meat"] = int(input("How much meat do you want in your tacos? (1-3)\n"))
        except:
            print("INVALID NUMBER")
    #cheese
    recipe["cheese"] = int(input("How much cheese do you want in your tacos? (1-4)\n"))
    while not recipe["cheese"] > 0 or not recipe["cheese"] <= 4:
        try:
            recipe["cheese"] = int(input("How much cheese do you want in your tacos? (1-4)\n"))
        except:
            print("INVALID NUMBER")
    #Hot Sauce
    recipe["hotSauce"] = int(input("How much Hot Sauce do you want in your tacos? (0-3)\n"))
    while not recipe["hotSauce"] > 0 or not recipe["hotSauce"] <= 3:
        try:
            recipe["hotSauce"] = int(input("How much Hot Sauce do you want in your tacos? (0-3)\n"))
        except:
            print("INVALID NUMBER")
    print("~~~~~~~~~~~~~~~~~~~~")
    print("Recipe: Meat:", recipe["meat"], "/ Cheese:", recipe["cheese"], "/ Hot Sauce:", recipe["hotSauce"])
    check = input("Do you like these changes?(y/n)\n")
    if check == "no" or check == "No" or check == "n" or check == "N":
        print("Reverting changes... RELOADING")
        changeRecipe(recipe)
    else:
        print("Changes successfuly made...")
        return recipe