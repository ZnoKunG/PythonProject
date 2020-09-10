def vatCal(totalPrice):
    result = totalPrice + (totalPrice*7/100)
    return result

TotalPrice = int(input("Put your price : "))
print("Your total price is",vatCal(TotalPrice))