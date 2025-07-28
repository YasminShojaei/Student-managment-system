from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

from controller.teacher_controller import TeacherController
from tkinter import messagebox as msg


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

        self.teacher_table = ttk.Treeview(teacher_window, columns=[1,2,3,4], show="headings", height=20)

        self.teacher_table.heading(1, text="teacher ID")
        self.teacher_table.heading(2, text="teacher Name")
        self.teacher_table.heading(3, text="teacher Family")
        self.teacher_table.heading(4, text="teacher Birthday")



        self.teacher_table.column(1, width=200, anchor="center")
        self.teacher_table.column(2, width=250, anchor="center")
        self.teacher_table.column(3, width=250, anchor="center")
        self.teacher_table.column(4, width=200, anchor="center")




        self.teacher_table.place(x=400, y=15, height=700)

        self.teacher_table.bind("<<TreeviewSelect>>", self.table_select_teacher)

        Button(teacher_window, text="Save", width=18, command=self.save_teacher).place(x=20, y=630)
        Button(teacher_window, text="edit", width=18, command=self.edit_teacher).place(x=180, y=630)
        Button(teacher_window, text="delete", width=18, command=self.delete_teacher).place(x=20, y=660)
        Button(teacher_window, text="clear", width=18, command=self.reset_teacher).place(x=180, y=660)
        Button(teacher_window, text="search", width=41, command=self.search_teacher).place(x=20, y=690)

        teacher_window.mainloop()


    def save_teacher(self):
        teacher_id = self.teacher_id.get()
        name = self.name.get()
        family = self.family.get()
        birth_date = self.birth_date.get()

        t_controller = TeacherController()
        result, message = t_controller.save_teacher(teacher_id, name, family, birth_date)

        if result:
            msg.showinfo("Teacher saved", message)
            self.load_teacher()
            self.reset_teacher()

        else:
            msg.showerror("Teacher not saved", message)


    def edit_teacher(self):
        teacher_id = self.teacher_id.get()
        name = self.name.get()
        family = self.family.get()
        birth_date = self.birth_date.get()

        controller = TeacherController()
        result, message = controller.edit_teacher(teacher_id, name, family, birth_date)
        if result:
            msg.showinfo("Teacher edited", message)
            self.load_teacher()
            self.reset_teacher()
        else:
            msg.showerror("Teacher not saved", message)

    def delete_teacher(self):
        teacher_id = self.teacher_id.get()

        if not teacher_id:
            msg.showerror("Error, please select a teacher id to delete")
            return

        controller = TeacherController()
        result, message = controller.delete_teacher(teacher_id)

        if result:
            msg.showinfo("Teacher deleted", message)
            self.load_teacher()
            self.reset_teacher()

        else:
            msg.showerror("Teacher not deleted", message)
    def reset_teacher(self):
        self.teacher_id.set(0)
        self.name.set("")
        self.family.set("")
        self.birth_date.set("")

    def search_teacher(self):
        teacher_id = self.teacher_id.get()
        name = self.name.get().strip()
        family = self.family.get().strip()

        controller = TeacherController()

        for row in self.teacher_table.get_children():
            self.teacher_table.delete(row)

        if teacher_id:
            success, result = controller.find_by_id(teacher_id)
            if success:
                self.reset_teacher()
                teacher = result
                self.teacher_table.insert("", "end", values=(teacher[0], teacher[1], teacher[2], teacher[3]))

                self.teacher_id.set(teacher[0])
                self.name.set(teacher[1])
                self.family.set(teacher[2])
                self.birth_date.set(teacher[3])

            else:
                msg.showerror("Teacher Not Found", "No teacher found with this ID")

        elif name or family:
            success, result = controller.find_by_name_family(name, family)
            if success and result:
                for teacher in result:
                    self.teacher_table.insert("", "end", values=(teacher[0], teacher[1], teacher[2], teacher[3]))

            else:
                msg.showerror("No Results", "No teachers matched your search")
        else:
            msg.showwarning("Missing Input", "Please enter ID or name/family to search")

    def load_teacher(self):
        controller = TeacherController()
        success, result = controller.find_all()

        if success:
            for row in self.teacher_table.get_children():
                self.teacher_table.delete(row)

            for teacher in result:
                self.teacher_table.insert('', 'end', values=teacher)

        else:
            msg.showerror("Load Error", f"Failed to load teacher data {result}")


    def table_select_teacher(self, event):
        selected_teacher = self.teacher_table.focus()

        if not selected_teacher:
            return

        values = self.teacher_table.item(selected_teacher)["values"]

        if values:
            self.teacher_id.set(values[0])
            self.name.set(values[1])
            self.family.set(values[2])
            self.birth_date.set(values[3])