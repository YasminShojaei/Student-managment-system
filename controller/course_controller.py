from model.entity.course import Course
from model.repository.course_repository import CourseRepository


class CourseController:
    def save_course(self, course_id, course_teacher, title, unit, course_date):
        try:
            course = Course(course_id, course_teacher, title, unit, course_date)
            course_repo = CourseRepository()
            course_repo.save_course(course)
            return True, f" course saved {course}"
        except Exception as e:
            return False, f"Error saving course {e}"

    def edit_course(self, course_id, course_teacher, title, unit, course_date):
        try:
            course = Course(course_id, course_teacher, title, unit, course_date)
            course_repo = CourseRepository()
            course_repo.edit_course(course)
            return True, f" course edited {course}"
        except Exception as e:
            return False, f"Error editing course {e}"

    def delete_course(self, course_id):
        try:
            course_repo = CourseRepository()
            course_repo.delete_course(course_id)
            return True, f" course removed {course_id}"
        except Exception as e:
            return False, f"Error removing course: {course_id} {e}"

    def find_all(self):
        try:
            course_repo = CourseRepository()
            return True, course_repo.find_all()
        except Exception as e:
            return False, f"Error finding all courses {e}"

    def find_by_id(self, course_id):
        try:
            course_repo = CourseRepository()
            return True, course_repo.find_by_id(course_id)
        except Exception as e:
            return False, f"Error finding course by id {course_id} {e}"

    def find_by_date(self, course_date):
        try:
            course_repo = CourseRepository()
            return True, course_repo.find_by_date(course_date)
        except Exception as e:
            return False, f"Error finding course by date {course_date} {e}"

    def find_by_title(self, title):
        try:
            course_repo = CourseRepository()
            return True, course_repo.find_by_title(title)
        except Exception as e:
            return False, f"Error finding course {title} {e}"