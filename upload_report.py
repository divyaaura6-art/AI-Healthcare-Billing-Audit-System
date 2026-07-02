

import sqlite3

DATABASE = "Database_11/healthcare.db"

def upload_lab_report(ticket_id, report_name):

    print("Ticket ID :", ticket_id)
    print("Report Name :", report_name)

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE ticket
        SET lab_report_pdf = ?
        WHERE ticket_id = ?
    """, (report_name, ticket_id))

    print("Rows Updated :", cursor.rowcount)

    conn.commit()
    conn.close()

    print("✅ Lab Report Attached Successfully")
print(DATABASE)