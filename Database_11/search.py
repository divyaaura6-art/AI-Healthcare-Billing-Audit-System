import sqlite3

DATABASE = "Database_11\healthcare.db"


# -------------------------------------
# Search Patient
# -------------------------------------
def search_patient(extracted_data):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""

        SELECT *
        FROM patients
        WHERE patient_name = ?
        AND dob = ?
        AND phone = ?

    """, (

        extracted_data["patient_name"],
        extracted_data["dob"],
        extracted_data["phone"]

    ))

    patient = cursor.fetchone()

    conn.close()

    return patient


# -------------------------------------
# Search Hospital
# -------------------------------------
def search_hospital(extracted_data):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""

        SELECT *
        FROM hospitals
        WHERE hospital_name = ?

    """, (

        extracted_data["hospital_name"],

    ))

    hospital = cursor.fetchone()

    conn.close()

    return hospital