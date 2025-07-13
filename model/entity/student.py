from model.tools.validation import *


class Student:
    def __init__(self, student_id, name, family, birth_date):
        self.student_id = student_id
        self.name = name
        self.family = family
        self.birth_date = birth_date

    def __repr__(self):
        return (self._student_id, self._name, self._family, self._birth_date)

    def to_tuple(self):
        return (self._student_id, self._name, self._family, self._birth_date)


    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        student_id_validator (value)
        self._student_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        student_name_validator (value)
        self._name = value

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, value):
        student_family_validator (value)
        self._family = value

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        student_birth_date_validator (value)
        self._birth_date = value