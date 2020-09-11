systemMenu = {'Soup':30,'Fried Rice':55,'Bread':20,'Coffee':35}
def showBill():
    print('--------My Food--------')
    TotalPrice = 0
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1],'THB')
        TotalPrice += int(menuList[number][1])
    print('Total Price :',TotalPrice,'THB')


menuList = []
while True:
    menuName = input("Please enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])
print(menuList)
showBill()
