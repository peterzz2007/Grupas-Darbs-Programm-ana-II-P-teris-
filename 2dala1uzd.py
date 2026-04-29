import sqlite3
import csv

conn = sqlite3.connect("2_dala_1_SQLite_peteris_.db")
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS GRAMATAS(
                BOOK_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                BOOK_NAME TEXT NOT NULL UNIQUE,
                BOOK_AUTHOR TEXT,
                BOOK_GENRE TEXT,
                BOOK_DOB INTEGER, 
                BOOK_PAGES INTEGER
)''')

c.execute('''CREATE TABLE IF NOT EXISTS LIETOTAJI(
                USER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                vards TEXT, 
                uzvards TEXT,
                nodarbosanas TEXT,
                dzimsanas_datums DATE,
                talruna_numurs INTEGER,
                majas_adrese TEXT
)''')

c.execute('''CREATE TABLE IF NOT EXISTS STATISTIKA(
                STAT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                TIME_READ DATE,
                READ_DATE DATE,
                BOOK_ID INTEGER, 
                USER_ID INTEGER, 
                FOREIGN KEY (BOOK_ID) REFERENCES GRAMATAS(BOOK_ID),
                FOREIGN KEY (USER_ID) REFERENCES LIETOTAJI(USER_ID)
)''')



file = open("lietotaji.csv", encoding="UTF-8")
contents = csv.reader(file, delimiter=";")
insert_data = "INSERT INTO LIETOTAJI (vards, uzvards, nodarbosanas, dzimsanas_datums, talruna_numurs, majas_adrese) VALUES(?, ?, ?, ?, ?, ?)"
c.executemany(insert_data, contents)
conn.commit()
