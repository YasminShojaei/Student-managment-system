import re
from datetime import datetime


def student_id_validator(student_id):
    if not (type(student_id) == int):
        raise TypeError("Student ID must be an integer")

def student_name_validator(student_name):
    if not (type(student_name) == str and re.fullmatch("[A-Za-z]{3,30}", student_name)):
        raise ValueError("Student name must contain only letters - (3-30)")

def student_family_validator(student_family):
    if not (type(student_family) == str and re.fullmatch("[A-Za-z]{3,30}", student_family)):
        raise ValueError("Student family name must contain only letters - (3-30)")

def student_birth_date_validator(student_birth_date):
    try:
        if type(student_birth_date) == str:
            datetime.strptime(student_birth_date, "%Y-%m-%d")
        elif type(student_birth_date) == datetime:
            pass

    except Exception as e:
        print(f"{e} not a valid date")

def teacher_id_validator(teacher_id):
    if not (type(teacher_id) == int):
        raise TypeError("Teacher ID must be an integer")

def teacher_name_validator(teacher_name):
    teacher_name = teacher_name.strip()
    if not (type(teacher_name) == str and re.fullmatch(r"[A-Za-z\s]{3,30}", teacher_name)):
        raise ValueError("Teacher name must contain only letters - (3-30)")

def teacher_family_validator(teacher_family):
    if not (type(teacher_family) == str and re.fullmatch(r"[A-Za-z\s]{3,30}", teacher_family)):
        raise ValueError("Teacher family name must contain only letters - (3-30)")

def teacher_birth_date_validator(teacher_birth_date):
    try:
        if type(teacher_birth_date) == str:
            datetime.strptime(teacher_birth_date, "%Y-%m-%d")
        elif type(teacher_birth_date) == datetime:
            pass

    except Exception as e:
        print(f"{e} not a valid date")

def course_id_validator(course_id):
    if not (type(course_id) == int and 1000 <= course_id <= 9999):
        raise ValueError("Course ID must be a 4-digit number between 1000 and 9999")

def course_teacher_validator(course_teacher):
    if not (type(course_teacher) == str and re.fullmatch(r"[A-Za-z\s]{3,40}", course_teacher)):
        raise ValueError("Course teacher name must contain only letters - (3-30)")

def course_title_validator(course_title):
    if not (type(course_title) == str and re.fullmatch("[A-Za-z]{3,20}", course_title)):
        raise ValueError("Course title must contain only letters - (3-20)")

def course_unit_validator(course_unit):
    if not (type(course_unit) == int and 2 <= course_unit <= 5 ):
        raise ValueError("Course unit must be between 2 and 5")

def course_date_validator(course_date):
    try:
        if type(course_date) == str:
            datetime.strptime(course_date, "%Y-%m-%d %H:%M")
        elif type(course_date) == datetime:
            pass
    except Exception as e:
        print(f"{e} not a valid date and time (example: 2025-07-14 14:30)")


