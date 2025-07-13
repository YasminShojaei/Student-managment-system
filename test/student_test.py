from model.entity.student import Student

student_1 = Student(1, "yasmin", "Shojaei", "2002-02-22")
print(student_1.to_tuple())
print(student_1.__repr__())