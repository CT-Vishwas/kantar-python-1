import sqlite3

# Create a connection
conn = sqlite3.connect("dev.db")
print("Database connected")

# Create a cursor
cur = conn.cursor()

# Create a table
query = """CREATE TABLE IF NOT EXISTS users(
          id INTEGER PRIMARY KEY AUTOINCREMENT, 
          name TEXT NOT NULL,
          age INTEGER,
          email TEXT UNIQUE
        )"""
cur.execute(query)
conn.commit()

cur.execute(
    "INSERT INTO users (name,age,email) VALUES(?,?,?)",
    ("Vishwas",25,"vishwas@cloudthat.com")
)

conn.commit()

users = [
    ("Jane",30,"jane@cloudthat.com"),
    ("Johnny",35,"johnny@loudthat.com")
]

cur.executemany(
    "INSERT INTO users (name,age,email) VALUES(?,?,?)",
    users
)

conn.commit()

cur.execute("SELECT * FROM users")
rows = cur.fetchall()

for row in rows:
    print(row)