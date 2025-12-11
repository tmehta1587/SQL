
import pandas as pd
import sqlite3

# -----------------------------
# 1. Connect to SQLite Database
# -----------------------------
database = "data.sqlite"  # make sure this file is in the same folder
conn = sqlite3.connect(database)
print('Opened database successfully')

# -----------------------------
# 2. (Optional) Create a sample Match table if not exists
# -----------------------------
# If your database already has the "Match" table, you can skip this section.
conn.execute("""
CREATE TABLE IF NOT EXISTS Match (
    Match_Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Season_Id INTEGER,
    Match_Winner TEXT,
    Win_Margin REAL,
    Man_of_the_Match TEXT,
    Venue_Id INTEGER
);
""")
print("Table 'Match' checked/created successfully ")

# -----------------------------
# 3. (Optional) Insert sample data (remove if you already have data)
# -----------------------------
sample_data = [
    (9, 'Team A', 45, 'Player 1', 101),
    (9, 'Team B', 22, 'Player 2', 102),
    (9, 'Team A', 10, 'Player 3', 101),
    (8, 'Team C', 60, 'Player 1', 103),
]
conn.executemany("""
INSERT INTO Match (Season_Id, Match_Winner, Win_Margin, Man_of_the_Match, Venue_Id)
VALUES (?, ?, ?, ?, ?);
""", sample_data)
conn.commit()
print("Sample data inserted ")

# -----------------------------
# 4. View available tables
# -----------------------------
tables = pd.read_sql("""
SELECT name 
FROM sqlite_master 
WHERE type='table';
""", conn)
print("\n Tables in Database:")
print(tables)

# -----------------------------
# 5. Load Match table into DataFrame
# -----------------------------
matches = pd.read_sql("SELECT * FROM Match;", conn)
print("\n Match Table Preview:")
print(matches.head())

# -----------------------------
# 6. Queries
# -----------------------------

# Average Win Margin of all winning teams for Season 9
result1 = pd.read_sql("""
SELECT Match_Winner, AVG(Win_Margin) AS Avg_Win_Margin
FROM Match
WHERE Season_Id = 9
GROUP BY Match_Winner
ORDER BY Avg_Win_Margin;
""", conn)
print("\nAverage Win Margin (Season 9):")
print(result1)

# Count of venues for Season 9
result2 = pd.read_sql("""
SELECT COUNT(DISTINCT Venue_Id) AS Venue_Count
FROM Match
WHERE Season_Id = 9;
""", conn)
print("\nVenue Count (Season 9):")
print(result2)

# Min, Max, Avg Win Margin + total number of unique Man of the Match
result3 = pd.read_sql("""
SELECT 
    MIN(Win_Margin) AS Min_Win_Margin, 
    MAX(Win_Margin) AS Max_Win_Margin, 
    AVG(Win_Margin) AS Avg_Win_Margin, 
    COUNT(DISTINCT Man_of_the_Match) AS Unique_MOM_Count
FROM Match;
""", conn)
print("\n Stats Across All Seasons:")
print(result3)

# Total Win Margin of all winners in Season 9
result4 = pd.read_sql("""
SELECT SUM(Win_Margin) AS Total_Win_Margin
FROM Match
WHERE Season_Id = 9;
""", conn)
print("\nTotal Win Margin (Season 9):")
print(result4)

# -----------------------------
# 7. Close connection
# -----------------------------
conn.close()
print("\nDatabase connection closed ")