def start():
    print "You have nothing to eat. The fridge is empty."
    print "Choose random number from 1 to 5."

    choice = raw_input("> ")

    if choice == "1" or choice == "4":
        #print "fridge"
        fridge()
    elif choice == "2" or choice == "3":
        store()
        #print "store"
    else:
        cafe()
        #print "cafe"

def fridge():
    print "There are some veggies in your fridge."
    print "Open the fridge. Take potato, chicken, carrot, onion and some spicies and cook CHICKEN or SOUP."

def store():
    print "We have no veggies and meat."
    print "First of all, go to the nearest grociery store and buy Pasta, Meat and some Veggies."

def cafe():
    print "Oppsy! Nothing in the fridge and no energy to cook."
    print "Let's eat somewhere or order something. Choose 1-3."

    cafe = raw_input("> ")

    if cafe == "1":
        print "Go to eat to Koreana"
    elif cafe == "2":
        print "Order some pizza"
    else:
        print "It's time to eat SUSI!!!"

start()
