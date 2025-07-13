import re
from datetime import datetime


def student_id_validator(student_id):
    pass

def student_name_validator(student_name):
    if not (type(student_name) == str and re.match("[A-Za-z]{3,30}", student_name)):
        raise ValueError("Student name must contain only letters - (3-30)")

def student_family_validator(student_family):
    if not (type(student_family) == str and re.match("[A-Za-z]{3,30}", student_family)):
        raise ValueError("Student family name must contain only letters - (3-30)")

def student_birth_date_validator(student_birth_date):
    try:
        if type(student_birth_date) == str:
            datetime.strptime(student_birth_date, "%Y-%m-%d")
        elif type(student_birth_date) == datetime:
            pass

    except Exception as e:
        print(f"{e} not a valid date")
