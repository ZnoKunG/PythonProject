totalPrice = float(input("Total price :"))
def vatCalculator(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result

print(vatCalculator(totalPrice))