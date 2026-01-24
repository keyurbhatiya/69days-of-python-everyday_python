# The "Blueprint" (Class)
class Smartphone:
    def __init__(self, brand, model, battery_life):
        # These are attributes (Data)
        self.brand = brand
        self.model = model
        self.battery = battery_life

    # This is a method (Action)
    def describe_phone(self):
        return f"This is a {self.brand} {self.model} with {self.battery}% battery."

# Creating "Objects" (Instances of the class)
my_phone = Smartphone("Apple", "iPhone 17", 95)
your_phone = Smartphone("Samsung", "Galaxy S25", 88)

# Accessing the data and actions
print(my_phone.describe_phone())
print(your_phone.brand) 
print(your_phone.battery)