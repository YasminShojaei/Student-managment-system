from model.entity.student import Student
from model.repository.student_reposity import StudentRepository


class StudentController:

    def save_student(self, student_id, name, family, birth_date, course_name):

        try:
            student = Student(student_id, name, family, birth_date, course_name)
            student_repo = StudentRepository()
            student_repo.save_student(student)
            return True, f"Student saved {student}"

        except Exception as e:
            return False, f"Error saving student {e}"

    def edit_student(self, student_id, name, family, birth_date, course_name):

        try:
            student = Student(student_id, name, family, birth_date, course_name)
            student_repo = StudentRepository()
            student_repo.edit_student(student)
            return True, f"Student edited {student}"

        except Exception as e:
            return False, f"Error editing student {e}"

    def delete_student(self, student_id):

        try:
            student_repo = StudentRepository()
            student_repo.delete_student(student_id)
            return True, f"Student removed {student_id}"

        except Exception as e:
            return False, f"Error removing student: {student_id} {e}"

    def find_all(self):

        try:
            student_repo = StudentRepository()
            return True, student_repo.find_all()

        except Exception as e:
            return False, f"Error finding all students {e}"

    def find_by_id(self, student_id):

        try:
            student_repo = StudentRepository()
            return True, student_repo.find_by_id(student_id)

        except Exception as e:
            return False, f"Error finding student by id {student_id} {e}"

    def find_by_name_family(self, name, family):

        try:
            student_repo = StudentRepository()
            return True, student_repo.find_by_name_family(name, family)

        except Exception as e:
            return False, f"Error finding student: {name}, {family} {e}"