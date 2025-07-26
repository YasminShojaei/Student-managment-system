import sqlite3
from model.tools.student_data_list import course_values
import os

class StudentRepository:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        db_path = os.path.join(os.path.dirname(__file__), "university_db.sqlite")
        print("DB absolute path:", db_path)
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def disconnect(self, commit = False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save_student(self, new_student):
        self.connect()
        self.cursor.execute(
            """insert into students
                   (name, family, birth_date, course_name)
               values (?, ?, ?, ?)""",
            (new_student.name, new_student.family, new_student.birth_date, new_student.course_name)
        )
        self.disconnect(commit=True)

    def edit_student(self, new_student):
        self.connect()
        self.cursor.execute("update students set name=?, family=?, birth_date=?, course_name=? where student_id = ?",
                       [new_student.name, new_student.family, new_student.birth_date, new_student.course_name, new_student.student_id])
        self.disconnect(commit = True)

    def delete_student(self, student_id):
        self.connect()
        self.cursor.execute("delete from students where student_id = ?", [student_id])
        self.disconnect(commit = True)

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from students")
        student_list = self.cursor.fetchall()
        self.disconnect()
        return student_list

    def find_by_id(self, student_id):
        self.connect()
        self.cursor.execute("select * from students where student_id = ?;", [student_id])
        student_list = self.cursor.fetchone()
        self.disconnect()
        return student_list

    def find_by_name_family(self, name, family):
        self.connect()
        self.cursor.execute("select * from students where name like ? and family like ?;", [name + "%", family + "%"])
        student_list = self.cursor.fetchone()
        self.disconnect()
        return student_list
