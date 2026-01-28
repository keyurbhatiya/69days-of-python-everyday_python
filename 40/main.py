# Python Polymorphism Explained: One Interface, Many Forms (Day 40)

class Dog:
    def speak(self):
        return "Woof! Woof!"
    
class Cat:
    def speak(self):
        return "Meow! Meow!"

class Parrot:
    def speak(self):
        return "Hello! hello!" 

# polymorphism action a single function that handles any animal

def animal_sound(animal):
    print(animal.speak())

# create objects

my_dog = Dog()
my_cat = Cat()
my_parrot = Parrot()

# one function many uses

print("testing polymorphism: ")
animal_sound(my_dog)
animal_sound(my_cat)
animal_sound(my_parrot)

# loop with 

print("\n looping through animals : ")
for animal in [my_dog,my_cat,my_parrot]:
    print(animal.speak())