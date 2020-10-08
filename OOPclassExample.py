class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to",self.name,self.lastName,"'s cart")

customer1 = Customer()
customer1.name = "Zno"
customer1.lastName = "s"
customer1.addCart()

customer2 = Customer()
customer2.name = "Able"
customer2.lastName = "s"
customer2.addCart()

customer3 = Customer()
customer3.name = "BB"
customer3.lastName = "s"
customer3.addCart()

customer4 = Customer()
customer4.name = "Bang"
customer4.lastName = "N"
customer4.addCart()
