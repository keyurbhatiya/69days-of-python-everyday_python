# day 19

# working with json in python

import json 

# python dictionary

student = {
    "name": "Sir",
    "age": 21,
    "Course": "Python",
    "Skills": ["Python","Django","Flask"]

}

# print(student)

# convert python dict to json string

json_data = json.dumps(student) #dump = convert to json string

# print("Json data:")
# print(json_data)

# convert json string back to python dict

python_data = json.loads(json_data) #load  convert to python dict

# print("Python dict :")
# print(python_data)

# write json data to file

with open("student.json","w") as file:
    json.dump(student,file)

# print("json data written sucess")


# read json data from file

with open("student.json","r") as file:
    data = json.load(file)
print("data read from json file :")
print(data)


# access json data

print("Name :",data["name"])
print("Skills :",data["Skills"])

print("end of day 19")