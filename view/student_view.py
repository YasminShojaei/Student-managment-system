from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk
from patsy.state import center
from qtconsole.mainwindow import background

from controller.student_controller import StudentController
from model.entity.student import Student
from model.tools.student_data_list import course_values

#
# class StudentView:
#
#     def save_student(self):
#         pass
#
#     def edit_student(self):
#         pass
#
#     def delete_student(self):
#         pass
#
#     def reset_student(self):
#         pass
#
#     def search_student(self):
#         pass
#
#     def load_student(self):
#         pass
#
#     def table_select_student(self, event):
#         pass
#
#     def __init__(self):

student_window = Tk()
student_window.title("Student")
student_window.geometry("1920x1920")

img = Image.open("student_picture.png")
photo = ImageTk.PhotoImage(img)
my_lable = Label(student_window, image=photo)
my_lable.image = photo
my_lable.pack()
my_lable.place(x=0, y=0)

# student id
Label(student_window,
      text="Student id",
      background="light blue",
      font=("Arial", 12)
      ).place(x=20, y=400)
student_id = IntVar(value=0)
Entry(student_window, background="light blue", font=("Arial", 12), textvariable=student_id).place(x=135, y=400)

# student name
Label(student_window,
      text="Student Name",
      background="light blue",
      font=("Arial", 12)
      ).place(x=20, y=450)
student_name = StringVar()
Entry(student_window, background="light blue", font=("Arial", 12), textvariable=student_id).place(x=135, y=450)

# student family
Label(student_window,
      text="Student family",
      background="light blue",
      font=("Arial", 12)
      ).place(x=20, y=500)
student_family = StringVar()
Entry(student_window, background="light blue", font=("Arial", 12), textvariable=student_id).place(x=135, y=500)

# student birthdate
Label(student_window,
      text="Student bday",
      background="light blue",
      font=("Arial", 12)
      ).place(x=20, y=550)
student_bday = StringVar()
Entry(student_window, background="light blue", font=("Arial", 12), textvariable=student_id).place(x=135, y=550)

Label(student_window,
      text="Course",
      background="light blue",
      font=("Arial", 12)
      ).place(x=20, y=600)
student_course = StringVar()
ttk.Combobox(student_window, textvariable=student_course, state="readonly", values=course_values).place(x=135, y=600)
student_table = ttk.Treeview(student_window, columns=[1,2,3,4,5], show="headings", height=20)

student_table.heading(1, text="Student ID")
student_table.heading(2, text="Student Name")
student_table.heading(3, text="Student Family")
student_table.heading(4, text="Student Birthday")
student_table.heading(5, text="Course")

student_table.column(1, width=150, anchor="center")
student_table.column(2, width=200, anchor="center")
student_table.column(3, width=200, anchor="center")
student_table.column(4, width=200, anchor="center")
student_table.column(5, width=200, anchor="center")

student_table.place(x=400, y=15, height=710)

Button(student_window, text="Save", width=18).place(x=20, y=650)
Button(student_window, text="edit", width=18).place(x=180, y=650)
Button(student_window, text="delete", width=18).place(x=20, y=680)
Button(student_window, text="clear", width=18).place(x=180, y=680)
Button(student_window, text="search", width=41).place(x=20, y=710)






student_window.mainloop()
