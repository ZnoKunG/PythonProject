usernameInput = input("Username : ")
passwordInput = input("Password : ")
while usernameInput != "admin" or passwordInput != "1234":
    print("!!Incorrect Username/Password!!")
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
print("Done !")