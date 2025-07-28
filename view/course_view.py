from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

from controller.course_controller import CourseController
from tkinter import messagebox as msg

from controller.teacher_controller import TeacherController


class CourseView:

    def __init__(self):
        course_window = Tk()
        course_window.title("Course")
        course_window.geometry("1920x1920")
        course_window.config(cursor="hand2", background="light blue")

        img = Image.open("course_picture.png")
        photo = ImageTk.PhotoImage(img)
        my_label = Label(course_window, image=photo)
        my_label.image = photo
        my_label.pack()
        my_label.place(x=0, y=0)

      # course id
        Label(course_window,
            text="course id",
            background="light blue",
            font=("Arial", 12)
            ).place(x=20, y=300)
        self.course_id = IntVar(value=0)
        Entry(course_window, textvariable=self.course_id, background="light blue", font=("Arial", 12)).place(x=135, y=300)

      # course teacher
        Label(course_window,
            text="course teacher",
            background="light blue",
            font=("Arial", 12)
            ).place(x=20, y=350)

        self.course_teacher = StringVar()

        self.course_teacher_combobox = ttk.Combobox(course_window,
                                                    textvariable=self.course_teacher,
                                                    state="readonly",
                                                    font=("Arial", 12))

        t_controller = TeacherController()
        teacher_names = t_controller.get_all_teachers_names()

        if teacher_names:
            self.course_teacher_combobox["values"] = teacher_names
            self.course_teacher_combobox.current(0)

        else:
            self.course_teacher_combobox["values"] = ["first save the teacher"]
            self.course_teacher_combobox.current(0)

        self.course_teacher_combobox.place(x=135, y=350, width=200)

      # course title
        Label(course_window,
            text="course title",
            background="light blue",
            font=("Arial", 12)
            ).place(x=20, y=400)
        self.course_title = StringVar()
        Entry(course_window, textvariable=self.course_title, background="light blue", font=("Arial", 12)).place(x=135, y=400)

      # course unit
        Label(course_window,
            text="course unit",
            background="light blue",
            font=("Arial", 12)
            ).place(x=20, y=450)
        self.course_unit = IntVar(value=0)
        Entry(course_window, textvariable=self.course_unit, background="light blue", font=("Arial", 12)).place(x=135, y=450)

        # course date
        Label(course_window,
            text="course date",
            background="light blue",
            font=("Arial", 12)
            ).place(x=20, y=500)
        self.course_date = StringVar()
        Entry(course_window, textvariable=self.course_date, background="light blue", font=("Arial", 12)).place(x=135, y=500)

        self.course_table = ttk.Treeview(course_window, columns=[1,2,3,4, 5], show="headings", height=20)

        self.course_table.heading(1, text="course ID")
        self.course_table.heading(2, text="course teacher")
        self.course_table.heading(3, text="course title")
        self.course_table.heading(4, text="course unit")
        self.course_table.heading(5, text="course date")



        self.course_table.column(1, width=200, anchor="center")
        self.course_table.column(2, width=250, anchor="center")
        self.course_table.column(3, width=250, anchor="center")
        self.course_table.column(4, width=200, anchor="center")
        self.course_table.column(5, width=200, anchor="center")


        self.course_table.place(x=400, y=15, height=670)

        self.course_table.bind("<<TreeviewSelect>>", self.table_select_course)

        Button(course_window, text="Save", width=18, command=self.save_course).place(x=20, y=600)
        Button(course_window, text="edit", width=18, command=self.edit_course).place(x=180, y=600)
        Button(course_window, text="delete", width=18, command=self.delete_course).place(x=20, y=630)
        Button(course_window, text="clear", width=18, command=self.reset_course).place(x=180, y=630)
        Button(course_window, text="search", width=41, command=self.search_course).place(x=20, y=660)

        course_window.mainloop()


    def save_course(self):
        course_id = self.course_id.get()
        course_teacher = self.course_teacher.get()
        course_title = self.course_title.get()
        course_unit = self.course_unit.get()
        course_date = self.course_date.get()

        c_controller = CourseController()
        result, message = c_controller.save_course(course_id, course_teacher, course_title, course_unit, course_date)

        if result:
            msg.showinfo("course saved", message)
            self.load_course()
            self.reset_course()

        else:
            msg.showerror("course not saved", message)


    def edit_course(self):
        course_id = self.course_id.get()
        course_teacher = self.course_teacher.get()
        course_title = self.course_title.get()
        course_unit = self.course_unit.get()
        course_date = self.course_date.get()

        controller = CourseController()
        result, message = controller.edit_course(course_id, course_teacher, course_title, course_unit, course_date)
        if result:
            msg.showinfo("course edited", message)
            self.load_course()
            self.reset_course()
        else:
            msg.showerror("course not saved", message)

    def delete_course(self):
        course_id = self.course_id.get()

        if not course_id:
            msg.showerror("Error, please select a course id to delete")
            return

        controller = CourseController()
        result, message = controller.delete_course(course_id)

        if result:
            msg.showinfo("course deleted", message)
            self.load_course()
            self.reset_course()

        else:
            msg.showerror("course not deleted", message)

    def reset_course(self):
        self.course_id.set(0)
        self.course_teacher.set("")
        self.course_title.set("")
        self.course_unit.set(0)
        self.course_date.set("")


    def search_course(self):
        course_id = self.course_id.get()
        course_date = self.course_date.get().strip()
        course_title = self.course_title.get().strip()

        controller = CourseController()

        for row in self.course_table.get_children():
            self.course_table.delete(row)

        if course_id:
            success, result = controller.find_by_id(course_id)
            if success:
                self.reset_course()
                course = result
                self.course_table.insert("", "end", values=(course[0], course[1], course[2], course[3], course[4]))

                self.course_id.set(course[0])
                self.course_teacher.set(course[1])
                self.course_title.set(course[2])
                self.course_unit.set(course[3])
                self.course_date.set(course[4])

            else:
                msg.showerror("Course Not Found", "No course found with this ID")

        elif course_title:
            success, result = controller.find_by_title(course_title)
            if success and result:
                for course in result:
                    self.course_table.insert("", "end", values=(course[0], course[1], course[2], course[3], course[4]))

            else:
                msg.showerror("Course Not Found", "No course found with this title")

        elif course_date:
            success, result = controller.find_by_date(course_date)
            if success and result:
                for course in result:
                    self.course_table.insert("", "end", values=(course[0], course[1], course[2], course[3], course[4]))
            else:
                msg.showerror("Course Not Found", "No course found with this date")

        else:
            msg.showwarning("Search Input Required", "Please enter at least one field to search")

    def load_course(self):
        controller = CourseController()
        success, result = controller.find_all()

        if success:
            for row in self.course_table.get_children():
                self.course_table.delete(row)

            for course in result:
                self.course_table.insert('', 'end', values=course)

        else:
            msg.showerror("Load Error", f"Failed to load course data {result}")


    def table_select_course(self, event):
        selected_course = self.course_table.focus()

        if not selected_course:
            return

        values = self.course_table.item(selected_course)["values"]

        if values:
            self.course_id.set(values[0])
            self.course_teacher.set(values[1])
            self.course_title.set(values[2])
            self.course_unit.set(values[3])
            self.course_date.set(values[4])
