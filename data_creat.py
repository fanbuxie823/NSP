import sqlite3

conn = sqlite3.connect('DATA.db')
print ("Opened database successfully");

conn.execute('''CREATE TABLE DATA_2HOURS
       (ID INT PRIMARY KEY     NOT NULL,
       TEMP           INT    NOT NULL,
       HUM            INT    NOT NULL);''')
print ("Table created successfully");

conn.execute('''CREATE TABLE DATA_24HOURS
       (ID INT PRIMARY KEY     NOT NULL,
       TEMP           INT    NOT NULL,
       HUM            INT    NOT NULL);''')
print ("Table created successfully");

conn.close()
