from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello():
    return print('_____________________hello world with python in airflow_____________________')

with DAG(dag_id="dependencias_3.5", start_date=datetime(2024, 3, 25)) as dag:

  t1 = DummyOperator(task_id="first_task")

  t2 = PythonOperator(task_id='second_task', 
                      python_callable=print_hello)

  t3 = DummyOperator(task_id="third_task")

  t1 >> t2 >> t3
