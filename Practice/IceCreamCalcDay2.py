"Take a list of an order and use a function to calucate price. Store name and price into list for records"


RecordCost = []


cup = True
addOn = False


def order(Name, cupSize, addOnNum, StandardTops, FancyTops, recordCost):
    total = 0
    if addOnNum == "0":
        total += 0
    elif cupSize == "1":
        total += 0.59
    elif cupSize == "2":
        total += 0.99
    elif cupSize == "3":
        total += 1.49
    else:
        print("incorrect number")
        

    if cupSize == "2":
        total += 4.99
    elif cupSize == "1":
        total += 3.99
    else:
        print("incorrect number")
        

    if StandardTops <9 and StandardTops >1:
        total += .29
    elif StandardTops == 0:
        total += 0
    else:
        print("incorrect number")
    
    if FancyTops <5 and FancyTops >1:
        total += .59
    elif StandardTops == 0:
        total += 0
    else:
        print("incorrect number")
        
    RecordCost.append(Name)
    RecordCost.append(total)

#Customers = int(input("How many customers: "))

while True:
    Name = input("Name:")
    cupSize = input("1. Small($3.99)\n2. Large($4.99)?\n")
            
    
    addOnNum = input("Add Ons.\n0. None\n1. Dipped Sugar Cone($0.59)\n2. Waffle Cone($0.99)\n3. Chocolate Dipped Waffle Cone($1.49)\n")
    
    StandardTops = int(input("Standard Toppings.\n0. None\n1. Rainbow Sprinkles($0.29)\n2. Chocolate Chips($0.29)\n3. Whipped Cream($0.29)\n4. Waffle Cone Pieces($0.29)\n5. Chocolate Syrup($0.29)\n6. Strawberry Sauce($0.29)\n7. Brownie Chunks($0.29)\n8. Cookie Chunks($0.29)"))
    FancyTops = int(input("Fancy Toppings.\n0. None\n1. Hot Fudge/Caramel($0.59)\n2. Nuts($0.59)\n3. Fruit($0.59)\n4. Candy($0.59)"))
    #Customers -= 1
    order(Name, cupSize, addOnNum, StandardTops, FancyTops, RecordCost)
    print(RecordCost)

