usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "admin" and passwordInput == "1234":
    print("Done !")
    print("------- ABC Shop ------")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    userSelected = int(input(">>"))
    if userSelected == 1:
        price = int(input("Price (THB) : "))
        vat = 7
        result = price + (price * vat / 100)
        print(result)
    elif userSelected == 2:
        price1 = int(input("First Product's Price : "))
        price2 = int(input("Second Product's Price : "))
        print("Total price : ",price1 + price2)