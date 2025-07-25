from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk
from PyQt5.QtGui.QRawFont import familyName

from controller.student_controller import StudentController
from controller.course_controller import CourseController
from model.entity.student import Student
from model.tools.student_data_list import course_values


class StudentView:

    def save_student(self):
        student_id = self.student_id.get()
        name = self.name.get()
        family = self.family.get()
        birth_date = self.birth_date.get()
        selected_course = self.course.get()

        # student = Student(student_id,name,family,birth_date, )

    def edit_student(self):
        pass

    def delete_student(self):
        pass

    def reset_student(self):
        pass

    def search_student(self):
        pass

    def load_student(self):
        pass

    def table_select_student(self, event):
        pass

    def __init__(self):

      student_window = Tk()
      student_window.title("Student")
      student_window.geometry("1920x1920")
      student_window.config(cursor="hand2", background="light blue")

      img = Image.open("student_picture.png")
      photo = ImageTk.PhotoImage(img)
      my_label = Label(student_window, image=photo)
      my_label.image = photo
      my_label.pack()
      my_label.place(x=0, y=0)

      # student id
      Label(student_window,
            text="Student id",
            background="light blue",
            font=("Arial", 12)
            ).place(x=20, y=400)
      self.student_id = IntVar(value=0)
      Entry(student_window, textvariable=self.student_id, background="light blue", font=("Arial", 12)).place(x=135, y=400)

      # student name
      Label(student_window,
            text="Student Name",
            background="light blue",
            font=("Arial", 12)
            ).place(x=20, y=450)
      self.name = StringVar()
      Entry(student_window, textvariable=self.name, background="light blue", font=("Arial", 12)).place(x=135, y=450)

      # student family
      Label(student_window,
            text="Student family",
            background="light blue",
            font=("Arial", 12)
            ).place(x=20, y=500)
      self.family = StringVar()
      Entry(student_window, textvariable=self.family, background="light blue", font=("Arial", 12)).place(x=135, y=500)

      # student birthdate
      Label(student_window,
            text="Student bday",
            background="light blue",
            font=("Arial", 12)
            ).place(x=20, y=550)
      self.birth_date = StringVar()
      Entry(student_window, textvariable=self.birth_date, background="light blue", font=("Arial", 12)).place(x=135, y=550)

      Label(student_window,
            text="Course",
            background="light blue",
            font=("Arial", 12)
            ).place(x=20, y=600)
      self.course = StringVar()
      self.course_combobox = ttk.Combobox(student_window, textvariable=self.course, state="readonly",background="light blue", font=("Arial", 12))
      course_controller=CourseController()
      course_name = course_controller.get_all_course_names()
      self.course_combobox["values"] = course_name

      student_table = ttk.Treeview(student_window, columns=[1,2,3,4,5], show="headings", height=20)

      self.student_table.heading(1, text="Student ID")
      self.student_table.heading(2, text="Student Name")
      self.student_table.heading(3, text="Student Family")
      self.student_table.heading(4, text="Student Birthday")
      self.student_table.heading(5, text="Course")

      self.student_table.column(1, width=150, anchor="center")
      self.student_table.column(2, width=200, anchor="center")
      self.student_table.column(3, width=200, anchor="center")
      self.student_table.column(4, width=200, anchor="center")
      self.student_table.column(5, width=200, anchor="center")

      self.student_table.place(x=400, y=15, height=710)

      Button(student_window, text="Save", width=18, command=self.save_student).place(x=20, y=650)
      Button(student_window, text="edit", width=18, command=self.edit_student).place(x=180, y=650)
      Button(student_window, text="delete", width=18, command=self.delete_student).place(x=20, y=680)
      Button(student_window, text="clear", width=18, command=self.reset_student).place(x=180, y=680)
      Button(student_window, text="search", width=41, command=self.search_student).place(x=20, y=710)

      student_window.mainloop()
