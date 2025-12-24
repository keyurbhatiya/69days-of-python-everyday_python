################################## Day 4: 69 Days of Python #####################################

# conditional statements in Python

# simple if statement
age = 18

if age >= 18:
    print("You are eligible to vote.")

# if-else statement

marks = 45

if marks >= 50:
    print("You passed the exam.")
else :
    print("You failed the exam.")

# if - elif - else statement

score = 75

if score >= 90:
    print("Grade:A")
elif score >= 70:
    print("grade:B")
elif score >= 50:
    print("Grade:c")
else:
    print("Grade: Fail")

print("###########################################")

print("---------------While Loop-------------------")

# while loop example

count = 1

while count <= 6:
    print("Count:",count)
    count += 1


print("###########################################")

# while loop with break statement

num = 1

while num <= 10:
    if num == 5:
        break
    print("Number:",num)
    num += 1

print("###########################################")


# while loop with continue
n = 0

while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)

print("----------------------------------- End of Day 4 -----------------------------------")