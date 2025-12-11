
import sqlite3

conn = sqlite3.connect('database.sqlite')

print("Opened database successfully")

conn.execute('''CREATE TABLE CLASS1

(SNO INT PRIMARY KEY NOT NULL,

Roll_No INT NOT NULL,

Name TEXT NOT NULL,

AGE INT DEFAULT (15),

GENDER TEXT NOT NULL,

Email_ID TEXT NOT NULL,

Contact_No REAL NOT NULL);''')

print("Table created successfully")

conn.execute("""

INSERT INTO CLASS1 (SNO, Roll_No, NAME, AGE, Gender, Email_ID, Contact_No)

VALUES (1, 23, 'John Doe', 15, 'M', 'john@example.com', '1234567890');

""")

conn.execute("""
INSERT INTO CLASS1 (SNO,Roll_No,NAME,AGE,Gender,Email_ID,Contact_No) \

VALUES (2, 2, 'Aisha', 14, 'Female', 'aish@gmail.com', 9080900 );
""")



conn.commit()
print("Records created successfully")

import pandas as pd 
tables = pd.read_sql("""SELECT * 
                     FROM sqlite_master
                     WHERE type='table';""",conn)
print(tables)

class_10d = pd.read_sql("""SELECT *
                        FROM CLASS1;""",conn)

print(class_10d.head())


