"Ice cream shop cash register broke. This is a replacement calculator for the menue items"


cupSize = ""
addOnNum = 0
numToppings = 0

total = 0

#booleans
cup = True
addOn = False

while cup:
    cupSize = input("Small($3.99) or Large($4.99)?")
    if cupSize == "Large":
        cup =False
        cupSize = "large"
        total += 4.99
    elif cupSize == "Small":
        cup =False
        cupSize = "small"
        total += 3.99
    elif cupSize == "small":
        cup =False
        total += 3.99
    elif cupSize == "large":
        cup =False
        total += 4.99
print(total)        

addOn = True
while addOn:
    cupSize = input("0, 1, 2, 3 for add ons. \n 0. None \n 1. Dipped Sugar Cone($0.59) \n 2. Waffle Cone($0.99) \n 3. Chocolate Dipped Waffle Cone($1.49) \n")
    if addOnNum == "0":
        addOn =False
        total += 0
    elif cupSize == "1":
        addOn =False
        total += 0.59
    elif cupSize == "2":
        addOn =False
        total += 0.99
    elif cupSize == "3":
        addOn =False
        total += 1.49
print(total)        