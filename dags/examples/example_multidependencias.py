from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import time

def prints():
    timestamp = int(time.time())
    print("Current timestamp:", timestamp)

def prints2():
    time.sleep(3)
    timestamp = int(time.time())
    print("Current timestamp2:", timestamp)

with DAG(dag_id="example_dependencias", 
         description='our first DAG making depencies between taks',
         # schedule_interval='@once',
         max_active_runs=1,
         start_date=datetime(2024, 3, 20)) as dag:

    t1 = DummyOperator(task_id="example_task1")
    
    t2 = PythonOperator(task_id='example_task2', 
                        python_callable=prints)

    t3 = BashOperator(task_id="example_task3", 
                      bash_command="echo '_______Hello people________'")

    t4 = PythonOperator(task_id='example_task4', 
                        python_callable=prints2)

    t5 = BashOperator(task_id="example_task5", 
                      bash_command="echo '_______task5________'")

    t6 = BashOperator(task_id="example_task6", 
                      bash_command="echo '_______task6________'")

    t7 = DummyOperator(task_id="example_task7")

    t1 >> t2 >> t3 >> t4 >> [t5,t6] >> t7