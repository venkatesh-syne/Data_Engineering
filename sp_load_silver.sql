CREATE OR REPLACE PROCEDURE `scenic-kiln-351104.banking_silver.sp_load_silver`
BEGIN

-- =========================================================
-- CUSTOMER PROFILE
-- =========================================================

DELETE FROM banking_silver.customer_profile
WHERE TRUE;

INSERT INTO banking_silver.customer_profile (

customer_id,
full_name,
email,
phone,
total_accounts,
total_balance,
total_cards,
total_loans,
total_loan_amount,
created_at

)

SELECT

c.customer_id,

CONCAT(c.first_name, ' ', c.last_name) AS full_name,

LOWER(c.email) AS email,

c.phone,

COUNT(DISTINCT a.account_id) AS total_accounts,

ROUND(COALESCE(SUM(DISTINCT a.balance),0),2) AS total_balance,

COUNT(DISTINCT cd.card_id) AS total_cards,

COUNT(DISTINCT l.loan_id) AS total_loans,

ROUND(COALESCE(SUM(DISTINCT l.loan_amount),0),2) AS total_loan_amount,

CURRENT_TIMESTAMP() AS created_at

FROM banking_bronze.customers_raw c

LEFT JOIN banking_bronze.accounts_raw a
ON c.customer_id = a.customer_id

LEFT JOIN banking_bronze.cards_raw cd
ON c.customer_id = cd.customer_id

LEFT JOIN banking_bronze.loans_raw l
ON c.customer_id = l.customer_id

GROUP BY

c.customer_id,
full_name,
email,
phone;

-- =========================================================
-- TRANSACTION ENRICHMENT
-- =========================================================

DELETE FROM banking_silver.transactions_enriched
WHERE TRUE;

INSERT INTO banking_silver.transactions_enriched (

transaction_id,
account_id,
customer_id,
account_type,
account_status,
transaction_type,
amount,
net_amount,
transaction_time,
txn_hour,
txn_day,
txn_risk_level,
suspicious_flag,
created_at

)

SELECT

t.transaction_id,

t.account_id,

a.customer_id,

a.account_type,

a.status AS account_status,

t.transaction_type,

t.amount,

CASE
    WHEN t.transaction_type = 'credit'
    THEN t.amount
    ELSE -t.amount
END AS net_amount,

t.transaction_time,

EXTRACT(HOUR FROM t.transaction_time) AS txn_hour,

EXTRACT(DAYOFWEEK FROM t.transaction_time) AS txn_day,

CASE
    WHEN t.amount > 4000 THEN 'HIGH'
    WHEN t.amount > 2000 THEN 'MEDIUM'
    ELSE 'LOW'
END AS txn_risk_level,

CASE
    WHEN t.transaction_type = 'debit'
         AND t.amount > (a.balance * 0.8)
    THEN 'YES'
    ELSE 'NO'
END AS suspicious_flag,

CURRENT_TIMESTAMP()

FROM banking_bronze.transactions_raw t

INNER JOIN banking_bronze.accounts_raw a
ON t.account_id = a.account_id

WHERE

t.amount > 0

AND t.transaction_type IN ('credit','debit');

-- =========================================================
-- LOAN ANALYTICS
-- =========================================================

DELETE FROM banking_silver.loan_analytics
WHERE TRUE;

INSERT INTO banking_silver.loan_analytics (

loan_id,
customer_id,
full_name,
loan_amount,
interest_rate,
loan_status,
interest_category,
loan_segment,
created_at

)

SELECT

l.loan_id,

l.customer_id,

cp.full_name,

l.loan_amount,

l.interest_rate,

l.loan_status,

CASE
    WHEN l.interest_rate > 10 THEN 'HIGH_INTEREST'
    WHEN l.interest_rate > 7 THEN 'MEDIUM_INTEREST'
    ELSE 'LOW_INTEREST'
END AS interest_category,

CASE
    WHEN l.loan_amount > 300000 THEN 'HIGH_VALUE'
    ELSE 'NORMAL'
END AS loan_segment,

CURRENT_TIMESTAMP()

FROM banking_bronze.loans_raw l

LEFT JOIN banking_silver.customer_profile cp
ON l.customer_id = cp.customer_id;

END