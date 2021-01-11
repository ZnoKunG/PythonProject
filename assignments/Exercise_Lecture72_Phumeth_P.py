menuList = []

def showBill():
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number])

while True:
  menuName = input("Plese Enter Menu :")
  if(menuName.lower() == "exit"):
    break
  else:
      menuPrice = input("Price :")
      menuList.append([menuName,menuPrice])
showBill()
totalPrice = 0
for number in range(len(menuList)):
    totalPrice += int(menuList[number][1])
print("Totalprice :", totalPrice)