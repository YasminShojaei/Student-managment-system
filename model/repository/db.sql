--  student save
insert into students
(student_id, name, family, birth_date)
values
    (?, 'sogol', 'shojaei', 1376-02-25);


-- search / find student
select *
from students
where student_id = ?;

-- edit student
update students set student_id=?, name= ?, family=?, birth_date=?
where student_id = ?;


-- delete student
delete from students where student_id = ?;