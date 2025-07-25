from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

from controller.teacher_controller import TeacherController
from model.entity.teacher import Teacher


class TeacherView:

    def save_teacher(self):
        pass

    def edit_teacher(self):
        pass

    def delete_teacher(self):
        pass

    def reset_teacher(self):
        pass

    def search_teacher(self):
        pass

    def load_teacher(self):
        pass

    def table_select_teacher(self, event):
        pass

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
            ).place(x=20, y=400)
      self.teacher_id = IntVar(value=0)
      Entry(teacher_window, textvariable=self.teacher_id, background="light blue", font=("Arial", 12)).place(x=135, y=400)

      # teacher name
      Label(teacher_window,
            text="teacher Name",
            background="light blue",
            font=("Arial", 12)
            ).place(x=20, y=450)
      self.name = StringVar()
      Entry(teacher_window, textvariable=self.name, background="light blue", font=("Arial", 12)).place(x=135, y=450)

      # teacher family
      Label(teacher_window,
            text="teacher family",
            background="light blue",
            font=("Arial", 12)
            ).place(x=20, y=500)
      self.family = StringVar()
      Entry(teacher_window, textvariable=self.family, background="light blue", font=("Arial", 12)).place(x=135, y=500)

      # teacher birthdate
      Label(teacher_window,
            text="teacher bday",
            background="light blue",
            font=("Arial", 12)
            ).place(x=20, y=550)
      self.birth_date = StringVar()
      Entry(teacher_window, textvariable=self.birth_date, background="light blue", font=("Arial", 12)).place(x=135, y=550)

      Label(teacher_window,
            text="Course",
            background="light blue",
            font=("Arial", 12)
            ).place(x=20, y=600)
      self.course = StringVar()
      Entry(teacher_window, textvariable=self.birth_date, background="light blue", font=("Arial", 12)).place(x=135, y=600)

      self.teacher_table = ttk.Treeview(teacher_window, columns=[1,2,3,4,5], show="headings", height=20)

      self.teacher_table.heading(1, text="teacher ID")
      self.teacher_table.heading(2, text="teacher Name")
      self.teacher_table.heading(3, text="teacher Family")
      self.teacher_table.heading(4, text="teacher Birthday")
      self.teacher_table.heading(5, text="Course")

      self.teacher_table.column(1, width=150, anchor="center")
      self.teacher_table.column(2, width=200, anchor="center")
      self.teacher_table.column(3, width=200, anchor="center")
      self.teacher_table.column(4, width=200, anchor="center")
      self.teacher_table.column(5, width=200, anchor="center")

      self.teacher_table.place(x=400, y=15, height=710)

      Button(teacher_window, text="Save", width=18, command=self.save_teacher).place(x=20, y=650)
      Button(teacher_window, text="edit", width=18, command=self.edit_teacher).place(x=180, y=650)
      Button(teacher_window, text="delete", width=18, command=self.delete_teacher).place(x=20, y=680)
      Button(teacher_window, text="clear", width=18, command=self.reset_teacher).place(x=180, y=680)
      Button(teacher_window, text="search", width=41, command=self.search_teacher).place(x=20, y=710)

      teacher_window.mainloop()
