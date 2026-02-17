from customer_class import Customer

def runCustomers(recipe, price, ingredients):
    customers = []
    for i in range(10):
        customers.append(Customer())

    tacosSold = 0
    money = 0

    for i in range(len(customers)):
        attributes = customers[i].get_customer_attributes()
        cheesy_pref = attributes["cheesy"]
        spice_pref = attributes["spice"]
        price_limit = attributes["price"]

        print(f"Customer {i + 1} walks up to the truck...")

        if price > price_limit:
            print(f"Customer {i + 1} looked at the price and walked away. you can't monopolize your customers")
        elif abs(recipe["cheese"] - cheesy_pref) > 1:
            print(f"Customer {i + 1} didnt like the cheese amount. They said they couldn't even see the shell")
        elif abs(recipe["hotSauce"] - spice_pref) > 1:
            print(f"Customer {i + 1} didnt like the spice level. Your customer said they didn't want to be a fire breathing dragon")
        else:
            if ingredients["shells"] >= 1 and ingredients["meat"] >= recipe["meat"] and ingredients["cheese"] >= recipe["cheese"] and ingredients["hotSauce"] >= recipe["hotSauce"]:
                print(f"Customer {i + 1} bought a taco! +${price}")
                tacosSold += 1
                money += price
                ingredients["shells"] -= 1
                ingredients["meat"] -= recipe["meat"]
                ingredients["cheese"] -= recipe["cheese"]
                ingredients["hotSauce"] -= recipe["hotSauce"]
            else:
                print(f"Customer {i + 1} wanted to buy but you ran out of ingredients!!")

    print("~~~~~~~~~~END OF DAY~~~~~~~~~~")
    print(f"Tacos sold: {tacosSold}")
    print(f"Money earned today: ${money}")
    return money
