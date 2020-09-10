def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        print("Your Username or Password is wrong")
        return login()
def showMenu():
    print("------- ABC Shop ------")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()
def menuSelect():
    userSelected = int(input(">> "))
    if userSelected == 1:
        return vatCal(int(input("Put your price : ")))
    elif userSelected == 2:
        return priceCal()
def vatCal(price):
    vat = 7
    result = price + (price * vat / 100)
    print("Total price is",result,"THB")
def priceCal():
    price1 = int(input("First Product's Price : "))
    price2 = int(input("Second Product's Price : "))
    return vatCal(price1+price2)

login()