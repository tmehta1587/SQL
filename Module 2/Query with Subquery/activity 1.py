
import pandas as pd
import sqlite3

database = "database.sqlite"
conn = sqlite3.connect(database)
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS Team;
DROP TABLE IF EXISTS Season;
DROP TABLE IF EXISTS Match;
DROP TABLE IF EXISTS Batman_Scored;
                     
CREATE TABLE Team(
    Team_Id INTEGER PRIMARY KEY,
    Team_Name TEXT
);
                     
CREATE TABLE Season(
    Season_Id INTEGER PRIMARY KEY,\
    Season_Year INTEGER
);
                     
CREATE TABLE Match(
    Match_Id INTEGER PRIMARY KEY,
    Season_Id INTEGER,
    Team_1 INTEGER,
    Team_2 INTEGER,
    Toss_Winner INTEGER,
    Match_Winner INTEGER
);
                     
CREATE TABLE Batsman_Scored (
    Match_Id INTEGER,
    Innings_No INTEGER,
    Runs_Scored INTEGER
);
""")

teams = [
    (1, "Mumbai Indians"),
    (2, "Royal Challengers Bangalore"),
    (3, "Chennai Super Kings"),
    (4, "Kolkata Knight Riders")
]

cursor.executemany("INSERT INTO Team VALUES(?,?)", teams)
seasons = [
    (7, 2014),
    (8, 2015)
]
cursor.executemany("INSERT INTO Season VALUES (?,?)", seasons)

matches = [
    (1, 8, 3, 1, 3, 3), 
    (2, 8, 3, 2, 2, 3),
    (3, 8, 1, 3, 1, 1),
    (4, 8, 3, 4, 3, 4)
]
cursor.executemany("INSERT INTO Match VALUES(?,?,?,?,?,?)", matches)

batsman_scores = [
    (1,1,60),
    (1,2,45),
    (2,1,72),
    (2,2,30),
    (3,3,50),
    (3,2,20),
    (4,1,90),
    (4,2,10)
]
cursor.executemany("INSERT INTO Batsman_Scored VALUES (?,?,?)", batsman_scores)

conn.commit()

tables = pd.read_sql("""
SELECT name FROM sqlite_master WHERE type='table';
""", conn)
print("\nTables in Database")
print(tables)

team = pd.read_sql("SELECT * FROM Team", conn)
print("\nTeam Table")
print(team)

season = pd.read_sql("SELECT * FROM Season", conn)
print("\nSeason Table")
print(season)

csk_matches_2015 = pd.read_sql("""
SELECT Match_Id, Team_2 AS Away_Team, Toss_Winner, Match_Winner
FROM Match
WHERE (Team_1 = 3 OR Team_2 = 3)
AND Season_Id = 8
""", conn)

print("\nMatches Played By Chennai Super Kings in Year 2015")
print(csk_matches_2015)

csk_wins = pd.read_sql("""
SELECT * 
FROM Match
WHERE Match_Winner = 3 AND Season_Id = 8
""", conn)

print("\nMatches Won By CSK in Year 2015")
print(csk_wins)

match_runs = pd.read_sql("""
SELECT MATCH_Id, Runs_Scores AS Total_Runs, Innings_No
FROM Batsman_Scored > 5
AND Match_Id IN (
    SELECT Match_Id FROM Match WHERE Season_Id = 8)
""", conn)

print("\nMatches with Runs Greater Than 5 in Year 2015")
print(match_runs)

avg_runs = pd.read_sql("""
SELECT Match_Id, Runs_Scored AS Total_Runs, Innings_No
FROM Batsman_Scored
WHERE Innings_No = 1
AND Runs_Scored > 
    (SELECT AVG(Runs_Scored) FROM Batsman_Scored)
""", conn)

print("\nMatches with Runs Greater Than Average Runs")
print(avg_runs)

conn.close()