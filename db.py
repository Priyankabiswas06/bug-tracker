import sqlite3

db = sqlite3.connect("bugs.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS bugs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    status TEXT
)
""")

db.commit()
db.close()

print(" Database created successfully")
