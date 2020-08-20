NumInput = int(input("Put a number : "))
for i in range(NumInput):
    print((" "*(NumInput+1-i))+("*"*((2*i)-1)))