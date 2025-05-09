class Vehicle:
    def move(self):
        return "Moving..."

class Car(Vehicle):
    def move(self):
        return "Driving on the road 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying in the sky ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing on water 🚤"

# Function demonstrating polymorphism
def vehicle_action(vehicle):
    print(vehicle.move())

# Creating instances
car = Car()
plane = Plane()
boat = Boat()

# Calling the same method, but different behaviors!
vehicle_action(car)    # Output: Driving on the road 🚗
vehicle_action(plane)  # Output: Flying in the sky ✈️
vehicle_action(boat)   # Output: Sailing on water 🚤