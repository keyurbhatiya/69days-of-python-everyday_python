# python SQLite Tutorial : How to store data Locally Forever

import sqlite3

# 1. connect to the database
# file collage.db

connection = sqlite3.connect("collage.db")

# 2. create a cursor object to execute sql cmds

cursor = connection.cursor()

# 3. create a table using sql syntax

# we use IF NOT exists so the code doesn't crash if we run twice

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
    id Integer Primary Key Autoincrement,
    name Text NOT NULL,
    grade Integer NOT NULL,
    email Text Unique
    )
""")

# 4 insert data into the table

new_students = [
    ("Rahul sharma", 10 , "rahul@example.com"),
    ("Priya Patel", 9, "priya@example.com"),
    ("Amit verma" , 11 , "amit@example.com")
]

# executemany() is efficient for inserting multiple rows at once

cursor.executemany("INSERT OR IGNORE INTO students (name,grade,email) VALUES (?,?,?)",new_students)

#  5. commit the changes to save them persistently

connection.commit()
print("Data inserted sucess!")


# 6. query (fetch) data from the database

print("\n -- current students List --")

cursor.execute("select * from students")
all_students = cursor.fetchall()

for student in all_students:
    # student is a tuple containing (id,name,grade,email)
    print(f"ID: {student[0]}, Name: {student[1]}, Grade: {student[2]}")

# close the connection when done

connection.close()