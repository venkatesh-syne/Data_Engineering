TABLE_CONFIG = {

    "customers": {
        "path":
        "gs://batch3-banking-raw-data/raw/mysql/customers/*/*.csv",
        "table":
        "banking_bronze.customers_raw"
    },

    "accounts": {
        "path":
        "gs://batch3-banking-raw-data/raw/mysql/accounts/*/*.csv",
        "table":
        "banking_bronze.accounts_raw"
    },

    "cards": {
        "path":
        "gs://batch3-banking-raw-data/raw/mysql/cards/*/*.csv",
        "table":
        "banking_bronze.cards_raw"
    },

    "loans": {
        "path":
        "gs://batch3-banking-raw-data/raw/mysql/loans/*/*.csv",
        "table":
        "banking_bronze.loans_raw"
    },

    "transactions": {
        "path":
        "gs://batch3-banking-raw-data/raw/mysql/transactions/*/*.csv",
        "table":
        "banking_bronze.transactions_raw"
    }
}