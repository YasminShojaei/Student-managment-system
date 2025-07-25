import sqlite3
import os

# این کد ها را جهت مطلق سازی مسیر دیتا بیس اضافه مکینم که در فایل اچ به مشکل نخورم و دیتا بیس چدید نسازه
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "university_db.sqlite")


class CourseRepository:
    def connect(self):
        self.connection = sqlite3.connect(DB_PATH)
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
        self.connection = sqlite3.connect("university_db.sqlite")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT title FROM courses")
        course_names = [row[0] for row in self.cursor.fetchall()]
        self.cursor.close()
        self.connection.close()
        return course_names

