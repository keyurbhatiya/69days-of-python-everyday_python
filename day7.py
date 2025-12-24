################################## Day 7: 69 Days of Python #####################################

# Lambda function in python

# Normal Function
import numbers
from os import name


def add(a,b):
    return a+b
print(add(5,3))

print("--------------------")

# Lambda function (one-line function)

add_lambda = lambda a,b:a+b
print(add_lambda(10,5))

print("--------------")

# lambda with single argument
square = lambda x : x * x
print(square(4))

print("---------------")

# using lambda with list

numbers = [1,2,3,4,5]
squares = list(map(lambda x : x * x, numbers))

print(squares)

print("--------------------")

################# python scope #########################

# global variable

x = 10 # global var
def show_scope():
    x = 5  # local variable
    print("Inside function : ", x)

show_scope()
print("Outside Function :", x)

print("---------------------")

# using global keyword
y = 20

def change_value():
    global y 
    print(y)
    y = 50

change_value()
print("Updated global Value : ", y)

print("-----------------------")

################ args and kwargs ############3

# *args example

def add_numbers (*args):
    total=0
    for num in args:
        total += num
    print("Sum using args :" , total)

add_numbers(1,2,3,4)

print("---------------")

# **kwargs example

def student_info(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)

student_info(name = "Sir", Course = "Python",Level = "Beginner")

print("---------------------end day 7 of 69 days of python------------------")