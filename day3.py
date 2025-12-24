################################## Day 3: 69 Days of Python #####################################

# python booleans

# Boolean Values

print(10 > 9) # True
print(10 == 9) # False
print(10 < 9) # False

# example with if else
a = 200
b = 333

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")


# evaluate values and variables
print(bool(1))  # True
print(bool(0))  # False
print(bool("Hello"))  # True
print(bool(""))  # False


print("example with class")

class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))  # False

# functions that return boolean values

def myFunction() :
    return True
print(myFunction())  # True

print("python  Operators")

# python  Operators
print(10 + 5)  # Addition: 15
print(10 - 5)  # Subtraction: 5
print(10 * 5)  # Multiplication: 50
print(10 / 5)  # Division: 2.0
print(10 % 3)  # Modulus: 1
print(10 ** 2)  # Exponentiation: 100


# python Arithmetic Operators with variables
a = 15
b = 4
print(a + b)  # Addition: 19
print(a - b)  # Subtraction: 11
print(a * b)  # Multiplication: 60
print(a / b)  # Division: 3.75
print(a % b)  # Modulus: 3
print(a ** b)  # Exponentiation: 50625


# python Comparison Operators
x = 10
y = 5
print(x == y)  # Equal: False
print(x != y)  # Not Equal: True
print(x > y)   # Greater Than: True
print(x < y)   # Less Than: False
print(x >= y)  # Greater Than or Equal To: True
print(x <= y)  # Less Than or Equal To: False

print("logical Operators")

#  and ,or , not
a = 10
b = 5
print(a > 5 and b < 10)  # True
print(a > 5 or b > 10)   # True
print(not(a > 5 and b < 10))  # False


# creating and accessing lists
print("-------------lists in python ------------------")
my_list = ["apple", "banana", "cherry"]
print(my_list[0])  # apple
print(my_list[1])  # banana
print(my_list[2])  # cherry
print(my_list[-1]) # cherry
print(my_list[1:3]) # ['banana', 'cherry']

# list oprations
my_list.append("orange")
print(my_list)  # ['apple', 'banana', 'cherry', 'orange']
my_list.remove("banana")
print(my_list)  # ['apple', 'cherry', 'orange']

# check if item exists in list
print("apple" in my_list)  # True
print("banana" not in my_list)  # True
print(len(my_list))  # 3
print("--------------------------------------------------- end of Day 3 ---------------------------------------------------")