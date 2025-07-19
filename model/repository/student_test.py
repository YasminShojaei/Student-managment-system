from model.entity.student import Student
from model.repository.student_reposity import StudentRepository

# test passed
student_1 = Student(1380, "yasmin", "shojaei", "1380-02-12")
print(student_1.to_tuple())
print(student_1.__repr__())

# test passed
# student_repo = StudentRepository()
# student_repo.save_student(student_1)

# test passed
# student_repo = StudentRepository()
# student_repo.edit_student(student_1)

# test passed
# student_repo = StudentRepository()
# student_repo.delete_student(2005)

# test passed
# student_repo = StudentRepository()
# print(student_repo.find_all())

# test passed
# student_repo = StudentRepository()
# print(student_repo.find_by_id(1379))

# test passed
# student_repo = StudentRepository()
# print(student_repo.find_by_name_family("yasmin", "shojaei"))


