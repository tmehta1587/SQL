
import pandas as pd
import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)

conn.execute("""
CREATE TABLE IF NOT EXISTS Match1(
    Match_Id INTEGER PRIMARY KEY,
    Season_Id INTEGER,
    Match_Winner TEXT,
    Win_Margin INTEGER,
    Man_of_the_Match TEXT
);
""")

print("Table 'Match' checked/created successfully ")

sample_data = [
    (1,9, 'Team A', 45, 'Player 1'),
    (2,9, 'Team B', 22, 'Player 2'),
    (3,9, 'Team A', 10, 'Player 3'),
    (4,8, 'Team C', 60, 'Player 1')
]

conn.executemany("""

INSERT INTO Match1 (Match_Id, Season_Id, Match_Winner, Win_Margin, Man_of_the_Match)

VALUES (?, ?, ?, ?, ?);

""", sample_data)

conn.commit()

print("Sample data inserted")

tables = pd.read_sql("""
SELECT name 
FROM sqlite_master
WHERE type='table';
""", conn)
print("\n Tables in Database:")
print(tables)

matches = pd.read_sql("SELECT * FROM Match1;", conn)
print("\n Match Table Preview:")
print(matches.head())

result1 = pd.read_sql("""
SELECT Match_Winner, AVG(Win_Margin) AS Avg_Win_Margin
FROM Match1
WHERE Season_Id = 9
GROUP BY Match_Winner
ORDER BY Avg_Win_Margin;
""", conn)
print("\nAverage Win Margin(Season 9):")
print(result1)


result3 = pd.read_sql("""
SELECT 
    MIN(Win_Margin) AS Min_Win_Margin,
    MAX(Win_Margin) AS Max_Win_Margin, 
    AVG(Win_Margin) AS Avg_Min_Margin,
    COUNT(DISTINCT Man_of_the_MAtch) AS Unique_MOM_Count
FROM Match1;
""", conn)
print("\n Stats Across All Seasons: ")
print(result3)

result4 = pd.read_sql("""
SELECT SUM(Win_Margin) AS Total_Win_Margin
FROM Match1
WHERE Season_Id = 9;
""", conn)
print("\nTotal Win Margin (season 9):")
print(result4)

conn.close()
print("\nDatabase connection closed")
