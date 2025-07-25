INSERT INTO students
(student_id, name, family, birth_date, course_name)
VALUES
(1001, 'sogol', 'shojaei', '1376-02-25', 'Python');

SELECT *
FROM students
WHERE student_id = 1001;

UPDATE students
SET student_id = 1001,
    name = 'sogol',
    family = 'shojaei',
    birth_date = '1376-02-25',
    course_name = 'Python'
WHERE student_id = 1001;

DELETE FROM students
WHERE student_id = 1001;

SELECT * FROM students;
