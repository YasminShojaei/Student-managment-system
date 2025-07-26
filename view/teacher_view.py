from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from controller.teacher_controller import TeacherController
from controller.course_controller import CourseController
from tkinter import messagebox as msg
from model.repository.course_repository import CourseRepository
from model.repository.teacher_repository import TeacherRepository


class TeacherView:

    def __init__(self):
        teacher_window = Tk()
        teacher_window.title("Teacher")
        teacher_window.geometry("1920x1920")
        teacher_window.config(cursor="hand2", background="light blue")

        img = Image.open("teacher_picture.png")
        photo = ImageTk.PhotoImage(img)
        my_label = Label(teacher_window, image=photo)
        my_label.image = photo
        my_label.pack()
        my_label.place(x=0, y=0)

      # teacher id
        Label(teacher_window,
            text="teacher id",
            background="light blue",
            font=("Arial", 12)
            ).place(x=20, y=330)
        self.teacher_id = IntVar(value=0)
        Entry(teacher_window, textvariable=self.teacher_id, background="light blue", font=("Arial", 12)).place(x=135, y=330)

      # teacher name
        Label(teacher_window,
            text="teacher Name",
            background="light blue",
            font=("Arial", 12)
            ).place(x=20, y=370)
        self.name = StringVar()
        Entry(teacher_window, textvariable=self.name, background="light blue", font=("Arial", 12)).place(x=135, y=370)

      # teacher family
        Label(teacher_window,
            text="teacher family",
            background="light blue",
            font=("Arial", 12)
            ).place(x=20, y=410)
        self.family = StringVar()
        Entry(teacher_window, textvariable=self.family, background="light blue", font=("Arial", 12)).place(x=135, y=410)

      # teacher birthdate
        Label(teacher_window,
            text="teacher bday",
            background="light blue",
            font=("Arial", 12)
            ).place(x=20, y=450)
        self.birth_date = StringVar()
        Entry(teacher_window, textvariable=self.birth_date, background="light blue", font=("Arial", 12)).place(x=135, y=450)

        # course id
        Label(teacher_window, text="Course id", background="light blue", font=("Arial", 12)).place(x=20, y=490)
        self.course_id = IntVar()
        Entry(teacher_window, textvariable=self.course_id, background="light blue", font=("Arial", 12)).place(x=135,
                                                                                                              y=490)
        # course teacher

        Label(teacher_window, text="Course teacher", background="light blue", font=("Arial", 12)).place(x=20, y=530)
        self.course_teacher = StringVar()
        Entry(teacher_window, textvariable=self.course_teacher, background="light blue", font=("Arial", 12)).place(
            x=135, y=530)

        # course title
        Label(teacher_window, text="Course title", background="light blue", font=("Arial", 12)).place(x=20, y=570)
        self.course_title = StringVar()
        Entry(teacher_window, textvariable=self.course_title, background="light blue", font=("Arial", 12)).place(x=135,
                                                                                                                 y=570)

        # course unit

        Label(teacher_window, text="Course unit", background="light blue", font=("Arial", 12)).place(x=20, y=610)
        self.course_unit = IntVar()
        Entry(teacher_window, textvariable=self.course_unit, background="light blue", font=("Arial", 12)).place(x=135,
                                                                                                                y=610)

        # course date

        Label(teacher_window, text="Course date", background="light blue", font=("Arial", 12)).place(x=20, y=650)
        self.course_date = StringVar()
        Entry(teacher_window, textvariable=self.course_date, background="light blue", font=("Arial", 12)).place(x=135,
                                                                                                                y=650)


        self.teacher_table = ttk.Treeview(teacher_window, columns=[1,2,3,4,5,6,7,8,9], show="headings", height=20)

        self.teacher_table.heading(1, text="teacher ID")
        self.teacher_table.heading(2, text="teacher Name")
        self.teacher_table.heading(3, text="teacher Family")
        self.teacher_table.heading(4, text="teacher Birthday")
        self.teacher_table.heading(5, text="Course id")
        self.teacher_table.heading(6, text="Course teahcer")
        self.teacher_table.heading(7, text="Course title")
        self.teacher_table.heading(8, text="Course unit")
        self.teacher_table.heading(9, text="Course date")



        self.teacher_table.column(1, width=100, anchor="center")
        self.teacher_table.column(2, width=100, anchor="center")
        self.teacher_table.column(3, width=150, anchor="center")
        self.teacher_table.column(4, width=100, anchor="center")
        self.teacher_table.column(5, width=100, anchor="center")
        self.teacher_table.column(6, width=100, anchor="center")
        self.teacher_table.column(7, width=150, anchor="center")
        self.teacher_table.column(8, width=50, anchor="center")
        self.teacher_table.column(9, width=150, anchor="center")




        self.teacher_table.place(x=400, y=15, height=754)

        self.teacher_table.bind("<<TreeviewSelect>>", self.table_select_teacher)

        Button(teacher_window, text="Save", width=18, command=self.save_teacher).place(x=20, y=690)
        Button(teacher_window, text="edit", width=18, command=self.edit_teacher).place(x=180, y=690)
        Button(teacher_window, text="delete", width=18, command=self.delete_teacher).place(x=20, y=720)
        Button(teacher_window, text="clear", width=18, command=self.reset_teacher).place(x=180, y=720)
        Button(teacher_window, text="search", width=41, command=self.search_teacher).place(x=20, y=750)

        teacher_window.mainloop()


    def save_teacher(self):
        teacher_id = self.teacher_id.get()
        name = self.name.get()
        family = self.family.get()
        birth_date = self.birth_date.get()

        course_id = self.course_id.get()
        course_teacher = self.course_teacher.get()
        course_title = self.course_title.get()
        course_unit = self.course_unit.get()
        course_date = self.course_date.get()


        t_controller = TeacherController()
        result, message = t_controller.save_teacher(teacher_id, name, family, birth_date)

        if not result:
            msg.showerror("Error", f"Failed to save teacher: {message}")
            return

        c_controller = CourseController()
        result, message = c_controller.save_course(course_id, course_teacher, course_title, course_unit, course_date)

        if not result:
            msg.showerror("Error", f"Teacher saved, but course failed: {message}")
            return

        msg.showinfo("Success", "Teacher and Course saved successfully")
        self.load_teacher()
        self.reset_teacher()


    def edit_teacher(self):
        selected = self.teacher_table.focus()
        if not selected:
            msg.showwarning("Warning", "chose what to edit.")
            return


        teacher_id = self.teacher_id.get()
        name = self.name.get()
        family = self.family.get()
        birth_date = self.birth_date.get()

        course_id = self.course_id.get()
        course_teacher = self.course_teacher.get()
        course_title = self.course_title.get()
        course_unit = self.course_unit.get()
        course_date = self.course_date.get()


        t_controller = TeacherController()
        result, message = t_controller.edit_teacher(teacher_id, name, family, birth_date)

        if not result:
            msg.showerror("Error", f"teacher editing error: {message}")
            return


        c_controller = CourseController()
        result, message = c_controller.edit_course(course_id, course_teacher, course_title, course_unit, course_date)

        if not result:
            msg.showerror("Error", f"teacher was edited but not the course: {message}")
            return

        msg.showinfo("Success", "both teacher and course was edited")
        self.load_teacher()
        self.reset_teacher()


    def delete_teacher(self):
        selected = self.teacher_table.focus()
        if not selected:
            msg.showwarning("Warning", "choose what to delete.")
            return

        confirm = msg.askyesno("Confirm", "confirm deleting?")
        if not confirm:
            return

        values = self.teacher_table.item(selected, 'values')
        teacher_id = values[0]
        course_id = values[4]

        t_controller = TeacherController()
        result, message = t_controller.delete_teacher(teacher_id)

        if not result:
            msg.showerror("Error", f"teacher was not deleted: {message}")
            return

        c_controller = CourseController()
        result, message = c_controller.delete_course(course_id)

        if not result:
            msg.showerror("Error", f"teacher was deleted course not: {message}")
            return

        msg.showinfo("Success", "both teacher and course was deleted")
        self.load_teacher()
        self.reset_teacher()

    def reset_teacher(self):

        self.teacher_id.set("")
        self.name.set("")
        self.family.set("")
        self.birth_date.set("")


        self.course_id.set("")
        self.course_teacher.set("")
        self.course_title.set("")
        self.course_unit.set("")
        self.course_date.set("")

        self.teacher_table.selection_remove(self.teacher_table.focus())

    def search_teacher(self):
        name = self.name.get().strip()
        family = self.family.get().strip()
        course_title = self.course_title.get().strip()

        if not (name or family or course_title):
            msg.showwarning("Warning", "Please enter at least one search criteria.")
            return

        for row in self.teacher_table.get_children():
            self.teacher_table.delete(row)

        t_repo = TeacherRepository()
        c_repo = CourseRepository()

        t_repo.connect()
        query_t = "SELECT * FROM teachers WHERE 1=1"
        params_t = []
        if name:
            query_t += " AND name LIKE ?"
            params_t.append(name + "%")
        if family:
            query_t += " AND family LIKE ?"
            params_t.append(family + "%")
        t_repo.cursor.execute(query_t, params_t)
        teachers = t_repo.cursor.fetchall()
        t_repo.disconnect()

        c_repo.connect()
        query_c = "SELECT * FROM courses WHERE 1=1"
        params_c = []
        if course_title:
            query_c += " AND title LIKE ?"
            params_c.append(course_title + "%")
        c_repo.cursor.execute(query_c, params_c)
        courses = c_repo.cursor.fetchall()
        c_repo.disconnect()

        teachers_dict = {t[1]: t for t in teachers}

        if teachers and not courses:
            for t in teachers:
                self.teacher_table.insert("", "end", values=(
                    t[0], t[1], t[2], t[3], "", "", "", "", ""
                ))
            return

        if courses and not teachers:
            for c in courses:
                teacher = teachers_dict.get(c[1], None)
                if teacher:
                    self.teacher_table.insert("", "end", values=(
                        teacher[0], teacher[1], teacher[2], teacher[3],
                        c[0], c[1], c[2], c[3], c[4]
                    ))
                else:
                    self.teacher_table.insert("", "end", values=(
                        "", c[1], "", "", c[0], c[1], c[2], c[3], c[4]
                    ))
            return

        if teachers and courses:
            for c in courses:
                teacher = teachers_dict.get(c[1], None)
                if teacher:
                    self.teacher_table.insert("", "end", values=(
                        teacher[0], teacher[1], teacher[2], teacher[3],
                        c[0], c[1], c[2], c[3], c[4]
                    ))

            teacher_names_with_courses = set(c[1] for c in courses)
            for t in teachers:
                if t[1] not in teacher_names_with_courses:
                    self.teacher_table.insert("", "end", values=(
                        t[0], t[1], t[2], t[3], "", "", "", "", ""
                    ))

    def load_teacher(self):
        for row in self.teacher_table.get_children():
            self.teacher_table.delete(row)

        t_repo = TeacherRepository()
        c_repo = CourseRepository()

        teachers = t_repo.find_all()
        courses = c_repo.find_all()

        courses_dict = {}
        for course in courses:
            courses_dict[course[0]] = course

        for teacher in teachers:
            teacher_id = teacher[0]
            name = teacher[1]
            family = teacher[2]
            birth_date = teacher[3]

            related_courses = [course for course in courses if course[1] == name]
            if related_courses:
                for course in related_courses:
                    self.teacher_table.insert("", "end", values=(
                        teacher_id,
                        name,
                        family,
                        birth_date,
                        course[0],   # course_id
                        course[1],   # course_teacher
                        course[2],   # course_title
                        course[3],   # course_unit
                        course[4],   # course_date
                    ))
            else:
                self.teacher_table.insert("", "end", values=(
                    teacher_id,
                    name,
                    family,
                    birth_date,
                    "", "", "", "", ""
                ))

    def table_select_teacher(self, event):
        selected_item = self.teacher_table.focus()
        if not selected_item:
            return

        values = self.teacher_table.item(selected_item, "values")
        if not values:
            return

        self.teacher_id.set(values[0])
        self.name.set(values[1])
        self.family.set(values[2])
        self.birth_date.set(values[3])

        self.course_id.set(values[4])
        self.course_teacher.set(values[5])
        self.course_title.set(values[6])
        self.course_unit.set(values[7])
        self.course_date.set(values[8])

