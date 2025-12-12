
import numpy as np
import pandas as pd
import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)



conn.executescript("""

INSERT INTO Country (COUNTRY_ID, COUNTRY_NAME, CITY_NAME)

VALUES (1, 'INDIA', 'BANGALORE');

INSERT INTO Country (COUNTRY_ID, COUNTRY_NAME, CITY_NAME)

VALUES (1, 'INDIA', 'CHANDIGARH');

INSERT INTO Country (COUNTRY_ID, COUNTRY_NAME, CITY_NAME)

VALUES (1, 'INDIA', 'DELHI');

INSERT INTO Country (COUNTRY_ID, COUNTRY_NAME, CITY_NAME)

VALUES (1, 'INDIA', 'MUMBAI');

INSERT INTO Country (COUNTRY_ID, COUNTRY_NAME, CITY_NAME)

VALUES (1, 'INDIA', 'KOLKATA');

""") 



tables = pd.read_sql('''SELECT *
                     FROM sqlite_master
                     WHERE type='table' ''', conn)
print(tables)
print(pd.read_sql('''SELECT * FROM Country''', conn ))
joined_city = pd.read_sql("""SELECT c.Country_Id, c.Country_Name, ci.City_Name

FROM country c

INNER JOIN city ci

ON c.Country_Id == ci.Country_id""", conn)

print(joined_city)

joined_left = pd.read_sql('''SELECT * 
                          FROM player
                          LEFT JOIN season
                          ON player.Player_Id == season.Man_of_the_Series''', conn)
print(joined_left)

joined_cross = pd.read_sql('''SELECT c.Country_Id, c.Country_Name, ci.City_Name
                           FROM country c
                           CROSS JOIN city ci''', conn)
print(joined_cross)

union = pd.read_sql('''SELECT Player_Name
                    FROM player
                    UNION
                    SELECT Team_Name
                    FROM team''', conn)
print(union) 