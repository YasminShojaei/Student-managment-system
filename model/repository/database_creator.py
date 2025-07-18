import sqlite3

connection = sqlite3.connect("university_db.sqlite")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    family text NOT NULL,
    birth_date text NOT NULL
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS teachers (
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    family text NOT NULL,
    birth_date text NOT NULL
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER primary key, 
    course_teacher text NOT NULL,
    title TEXT NOT NULL,
    unit INTEGER NOT NULL,
    course_date TEXT NOT NULL
)
""")

connection.commit()
cursor.close()
connection.close()
