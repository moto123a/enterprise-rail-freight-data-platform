from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def run_etl():
    print("Running certified dataset ETL process")

dag = DAG(
    dag_id="supply_chain_etl",
    start_date=datetime(2024,1,1),
    schedule_interval="@daily",
    catchup=False
)

etl_task = PythonOperator(
    task_id="etl_pipeline",
    python_callable=run_etl,
    dag=dag
)

