from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello(country, **kwargs):
    print(f'I am processing this {country}')


with DAG(dag_id='example_python_operator', 
         description='Utilizando python operator', 
         start_date=datetime(2024, 2, 1), 
         schedule_interval='@once') as dag:

    t1 = PythonOperator(task_id='process_ar', 
                        python_callable=print_hello, 
                        op_kwargs={'country':'AR'})

    t2 = PythonOperator(task_id='process_uy', 
                        python_callable=print_hello, 
                        op_kwargs={'country':'UY'})

    t1 >> t2 
    