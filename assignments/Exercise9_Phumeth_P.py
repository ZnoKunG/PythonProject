usernameInput = input("Username : ")
passwordInput = input("Password : ")
while usernameInput != "admin" or passwordInput != "1234":
    print("Incorrect username or password")
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
print("Done")