CREATE OR REPLACE PROCEDURE `scenic-kiln-351104.banking_audit.sp_reconciliation`

BEGIN

DELETE FROM banking_audit.reconciliation
WHERE TRUE;

INSERT INTO banking_audit.reconciliation

SELECT

'transactions' AS table_name,

(SELECT COUNT(*) FROM banking_bronze.transactions_raw),

(SELECT COUNT(*) FROM banking_silver.transactions_enriched),

CASE
    WHEN
        (SELECT COUNT(*) FROM banking_bronze.transactions_raw)
        =
        (SELECT COUNT(*) FROM banking_silver.transactions_enriched)

    THEN 'MATCH'

    ELSE 'MISMATCH'

END,

CURRENT_TIMESTAMP();

END