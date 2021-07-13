"Take a list of an order and use a function to calucate price. Store name and price into list for records"


cupSize = ""
addOnNum = 0
RecordCost = []


cup = True
addOn = False


def order(Name, cupSize, addOnNum, recordCost):
    total = 0
    if addOnNum == "0":
        total += 0
    elif cupSize == "1":
        total += 0.59
    elif cupSize == "2":
        total += 0.99
    elif cupSize == "3":
        total += 1.49

    if cupSize == "2":
        total += 4.99
    elif cupSize == "1":
        total += 3.99
    
    RecordCost.append(Name)
    RecordCost.append(total)

#Customers = int(input("How many customers: "))

while True:
    Name = input("Name:")
    cupSize = input("1. Small($3.99)\n2. Large($4.99)?\n")
            
    
    addOnNum = input("Add Ons.\n0. None\n1. Dipped Sugar Cone($0.59)\n2. Waffle Cone($0.99)\n3. Chocolate Dipped Waffle Cone($1.49)\n")
        
    #Customers -= 1
    order(Name, cupSize, addOnNum, RecordCost)
    print(RecordCost)

