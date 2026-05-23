class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
    def start_engine(self):
        print("The engine is starting...")
class Car(Vehicle):
    def __init__(self, make, model, year, weight, num_doors, num_passengers):
        super().__init__(make, model, year, weight)
        self.num_doors = num_doors
        self.num_passengers = num_passengers
    def start_engine(self):
        print("The car's engine is starting...")
    def drive(self):
        print("The car is driving.")
class Truck(Vehicle):
    def __init__(self, make, model, year, weight, cargo_capacity, towing_capacity):
        super().__init__(make, model, year, weight)
        self.cargo_capacity = cargo_capacity
        self.towing_capacity = towing_capacity
    def start_engine(self):
        print("The truck's engine is starting...")
    def haul(self):
        print("The truck is hauling cargo.")
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, weight, num_wheels, has_sidecar):
        super().__init__(make, model, year, weight)
        self.num_wheels = num_wheels
        self.has_sidecar = has_sidecar
    def start_engine(self):
        print("The motorcycle's engine is starting...")
    def ride(self):
        print("The motorcycle is riding.")

my_car = Car("Dodge", "Challenger", 2023, 1900, 2, 5)
my_truck = Truck("Ford", "F-150", 2021, 2500, 1000, 3500)
my_motorcycle = Motorcycle("Honda", "CBR500R", 2023, 190, 2, False)

print("--- Car ---")
my_car.start_engine()
my_car.drive()

print("--- Truck ---")
my_truck.start_engine()
my_truck.haul()

print("--- Motorcycle ---")
my_motorcycle.start_engine()
my_motorcycle.ride()

print("--- Polymorphism ---")
vehicles = [my_car, my_truck, my_motorcycle]
for vehicle in vehicles:
    vehicle.start_engine()
