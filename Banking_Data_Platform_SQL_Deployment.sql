-- Banking Data Platform SQL Deployment Script


-- 1. Create Datasets
CREATE SCHEMA banking_bronze;
CREATE SCHEMA banking_silver;
CREATE SCHEMA banking_gold;
CREATE SCHEMA audit;
-- 2. Bronze Layer Tables
customers_raw
CREATE TABLE banking_bronze.customers_raw
(
    customer_id STRING,
    first_name STRING,
    last_name STRING,
    email STRING,
    phone STRING,
    address STRING,
    city STRING,
    state STRING,
    country STRING,
    created_date DATE,
    batch_id STRING,
    source_file STRING,
    ingestion_time TIMESTAMP
)
PARTITION BY DATE(ingestion_time)
CLUSTER BY customer_id;
accounts_raw
CREATE TABLE banking_bronze.accounts_raw
(
    account_id STRING,
    customer_id STRING,
    account_type STRING,
    account_status STRING,
    branch_code STRING,
    balance NUMERIC,
    open_date DATE,
    batch_id STRING,
    source_file STRING,
    ingestion_time TIMESTAMP
)
PARTITION BY DATE(ingestion_time)
CLUSTER BY customer_id;
cards_raw
CREATE TABLE banking_bronze.cards_raw
(
    card_id STRING,
    account_id STRING,
    card_type STRING,
    credit_limit NUMERIC,
    expiry_date DATE,
    status STRING,
    batch_id STRING,
    source_file STRING,
    ingestion_time TIMESTAMP
)
PARTITION BY DATE(ingestion_time)
CLUSTER BY account_id;
loans_raw
CREATE TABLE banking_bronze.loans_raw
(
    loan_id STRING,
    customer_id STRING,
    loan_type STRING,
    principal_amount NUMERIC,
    interest_rate NUMERIC,
    tenure_months INT64,
    loan_status STRING,
    batch_id STRING,
    source_file STRING,
    ingestion_time TIMESTAMP
)
PARTITION BY DATE(ingestion_time)
CLUSTER BY customer_id;
transactions_raw
CREATE TABLE banking_bronze.transactions_raw
(
    transaction_id STRING,
    account_id STRING,
    transaction_type STRING,
    transaction_amount NUMERIC,
    transaction_date TIMESTAMP,
    merchant_name STRING,
    batch_id STRING,
    source_file STRING,
    ingestion_time TIMESTAMP
)
PARTITION BY DATE(transaction_date)
CLUSTER BY account_id;
-- 3. Silver Layer Tables
customers
CREATE TABLE banking_silver.customers
(
    customer_id STRING,
    first_name STRING,
    last_name STRING,
    email STRING,
    phone STRING,
    city STRING,
    state STRING,
    country STRING,
    customer_status STRING,
    created_date DATE,
    load_timestamp TIMESTAMP
)
PARTITION BY created_date
CLUSTER BY customer_id;
accounts
CREATE TABLE banking_silver.accounts
(
    account_id STRING,
    customer_id STRING,
    account_type STRING,
    account_status STRING,
    branch_code STRING,
    balance NUMERIC,
    open_date DATE,
    load_timestamp TIMESTAMP
)
PARTITION BY open_date
CLUSTER BY customer_id;
cards
CREATE TABLE banking_silver.cards
(
    card_id STRING,
    account_id STRING,
    card_type STRING,
    credit_limit NUMERIC,
    expiry_date DATE,
    status STRING,
    load_timestamp TIMESTAMP
)
PARTITION BY expiry_date
CLUSTER BY account_id;
loans
CREATE TABLE banking_silver.loans
(
    loan_id STRING,
    customer_id STRING,
    loan_type STRING,
    principal_amount NUMERIC,
    interest_rate NUMERIC,
    tenure_months INT64,
    loan_status STRING,
    load_timestamp TIMESTAMP
)
PARTITION BY DATE(load_timestamp)
CLUSTER BY customer_id;
transactions
CREATE TABLE banking_silver.transactions
(
    transaction_id STRING,
    account_id STRING,
    transaction_type STRING,
    transaction_amount NUMERIC,
    transaction_date TIMESTAMP,
    merchant_name STRING,
    load_timestamp TIMESTAMP
)
PARTITION BY DATE(transaction_date)
CLUSTER BY account_id;
-- 4. Gold Layer Tables
customer_kpis
CREATE TABLE banking_gold.customer_kpis
(
    kpi_date DATE,
    total_customers INT64,
    active_customers INT64,
    new_customers INT64,
    load_timestamp TIMESTAMP
)
PARTITION BY kpi_date;
account_kpis
CREATE TABLE banking_gold.account_kpis
(
    kpi_date DATE,
    total_accounts INT64,
    active_accounts INT64,
    total_balance NUMERIC,
    avg_balance NUMERIC,
    load_timestamp TIMESTAMP
)
PARTITION BY kpi_date;
loan_kpis
CREATE TABLE banking_gold.loan_kpis
(
    kpi_date DATE,
    total_loans INT64,
    active_loans INT64,
    total_loan_amount NUMERIC,
    avg_interest_rate NUMERIC,
    load_timestamp TIMESTAMP
)
PARTITION BY kpi_date;
transaction_kpis
CREATE TABLE banking_gold.transaction_kpis
(
    kpi_date DATE,
    transaction_count INT64,
    transaction_amount NUMERIC,
    avg_transaction_amount NUMERIC,
    load_timestamp TIMESTAMP
)
PARTITION BY kpi_date;
-- 5. Audit Tables
job_audit
CREATE TABLE audit.job_audit
(
    batch_id STRING,
    job_name STRING,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    status STRING,
    source_count INT64,
    target_count INT64,
    created_by STRING,
    created_timestamp TIMESTAMP
)
PARTITION BY DATE(start_time)
CLUSTER BY batch_id;
pipeline_audit
CREATE TABLE audit.pipeline_audit
(
    batch_id STRING,
    pipeline_name STRING,
    task_name STRING,
    task_status STRING,
    execution_start TIMESTAMP,
    execution_end TIMESTAMP,
    error_message STRING
)
PARTITION BY DATE(execution_start);
-- 6. Reconciliation Table
CREATE TABLE audit.reconciliation
(
    batch_id STRING,
    table_name STRING,
    source_count INT64,
    bronze_count INT64,
    silver_count INT64,
    gold_count INT64,
    reconciliation_status STRING,
    reconciliation_time TIMESTAMP
)
PARTITION BY DATE(reconciliation_time)
CLUSTER BY table_name;
-- 7. Bronze → Silver Stored Procedure
CREATE OR REPLACE PROCEDURE banking_silver.sp_load_silver()
BEGIN

TRUNCATE TABLE banking_silver.customers;

INSERT INTO banking_silver.customers
SELECT
    customer_id,
    first_name,
    last_name,
    email,
    phone,
    city,
    state,
    country,
    'ACTIVE',
    created_date,
    CURRENT_TIMESTAMP()
FROM banking_bronze.customers_raw
QUALIFY ROW_NUMBER()
OVER(
PARTITION BY customer_id
ORDER BY ingestion_time DESC
)=1;

END;
-- 8. Silver → Gold Stored Procedure
CREATE OR REPLACE PROCEDURE banking_gold.sp_load_gold()
BEGIN

TRUNCATE TABLE banking_gold.customer_kpis;

INSERT INTO banking_gold.customer_kpis
SELECT
CURRENT_DATE(),
COUNT(*),
COUNTIF(customer_status='ACTIVE'),
COUNTIF(created_date=CURRENT_DATE()),
CURRENT_TIMESTAMP()
FROM banking_silver.customers;

END;
-- 9. Audit Start Procedure
CREATE OR REPLACE PROCEDURE audit.sp_audit_start(
    p_batch_id STRING,
    p_job_name STRING
)
BEGIN

INSERT INTO audit.job_audit
(
batch_id,
job_name,
start_time,
status,
created_timestamp
)
VALUES
(
p_batch_id,
p_job_name,
CURRENT_TIMESTAMP(),
'STARTED',
CURRENT_TIMESTAMP()
);

END;
-- 10. Audit End Procedure
CREATE OR REPLACE PROCEDURE audit.sp_audit_end(
    p_batch_id STRING,
    p_job_name STRING,
    p_status STRING,
    p_source_count INT64,
    p_target_count INT64
)
BEGIN

UPDATE audit.job_audit
SET
end_time = CURRENT_TIMESTAMP(),
status = p_status,
source_count = p_source_count,
target_count = p_target_count
WHERE batch_id = p_batch_id
AND job_name = p_job_name;

END;
-- 11. Reconciliation Procedure
CREATE OR REPLACE PROCEDURE audit.sp_reconciliation(
    p_batch_id STRING
)
BEGIN

INSERT INTO audit.reconciliation
SELECT
p_batch_id,
'CUSTOMERS',
(SELECT COUNT(*) FROM banking_bronze.customers_raw),
(SELECT COUNT(*) FROM banking_bronze.customers_raw),
(SELECT COUNT(*) FROM banking_silver.customers),
(SELECT COUNT(*) FROM banking_gold.customer_kpis),
CASE
WHEN
(SELECT COUNT(*) FROM banking_bronze.customers_raw)
=
(SELECT COUNT(*) FROM banking_silver.customers)
THEN 'PASS'
ELSE 'FAIL'
END,
CURRENT_TIMESTAMP();

END;