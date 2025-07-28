from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

from controller.student_controller import StudentController
from controller.course_controller import CourseController
from tkinter import messagebox as msg

class StudentView:
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

      self.course_combobox = ttk.Combobox(student_window,
                                          textvariable=self.course,
                                          state="readonly",
                                          font=("Arial", 12))

      course_controller = CourseController()
      course_names = course_controller.get_all_course_names()

      self.course_combobox["values"] = course_names

      if course_names:
          self.course_combobox.current(0)

      self.course_combobox.place(x=135, y=600, width=200)

      self.student_table = ttk.Treeview(student_window, columns=[1,2,3,4,5], show="headings", height=20)

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

      self.student_table.bind("<<TreeviewSelect>>", self.table_select_student)

      Button(student_window, text="Save", width=18, command=self.save_student).place(x=20, y=650)
      Button(student_window, text="edit", width=18, command=self.edit_student).place(x=180, y=650)
      Button(student_window, text="delete", width=18, command=self.delete_student).place(x=20, y=680)
      Button(student_window, text="clear", width=18, command=self.reset_student).place(x=180, y=680)
      Button(student_window, text="search", width=41, command=self.search_student).place(x=20, y=710)

      student_window.mainloop()


    def save_student(self):
        student_id = self.student_id.get()
        name = self.name.get()
        family = self.family.get()
        birth_date = self.birth_date.get()
        selected_course = self.course.get()

        controller = StudentController()
        result, message = controller.save_student(student_id, name, family, birth_date, selected_course)
        if result:
            msg.showinfo("Student Saved", message)
            self.load_student()
            self.reset_student()
        else:
            msg.showerror("Student Not Saved", message)

    def edit_student(self):
        student_id = self.student_id.get()
        name = self.name.get()
        family = self.family.get()
        birth_date = self.birth_date.get()
        selected_course = self.course.get()
        controller = StudentController()
        result, message = controller.edit_student(student_id, name, family, birth_date, selected_course)
        if result:
            msg.showinfo("Student Edited", message)
            self.load_student()
            self.reset_student()
        else:
            msg.showerror("Student Not Edited", message)

    def delete_student(self):
        student_id = self.student_id.get()

        if not student_id:
            msg.showerror("Error, please select a student id to delete")
            return

        controller = StudentController()
        result, message = controller.delete_student(student_id)

        if result:
            msg.showinfo("Student Deleted", message)
            self.load_student()
            self.reset_student()

        else:
            msg.showerror("Student Not Deleted", message)

    def reset_student(self):
        self.student_id.set(0)
        self.name.set("")
        self.family.set("")
        self.birth_date.set("")
        self.course.set("")
        self.student_table.selection_remove(self.student_table.selection())

    def search_student(self):
        student_id = self.student_id.get()
        name = self.name.get().strip()
        family = self.family.get().strip()

        controller = StudentController()

        for row in self.student_table.get_children():
            self.student_table.delete(row)

        if student_id:
            success, result = controller.find_by_id(student_id)
            if success:
                self.reset_student()
                student = result
                self.student_table.insert("", "end",
                                          values=(student[0], student[1], student[2], student[3], student[4]))

                self.student_id.set(student[0])
                self.name.set(student[1])
                self.family.set(student[2])
                self.birth_date.set(student[3])
                self.course.set(student[4])
            else:
                msg.showerror("Student Not Found", "No student found with this ID")

        elif name or family:
            success, result = controller.find_by_name_family(name, family)
            if success and result:
                for student in result:
                    self.student_table.insert("", "end",
                                              values=(student[0], student[1], student[2], student[3], student[4]))
            else:
                msg.showerror("No Results", "No students matched your search")
        else:
            msg.showwarning("Missing Input", "Please enter ID or name/family to search")

    def load_student(self):
        controller = StudentController()
        success, result = controller.find_all()

        if success:
            for row in self.student_table.get_children():
                self.student_table.delete(row)

            for student in result:
                self.student_table.insert("", "end", values=student)

        else:
            msg.showerror("Load Error", f"Error loading student {result}")

    def table_select_student(self, event):
        selected_item = self.student_table.focus()

        if not selected_item:
            return

        values = self.student_table.item(selected_item)["values"]

        if values:
            self.student_id.set(values[0])
            self.name.set(values[1])
            self.family.set(values[2])
            self.birth_date.set(values[3])
            self.course.set(values[4])

