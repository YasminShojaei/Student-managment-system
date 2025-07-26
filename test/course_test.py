import sqlite3
#
from controller.course_controller import CourseController
from model.entity.course import Course
from model.repository.course_repository import CourseRepository
#
# # test passed
# course_1 = Course(2525, "Ahmad Mesbah", "python", 5, "1404-06-06 14:30")
# print(course_1.to_tuple())
# print(course_1.__repr__())
#
course_repo = CourseRepository()
#
# test passed
# # course_repo.save_course(course_1)
# course_controller = CourseController()
# status, message = course_controller.save_course(2345, "Ali jalali", "English", 2, "1404-07-01 08:30")
# print(status, message)


from controller.course_controller import CourseController
import os
#
# print("Current working directory:", os.getcwd())
# print("File exists:", os.path.exists("model/repository/university_db.sqlite"))
# print("Current working directory:", os.getcwd())
#
# course_controller = CourseController()
# status, message = course_controller.save_course(2345, "Ali jalali", "English", 2, "1404-07-01 08:30")
# print(status, message)


# test passed
# course_repo.edit_course(course_1)
# course_controller = CourseController()
# status, message = course_controller.edit_course(5599, "Reza rezai", "python", 5, "1404-07-09 14:30")
# print(status, message)
#
# test passed
# course_repo.delete_course(2525)
# course_controller = CourseController()
# status, message = course_controller.delete_course(2525)
# print(status, message)
#
#
#
# test passed
# print(course_repo.find_all())
# course_controller = CourseController()
# status, message = course_controller.find_all()
# print(status, message)
#
#
# test passed
# print(course_repo.find_by_id(3359))
# course_controller = CourseController()
# status, message = course_controller.find_by_id(3359)
# print(status, message)
#
# print(course_repo.find_by_date("1404-09-06, 15:30"))
# course_controller = CourseController()
# status, message = course_controller.find_by_date("1404-09-06 15:30")
# print(status, message)
#
#
# test passed
# print(course_repo.find_by_title("java"))
course_controller = CourseController()
status, message = course_controller.find_by_title("java")
print(status, message)
#
