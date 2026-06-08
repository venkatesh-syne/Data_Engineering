import os
import sys

project_root = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.append(project_root)

import apache_beam as beam

from apache_beam.options.pipeline_options import PipelineOptions

from datetime import datetime

# Parsers

from parsers.customer_parser import ParseCustomer
from parsers.account_parser import ParseAccount
from parsers.card_parser import ParseCard
from parsers.loan_parser import ParseLoan
from parsers.transaction_parser import ParseTransaction

# BigQuery Schemas

from config.bq_schemas import (
    CUSTOMER_SCHEMA,
    ACCOUNT_SCHEMA,
    CARD_SCHEMA,
    LOAN_SCHEMA,
    TRANSACTION_SCHEMA
)

# ====================================================
# CONFIGURATION
# ====================================================

PROJECT_ID = "scenic-kiln-351104"

REGION = "us-east1"

TEMP_LOCATION = \
"gs://banking-dataflow-temp/temp"

STAGING_LOCATION = \
"gs://banking-dataflow-staging/staging"

BATCH_ID = datetime.utcnow().strftime(
    "BATCH_%Y%m%d_%H%M%S"
)

# ====================================================
# PIPELINE OPTIONS
# ====================================================

options = PipelineOptions(

    runner="DataflowRunner",   #"DirectRunner"

    project=PROJECT_ID,

    region="us-central1",

    worker_zone="us-central1-b",

    temp_location=TEMP_LOCATION,

    staging_location=STAGING_LOCATION,

    save_main_session=True,

    num_workers=1,

    max_num_workers=2
)

# ====================================================
# PIPELINE
# ====================================================

with beam.Pipeline(options=options) as p:

    # =================================================
    # CUSTOMERS
    # =================================================

    (
        p

        | "Read Customers"
        >> beam.io.ReadFromText(
            "gs://batch3-banking-raw-data/raw/mysql/customers/*/*.csv",
            skip_header_lines=1
        )

        | "Parse Customers"
        >> beam.ParDo(
            ParseCustomer(BATCH_ID)
        )

        | "Write Customers To BQ"
        >> beam.io.WriteToBigQuery(

            table=
            f"{PROJECT_ID}:banking_bronze.customers_raw",

            schema=CUSTOMER_SCHEMA,

            method="STREAMING_INSERTS",

            write_disposition=
            beam.io.BigQueryDisposition.WRITE_APPEND,

            create_disposition=
            beam.io.BigQueryDisposition.CREATE_NEVER
        )
    )

    # =================================================
    # ACCOUNTS
    # =================================================

    (
        p

        | "Read Accounts"
        >> beam.io.ReadFromText(
            "gs://batch3-banking-raw-data/raw/mysql/accounts/*/*.csv",
            skip_header_lines=1
        )

        | "Parse Accounts"
        >> beam.ParDo(
            ParseAccount(BATCH_ID)
        )

        | "Write Accounts To BQ"
        >> beam.io.WriteToBigQuery(

            table=
            f"{PROJECT_ID}:banking_bronze.accounts_raw",

            schema=ACCOUNT_SCHEMA,

            method="STREAMING_INSERTS",

            write_disposition=
            beam.io.BigQueryDisposition.WRITE_APPEND,

            create_disposition=
            beam.io.BigQueryDisposition.CREATE_NEVER
        )
    )

    # =================================================
    # CARDS
    # =================================================

    (
        p

        | "Read Cards"
        >> beam.io.ReadFromText(
            "gs://batch3-banking-raw-data/raw/mysql/cards/*/*.csv",
            skip_header_lines=1
        )

        | "Parse Cards"
        >> beam.ParDo(
            ParseCard(BATCH_ID)
        )

        | "Write Cards To BQ"
        >> beam.io.WriteToBigQuery(

            table=
            f"{PROJECT_ID}:banking_bronze.cards_raw",

            schema=CARD_SCHEMA,

            method="STREAMING_INSERTS",

            write_disposition=
            beam.io.BigQueryDisposition.WRITE_APPEND,

            create_disposition=
            beam.io.BigQueryDisposition.CREATE_NEVER
        )
    )

    # =================================================
    # LOANS
    # =================================================

    (
        p

        | "Read Loans"
        >> beam.io.ReadFromText(
            "gs://batch3-banking-raw-data/raw/mysql/loans/*/*.csv",
            skip_header_lines=1
        )

        | "Parse Loans"
        >> beam.ParDo(
            ParseLoan(BATCH_ID)
        )

        | "Write Loans To BQ"
        >> beam.io.WriteToBigQuery(

            table=
            f"{PROJECT_ID}:banking_bronze.loans_raw",

            schema=LOAN_SCHEMA,

            method="STREAMING_INSERTS",

            write_disposition=
            beam.io.BigQueryDisposition.WRITE_APPEND,

            create_disposition=
            beam.io.BigQueryDisposition.CREATE_NEVER
        )
    )

    # =================================================
    # TRANSACTIONS
    # =================================================

    (
        p

        | "Read Transactions"
        >> beam.io.ReadFromText(
            "gs://batch3-banking-raw-data/raw/mysql/transactions/*/*.csv",
            skip_header_lines=1
        )

        | "Parse Transactions"
        >> beam.ParDo(
            ParseTransaction(BATCH_ID)
        )

        | "Write Transactions To BQ"
        >> beam.io.WriteToBigQuery(

            table=
            f"{PROJECT_ID}:banking_bronze.transactions_raw",

            schema=TRANSACTION_SCHEMA,

            method="STREAMING_INSERTS",

            write_disposition=
            beam.io.BigQueryDisposition.WRITE_APPEND,

            create_disposition=
            beam.io.BigQueryDisposition.CREATE_NEVER
        )
    )

print(
    f"Banking Bronze Load Completed Successfully "
    f"for Batch: {BATCH_ID}"
)