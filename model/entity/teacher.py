from numba.core.rvsdg_frontend.rvsdg.bc2rvsdg import propagate_stack

from model.tools.validation import *

class Teacher:
    def __init__(self, teacher_id, name, family, birth_date):
        self._teacher_id = teacher_id
        self._name = name
        self._family = family
        self._birth_date = birth_date

    def __repr__(self):
        return (self._teacher_id, self._name, self._family, self._birth_date)

    def to_tuple(self):
        return (self._teacher_id, self._name, self._family, self._birth_date)

    @property
    def teacher_id(self):
        return self._teacher_id

    @teacher_id.setter
    def teacher_id(self, value):
        teacher_name_validator(value)
        self._teacher_id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        teacher_name_validator(value)
        self._name = value

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, value):
        teacher_family_validator(value)
        self._family = value

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        teacher_birth_date_validator(value)
        self._birth_date = value
