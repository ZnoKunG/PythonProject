#first method
NumInput = int(input("Put a number : "))
for i in range(NumInput):
    print("*"*(i+1))

#second method
for x in range(NumInput):
    text = ""
    for y in range(x+1):
        text += "*"
    print(text)