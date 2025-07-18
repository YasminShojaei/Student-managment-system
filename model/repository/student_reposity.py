import sqlite3
from model.entity import student


class StudentRepository:
    def save_student(self):
        connection = sqlite3.connect('university.db')
        curses = connection.cursor()
        curses.execute(
            """insert into students
                (student_id, name, family, birth_date)
        values
            (?, ?, ?, ?)""",
            [student.student_id, student.name, student.family, student.birth_date]
        )

        connection.commit()
        curses.close()
        connection.close()

    def edit_student(self, student):
        connection = sqlite3.connect('university.db')
        curses = connection.cursor()
        curses.execute("update students set student_id=?, name= ?, family=?, birth_date=? where student_id = ?;", [student.student_id, student.name, student.family, student.birth_date])
        connection.commit()
        curses.close()
        connection.close()

    def delete_student(self, student_id):
        connection = sqlite3.connect('university.db')
        curses = connection.cursor()
        curses.execute("delete from students where student_id = ?", [student_id])
        connection.commit()
        connection.commit()
        curses.close()
        connection.close()

    def find_all(self):
        connection = sqlite3.connect('university.db')
        curses = connection.cursor()
        curses.execute("select * from students")
        curses.close()
        connection.close()

    def find_by_id(self, student_id):
        connection = sqlite3.connect('university.db')
        curses = connection.cursor()
        curses.execute("select * from students where student_id = ?;", [student_id])
        curses.close()
        connection.close()

    def find_by_name_family(self, name, family):
        connection = sqlite3.connect('university.db')
        curses = connection.cursor()
        curses.execute("select * from students where name like ? and family like ?;", [name + "%", family + "%"])
        curses.close()
        connection.close()

