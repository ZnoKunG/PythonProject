username = input("Username : ")
password = input("Password : ")
Banana = 10
Apple = 12
Toothbrush = 30
Water = 10
Coffee = 15
Snacks = 20
TotalPrice = 0
if username == "customer" and password == "abc":
    print("Good Morning",username)
    print("Choose your products :\n"
          "1.Banana (10 THB)\n"
          "2.Apple (12 THB)\n"
          "3.Toothbrush (50 THB)\n"
          "4.Water (10 THB)\n"
          "5.Coffee (15 THB)\n"
          "6.Snacks (20 THB)")
    product1 = input("Product : ")
    if product1 == "Banana":
        num1 = int(input("How many ? : "))
        TotalPrice += Banana*num1
    elif product1 == "Apple":
        num1 = int(input("How many ? : "))
        TotalPrice += Apple*num1
    elif product1 == "Toothbrush":
        num1 = int(input("How many ? : "))
        TotalPrice += Toothbrush * num1
    elif product1 == "Water":
        num1 = int(input("How many ? : "))
        TotalPrice += Water * num1
    elif product1 == "Coffee":
        num1 = int(input("How many ? : "))
        TotalPrice += Coffee * num1
    elif product1 == "Snacks":
        num1 = int(input("How many ? : "))
        TotalPrice += Snacks * num1
    shoppingChoice1 = input("Anything else ? (Yes/No) : ")
    if shoppingChoice1 == "Yes":
        product2 = input("Product : ")
        if product2 == "Banana":
            num1 = int(input("How many ? : "))
            TotalPrice += Banana*num1
        elif product2 == "Apple":
            num1 = int(input("How many ? : "))
            TotalPrice += Apple*num1
        elif product2 == "Toothbrush":
            num1 = int(input("How many ? : "))
            TotalPrice += Toothbrush * num1
        elif product2 == "Water":
            num1 = int(input("How many ? : "))
            TotalPrice += Water * num1
        elif product2 == "Coffee":
            num1 = int(input("How many ? : "))
            TotalPrice += Coffee * num1
        elif product2 == "Snacks":
            num1 = int(input("How many ? : "))
            TotalPrice += Snacks * num1
    elif shoppingChoice1 == "No":
        print("Total price : ",TotalPrice)
    shoppingChoice2 = input("Anything else ? (Yes/No) : ")
    if shoppingChoice2 == "Yes":
        product3 = input("Product : ")
        if product3 == "Banana":
            num1 = int(input("How many ? : "))
            TotalPrice += Banana * num1
        elif product3 == "Apple":
            num1 = int(input("How many ? : "))
            TotalPrice += Apple * num1
        elif product3 == "Toothbrush":
            num1 = int(input("How many ? : "))
            TotalPrice += Toothbrush * num1
        elif product3 == "Water":
            num1 = int(input("How many ? : "))
            TotalPrice += Water * num1
        elif product3 == "Coffee":
            num1 = int(input("How many ? : "))
            TotalPrice += Coffee * num1
        elif product3 == "Snacks":
            num1 = int(input("How many ? : "))
            TotalPrice += Snacks * num1
    elif shoppingChoice2 == "No":
        print("Total price : ", TotalPrice)
    shoppingChoice3 = input("Anything else ? (Yes/No) : ")
    if shoppingChoice3 == "Yes":
        product4 = input("Product : ")
        if product4 == "Banana":
            num1 = int(input("How many ? : "))
            TotalPrice += Banana * num1
        elif product4 == "Apple":
            num1 = int(input("How many ? : "))
            TotalPrice += Apple * num1
        elif product4 == "Toothbrush":
            num1 = int(input("How many ? : "))
            TotalPrice += Toothbrush * num1
        elif product4 == "Water":
            num1 = int(input("How many ? : "))
            TotalPrice += Water * num1
        elif product4 == "Coffee":
            num1 = int(input("How many ? : "))
            TotalPrice += Coffee * num1
        elif product4 == "Snacks":
            num1 = int(input("How many ? : "))
            TotalPrice += Snacks * num1
    elif shoppingChoice3 == "No":
        print("Total price : ", TotalPrice)
    shoppingChoice4 = input("Anything else ? (Yes/No) : ")
    if shoppingChoice4 == "Yes":
        product5 = input("Product : ")
        if product5 == "Banana":
            num1 = int(input("How many ? : "))
            TotalPrice += Banana * num1
        elif product5 == "Apple":
            num1 = int(input("How many ? : "))
            TotalPrice += Apple * num1
        elif product5 == "Toothbrush":
            num1 = int(input("How many ? : "))
            TotalPrice += Toothbrush * num1
        elif product5 == "Water":
            num1 = int(input("How many ? : "))
            TotalPrice += Water * num1
        elif product5 == "Coffee":
            num1 = int(input("How many ? : "))
            TotalPrice += Coffee * num1
        elif product5 == "Snacks":
            num1 = int(input("How many ? : "))
            TotalPrice += Snacks * num1
    elif shoppingChoice4 == "No":
        print("Total price : ", TotalPrice)
    shoppingChoice5 = input("Anything else ? (Yes/No) : ")
    if shoppingChoice5 == "Yes":
        product6 = input("Product : ")
        if product6 == "Banana":
            num1 = int(input("How many ? : "))
            TotalPrice += Banana * num1
        elif product6 == "Apple":
            num1 = int(input("How many ? : "))
            TotalPrice += Apple * num1
        elif product6 == "Toothbrush":
            num1 = int(input("How many ? : "))
            TotalPrice += Toothbrush * num1
        elif product6 == "Water":
            num1 = int(input("How many ? : "))
            TotalPrice += Water * num1
        elif product6 == "Coffee":
            num1 = int(input("How many ? : "))
            TotalPrice += Coffee * num1
        elif product6 == "Snacks":
            num1 = int(input("How many ? : "))
            TotalPrice += Snacks * num1
    print("Total Price : ",TotalPrice)







