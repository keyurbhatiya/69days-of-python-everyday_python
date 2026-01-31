import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    # Create table for storing expenses
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            category TEXT,
            amount REAL
        )
    """)
    conn.commit()
    return conn

def add_expense(conn, category, amount):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (date, category, amount) VALUES (?, ?, ?)", 
                   (date, category, amount))
    conn.commit()
    print(f"✅ Added: ₹{amount} for {category}")

def view_expenses(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    
    print("\n--- 💸 Your Expense History ---")
    print(f"{'ID':<4} | {'Date':<20} | {'Category':<15} | {'Amount':<10}")
    print("-" * 55)
    for row in rows:
        print(f"{row[0]:<4} | {row[1]:<20} | {row[2]:<15} | ₹{row[3]:<10}")

def show_total(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]
    print(f"\n💰 Total Spending: ₹{total if total else 0:.2f}")

# Main Execution
if __name__ == "__main__":
    db_conn = init_db()
    
    # Interaction Menu
    while True:
        print("\n1. Add Expense | 2. View History | 3. Total Spending | 4. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            cat = input("Enter Category (Food/Travel/Rent): ")
            amt = float(input("Enter Amount: "))
            add_expense(db_conn, cat, amt)
        elif choice == '2':
            view_expenses(db_conn)
        elif choice == '3':
            show_total(db_conn)
        elif choice == '4':
            db_conn.close()
            break