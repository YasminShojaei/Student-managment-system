import sqlite3

from controller.student_controller import StudentController
from model.entity.student import Student
from model.repository.student_reposity import StudentRepository

# test passed
# student_1 = Student(1366, "arash", "arad", "1366-06-06", "java")
# print(student_1.to_tuple())
# print(student_1.__repr__())

# student_repo = StudentRepository()

# test passe
#
# controller = StudentController()
# status, message = controller.save_student(13, "yegane", "sanjari", "1389-10-10", "java")
# print(status, message)


# test passed
# student_repo.edit_student(student_1)
# student_controller = StudentController()
# status, message = student_controller.edit_student(1343, "alireza", "mohamadi", "1343-01-01", "java")
# print(status, message)

# test passed
# student_repo.delete_student(2005)
# student_controller = StudentController()
# status, message = student_controller.delete_student(13)
# print(status, message)



# test passed
# print(student_repo.find_all())
student_controller = StudentController()
status, message = student_controller.find_all()
print(status, message)


# test passed
# print(student_repo.find_by_id(1379))
# student_controller = StudentController()
# status, message = student_controller.find_by_id(1380)
# print(status, message)


# test passed
# print(student_repo.find_by_name_family("yasmin", "shojaei"))
# student_controller = StudentController()
# status, message = student_controller.find_by_name_family("yasmin", "shojaei")
# print(status, message)

