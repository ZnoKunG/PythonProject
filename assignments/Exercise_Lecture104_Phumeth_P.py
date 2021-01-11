class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added product to ",self.name,self.lastName,"'s cart")

customer1 = Customer()
customer1.name = "Kob"
customer1.lastName = "P"
customer2 = Customer()
customer2.name = "Aim"
customer2.lastName = "A"
customer3 = Customer()
customer3.name = "Phu"
customer3.lastName = "P"
customer4 = Customer()
customer4.name = "Win"
customer4.lastName = "W"
customer5 = Customer()
customer5.name = "Kai"
customer5.lastName = "K"

customer1.addCart()
customer2.addCart()
customer3.addCart()
customer4.addCart()
customer5.addCart()