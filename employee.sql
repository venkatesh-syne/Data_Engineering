‎
create table employee(
emp_id int,
name varchar(50),
dept_id int,
salary int
);
insert into employee values
(8,'Ramesh', 102, NULL),
(2,'sara', 101, 60000),
(3,'John', 102, 55000),
(4,'Priya', 102, 45000),
(5,'Ravi', 101, 70000);
 
 SELECT * FROM employee
 
SELECT *
FROM (
    SELECT 
	emp_id,
	name,
	dept_id,
	LAG(dept_id) OVER (ORDER BY emp_id) AS dept
    FROM employee
) t
WHERE dept_id = dept;




SELECT 
emp_id,
name,
salary,
SUM(salary) OVER (ORDER BY emp_id) AS total
FROM employee;


SELECT *
FROM (
SELECT 
emp_id,
name,
dept_id,
salary,
AVG(salary) OVER (PARTITION BY dept_id) AS deptavg
FROM employee
) t
WHERE salary > deptavg;