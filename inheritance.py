class Smartphone:
    def __init__(self, brand, model, battery_level=100):
        self.brand = brand
        self.model = model
        self.battery_level = battery_level

    def call(self, number):
        if self.battery_level > 0:
            self.battery_level -= 10  # Decrease battery on call
            return f"Calling {number}... 📞"
        return "Battery too low to make a call! 🔋"

    def charge(self):
        self.battery_level = 100
        return "Phone is fully charged! ⚡"

# Inheritance: A subclass with extra functionality
class SmartphonePro(Smartphone):
    def use_ai_assistant(self):
        return "Launching AI assistant... 🤖"

# Creating instances
phone1 = Smartphone("Samsung", "Galaxy S22")
phone2 = SmartphonePro("Apple", "iPhone 15 Pro")

# Testing methods
print(phone1.call("123456789"))  # Calling functionality
print(phone2.use_ai_assistant())  # Additional feature in Pro model