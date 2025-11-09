import sqlite3

# Create or connect to the database
conn = sqlite3.connect("diagnosis.db")

# Create a cursor
cursor = conn.cursor()

# Create a sample table for predictions or patient data
cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symptom TEXT NOT NULL,
    predicted_disease TEXT NOT NULL
)
""")  

# Save (commit) changes and close
conn.commit()
conn.close()

print("✅ Database and table created successfully.")