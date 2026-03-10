#recipes
recipe = {"meat": 1,
          "cheese": 1,
          "hotSauce": 0}

def changeRecipe(recipe):
    cheat = 0
    print("~~~~~~~~~~~RECIPE~~~~~~~~~~~")
    while True:
        copyRec = recipe.copy()
        #meat
        print("Current recipe: Meat:", recipe["meat"], "/ Cheese:", recipe["cheese"], "/ Hot Sauce:", recipe["hotSauce"])
        try:
            recipe["meat"] = int(input("How much meat do you want in your tacos? (1-3)\n"))
        except:
            print("No changes...")
        while recipe["meat"] != 1 and recipe["meat"] != 2 and recipe["meat"] != 3:
            print("INVALID NUMBER")
            try:
                recipe["meat"] = int(input("How much meat do you want in your tacos? (1-3)\n"))
            except:
                print("No changes...")
        #cheese
        try:
            recipe["cheese"] = int(input("How much cheese do you want in your tacos? (1-4)\n"))
        except:
            print("No changes...")
        while recipe["cheese"] != 1 and recipe["cheese"] != 2 and recipe["cheese"] != 3 and recipe["cheese"] != 4:
            print("INVALID NUMBER")
            try:
                recipe["cheese"] = int(input("How much cheese do you want in your tacos? (1-4)\n"))
            except:
                print("No changes...")
        #Hot Sauce
        try:
            recipe["hotSauce"] = int(input("How much Hot Sauce do you want in your tacos? (0-3)\n"))
        except:
            print("No changes...")
        while recipe["hotSauce"] != 1 and recipe["hotSauce"] != 2 and recipe["hotSauce"] != 3 and recipe["hotSauce"] != 0:
            print("INVALID NUMBER")
            try:
                recipe["hotSauce"] = int(input("How much Hot Sauce do you want in your tacos? (0-3)\n"))
            except:
                print("No changes...")
        print("~~~~~~~~~~~~~~~~~~~~")
        print("Recipe: Meat:", recipe["meat"], "/ Cheese:", recipe["cheese"], "/ Hot Sauce:", recipe["hotSauce"])
        check = input("Do you like these changes?(y/n)\n")
        if check == "no" or check == "No" or check == "n" or check == "N":
            print("Reverting changes... RELOADING")
            recipe = copyRec
            cheat += 1
            continue
        else:
            print("Changes successfuly made...")
            print("~~~~~~~~~~MENU~~~~~~~~~~")
            return recipe
    