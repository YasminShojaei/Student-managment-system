import sqlite3

from controller.teacher_controller import TeacherController
from model.entity.teacher import Teacher
from model.repository.teacher_repository import TeacherRepository
#
# # test passed
teacher_1 = Teacher(1355, "ali", "majidi", "1355-09-22")
# print(teacher_1.to_tuple())
# print(teacher_1.__repr__())
#
teacher_repo = TeacherRepository()
#
# test passed
# teacher_repo.save_teacher(teacher_1)
# teacher_controller = TeacherController()
# status, message = (teacher_controller.save_teacher(1357, "yas", "mirza", "1357-09-22"))
# print(status, message)
#
# test passed
# teacher_repo.edit_teacher(teacher_1)
# teacher_controller = TeacherController()
# status, message = teacher_controller.edit_teacher(2233, "yasaman", "yasai", "1357-02-02")
# print(status, message)

# test passed
# teacher_repo.delete_teacher(1377)
# teacher_controller = TeacherController()
# status, message = teacher_controller.delete_teacher(1342)
# print(status, message)

#
#
# test passed
# print(teacher_repo.find_all())
# teacher_controller = TeacherController()
# status, message = teacher_controller.find_all()
# print(status, message)

#
# test passed
# print(teacher_repo.find_by_id(1366))
# teacher_controller = TeacherController()
# status, message = teacher_controller.find_by_id(1366)
# print(status, message)

#
# test passed
# print(teacher_repo.find_by_name_family("Reza", "rezai"))
# teacher_controller = TeacherController()
# status, message = teacher_controller.find_by_name_family("yasaman", "mirzai")
# print(status, message)

