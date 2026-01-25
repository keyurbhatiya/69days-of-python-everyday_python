# stop being confused by self in python

class SmartDevice:
    def __init__(self,name,brand):
        # this run automatic when new device is created
        self.name = name
        self.brand = brand
        self.is_on = False

    def toggle_power(self):
        self.is_on=not self.is_on
        status = "ON" if self.is_on else "OFF"
        print(f"{self.name} is now {status}.")

# instance
light = SmartDevice("Living room light","Philips")
tv = SmartDevice("Bedroom Tv","Samsung")

light.toggle_power()
    