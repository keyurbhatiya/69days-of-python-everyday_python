################################## Day 6: 69 Days of Python #####################################

# python functions

# simple function

def greet():
    print("Hello, Welcome to the Everyday Python!")

greet()

print("-----------------")

# function with parameters

def greet_user(name):
    print("hello",name)

greet_user("Sir")
greet_user("Python Learner")

print("-----------------")


# function with multiple parameters

def add_numbers(a,b):
    print("Sum:",a+b)

add_numbers(10,5)

print("-----------------")

# function with default parameters

def country_name(country = "India"):
    print("Country:",country)

country_name()
country_name("USA")
print("---------------")

# function using input

def square_number():
    num = int(input("Enter a number: "))
    print("Square :", num * num)

square_number()

print("------------------End of Day 6------------------------------")

