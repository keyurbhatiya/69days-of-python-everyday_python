# Master SQL CRUD with Python: Creating & Reading Data (Day 42)

from multiprocessing import connection
import sqlite3

# database setup funcation

def create_connection(db_file):

    conn = None

    try:
        conn = sqlite3.connect(db_file)
        print(f" connected to SQLITE version : {sqlite3.version}")
        return conn
    
    except sqlite3.Error as e:
        print(f" Error connecting {e}")

    return conn

# create table

def create_table(conn):
    try:
        sql_create_books_table = """
        create Table IF NOT EXISTS books (
        book_id integer primary key autoincrement,
        title Text NOT NULL,
        author TEXT NOT NULL,
        price REAL NOT NULL,
        stock integer Default 0
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_books_table)
        print(" Table 'books' created successfully. ")
    
    except sqlite3.Error as e:
        print(f"Error creating table {e}")

# insert data to table

def insert_initial_data(conn):
    books_list = [
        ('The Python Way','Guido van Rossum',350,10),
        ('Automate boring stuff','AI sweigort',250,15),
        ('clean code','Robert c. martin',150,5),
        ('Effective Python','Brett slarkin',100,8),
        ('Learnig Python','Alan Beaulieu',100,20)
    ]

    sql_insert = "Insert into books (title,author,price,stock) values (?,?,?,?)"
    cursor = conn.cursor()
    cursor.executemany(sql_insert,books_list)
    conn.commit()
    print(f"Insert {cursor.rowcount} rows of data. ")


# reading all data from table

def read_all_data(conn):
    print("-- Reading All BOOKS --")
    cursor = conn.cursor()
    cursor.execute("Select * FROM books")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# read specific columns

def read_specific_columns(conn):
    print("-- Reading Titles & Prices Only --")
    cursor = conn.cursor()

    # selecting only specific columns save memory
    cursor.execute("Select title,price FROM books")
    rows = cursor.fetchall()

    for row in rows:
        print(f"Book: {row[0]} | Cost : {row[1]}")


# read filtered data

def read_filtered_data(conn,max_price):
    print(f"Findig Books under {max_price} (order by price) ")
    cursor = conn.cursor()

    # using where to filter and order by to sort
    sql_query = "Select title, price FROM books where price < ? order by price ASC"

    cursor.execute(sql_query,(max_price,))
    rows = cursor.fetchall()

    for row in rows:
        print(f" {row[1]} - {row[0]}")



# main execution

if __name__ == '__main__':
    database = "bookstore_inventory.db"

    # 1.connect
    connection = create_connection(database)

    if connection :
        # 2. create opration
        create_table(connection)

        # only once to run
        # insert_initial_data(connection)

        # 3. read opration
        read_all_data(connection)
        read_specific_columns(connection)
        read_filtered_data(connection,200) #under 200

        # 4. close connection
        connection.close()
        print("\n connection closed..")
