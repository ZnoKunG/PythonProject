def showBill():
    print('--------My Food--------')
    TotalPrice = 0
    for number in range(len(menuList)):
        print(menuList[number],priceList[number],'THB')
        TotalPrice += int(priceList[number])
    print("Total Price :",TotalPrice,"THB")


menuList = []
priceList = []
while True:
    menuName = input("Please enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()


