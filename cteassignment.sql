
--Second Highest Salary per Department
WITH second_high AS (
    SELECT dept_id,name,salary,DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rnk
    FROM emp
)
SELECT dept_id, name, salary
FROM second_high
WHERE rnk = 2;

--Top 2 Highest-Paid Employees in Each Department
WITH high_pay_emp AS (
    SELECT dept_id,name,salary,DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rnk
    FROM emp
)
SELECT dept_id, name, salary
FROM high_pay_emp
WHERE rnk <= 2;

--Salary Increased Compared to Previous Employee
WITH sal_compare AS (
    SELECT dept_id,name,salary,joining_date,
    LAG(salary) OVER (PARTITION BY dept_id ORDER BY joining_date) AS prev_salary
    FROM emp
)
SELECT *
FROM sal_compare
WHERE salary > prev_salary;

--Employee + Department Name
WITH emp_dept AS (
    SELECT e.emp_id,e.name,e.salary,d.dept_name
    FROM emp e
    JOIN dept d
    ON e.dept_id = d.dept_id
)
SELECT *
FROM emp_dept;


--Top Sales Employee
   --Need to understand the requirement.
--Latest Employee per Department
WITH latest_emp AS (
    SELECT 
        dept_id,name,joining_date,
        ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY joining_date DESC) AS rn
    FROM emp
)
SELECT dept_id, name, joining_date
FROM latest_emp
WHERE rn = 1;

--window functions assignment
-- Find consecutive duplicate values ? hint(using lag)
SELECT *
FROM (
    SELECT emp_id,name,dept_id,salary,
        LAG(salary) OVER (PARTITION BY dept_id ORDER BY emp_id) AS prev_salary
    FROM employee
) dept_data
WHERE salary = prev_salary;

-- Running total of salary

SELECT emp_id,name,dept_id,salary,
    SUM(salary) OVER (ORDER BY emp_id) AS running_total
FROM employee;

-- Find employees earning more than department average

SELECT *
FROM (
    SELECT emp_id,name,dept_id,salary,
        AVG(salary) OVER (PARTITION BY dept_id) AS dept_avg
    FROM employee
) dept_data
WHERE salary > dept_avg;


-- Find department earning less than department average
SELECT *
FROM (
    SELECT emp_id,name,dept_id,salary,
        AVG(salary) OVER (PARTITION BY dept_id) AS dept_avg
    FROM employee
) dept_data
WHERE salary < dept_avg;