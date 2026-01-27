################################## Day 2: 69 Days of Python #####################################

# Python Data Types

# Built -in Data Types

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType



# Get data data types
print(type("Hello, World!"))  # <class 'str'>

## 1. integer
a = 10
print(type(a))  # <class 'int'>

## 2. float
b = 20.5
print(type(b))  # <class 'float'>

## 3. complex
c = 2 + 3j
print(type(c))  # <class 'complex'>


# Python Numbers

x = 5
y = 2.5
z = 1 + 2j

# Type Conversion

# Convert int to float:
x = 5
print(x)
y = float(x)
print(y)  # 5.0
print(type(y))  # <class 'float'>


# convert from int to complex:
x = 5
print(x)
y = complex(x)
print(y)  # (5+0j)
print(type(y))  # <class 'complex'>



###################### Python strings #########################

# String Creation
str1 = "Hello, World!"
str2 = 'Python is fun.'
str3 = """This is a
multi-line string."""
str4 = '''Another multi-line
string.'''

# String Indexing

my_string = "Hello, World!"
print(my_string[0])    # H
print(my_string[-1])   # d
print(my_string[7:12]) # World
print(my_string[:5])   # Hello
print(my_string[7:])   # World!

# String Methods
my_string = "hello, world!"
print(my_string.upper())      # HELLO, WORLD!
print(my_string.lower())      # hello, world!

# Quoting in Strings
single_quote_str = 'He said, "Hello!"'
double_quote_str = "It's a beautiful day!"
triple_quote_str = '''He said, "It's a beautiful day!"'''
print(single_quote_str)
print(double_quote_str)
print(triple_quote_str)


# String Formatting
name = "Alice"
age = 30
formatted_str = f"My name is {name} and I am {age} years old."
print(formatted_str)  # My name is Alice and I am 30 years old.
# Using format() method
formatted_str2 = "My name is {} and I am {} years old.".format(name, age)
print(formatted_str2)  # My name is Alice and I am 30 years old

print("--------------------------------------------------- String Arrays ---------------------------------------------------")

# String Arrays
string_array = ["apple", "banana", "cherry"]
print(string_array[0])  # apple
print(string_array[1])  # banana
print(string_array[2])  # cherry


# Looping through a string array
for fruit in "Mango, Orange, Pineapple":
    # print(fruit)
    pass


# Checking array and  length of string array
print("banana" in string_array)  # True
print(len(string_array))         # 3
print(len("banana"))             # 6


# Check if not in array
print("grape" not in string_array)  # True
print("apple" not in string_array)  # False

# slice to the end
b = "hello world from everyday python."
print(b[6:])  # world from everyday python.

# Negative Indexing
print(b[-7:])  # python.

# Reverse a string and replace
reversed_b = b[::-1]
print(reversed_b)  # .nohtyp yadreyda morf dlrow olleh
replaced_b = b.replace("everyday", "daily")
print(replaced_b)  # hello world from daily python.


print("--------------------------------------------------- End of Day 2 ---------------------------------------------------")