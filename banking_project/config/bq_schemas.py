CUSTOMER_SCHEMA = {
    "fields": [
        {"name": "customer_id", "type": "INTEGER"},
        {"name": "first_name", "type": "STRING"},
        {"name": "last_name", "type": "STRING"},
        {"name": "email", "type": "STRING"},
        {"name": "phone", "type": "STRING"},
        {"name": "created_at", "type": "TIMESTAMP"},
        {"name": "batch_id", "type": "STRING"},
        {"name": "ingestion_time", "type": "TIMESTAMP"}
    ]
}

ACCOUNT_SCHEMA = {
    "fields": [
        {"name": "account_id", "type": "INTEGER"},
        {"name": "customer_id", "type": "INTEGER"},
        {"name": "account_type", "type": "STRING"},
        {"name": "balance", "type": "FLOAT"},
        {"name": "status", "type": "STRING"},
        {"name": "created_at", "type": "TIMESTAMP"},
        {"name": "batch_id", "type": "STRING"},
        {"name": "ingestion_time", "type": "TIMESTAMP"}
    ]
}

CARD_SCHEMA = {
    "fields": [
        {"name": "card_id", "type": "INTEGER"},
        {"name": "customer_id", "type": "INTEGER"},
        {"name": "card_type", "type": "STRING"},
        {"name": "card_limit", "type": "FLOAT"},
        {"name": "issued_date", "type": "DATE"},
        {"name": "batch_id", "type": "STRING"},
        {"name": "ingestion_time", "type": "TIMESTAMP"}
    ]
}

LOAN_SCHEMA = {
    "fields": [
        {"name": "loan_id", "type": "INTEGER"},
        {"name": "customer_id", "type": "INTEGER"},
        {"name": "loan_amount", "type": "FLOAT"},
        {"name": "interest_rate", "type": "FLOAT"},
        {"name": "loan_status", "type": "STRING"},
        {"name": "created_at", "type": "TIMESTAMP"},
        {"name": "batch_id", "type": "STRING"},
        {"name": "ingestion_time", "type": "TIMESTAMP"}
    ]
}

TRANSACTION_SCHEMA = {
    "fields": [
        {"name": "transaction_id", "type": "INTEGER"},
        {"name": "account_id", "type": "INTEGER"},
        {"name": "transaction_type", "type": "STRING"},
        {"name": "amount", "type": "FLOAT"},
        {"name": "transaction_time", "type": "TIMESTAMP"},
        {"name": "description", "type": "STRING"},
        {"name": "batch_id", "type": "STRING"},
        {"name": "ingestion_time", "type": "TIMESTAMP"}
    ]
}