#This is how the player will set pricing for their game.
def pricingInternal(price):
    print(f"Current price per taco is ${price}")
    price = 0
    while price <= 0 or price > 5:
        try:
            price = float(input("What do you want to set your new price as? \n"))
            if price <= 0 or price > 5:
                print("This is an INVALID price, please try again")
        except:
            print("This is an INVALID price, please try again")
            continue
    print(f"Your price is ${price}")
    check = input("Do you like these changes?(y/n)\n")
    if check == "no" or check == "No" or check == "n" or check == "N":
        print("Reverting changes... RELOADING")
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
        pricingInternal(price)
    elif check != "y" or check != "Y" or check != "yes" or check != "Yes" or check != "no" or check != "No" or check != "n" or check != "N":
        print("This is not an option")
    else:
        print("Changes successfuly made...")
        return price

def changePrice(price):
    print("~~~~~~~~~~~PRICE~~~~~~~~~~~~")
    pricingInternal(price)



   
