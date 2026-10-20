import sqlite3

DB_NAME = "database.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        );
    """)

    conn.commit()
    conn.close()

def get_all_transactions():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def add_transaction(data):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO transactions (name, amount, category, date)
        VALUES (?, ?, ?, ?)
    """, (data["name"], data["amount"], data["category"], data["date"]))
    conn.commit()
    conn.close()

def update_transaction(id, data):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE transactions
        SET name = ?, amount = ?, category = ?, date = ?
        WHERE id = ?
    """, (data["name"], data["amount"], data["category"], data["date"], id))
    conn.commit()
    conn.close()

def delete_transaction(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions WHERE id = ?", (id,))
    conn.commit()
    conn.close()
