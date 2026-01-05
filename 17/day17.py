# file handling in python

# write to a file

# file = open("example.txt","w") # w is for write
# file.write("Welcome to everyday python \n")
# file.write("Day 17 : File Handling in python")
# file.close()

# print("File written success")

# reading from a file

# file = open("example.txt","r") # r is for read
# content = file.read()
# print(content)
# file.close()

# appending to a file

# file = open("example.txt","a") # a is for append
# file.write("\n This line is added later")
# file.close()

# print("content append success")

# reading file line by line

# file = open("example.txt","r")
# for line in file:
#     print(line.strip()) # strip() is used to remove extra new line
# file.close()

# using with statement (best practice)
with open("example2.txt","w") as file: # with statement automatically closes the file
    file.write("This is an example of using with statement \n")
    file.write("File handling made easy!")

print("End of day 17")
