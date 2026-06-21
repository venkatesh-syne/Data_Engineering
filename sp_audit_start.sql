CREATE OR REPLACE PROCEDURE `scenic-kiln-351104.audit.sp_audit_start`
BEGIN

INSERT INTO audit.job_audit
(
  batch_id,
  job_name,
  start_time,
  status
)
VALUES
(
  p_batch_id,
  'BANKING_PIPELINE',
  CURRENT_TIMESTAMP(),
  'STARTED'
);

END