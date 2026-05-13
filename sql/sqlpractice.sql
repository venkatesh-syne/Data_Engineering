create database practice
use practice;
create table retail_store
(
   product_id int,
   product_name varchar(50),
   price decimal(5,2)   
);
desc retail_store
select * from retail_store
insert into retail_store values(101,'dal',20.50);
insert into retail_store values(102,'soya',15.50);
insert into retail_store values(103,'maida',10.50);
insert into retail_store values(105,'jagerry',40.50),(106,'jeera',10.50),(107,'curd',60.50);
insert into retail_store (product_id,product_name) values (104,'sugar');

--DELETE is a targeted row-by-row operation used for specific data removal, 
--while TRUNCATE is a high-performance command used to wipe all data from a table

update retail_store set price=24.50 where product_id = 104

delete from retail_store where product_name='jagerry';

delete from retail_store

alter table retail_store modify column product_name varchar(40);
alter table retail_store add column address varchar(30);

ALTER TABLE retail_store RENAME TO retail_stores;
RENAME TABLE retail_stores TO retail_store;

alter table retail_store drop address
drop table retail_store 
truncate table retail_store

create table employees
(
   EmployeeID INT,
   Name VARCHAR (50), 
   Department VARCHAR(50), 
   Salary DECIMAL(7,2), 
   City VARCHAR(20)
);
select * from employees

-- 1. INSERT Operations (Adding Data):

-- Single Row: Add a new employee with EmployeeID = 201, Name = 'venkat', Department = 'IT', and Salary = 45000.

insert into employees values(201,'venkat','IT',50000,'hyderabad')

-- Multiple Rows: In one statement, insert two new products into a Products table with ProductID, ProductName, and Price.

insert into employees values(202,'preethi','HR',45000,'Hyderabad'),(203,'nehan','Finance',35000,'Pune')

-- Partial Columns: Insert a new record into a Students table specifying only Name and Age, allowing other columns to 
take their default values.

insert into employees (EmployeeID,Name,salary,City) values(204,'sathvik',40000,'mumbai')

-- 2. UPDATE Operations (Modifying Data)
-- Conditional Update: Increase the salary of all employees in the 'Sales' department by 10%.

update employees set salary = salary * 1.10 where department= 'HR'

-- Multiple Fields: For a specific record (e.g., EmployeeID = 3), change the LastName to 'Drexler' and 
-- set their Salary to 1000.

update employees set Name='venkatesh' , salary = 65000 where employeeid=201

-- Mass Update: Change the salary to 90000 for all employees where the current empID is 201.

insert into employees values(201,'rajesh','IT',40000,'Pune')

update employees set salary = 90000 where EmployeeID=201


-- Nullify Data: Use an UPDATE statement to set a specific field to NULL for a subset of records (if the column allows nulls).

select * from employees

update employees set Department = NULL where EmployeeID=202

-- 3. DELETE Operations (Removing Data) 
-- Single Record: Remove the record for the employee whose EmployeeID is 204.

  delete from employees where employeeid = 204

-- Conditional Delete: Delete all employees from the employees table where the salary is less than 50000.

delete from employees where salary < 50000 

-- Date-Based Delete: Delete all student records from a Students table whose AdmissionDate was before '2023-01-01'.

DELETE FROM Students WHERE AdmissionDate < '2023-01-01';

-- All Rows: Write a command to delete all rows from a table while keeping the table structure intact.

delete from employees