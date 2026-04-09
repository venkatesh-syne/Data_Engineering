from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    print("Extracting Data")

def transform():
    print("Transforming Data")

def load():
    print("Transforming Data")


with DAG(
    dag_id = "ETL_Pipeline",
    start_date = datetime(2024,1,1),
    schedule_interval = "*/2 * * * *",
    catchup = False
) as dag:
    
    t1 = PythonOperator(
        task_id = "extract",
        python_callable = extract)
    
    t2 = PythonOperator(
        task_id = "transform",
        python_callable = transform)
    
    t3 = PythonOperator(
        task_id = "load",
        python_callable = load)
    
    t1 >> t2 >> t3