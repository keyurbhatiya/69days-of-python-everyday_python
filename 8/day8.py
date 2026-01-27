################################## Day 8: 69 Days of Python #####################################

# python tuple

# creating a tuple

my_tuple = ("apple","banana","cherry")
print(my_tuple)

# accessing tuple items
print(my_tuple[0])
print(my_tuple[-1])

# tuple slicing
print(my_tuple[1:3])

# tuple is immutable (cannot change value)
# my_tuple [0] = "orange" #this will cause an error

print("----------------------")

# loop through tuple
for item in my_tuple:
    print(item)

print("--------------------------")

# python sets

# creating a set
my_set = {"apple","banana","cherry"}
print(my_set)

# sets do not allow duplicate values
duplicate_set = {"apple","banana","apple"}
print(duplicate_set)

# add items to set
my_set.add("orange")
print(my_set)

# remove items from set
my_set.remove("banana")
print(my_set)

print("------------------")

# check item exits in set
print("apple" in my_set)
print("grape" not in my_set)

# loop through set
for item in my_set:
    print(item)

print("-------------------------end day 8 of 69days of python!-----------------------")