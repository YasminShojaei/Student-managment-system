from model.entity.course import Course

course_1 = Course(1234, "Mesbah", "python", 3, "2025-08-08 14:30")
print(course_1.to_tuple())
print(course_1.__repr__())
