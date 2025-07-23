import sqlite3
import os

# Path to your SQLite database
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'db.sqlite3')

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print('Tables in the database:')
for table in tables:
    print(table[0])

conn.close()
