import sqlite3

conn = sqlite3.connect("healthcare.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS ticket")

cursor.execute("""
CREATE TABLE ticket(

    ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,

    patient_id INTEGER NOT NULL,

    hospital_name TEXT NOT NULL,

    discount_applied TEXT,

    status TEXT DEFAULT 'ACTIVE',

    lab_report_pdf TEXT

)
""")

conn.commit()
conn.close()

print("Ticket table created successfully!")