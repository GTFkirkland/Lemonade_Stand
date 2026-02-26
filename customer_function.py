from customer_class import Customer
import inventory
import random
from customer_names import He_names, She_names
from time import sleep
def runCustomers(recipe, price, ingredients):
    global He_names
    global She_names
    customers = []
    numberOfcustomers = inventory.maxTacos(ingredients)
    for i in range(numberOfcustomers):
        customers.append(Customer())

    tacosSold = 0
    money = 0
    gender = ["He", "She"]
    sadCounter = {"too little cheese": 0,
                  "too much cheese": 0,
                  "too little sauce": 0,
                  "too much sauce": 0,
                  "too high price": 0}
    for i in range(len(customers)):
        attributes = customers[i].get_customer_attributes()
        cheesy_pref = attributes["cheesy"]
        spice_pref = attributes["spice"]
        price_limit = attributes["price"]
        chosenGender = random.choice(gender)
        if chosenGender == "He":
            name = random.choice(He_names)
        else:
            name = random.choice(She_names)
        print(f"Customer {i + 1}-{name} walks up to the truck...")

        #original code if you don't like the changes:
        #elif abs(recipe["hotSauce"] - spice_pref) >= 1:
            #print(f"Customer {i + 1} didn't like the spice level. Your customer said they didn't want to be a fire breathing dragon")
        
        if price > price_limit+((recipe["meat"]*1.5)-0.5): #added some cusion to make it more plausable (see bottom for math details)
            print(f"{name} looked at the price and walked away. you can't monopolize your customers❌")
            sadCounter["too high price"] += 1
        elif recipe["cheese"] - cheesy_pref >1: #too much cheese(you can go 1 over for realism and 1 under)
            print(f"{name} didn't like the cheese amount. {name} said {chosenGender.lower()} couldn't even see the shell❌")
            sadCounter["too much cheese"] += 1
        elif recipe["cheese"] - cheesy_pref <-1: #too little cheese
            print(f"{name} didn't like the cheese amount. {name} didn't say {chosenGender.lower()} was lactose intolerant❌")
            sadCounter["too little cheese"] += 1
        elif recipe["hotSauce"] - spice_pref >1: #too much hotsauce
            print(f"{name} didn't like the spice level. {name} said {chosenGender.lower()} didn't want to be a fire breathing dragon❌")
            sadCounter["too much sauce"] += 1
        elif recipe["hotSauce"] - spice_pref <-1: #too little hot sauce(you can go 1 under for realism)
            print(f"{name} didn't like the spice level. {name} didn't say {chosenGender.lower()} wanted a dry, bland taco❌")
            sadCounter["too little sauce"] += 1
        else:
            if ingredients["shells"] >= 1 and ingredients["meat"] >= recipe["meat"] and ingredients["cheese"] >= recipe["cheese"] and ingredients["hotSauce"] >= recipe["hotSauce"]:
                print(f"{name} bought a taco! +${price}✅")
                tacosSold += 1
                money += price
                ingredients["shells"] -= 1
                ingredients["meat"] -= recipe["meat"]
                ingredients["cheese"] -= recipe["cheese"]
                ingredients["hotSauce"] -= recipe["hotSauce"]
            else:
                print(f"Customer {i + 1} wanted to buy but you ran out of ingredients!!")
        sleep(random.random()*0.3)

    print("~~~~~~~~~~END OF DAY~~~~~~~~~~")
    print(f"Tacos sold: {tacosSold}")
    print(f"Money earned today: ${money}")
    print(f"""{sadCounter['too high price']} customers thought the price was too high
{sadCounter['too little cheese']} customers thought there wasn't enough cheese
{sadCounter['too much cheese']} customers thought there was too much cheese
{sadCounter['too little sauce']} customers thought the taco looked too mild
{sadCounter['too much sauce']} customers thought the taco looked too spicy""")
    #some ingredients spoil
    ingredients["shells"] = round(ingredients["shells"]/1.5)
    ingredients["meat"] = round(ingredients["meat"]/4)
    ingredients["cheese"] = round(ingredients["cheese"]/2)
    #hotsauce doesn't spoil
    if ingredients["shells"] + ingredients["meat"] + ingredients["cheese"] == 0:
        print("You successfuly sold all of your tacos!✅")
    else:
        print("Some of your ingredients spoiled...❌")
    return money




#basicaly, for the price I decided that each meat you put in, the more lenient the customers would be about the "too high of a price"- making more than one meat do something
#1meat = 1.0 cusion(price can go 1 over price preference), 2meat = 2.5 cusion(price can go 2.5 over price preference), 3meat = 4.0 cusion(price can go 4.0 over price preference)