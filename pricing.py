#This is how the player will set pricing for their game.

price = 0 

def pricing():
    global price
    price=int(input("What would you like to set your price as:"))
    while price < 0:
        print("This is an invalid price please try again...")  
pricing()
   
