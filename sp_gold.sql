CREATE OR REPLACE PROCEDURE `scenic-kiln-351104.banking_gold.sp_load_gold`
BEGIN

-- =========================================================
-- DAILY BANK KPI
-- =========================================================

DELETE FROM banking_gold.daily_bank_kpi
WHERE TRUE;

INSERT INTO banking_gold.daily_bank_kpi (

txn_date,
total_transactions,
active_customers,
total_transaction_amount,
avg_transaction_amount,
max_transaction_amount,
min_transaction_amount,
total_credit_amount,
total_debit_amount,
high_risk_transactions,
suspicious_transactions,
created_at

)

SELECT

DATE(transaction_time) AS txn_date,

COUNT(*) AS total_transactions,

COUNT(DISTINCT customer_id) AS active_customers,

ROUND(SUM(amount),2) AS total_transaction_amount,

ROUND(AVG(amount),2) AS avg_transaction_amount,

ROUND(MAX(amount),2) AS max_transaction_amount,

ROUND(MIN(amount),2) AS min_transaction_amount,

ROUND(SUM(
    CASE
        WHEN transaction_type = 'credit'
        THEN amount
        ELSE 0
    END
),2) AS total_credit_amount,

ROUND(SUM(
    CASE
        WHEN transaction_type = 'debit'
        THEN amount
        ELSE 0
    END
),2) AS total_debit_amount,

COUNT(
    CASE
        WHEN txn_risk_level = 'HIGH'
        THEN 1
    END
) AS high_risk_transactions,

COUNT(
    CASE
        WHEN suspicious_flag = 'YES'
        THEN 1
    END
) AS suspicious_transactions,

CURRENT_TIMESTAMP()

FROM banking_silver.transactions_enriched

GROUP BY txn_date;

-- =========================================================
-- CUSTOMER 360 KPI
-- =========================================================

DELETE FROM banking_gold.customer_360
WHERE TRUE;

INSERT INTO banking_gold.customer_360 (

customer_id,
full_name,
total_accounts,
total_balance,
total_cards,
total_loans,
total_loan_amount,
total_transactions,
total_spend,
avg_transaction_value,
highest_transaction,
high_risk_txn_count,
suspicious_txn_count,
created_at

)

SELECT

cp.customer_id,

cp.full_name,

cp.total_accounts,

cp.total_balance,

cp.total_cards,

cp.total_loans,

cp.total_loan_amount,

COUNT(te.transaction_id) AS total_transactions,

ROUND(COALESCE(SUM(te.amount),0),2) AS total_spend,

ROUND(COALESCE(AVG(te.amount),0),2) AS avg_transaction_value,

ROUND(COALESCE(MAX(te.amount),0),2) AS highest_transaction,

COUNT(
    CASE
        WHEN te.txn_risk_level = 'HIGH'
        THEN 1
    END
) AS high_risk_txn_count,

COUNT(
    CASE
        WHEN te.suspicious_flag = 'YES'
        THEN 1
    END
) AS suspicious_txn_count,

CURRENT_TIMESTAMP()

FROM banking_silver.customer_profile cp

LEFT JOIN banking_silver.transactions_enriched te
ON cp.customer_id = te.customer_id

GROUP BY

cp.customer_id,
cp.full_name,
cp.total_accounts,
cp.total_balance,
cp.total_cards,
cp.total_loans,
cp.total_loan_amount;

-- =========================================================
-- FRAUD DETECTION
-- =========================================================

DELETE FROM banking_gold.fraud_transactions
WHERE TRUE;

INSERT INTO banking_gold.fraud_transactions

SELECT *

FROM banking_silver.transactions_enriched

WHERE

txn_risk_level = 'HIGH'

AND suspicious_flag = 'YES'

AND txn_hour BETWEEN 0 AND 4;

END