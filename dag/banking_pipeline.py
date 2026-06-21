from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.operators.dataflow import DataflowStartFlexTemplateOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator

from datetime import datetime

PROJECT_ID = "scenic-kiln-351104"

REGION = "us-central1"

FLEX_TEMPLATE = (
    "gs://banking-dataflow-template/banking-bronze.json"
)


def generate_batch_id(**kwargs):

    batch_id = datetime.utcnow().strftime("%Y%m%d%H%M%S")

    kwargs["ti"].xcom_push(
        key="batch_id",
        value=batch_id
    )


with DAG(
    dag_id="banking_pipeline",
    start_date=datetime(2025,1,1),
    schedule="0 10 * * *",
    catchup=False
) as dag:

    create_batch = PythonOperator(
        task_id="generate_batch_id",
        python_callable=generate_batch_id
    )

    start_audit = BigQueryInsertJobOperator(
        task_id="start_audit",
        configuration={
            "query":{
                "query":"""
                CALL audit.sp_audit_start(
                '{{ ti.xcom_pull(task_ids="generate_batch_id", key="batch_id") }}',
                'BANKING_PIPELINE'
                );
                """,
                "useLegacySql":False
            }
        }
    )

    run_dataflow = DataflowStartFlexTemplateOperator(
        task_id="run_dataflow",

        project_id=PROJECT_ID,

        location=REGION,

        body={
            "launchParameter":{
                "jobName":"banking-bronze-load",

                "containerSpecGcsPath":
                FLEX_TEMPLATE,

                "parameters":{

                    "batch_id":
                    "{{ ti.xcom_pull(task_ids='generate_batch_id', key='batch_id') }}"
                }
            }
        }
    )

    run_silver = BigQueryInsertJobOperator(
        task_id="run_silver",

        configuration={
            "query":{
                "query":"CALL banking_silver.sp_load_silver();",
                "useLegacySql":False
            }
        }
    )

    run_gold = BigQueryInsertJobOperator(
        task_id="run_gold",

        configuration={
            "query":{
                "query":"CALL banking_gold.sp_load_gold();",
                "useLegacySql":False
            }
        }
    )

    reconciliation = BigQueryInsertJobOperator(
        task_id="reconciliation",

        configuration={
            "query":{
                "query":"CALL banking_audit.sp_reconciliation();",
                "useLegacySql":False
            }
        }
    )

    end_audit = BigQueryInsertJobOperator(
        task_id="end_audit",

        configuration={
            "query":{
                "query":"""
                CALL audit.sp_audit_end(
                '{{ ti.xcom_pull(task_ids="generate_batch_id", key="batch_id") }}','
                );
                """,
                "useLegacySql":False
            }
        }
    )

    (
        create_batch
        >> start_audit
        >> run_dataflow
        >> run_silver
        >> run_gold
        >> reconciliation
        >> end_audit
    )