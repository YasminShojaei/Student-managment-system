import sqlite3
from model.entity import student


class StudentRepository:
    def connect(self):
        self.connection = sqlite3.connect("university_db.sqlite")
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
                   (student_id, name, family, birth_date)
            values 
                   (?, ?, ?, ?)""",
            [new_student.student_id, new_student.name, new_student.family, new_student.birth_date]
        )
        self.disconnect(commit=True)

    def edit_student(self, student):
        self.connect()

        self.cursor.execute("update students set student_id=?, name=?, family=?, birth_date=? where student_id = ?",
                       [student.student_id, student.name, student.family, student.birth_date])
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
