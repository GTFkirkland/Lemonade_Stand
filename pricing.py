#This is how the player will set pricing for their game.
def pricingInternal(price):
    print(f"Current price per taco is ${price}")
    copyPrice = 0
    while copyPrice <= 0 or copyPrice > 15:
        try:
            copyPrice = float(input("What do you want to set your new price as? \n"))
            if copyPrice <= 0 or copyPrice > 15:
                print("This is an INVALID price, please try again")
        except:
            print("This is an INVALID price, please try again")
            continue
    print(f"Your price is ${copyPrice}")
    check = input("Do you like these changes?(y/n)\n")
    if check == "no" or check == "No" or check == "n" or check == "N":
        print("Reverting changes... RELOADING")
        return pricingInternal(price)
    else:
        print("Changes successfuly made...")
        print("~~~~~~~~~~MENU~~~~~~~~~~")
        return copyPrice
    

def changePrice(price):
    print("~~~~~~~~~~~PRICE~~~~~~~~~~~~")
    price = pricingInternal(price)
    return price



   
