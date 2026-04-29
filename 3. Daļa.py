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

        c.execute('''INSERT INTO DOCTORATES (DOCTORATE_NAME, PATIENT_COUNT) VALUES (?, ?)''', (self.doc_name, self.patient_count))
        print(f"Doktorāts {self.doc_name} tika veiksmīgi pievienots ar {self.patient_count} pacientiem!")
        conn.commit()

    def view_data(self):
        c.execute('''SELECT * FROM DOCTORATES''')
        for row in c.fetchall():
            val1 = row[1]
            val2 = row[2]
            print(f"{val1} apkalpo {val2} pacientus!")

selection = input("Ko jūs vēlaties darīt? 1 - Pievienot doktorātu, 2 - Apskatīt doktorātus: ")
if selection == "1":
    name = input("Ievadiet doktorāta vārdu!: ")
    count = input("Ievadiet pacientu skaitu!: ")
    docs = Doctorates(name, count)
    docs.insert_data()
elif selection == "2":
    obj = Doctorates("","")
    obj.view_data()
