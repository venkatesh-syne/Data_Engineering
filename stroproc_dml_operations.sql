delimiter $$

create procedure get_patient (
	in p_id	int
   )
begin
	select * from patients where patient_id = p_id;
end $$

delimiter ;

call get_patient(3);


DELIMITER $$

CREATE PROCEDURE manage_patients(
    IN p_action VARCHAR(10),
    IN p_patient_id INT,
    IN p_name VARCHAR(50),
    IN p_age INT,
    IN p_gender CHAR(1)
)
BEGIN

    DECLARE v_count INT DEFAULT 0;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SELECT 'Error occurred. Transaction rolled back' AS message;
    END;

    START TRANSACTION;

    SELECT COUNT(*) INTO v_count
    FROM patients
    WHERE patient_id = p_patient_id;

    IF p_action = 'INSERT' THEN
        IF v_count = 0 THEN
            INSERT INTO patients(patient_id, name, age, gender)
            VALUES (p_patient_id, p_name, p_age, p_gender);
            SELECT 'Insert successful' AS message;
        ELSE
            SELECT 'Patient already exists' AS message;
        END IF;

    ELSEIF p_action = 'UPDATE' THEN
        IF v_count > 0 THEN
            UPDATE patients
            SET name = p_name,
                age = p_age,
                gender = p_gender
            WHERE patient_id = p_patient_id;
            SELECT 'Update successful' AS message;
        ELSE
            SELECT 'Patient not found' AS message;
        END IF;

    ELSEIF p_action = 'DELETE' THEN
        IF v_count > 0 THEN
            DELETE FROM patients
            WHERE patient_id = p_patient_id;
            SELECT 'Delete successful' AS message;
        ELSE
            SELECT 'Patient not found' AS message;
        END IF;

    ELSEIF p_action = 'SELECT' THEN
        SELECT * FROM patients
        WHERE patient_id = p_patient_id;

    ELSE
        SELECT 'Invalid action' AS message;
    END IF;

    COMMIT;

END $$

DELIMITER ;

call manage_patients('INSERT',11,'venky',35,'M');
call manage_patients('UPDATE',9,'raj',27,'M');
call manage_patients('DELETE',9,NULL,NULL,NULL);
call manage_patients('SELECT',10,NULL,NULL,NULL);
select * from patients
















