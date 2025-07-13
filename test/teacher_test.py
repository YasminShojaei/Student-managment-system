from model.entity.teacher import Teacher

teacher_1 = Teacher(1, "Ahmadali", "mesbah", "1995-01-01")
print(teacher_1.to_tuple())
print(teacher_1.__repr__())