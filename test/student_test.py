from model.entity.student import Student
from model.repository.student_reposity import StudentRepository


student_1 = Student(4, "mahsa", "rezai", "2001-02-22")
print(student_1.to_tuple())
print(student_1.__repr__())

student_repo = StudentRepository()
student_repo.save_student(student_1)