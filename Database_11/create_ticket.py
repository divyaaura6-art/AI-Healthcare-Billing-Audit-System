import sqlite3

DATABASE = "Database_11/healthcare.db"

def create_ticket(patient, hospital, extracted_data):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    patient_id = patient[0]

    if hospital:
        discount = "YES"
    else:
        discount = "NO"

    cursor.execute("""

        INSERT INTO ticket(

            patient_id,

            hospital_name,

            discount_applied,

            status

        )

        VALUES(?,?,?,?)

    """,

    (

        patient_id,

        extracted_data["hospital_name"],

        discount,

        "ACTIVE"

    ))

    conn.commit()

    ticket_id = cursor.lastrowid

    conn.close()

    return ticket_id