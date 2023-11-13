import sqlite3

conn = sqlite3.connect('contact.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS contacts
(id INTEGER PRIMARY KEY,
name TEXT,
address REAL,
phone_number INTEGER,
email TEXT)""")

conn.commit()
conn.close()