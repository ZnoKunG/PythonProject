userName = input("Username :")
passWord = input("Password :")
if userName == "Gundam" and passWord == "destiny":
    print("Welcome to iModelShop")
    print("________iModelShop________")
    print("1. MG Barbatos       1620 THB")
    print("2. RG Astray RED      900 THB")
    print("3. SD Cross           500 THB")
    print("4. HD RX-78           780 THB")
    print("5. RG Wing Zero      1060 THB")
    userSelected = int(input("Which model do you want? (1-5) : "))
    number = int(input("Number : "))
    price1 = 1620
    price2 = 900
    price3 = 500
    price4 = 780
    price5 = 1060
    if userSelected == 1:
        result = price1 * number
        print("Price =", result, "THB")
    elif userSelected == 2:
        result = price2 * number
        print("Price =", result, "THB")
    elif userSelected == 3:
        result = price3 * number
        print("Price =", result, "THB")
    elif userSelected == 4:
        result = price4 * number
        print("Price =", result, "THB")
    elif userSelected == 5:
        result = price5 * number
        print("Print =", result, "THB")
    else:
        print("Wrong number")
else:
    print("Username or password incorrect")