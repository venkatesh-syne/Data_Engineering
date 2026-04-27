create table emp(
empid int,
name varchar(50),
email varchar(50),
city varchar(20),
department varchar(10)
);
insert into emp values(101,'venkat','venkat@gmail.com','HYD','IT'),(102,'venky','venkat@gmail.com','Pune','HR');
insert into emp values(103,'raghav','raghav@gmail.com','mumbai','Finance'),(104,'venkatesh','venaktesh@gmail.com','HYD','Admin');
insert into emp values(105,'preethi','preethi@gmail.com','delhi','IT'),(106,'nehan','nehan@gmail.com','pune','sales');
insert into emp values(107,'lavanya','lavanya@gmail.com','delhi','IT'),(108,'lavanya','lavanya@gmail.com','delhi','IT');
select * from emp
insert into emp (empid,name,email,city) values(102,'shyam','shyam@gmail.com','noida')
update emp set salary = 5000 where empid=101;
update emp set salary = 4000 where empid=102;
update emp set salary = 4500 where empid=103;
update emp set salary = 6000 where empid=104;
update emp set salary = 8500 where empid=105;
update emp set salary = 3000 where empid=106;
update emp set salary = 9500 where empid=107;
alter table emp add column salary decimal(6,2);

select name,email,department,city,count(*) 
from emp 
group by name,email,department,city
having count(*) > 1;

DELETE e1
FROM emp e1
JOIN emp e2
ON e1.email = e2.email
AND e1.empid > e2.empid;

select max(salary) as second_Highest
from emp 
where salary < (select max(salary) from emp)



SELECT DISTINCT salary
FROM emp
ORDER BY salary DESC
LIMIT 2,1;

create table emp1(
empid int,
name varchar(50),
department_id int
);
select * from emp
insert into emp1 values(101,'venkat',201),(102,'preethi',202),(103,'nehan',201),(104,'lavanya',202);
select * from emp1
delete from emp1;
create table department(
department_id int,
department_name varchar(12)
);
INSERT INTO emp1 VALUES (105,'Ravi',999);
insert into department values(201,'sales'),(202,'IT'),(203,'HR');
select * from department
update emp1 set department_id = NULL where empid = 102;

SELECT e.*
FROM emp1 e
LEFT JOIN department d
ON e.department_id = d.department_id
-- WHERE d.department_id IS NULL;

CREATE TABLE product (
product_id INT PRIMARY KEY,
product_name VARCHAR(50),
category VARCHAR(30),
price DECIMAL(10,2),
stock_quantity INT
);

INSERT INTO product VALUES
(101,'Laptop','Electronics',55000,10),
(102,'Mouse','Electronics',500,50),
(103,'Shirt','Clothing',1200,30),
(104,'Mobile','Electronics',25000,15),
(105,'Shoes','Footwear',3000,20);

select * from product



select sum(price * stock_quantity) as total_revenue from product;
select product_name,price * stock_quantity as total_revenue from product;

SELECT category, sum(price * stock_quantity) AS total_revenue
FROM product
GROUP BY category;


select * from emp order by salary DESC limit 3
select max(salary) from emp


select max(salary) as second_Highest 
from emp
where salary < (select max(salary) from emp)

select max(salary) as second_Highest
from emp 
where salary < (select max(salary) from emp)

CREATE TABLE customer (
order_id INT,
customer_id INT,
product_name VARCHAR(50),
amount DECIMAL(10,2),
order_date DATE
);

INSERT INTO customer VALUES
(1, 101, 'Laptop', 55000, '2024-01-10'),
(2, 102, 'Mouse', 500, '2024-01-11'),
(3, 103, 'Phone', 25000, '2024-01-12'),
(4, 104, 'Shoes', 3000, '2024-01-13'),
(5, 101, 'Keyboard', 1500, '2024-01-14');
select * from customer

CREATE TABLE returns (
return_id INT,
customer_id INT,
order_id INT,
return_reason VARCHAR(100),
return_date DATE
);
INSERT INTO returns VALUES
(1, 102, 2, 'Defective', '2024-01-15'),
(2, 103, 3, 'Not needed', '2024-01-16');
select * from returns



SELECT DISTINCT c.customer_id
FROM customer c
LEFT JOIN returns r
ON c.customer_id = r.customer_id
WHERE r.customer_id IS NULL;

SELECT DISTINCT c.customer_id
FROM customer c
JOIN returns o
ON c.customer_id = o.customer_id
WHERE c.customer_id NOT IN (
    SELECT customer_id
    FROM returns
);


select * from customer
select * from emp1
select customer_id, count(*) as order_count
from customer
group by customer_id


select * from emp where year(hire_date) = 2023

select customer_id, avg(amount) as avg_amount_value
from customer
group by customer_id
select * from product
select * from returns

select customer_id,max(order_date) as latest_order from customer group by customer_id


CREATE TABLE sales (
sale_id INT PRIMARY KEY,
product_id INT,
quantity INT,
sale_date DATE
);

INSERT INTO sales VALUES
(1,101,2,'2024-01-10'),
(2,103,1,'2024-01-11'),
(3,101,1,'2024-01-12'),
(4,105,3,'2024-01-13');

select * from sales

SELECT p.*
FROM product p
LEFT JOIN sales s
ON p.product_id = s.product_id
WHERE s.product_id IS NULL;

SELECT *
FROM product
WHERE product_id NOT IN (
    SELECT product_id FROM sales
);