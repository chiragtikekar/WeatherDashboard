import sqlite3

def get_connection():
    conn = sqlite3.connect("locations.db")
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS locations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()
