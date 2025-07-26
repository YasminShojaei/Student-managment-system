import sqlite3
import os

class CourseRepository:
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

    def save_course(self, new_course):
        self.connect()
        self.cursor.execute(
            """insert into courses
                   (course_id, course_teacher, title, unit, course_date)
            values 
                   (?, ?, ?, ?, ?)""",
            [new_course.course_id, new_course.course_teacher, new_course.title, new_course.unit, new_course.course_date]
        )
        self.disconnect(commit=True)

    def edit_course(self, new_course):
        self.connect()
        self.cursor.execute("update courses set course_teacher=?, title=?, unit=?, course_date=? where course_id = ?",
                       [new_course.course_teacher, new_course.title, new_course.unit, new_course.course_date, new_course.course_id])
        self.disconnect(commit = True)

    def delete_course(self, course_id):
        self.connect()
        self.cursor.execute("delete from courses where course_id = ?", [course_id])
        self.disconnect(commit = True)

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from courses")
        course_list = self.cursor.fetchall()
        self.disconnect()
        return course_list

    def find_by_id(self, course_id):
        self.connect()
        self.cursor.execute("select * from courses where course_id = ?;", [course_id])
        course_list = self.cursor.fetchone()
        self.disconnect()
        return course_list

    def find_by_date(self, course_date):
        self.connect()
        self.cursor.execute("select * from courses where course_date = ?;", [course_date])
        course_list = self.cursor.fetchone()
        self.disconnect()
        return course_list

    def find_by_title(self, title):
        self.connect()
        self.cursor.execute("select * from courses where title like ?;", [title + "%"])
        course_list = self.cursor.fetchone()
        self.disconnect()
        return course_list

    def get_all_course_names(self):
        self.connect()
        self.cursor.execute("SELECT title FROM courses")
        course_names = [row[0] for row in self.cursor.fetchall()]
        self.disconnect()
        return course_names

