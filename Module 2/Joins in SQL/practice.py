import sqlite3

conn = sqlite3.connect("mavericks_cricket.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Player (
    Player_ID INTEGER PRIMARY KEY,
    Player_Name TEXT,
    Player_Role TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Match (
    Match_ID INTEGER PRIMARY KEY,
    Match_Date TEXT,
    Opponent TEXT,
    Venue TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Player_Match (
    PlayerMatch_ID INTEGER PRIMARY KEY,
    Player_ID INTEGER,
    Match_ID INTEGER,
    Runs INTEGER,
    Wickets INTEGER,
    Catches INTEGER,
    FOREIGN KEY (Player_ID) REFERENCES Player(Player_ID),
    FOREIGN KEY (Match_ID) REFERENCES Match(Match_ID)
);
""")
cursor.executemany("""
INSERT INTO Player (Player_ID, Player_Name, Player_Role)
VALUES (?, ?, ?);
""", [
    (1, 'Rohit Kumar', 'Batsman'),
    (2, 'Vijay Singh', 'Bowler'),
    (3, 'Arjun Menon', 'All-Rounder'),
    (4, 'Rahul Dev', 'Batsman')
])

cursor.executemany("""
INSERT INTO Match (Match_ID, Match_Date, Opponent, Venue)
VALUES (?, ?, ?, ?);
""", [
    (101, '2025-01-10', 'Tigers', 'Mumbai'),
    (102, '2025-01-15', 'Warriors', 'Delhi'),
    (103, '2025-02-01', 'Kings', 'Chennai')
])

cursor.executemany("""
INSERT INTO Player_Match (PlayerMatch_ID, Player_ID, Match_ID, Runs, Wickets, Catches)
VALUES (?, ?, ?, ?, ?, ?);
""", [
    (1001, 1, 101, 75, 0, 1),
    (1002, 2, 101, 10, 3, 0),
    (1003, 3, 102, 40, 2, 1),
    (1004, 1, 102, 55, 0, 2),
    (1005, 3, 103, 20, 1, 0)
])

conn.commit()

print("\n INNER JOIN:")
for row in cursor.execute("""
SELECT 
    Player.Player_Name,
    Match.Match_Date,
    Player_Match.Runs,
    Player_Match.Wickets,
    Player_Match.Catches
FROM Player_Match
INNER JOIN Player ON Player.Player_ID = Player_Match.Player_ID
INNER JOIN Match ON Match.Match_ID = Player_Match.Match_ID;
"""):
    print(row)

print("\n LEFT JOIN (All Players):")
for row in cursor.execute("""
SELECT
    Player.Player_Name,
    Player_Match.Match_ID,
    Player_Match.Runs
FROM Player
LEFT JOIN Player_Match
ON Player.Player_ID = Player_Match.Player_ID;
"""):
    print(row)

print("\nRIGHT JOIN Equivalent (All Matches):")
for row in cursor.execute("""
SELECT
    Match.Match_ID,
    Match.Match_Date,
    Player.Player_Name,
    Player_Match.Runs
FROM Match
LEFT JOIN Player_Match ON Match.Match_ID = Player_Match.Match_ID
LEFT JOIN Player ON Player.Player_ID = Player_Match.Player_ID;
"""):
    print(row)

print("\nFULL OUTER JOIN Equivalent:")
for row in cursor.execute("""
SELECT P.Player_ID, P.Player_Name, PM.Match_ID
FROM Player P
LEFT JOIN Player_Match PM ON P.Player_ID = PM.Player_ID

UNION

SELECT P.Player_ID, P.Player_Name, PM.Match_ID
FROM Player_Match PM
LEFT JOIN Player P ON P.Player_ID = PM.Player_ID;
"""):
    print(row)

print("\n SELF JOIN (Players with same role):")
for row in cursor.execute("""
SELECT 
    A.Player_Name AS Player1,
    B.Player_Name AS Player2,
    A.Player_Role
FROM Player A
JOIN Player B
ON A.Player_Role = B.Player_Role
AND A.Player_ID <> B.Player_ID;
"""):
    print(row)

# Close connection
conn.close()
