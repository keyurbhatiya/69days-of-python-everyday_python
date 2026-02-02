import sqlite3

class LibraryManager:
    def __init__(self, db_name="library.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.setup_db()

    def setup_db(self):
        """Creates the books table if it doesn't exist."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                is_issued INTEGER DEFAULT 0
            )
        """)
        self.conn.commit()

    def add_book(self, title, author):
        self.cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
        self.conn.commit()
        print(f"📖 Added: '{title}' by {author}")

    def view_books(self):
        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()
        print("\n--- 📚 Library Inventory ---")
        for b in books:
            status = "❌ Issued" if b[3] else "✅ Available"
            print(f"ID: {b[0]} | {b[1]} - {b[2]} [{status}]")

    def issue_book(self, book_id):
        self.cursor.execute("UPDATE books SET is_issued = 1 WHERE id = ? AND is_issued = 0", (book_id,))
        if self.cursor.rowcount > 0:
            self.conn.commit()
            print(f"✅ Book ID {book_id} has been issued.")
        else:
            print(f"⚠️ Book ID {book_id} is already issued or doesn't exist.")

    def return_book(self, book_id):
        self.cursor.execute("UPDATE books SET is_issued = 0 WHERE id = ?", (book_id,))
        self.conn.commit()
        print(f"🔄 Book ID {book_id} returned to inventory.")

# --- Interactive System ---
if __name__ == "__main__":
    lib = LibraryManager()
    
    while True:
        print("\n1. Add Book | 2. View Books | 3. Issue Book | 4. Return Book | 5. Exit")
        choice = input("Choice: ")
        
        if choice == '1':
            t = input("Title: "); a = input("Author: ")
            lib.add_book(t, a)
        elif choice == '2':
            lib.view_books()
        elif choice == '3':
            id = input("Enter Book ID to issue: ")
            lib.issue_book(id)
        elif choice == '4':
            id = input("Enter Book ID to return: ")
            lib.return_book(id)
        elif choice == '5':
            break