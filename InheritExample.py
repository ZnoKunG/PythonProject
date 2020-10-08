class Vehicle:
    licenseNumber = ""
    serialCode = ""
    face = ""
    def turnOnAirCon(self):
        print("Turn on : Air")

class Car(Vehicle):
    def sayHello(self):
        print("Hello World")
class Pickup(Vehicle):
    pass
class Van(Vehicle):
    pass
class EstateCar(Vehicle):
    pass

car1 = Car()
car1.turnOnAirCon()

pickup1 = Pickup()
pickup1.turnOnAirCon()

van1 = Van()
van1.turnOnAirCon()

estatecar1 = EstateCar()
estatecar1.turnOnAirCon()

