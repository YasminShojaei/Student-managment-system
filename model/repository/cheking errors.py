import sqlite3

conn = sqlite3.connect("university_db.sqlite")
cursor = conn.cursor()
cursor.execute("SELECT title FROM courses")
rows = cursor.fetchall()
print(rows)
conn.close()
