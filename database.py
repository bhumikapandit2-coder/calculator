import sqlite3

# Database Connection
conn = sqlite3.connect("calculator.db")
cursor = conn.cursor()

# Table Create
cursor.execute("""
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    num1 REAL,
    operator TEXT,
    num2 REAL,
    result TEXT
)
""")

conn.commit()