class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand         
        self.model = model
        self.__fuel_level = 100     

    def fuel_status(self):
        return f"Fuel at {self.__fuel_level}%"

    def move(self):
        return "The vehicle is moving"

class Car(Vehicle):
    def move(self):
        return f"The {self.brand} {self.model} cruises on the highway"

class ElectricCar(Car):
    def move(self):
        return f"The {self.brand} {self.model} glides silently on electricity"

class Boat(Vehicle):
    def move(self):
        return f"The {self.brand} {self.model} cuts through the waves"

class Flyer:
    def fly(self):
        return "Taking to the skies"

class SeaPlane(Vehicle, Flyer):
    def move(self):
        return f"The {self.brand} {self.model} can taxi on water and then fly"



def demonstrate_oops():
    tesla = ElectricCar("Tesla", "Model S")
    yamaha = Boat("Yamaha", "AR250")
    beaver = SeaPlane("de Havilland", "Beaver")

    print(f"--- Polymorphism in Action ---")
    for transport in [tesla, yamaha, beaver]:
        print(f"{transport.brand}: {transport.move()}")

    print(f"\n--- Multiple Inheritance ---")
    print(beaver.fly())

    print(f"\n--- Encapsulation ---")
   
    print(tesla.fuel_status())

if __name__ == "__main__":
    demonstrate_oops()