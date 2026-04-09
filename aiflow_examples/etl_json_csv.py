from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import json
import pandas as pd

Raw_File = "/opt/airflow/dags/users_raw.json"
Processed_File = "/opt/airflow/dags/users_clean.csv"

def extract():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    data = response.json()
    with open(Raw_File,"w") as f:
        json.dump(data,f)

def transformation():
    with open(Raw_File,"r") as f:
        data = json.load(f)

    df = pd.DataFrame(data)

    df = df[["id","name","email","phone","website"]]
    df.to_csv(Processed_File, index = False)
    print("Data transformed")

def load():
    df = pd.read_csv(Processed_File)
    print("Final Data",df)

with DAG(
    dag_id = "ETL_Pipeline_json_to_csv",
    start_date = datetime(2024,1,1),
    schedule_interval = "*/10 * * * *",
    catchup = False
) as dag:
    
    t1 = PythonOperator(
        task_id = "extract",
        python_callable = extract)
    
    t2 = PythonOperator(
        task_id = "transform",
        python_callable = transformation)
    
    t3 = PythonOperator(
        task_id = "load",
        python_callable = load)
    
    t1 >> t2 >> t3