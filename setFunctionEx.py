userInput = int(input("Enter a number of your favourite fruits : "))
myFruits = set()
while len(myFruits) < userInput :
    myFruits.add(input("Fruits : "))
