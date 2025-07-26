from model.tools.validation import course_id_validator, course_title_validator, course_unit_validator, \
    course_date_validator, course_teacher_validator


class Course:
    def __init__(self, course_id, course_teacher, title, unit, course_date):
        self.course_id = course_id
        self.course_teacher = course_teacher
        self.title = title
        self.unit = unit
        self.course_date = course_date


    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return (self._course_id, self._course_teacher, self._title, self._unit, self._course_date)

    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        course_id_validator(value)
        self._course_id = value

    @property
    def course_teacher(self):
        return self._course_teacher

    @course_teacher.setter
    def course_teacher(self, value):
        course_teacher_validator(value)
        self._course_teacher = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        course_title_validator(value)
        self._title = value

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        course_unit_validator(value)
        self._unit = value

    @property
    def course_date(self):
        return self._course_date

    @course_date.setter
    def course_date(self, value):
        course_date_validator(value)
        self._course_date = value

