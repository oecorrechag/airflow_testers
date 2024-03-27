from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello():
    return print('_____________________hello world with python in airflow_____________________')

with DAG(dag_id="primer_dag_python",
         description="Utilizando python Operator",
        #  schedule_interval='@once',
         max_active_runs=1,
         start_date=datetime(2024, 3, 1), 
         end_date=datetime(2024, 3, 20)) as dag:

    t1 = PythonOperator(task_id='primer_task_python',
                        python_callable=print_hello)

    t1
