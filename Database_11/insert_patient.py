import sqlite3

# Connect to the database
conn = sqlite3.connect("healthcare.db")
cursor = conn.cursor()

# Fetch all tickets
cursor.execute("SELECT * FROM ticket")

tickets = cursor.fetchall()

print("\n========== TICKET TABLE ==========\n")

if tickets:
    for ticket in tickets:
        print(ticket)
else:
    print("No tickets found.")

conn.close()