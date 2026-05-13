insert into patients (patient_id,name,age,gender) values(1,"raj",26,"male")
use hospital
delimiter $$

create procedure insert_patient (
	in p_id	int,
    in p_name varchar(20),
    in p_age int,
    in p_gender varchar(10)
)
begin
	insert into patients (patient_id,name,age,gender) values(p_id,p_name,p_age,p_gender);
end $$

delimiter ;

call insert_patient (9,"raj",27,"male");
call insert_patient (10,"sandy",28,"F");

select * from patients