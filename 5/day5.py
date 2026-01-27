################################## Day 5: 69 Days of Python #####################################

# for loop in python

# using for loop with range()

for i in range(1,11):
    print(i)

print("-------------- end ---------------------")

# print  even numbers from 1 to 30

for i in range(2,31,2):
    print(i)

print("--------------end---------------------")

# looping through a string

word = "Python"
for char in word:
    print(char)

print("-----------------end-----------------------")


# looping through a list

fruits = ['apple','banana','cherry']
for fruit in fruits:
    print(fruit)

print("-----------------end-----------------------")


# using break in for loop

for i in range(1,12):
    if i == 6:
        break
    print(i)

print("-----------------end-----------------------")

# using continue in for loop

for i in range(1,6):
    if i == 2:
        continue
    print(i)

print("--------------------end day 5-----------------------")