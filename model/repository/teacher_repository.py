import sqlite3


class TeacherRepository:
    def connect(self):
        self.connection = sqlite3.connect("university_db.sqlite")
        self.cursor = self.connection.cursor()

    def disconnect(self, commit = False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save_teacher(self, new_teacher):
        self.connect()
        self.cursor.execute(
            """insert into teachers
                   (teacher_id, name, family, birth_date)
            values 
                   (?, ?, ?, ?)""",
            [new_teacher.teacher_id, new_teacher.name, new_teacher.family, new_teacher.birth_date]
        )
        self.disconnect(commit=True)

    def edit_teacher(self, new_teacher):
        self.connect()
        self.cursor.execute("update teachers set name=?, family=?, birth_date=? where teacher_id = ?",
                       [new_teacher.name, new_teacher.family, new_teacher.birth_date, new_teacher.teacher_id])
        self.disconnect(commit = True)

    def delete_teacher(self, teacher_id):
        self.connect()
        self.cursor.execute("delete from teachers where teacher_id = ?", [teacher_id])
        self.disconnect(commit = True)

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from teachers")
        teacher_list = self.cursor.fetchall()
        self.disconnect()
        return teacher_list

    def find_by_id(self, teacher_id):
        self.connect()
        self.cursor.execute("select * from teachers where teacher_id = ?;", [teacher_id])
        teacher_list = self.cursor.fetchone()
        self.disconnect()
        return teacher_list

    def find_by_name_family(self, name, family):
        self.connect()
        self.cursor.execute("select * from teachers where name like ? and family like ?;", [name + "%", family + "%"])
        teacher_list = self.cursor.fetchone()
        self.disconnect()
        return teacher_list
