# How to Use Decorators in Python | Master Function Wrappers

# import libaries

import functools
import time
from unittest import result

def log_execution(func):
    @functools.wraps(func) # keeps original function's name and meta data

    def wrapper(*args,**kwargs):
        print(f"Calling function : '{func.__name__}'")
        print(f"Arguments : {args},{kwargs}")

        start_time = time.perf_counter()
        result = func(*args,**kwargs) # execute actual function
        end_time = time.perf_counter()
        
        print(f"Execution time :  {end_time-start_time:.6f} second")
        print(f"Result : {result}\n")
        return result
    return wrapper

@log_execution
def greet(name,message = "Welcome to Day 44 "):
    time.sleep(1) # delay
    return f"Hello {name},{message}!"

@log_execution
def add_numbers(a,b):
    return a+b

greet("Sir ")
add_numbers(10,20)