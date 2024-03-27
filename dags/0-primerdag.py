from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

with DAG(dag_id="miprimerdag",
         description="Nuestro primer DAG",
         max_active_runs=1,
         schedule_interval="@once",
         start_date=datetime(2024, 3, 1), 
         end_date=datetime(2024, 3, 20)) as dag:
    
    t1 = DummyOperator(task_id="dummy")
    t1
