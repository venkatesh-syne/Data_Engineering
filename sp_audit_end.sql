CREATE OR REPLACE PROCEDURE `scenic-kiln-351104.audit.sp_audit_end`
BEGIN

DECLARE v_source_count INT64;
DECLARE v_target_count INT64;

set v_source_count = (
  SELECT COUNT(*)
  FROM `scenic-kiln-351104.banking_bronze.customers_raw`
);


set v_target_count = (
  SELECT COUNT(*)
  FROM `scenic-kiln-351104.banking_silver.customer_profile`
);

UPDATE audit.job_audit
SET
    end_time = CURRENT_TIMESTAMP(),
    status = 'SUCCESS',
    source_count = v_source_count,
    target_count = v_target_count
WHERE batch_id = p_batch_id
AND job_name = p_job_name;

END