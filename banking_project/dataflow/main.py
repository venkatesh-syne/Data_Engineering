import apache_beam as beam

from apache_beam.options.pipeline_options import PipelineOptions

from apache_beam.io.gcp.bigquery import WriteToBigQuery

from datetime import datetime

# Config

from config.table_config import TABLE_CONFIG

from config.bq_schemas import *

# Parsers

from parsers.customer_parser import ParseCustomer
from parsers.account_parser import ParseAccount
from parsers.card_parser import ParseCard
from parsers.loan_parser import ParseLoan
from parsers.transaction_parser import ParseTransaction

# Validations

from validations.customer_validation import ValidateCustomer
from validations.account_validation import ValidateAccount
from validations.card_validation import ValidateCard
from validations.loan_validation import ValidateLoan
from validations.transaction_validation import ValidateTransaction


PROJECT_ID = "scenic-kiln-351104"

REGION = "us-central1"

TEMP_LOCATION = "gs://banking-dataflow-temp/temp"

STAGING_LOCATION = "gs://banking-dataflow-temp/staging"

JOB_NAME = f"banking-bronze-{datetime.now().strftime('%Y%m%d%H%M%S')}"

BATCH_ID = datetime.now().strftime("%Y%m%d%H%M%S")


options = PipelineOptions(
    runner="DataflowRunner",
    project=PROJECT_ID,
    region="us-central1",
    temp_location=TEMP_LOCATION,
    staging_location=STAGING_LOCATION,
    job_name=JOB_NAME,
    save_main_session=True,
    machine_type="e2-standard-2",
    num_workers=1,
    max_num_workers=2
)

p = beam.Pipeline(options=options)

# ==================================================
# CUSTOMERS
# ==================================================

(
    p
    | "Read Customer" >>
    beam.io.ReadFromText(
        TABLE_CONFIG["customers"]["path"],
        skip_header_lines=1
    )

    | "Parse Customer" >>
    beam.ParDo(ParseCustomer(BATCH_ID))

    | "Validate Customer" >>
    beam.ParDo(ValidateCustomer())

    | "Write Customer" >>
    WriteToBigQuery(

        table=f"{PROJECT_ID}:banking_bronze.customers_raw",

        schema=CUSTOMER_SCHEMA,

        write_disposition="WRITE_APPEND",

        create_disposition="CREATE_NEVER"
    )
)

# ==================================================
# ACCOUNTS
# ==================================================

(
    p
    | "Read Accounts" >>
    beam.io.ReadFromText(
        TABLE_CONFIG["accounts"]["path"],
        skip_header_lines=1
    )

    | "Parse Accounts" >>
    beam.ParDo(ParseAccount(BATCH_ID))

    | "Validate Accounts" >>
    beam.ParDo(ValidateAccount())

    | "Write Accounts" >>
    WriteToBigQuery(

        table=f"{PROJECT_ID}:banking_bronze.accounts_raw",

        schema=ACCOUNT_SCHEMA,

        write_disposition="WRITE_APPEND",

        create_disposition="CREATE_NEVER"
    )
)

# ==================================================
# CARDS
# ==================================================

(
    p
    | "Read Cards" >>
    beam.io.ReadFromText(
        TABLE_CONFIG["cards"]["path"],
        skip_header_lines=1
    )

    | "Parse Cards" >>
    beam.ParDo(ParseCard(BATCH_ID))

    | "Validate Cards" >>
    beam.ParDo(ValidateCard())

    | "Write Cards" >>
    WriteToBigQuery(

        table=f"{PROJECT_ID}:banking_bronze.cards_raw",

        schema=CARD_SCHEMA,

        write_disposition="WRITE_APPEND",

        create_disposition="CREATE_NEVER"
    )
)

# ==================================================
# LOANS
# ==================================================

(
    p
    | "Read Loans" >>
    beam.io.ReadFromText(
        TABLE_CONFIG["loans"]["path"],
        skip_header_lines=1
    )

    | "Parse Loans" >>
    beam.ParDo(ParseLoan(BATCH_ID))

    | "Validate Loans" >>
    beam.ParDo(ValidateLoan())

    | "Write Loans" >>
    WriteToBigQuery(

        table=f"{PROJECT_ID}:banking_bronze.loans_raw",

        schema=LOAN_SCHEMA,

        write_disposition="WRITE_APPEND",

        create_disposition="CREATE_NEVER"
    )
)

# ==================================================
# TRANSACTIONS
# ==================================================

(
    p
    | "Read Transactions" >>
    beam.io.ReadFromText(
        TABLE_CONFIG["transactions"]["path"],
        skip_header_lines=1
    )

    | "Parse Transactions" >>
    beam.ParDo(ParseTransaction(BATCH_ID))

    | "Validate Transactions" >>
    beam.ParDo(ValidateTransaction())

    | "Write Transactions" >>
    WriteToBigQuery(

        table=f"{PROJECT_ID}:banking_bronze.transactions_raw",

        schema=TRANSACTION_SCHEMA,

        write_disposition="WRITE_APPEND",

        create_disposition="CREATE_NEVER"
    )
)

result = p.run()

result.wait_until_finish()