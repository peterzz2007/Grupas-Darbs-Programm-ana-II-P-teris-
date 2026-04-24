import sqlite3

conn = sqlite3.connect('doctorates.db')
c = conn.cursor()
c.execute('''
                CREATE TABLE IF NOT EXISTS DOCTORATES(
                    DOCTORATE_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    DOCTORATE_NAME TEXT NOT NULL UNIQUE,
                    PATIENT_COUNT INTEGER NOT NULL 
                                    )
        ''')

class Doctorates():
    def __init__(self, doc_name, patient_count):
        self.doc_name = doc_name
        self.patient_count = patient_count

    def insert_data(self):

        c.execute('''INSERT INTO DOCTORATES (DOCTORATE_NAME, PATIENT_COUNT) VALUES = (?, ?)''', (self.doc_name, self.patient_count))
        print("Doktorāts veiksmīgi pievienots!")

    def view_data(self):
        c.execute('''SELECT * FROM DOCTORATES''')
        for row in c.fetchall():
            print(row[0])

selection = input("Ko jūs vēlaties darīt? 1 - Pievienot doktorātu, 2 - Apskatīt doktorātus: ")
if selection == 1:
    print("success")
    name = input("Ievadiet doktorāta vārdu!: ")
    count = input("Ievadiet pacientu skaitu!: ")
    Doctorates.insert_data()
    docs = Doctorates(name, count)
elif selection == 2:
    Doctorates.view_data()
