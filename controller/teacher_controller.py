from model.entity.teacher import Teacher
from model.repository.teacher_repository import TeacherRepository


class TeacherController:

    def save_teacher(self, teacher_id, name, family, birth_date):

        try:
            teacher = Teacher(teacher_id, name, family, birth_date)
            teacher_repo = TeacherRepository()
            teacher_repo.save_teacher(teacher)
            return True, f"Teacher saved {teacher}"

        except Exception as e:
            return False, f"Error saving teacher {e}"

    def edit_teacher(self, teacher_id, name, family, birth_date):

        try:
            teacher = Teacher(teacher_id, name, family, birth_date)
            teacher_repo = TeacherRepository()
            teacher_repo.edit_teacher(teacher)
            return True, f"Teacher edited {teacher}"

        except Exception as e:
            return False, f"Error editing teacher {e}"

    def delete_teacher(self, teacher_id):

        try:
            teacher_repo = TeacherRepository()
            teacher_repo.delete_teacher(teacher_id)
            return True, f"Teacher removed {teacher_id}"

        except Exception as e:
            return False, f"Error removing teacher: {teacher_id} {e}"

    def find_all(self):

        try:
            teacher_repo = TeacherRepository()
            return True, teacher_repo.find_all()

        except Exception as e:
            return False, f"Error finding all teachers {e}"

    def find_by_id(self, teacher_id):

        try:
            teacher_repo = TeacherRepository()
            return True, teacher_repo.find_by_id(teacher_id)

        except Exception as e:
            return False, f"Error finding teacher by id {teacher_id} {e}"

    def find_by_name_family(self, name, family):

        try:
            teacher_repo = TeacherRepository()
            return True, teacher_repo.find_by_name_family(name, family)

        except Exception as e:
            return False, f"Error finding teacher: {name}, {family} {e}"

    def get_all_teachers_names(self):

        teacher_repo = TeacherRepository()
        return teacher_repo.get_all_teachers_names()