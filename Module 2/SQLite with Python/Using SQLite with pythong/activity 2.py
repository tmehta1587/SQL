
import pandas as pd
import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
);
""")

cursor.execute("INSERT INTO students (name,age) VALUES (?,?)", ('Alice', 14))
cursor.execute("INSERT INTO students (name,age) VALUES (?,?)", ('Bob', 15)) 

conn.commit()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("Using cursor.fetchall():", rows)
df = pd.read_sql("SELECT * FROM students", conn)
print("\nUsing pandas DataFrame:")
print(df)

conn.close()